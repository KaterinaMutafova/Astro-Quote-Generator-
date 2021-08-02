
import random
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from quote_generator.profiles.models import UserProfile
from quote_generator.quotes.forms import QuoteForm, AuthorForm, MyElementForm
from quote_generator.quotes.models import Quote, Author


# Create your views here.

def get_color_theme(request):
    pass


def base(request):
    quotes = Quote.objects.all()
    the_quote_object = random.choice(quotes)

    context = {
        'quotes': quotes,
        'the_quote_object': the_quote_object,

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
        return redirect(quote_details, pk=quote.pk)
    context = {
        'form': form,
    }
    return render(request, template, context)


def edit_quote(request, pk):
    quote = Quote.objects.get(pk=pk)
    template = 'quotes/edit_quote.html'
    if request.method == 'GET':
        form = QuoteForm(instance=quote)
        context = {
            'form': form,
        }
        return render(request, template, context)
    form = QuoteForm(request.POST, request.FILES, instance=quote)
    if form.is_valid():
        quote = form.save()
        quote.save()
        return redirect(quote_details, pk=pk)
    context = {
        'form': form,
    }
    return render(request, template, context)



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
    quote.delete()
    return redirect(show_all_quotes)


def quote_details(request, pk):
    the_quote_object = Quote.objects.get(pk=pk)
    quotes = Quote.objects.all()
    count_quotes = len(quotes)
    template = 'quotes/quote_details.html'
    if the_quote_object.pk == 1:
        prev_pk = count_quotes
    else:
        prev_pk = pk -1
    if the_quote_object.pk == count_quotes:
        next_pk = 1
    else:
        next_pk = pk + 1
    prev_quote = Quote.objects.get(pk=prev_pk)
    next_quote = Quote.objects.get(pk=next_pk)
    context = {
        'the_quote_object': the_quote_object,
        'prev_quote': prev_quote,
        'next_quote': next_quote,
        'count_quotes': count_quotes,


    }
    return render(request, template, context)


@login_required()
def change_quote(request):
    template = 'quote_in_balloon.html'
    if request.method == "GET":
        quotes = Quote.objects.all()
        count_quotes = len(quotes)
        index = random.randint(1, count_quotes)
        quote = Quote.objects.get(pk=index)
        elementform = MyElementForm()

        context = {
            'quote': quote,
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


    the_quote_object = random.choice(quotes)
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
    print(form)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {
        'form': form,
    }
    return render(request, template, context)


