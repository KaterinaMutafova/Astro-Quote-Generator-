import random
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import Group
# from django.http import HttpResponse
from django.shortcuts import render, redirect
# from quote_generator.profiles.models import UserProfile
from quote_generator.quotes.forms import QuoteForm, AuthorForm, MyElementForm
from quote_generator.quotes.models import Quote, Author
from quote_generator.quotes.models.like_model import Like

# Create your views here.


def base(request):
    quotes = Quote.objects.all()
    the_quote_object = None
    all_likes = Like.objects.filter(quote=the_quote_object)
    count_all_likes = len(all_likes)
    is_liked_by_user = False

    if quotes:
        the_quote_object = random.choice(quotes)
        all_likes = Like.objects.filter(quote=the_quote_object)
        count_all_likes = len(all_likes)
        is_liked_by_user = the_quote_object.like_set.filter(user_id=request.user.id) \
            .exists()

    context = {
        'quotes': quotes,
        'the_quote_object': the_quote_object,
        'count_all_likes': count_all_likes,
        'is_liked_by_user': is_liked_by_user,

    }
    return render(request, 'index.html', context)


@login_required()
def add_quote(request):
    template = 'quotes/add_quote.html'
    if request.method == "GET":
        form = QuoteForm()
        context = {
            'form': form,
        }
        return render(request, template, context)
    form = QuoteForm(request.POST, request.FILES)
    if form.is_valid():
        quote = form.save(commit=False)
        quote.added_by = request.user
        quote.save()

        # # Check if user has changed the group to Special user
        # user = request.user
        # quotes_added_by_user = Quote.objects.filter(added_by=request.user.id)
        # if len(quotes_added_by_user) >= 8:
        #     my_special_group = Group.objects.get(name='Special user')
        #     my_special_group.user_set.add(user)

        return redirect(quote_details, pk=quote.pk)
    context = {
        'form': form,
    }
    return render(request, template, context)


def get_the_image(instance_model, current_pic, new_pic):
    if new_pic == current_pic:
        current_pic.delete()
        instance_model.image = new_pic
    elif not (new_pic == current_pic) and new_pic is not None:
        current_pic.delete()
        instance_model.image = new_pic
    return instance_model.image


@login_required()
def edit_quote(request, pk):
    quote = Quote.objects.get(pk=pk)
    template = 'quotes/edit_quote.html'
    if request.method == 'GET':
        form = QuoteForm(instance=quote)
        context = {
            'form': form,
        }
        return render(request, template, context)
    current_pic = quote.image
    form = QuoteForm(request.POST, request.FILES, instance=quote)
    new_pic = request.FILES.get('image')
    if form.is_valid():
        quote.image = get_the_image(quote, current_pic, new_pic)
        quote = form.save()
        quote.save()
        return redirect(quote_details, pk=pk)
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required()
def delete_quote(request, pk):
    quote = Quote.objects.get(pk=pk)
    template = 'quotes/delete_quote.html'
    if request.method == "GET":
        form = QuoteForm(instance=quote)
        for name, field in form.fields.items():
            field.widget.attrs['disabled'] = True
        form.save(commit=False)
        context = {
            'form': form,

        }
        return render(request, template, context)
    image = quote.image
    image.delete()
    quote.delete()
    return redirect(show_all_quotes)


def quote_details(request, pk):
    the_quote_object = Quote.objects.get(pk=pk)
    quotes = Quote.objects.all().order_by('id')
    # likes_by_user = Like.objects.filter(quote=the_quote_object, user=request.user)
    all_likes = Like.objects.filter(quote=the_quote_object)
    count_all_likes = len(all_likes)
    count_quotes = len(quotes)
    template = 'quotes/quote_details.html'
    if the_quote_object == Quote.objects.all().order_by('id').first():
        prev_quote = Quote.objects.all().order_by('id').last()
    else:
        prev_quote = Quote.objects.filter(id__lt=the_quote_object.id).order_by('id').last()
    if the_quote_object == Quote.objects.all().order_by('id').last():
        next_quote = Quote.objects.all().order_by('id').first()
    else:
        next_quote = Quote.objects.filter(id__gt=the_quote_object.id).order_by('id').first()

    the_quote_object.likes_count = the_quote_object.like_set.count()
    is_added_by_the_user = the_quote_object.added_by == request.user
    is_liked_by_user = the_quote_object.like_set.filter(user_id=request.user.id) \
        .exists()

    context = {
        'the_quote_object': the_quote_object,
        'prev_quote': prev_quote,
        'next_quote': next_quote,
        'count_quotes': count_quotes,
        'is_added_by_the_user': is_added_by_the_user,
        'is_liked_by_user': is_liked_by_user,
        'count_all_likes': count_all_likes,
    }
    return render(request, template, context)


@login_required()
def change_quote(request):
    template = 'quote_in_balloon.html'
    if request.method == "GET":
        # quotes = Quote.objects.all()
        # count_quotes = len(quotes)
        # index = random.randint(1, count_quotes)
        # quote = Quote.objects.get(pk=index)
        elementform = MyElementForm()

        context = {
            # 'quote': quote,
            'elementform': elementform,
        }
        return render(request, template, context)

    elementform = MyElementForm(request.POST or None)

    quotes = ''
    chosen_sign = ''
    chosen_element = ''
    chosen_moon_sign = ''

    if elementform.is_valid():
        chosen_sign = elementform.cleaned_data['sign']
        chosen_element = elementform.cleaned_data['element']
        chosen_moon_sign = elementform.cleaned_data['moon']

        quotes_signs = Quote.objects.filter(sign=chosen_sign)
        quotes_elements = Quote.objects.filter(element=chosen_element)
        quotes_moon_sign = Quote.objects.filter(sign=chosen_moon_sign)

        if chosen_sign or chosen_element or quotes_moon_sign:
            quotes = quotes_signs | quotes_elements | quotes_moon_sign
        else:
            quotes = Quote.objects.all()

    if quotes:
        the_quote_object = random.choice(quotes)
    else:
        the_quote_object = None
    context = {
        'the_quote_object': the_quote_object,
        'chosen_sign': chosen_sign,
        'chosen_element': chosen_element,
        'chosen_moon_sign': chosen_moon_sign,
        'elementform': elementform,

    }
    return render(request, template, context)

    # dict_signs = {
    #     'овен': 1, 'телец': 2, 'близнаци': 3, 'рак': 4, 'лъв': 5, 'дева': 6,
    #     'везни': 7, 'скорпион': 8, 'стрелец': 9, 'козирог': 10, 'водолей': 11, 'риби': 12
    # }


def show_all_quotes(request):
    template = 'all_quotes.html'
    quotes = Quote.objects.all()
    context = {
        'quotes': quotes,
    }
    return render(request, template, context)


@login_required
def like_quote(request, pk):
    the_quote_object = Quote.objects.get(pk=pk)
    like_quote_by_user = the_quote_object.like_set.filter(user_id=request.user.id).first()
    if like_quote_by_user:
        like_quote_by_user.delete()
    else:
        like = Like(
            quote=the_quote_object,
            user=request.user,
        )
        like.save()

    return redirect('quote_details', the_quote_object.id)



def show_all_authors(request):
    template = 'all_authors.html'
    authors = Author.objects.all()
    context = {
        'authors': authors,
    }

    return render(request, template, context)


def elements_index(request):
    template = 'elements_index.html'

    return render(request, template)


@login_required()
def add_author(request):
    template = 'authors/add_author.html'
    if request.method == "GET":
        form = AuthorForm()
        context = {
            'form': form,
        }
        return render(request, template, context)
    form = AuthorForm(request.POST, request.FILES)
    if form.is_valid():
        author = form.save()
        author.save()
        return redirect(author_details, pk=author.pk)
    context = {
        'form': form,
    }
    return render(request, template, context)





@login_required()
def edit_author(request, pk):
    template = 'authors/edit_author.html'
    author = Author.objects.get(pk=pk)
    if request.method == "GET":
        form = AuthorForm(instance=author)
        context = {
            'form': form,
        }
        return render(request, template, context)
    current_pic = author.image
    form = AuthorForm(request.POST, request.FILES, instance=author)
    new_pic = request.FILES.get('image')
    if form.is_valid():
        author.image = get_the_image(author, current_pic, new_pic)
        author = form.save()
        author.save()
        return redirect(author_details, pk=pk)
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required()
def delete_author(request, pk):
    template = 'authors/delete_author.html'
    author = Author.objects.get(pk=pk)
    form = AuthorForm(instance=author)
    context = {
        'form': form,

    }
    return render(request, template, context)





def author_details(request, pk):
    template = 'authors/author_details.html'
    author = Author.objects.get(pk=pk)
    context = {
        'author': author,
    }
    return render(request, template, context)


def idea(request):
    template = 'idea.html'
    return render(request, template)
