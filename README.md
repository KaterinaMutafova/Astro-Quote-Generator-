**Astro-Quote Generator**

![alt text](D:\Razni\IT\SoftUni\PYTHON\Python Web\quote_generator\astrology-api-stuff-packages\pics_for_github\fire.jpg)
<img src="https://github.com/KaterinaMutafova/Astro-Quote-Generator-/blob/master/astrology-api-stuff-packages/pics_for_github/fire.JPG">


**Main idea:**
The final SoftUni Project for the course Python Web Framework.
It is  called Astro-Quote Generator - "Knowledge from the Stars". 
It combines astrological knowledge and a hundred and more clever, practical,
spiritual, inspirational and deeply moving thoughts by famous and not so famous authors.


**Structure  of the  database with quotes:**
Quotes added by users, each connected to one of the 12 Zodiac signs and 
its corresponding Element(Fire, Earth, Wind, Water). Each quote is also connected
to an Author as a foreign key.

![alt text](D:\Razni\IT\SoftUni\PYTHON\Python Web\quote_generator\astrology-api-stuff-packages\pics_for_github/database.JPG)
<img src="https://github.com/KaterinaMutafova/Astro-Quote-Generator-/blob/master/astrology-api-stuff-packages/pics_for_github/database.JPG">

**Main functions:**
* --> For all users:
   * -- Generating a random quote from the whole Database
        whenever the landing page is refreshed. 
   * -- Reading all the build in information about the elements, zodiac signs etc.
    
![alt text](D:\Razni\IT\SoftUni\PYTHON\Python Web\quote_generator\astrology-api-stuff-packages\pics_for_github\daily_quote.jpg)
<img src="https://github.com/KaterinaMutafova/Astro-Quote-Generator-/blob/master/astrology-api-stuff-packages/pics_for_github/daily_quote.JPG">

* --> For registered regular users:
   * -- The regular user has a badge with one star below the profile's greeting note.
   * -- The regular user can generate a random quote from the whole Database using 
        three types of filters - a filter by Zodiac sign, Moon sign and a filter by Element.
        The filters can be used separately and combined.
   * -- The regular user can create a new quote or an author in the database.
        The user can view all the submitted quotes and authors but can edit and delete
        only the quotes that the user has added and  the  user  can only edit and authors
        which he/she has added.
        If the user manages  to provide the site with a certain number of quotes, 
        the user receives a Badge with two stars. The submitted quotes will be counted and 
        visible for the registered users in their profile. 
     
![alt text](D:\Razni\IT\SoftUni\PYTHON\Python Web\quote_generator\astrology-api-stuff-packages\pics_for_github\regular_user.JPG)
<img src="https://github.com/KaterinaMutafova/Astro-Quote-Generator-/blob/master/astrology-api-stuff-packages/pics_for_github/regular_user.JPG">
   
  
* --> For registered special users:
   * -- All functions available  to regular users.
   * -- The special user has a badge with two stars below the profile's greeting note.
   * -- The successful users will receive the  special feature to change their background theme 
        as they wish. There are several different background colour themes to choose from. 

![alt text](D:\Razni\IT\SoftUni\PYTHON\Python Web\quote_generator\astrology-api-stuff-packages\pics_for_github\special_user.JPG)
<img src="https://github.com/KaterinaMutafova/Astro-Quote-Generator-/blob/master/astrology-api-stuff-packages/pics_for_github/special_user.JPG">

* --> For the superuser and the staff:
   * -- The superuser and staff have a badge with three stars below the profile's greeting note.
   * -- All functions available  to regular and  special users plus the ability to edit
        and delete all quotes and authors. 
   * -- access to the Admin part where all CRUD functions are available plus filtering through
        the different models. 
    

![alt text](D:\Razni\IT\SoftUni\PYTHON\Python Web\quote_generator\astrology-api-stuff-packages\pics_for_github\super_user.JPG)
<img src="https://github.com/KaterinaMutafova/Astro-Quote-Generator-/blob/master/astrology-api-stuff-packages/pics_for_github/super_user.JPG">
 


**Front-end Effects:**
* --> The main background changes its colour randomly every time it is loaded(like the sky). 
* --> The decorating Star images have a hover action - they enlarge.
* --> The navbar text shines in golden colour(like  the  stars) when hovered.
* --> The dropdown menus of the navbar follow the whole style of the project.
* --> The fixed Star on the left stays on screen when scrolling, and it is a hotlink to the top.
* --> The top main front text above the main front image has a special shining effect.
* --> Bulgarian font cyrillic - Simbal

![alt text](D:\Razni\IT\SoftUni\PYTHON\Python Web\quote_generator\astrology-api-stuff-packages\pics_for_github\dropdown_hover_effect.jpg) 
<img src="https://github.com/KaterinaMutafova/Astro-Quote-Generator-/blob/master/astrology-api-stuff-packages/pics_for_github/dropdown_hover_effect.jpg">

![alt text](D:\Razni\IT\SoftUni\PYTHON\Python Web\quote_generator\astrology-api-stuff-packages\pics_for_github\star_enlargement.jpg)
<img src="https://github.com/KaterinaMutafova/Astro-Quote-Generator-/blob/master/astrology-api-stuff-packages/pics_for_github/star_enlargement.jpg">

![alt text](D:\Razni\IT\SoftUni\PYTHON\Python Web\quote_generator\astrology-api-stuff-packages\pics_for_github\star_1_reg.JPG)
<img src="https://github.com/KaterinaMutafova/Astro-Quote-Generator-/blob/master/astrology-api-stuff-packages/pics_for_github/star_1_reg.JPG">

![alt text](D:\Razni\IT\SoftUni\PYTHON\Python Web\quote_generator\astrology-api-stuff-packages\pics_for_github\stars_2_special.JPG)
<img src="https://github.com/KaterinaMutafova/Astro-Quote-Generator-/blob/master/astrology-api-stuff-packages/pics_for_github/stars_2_special.JPG">

![alt text](D:\Razni\IT\SoftUni\PYTHON\Python Web\quote_generator\astrology-api-stuff-packages\pics_for_github\stars_3_super.JPG)
<img src="https://github.com/KaterinaMutafova/Astro-Quote-Generator-/blob/master/astrology-api-stuff-packages/pics_for_github/stars_3_super.JPG">


**Backend Explanation:**
* --> Main apps:
  * --> *auth_quotes*
     *  --> Main models: 
         *  -- QuoteUser(AbstractBaseUser, PermissionsMixin)
             *  - with custom RegisterForm(UserCreationForm)
             *  - with custom LoginForm(forms.Form)
  * --> *profiles*
     *  --> Main models:
         *   -- UserProfile(models.Model)
                - with custom ProfileForm(forms.ModelForm):
  * --> *quotes*
     *  --> Main models:
         *   -- Quote - all CRUD actions for the creator of the quote and the superuser and  staff.
         *   -- Author - all CRUD actions for the creator of the quote and the superuser and  staff.
         *   -- Like - All users can like all quotes only one time. If the quote is unliked by the  user,
                the quote  becomes liked and  vice versa. 
  * --> *shared*
      * --> Templatetags
         *   -- my_filter - Adds quotation marks to all quotes in the templates 
         *   -- my_group_filter - Checks if a certain group is in the user's groups
         *   -- my_simple_tag - It gets the colour theme from the current user's
                profile and keeps it present in every open template through the hidden
                input field in 'color_theme.html' file, which is included in the 'base.html'.
      * --> Signals
         *   -- user_created - creates an extended profile to the on user creation
         *   -- add_regular_user - adds the newly created user to the group "Regular user"
         *   -- add_special_user - adds a regular user to the group "Special user" when the
                user has added a certain number of quotes to the database
         *   -- check_is_complete - Checks if the user has completed all the important fields in the profile
      * --> Validators
         *   -- Validates if there is a value in the email field


**Main filter function - explanation:**
* --> The  main function of the  site is  to generate quotes from the database, based on
    the chosen filters. The filters are combined and if all of them are selected - the
    filtered Querysets from the three are united and the generator picks from among all 
    the chosen filters. 
* --> The main page of the site generates a random quote from among the whole database.
![alt text](D:\Razni\IT\SoftUni\PYTHON\Python Web\quote_generator\astrology-api-stuff-packages\pics_for_github\main_filters.JPG)
  <img src="https://github.com/KaterinaMutafova/Astro-Quote-Generator-/blob/master/astrology-api-stuff-packages/pics_for_github/main_filters.JPG">
  
![alt text](D:\Razni\IT\SoftUni\PYTHON\Python Web\quote_generator\astrology-api-stuff-packages\pics_for_github\filtered_quote.JPG)  
<img src="https://github.com/KaterinaMutafova/Astro-Quote-Generator-/blob/master/astrology-api-stuff-packages/pics_for_github/filtered_quote.JPG">

![alt text](D:\Razni\IT\SoftUni\PYTHON\Python Web\quote_generator\astrology-api-stuff-packages\pics_for_github\filtered_quote2.JPG)  
<img src="https://github.com/KaterinaMutafova/Astro-Quote-Generator-/blob/master/astrology-api-stuff-packages/pics_for_github/filtered_quote2.JPG">

**Special JS function explanation:**
* --> Purely for entertainment and decorative purposes and in order to provide a 
    special feature to stimulate the user's activity.
   * -- In the  file 'main.js' - There ia a function which is loaded on the 
        <body> tag in the  'base.html' file and  it  is executed every time each of 
        the pages is reloaded. In the JS function there are several hard codded 
        lists consisting of different colours with common hues --> 
        (const colors0, const colors1, etc). They are all part of one big list --> 
        (let colorThemes )
   * -- These several themes correspond with named  themes with numbers in a dropdown
        field in the user's profile menu page --> 'синьо звездно небе', 'оранжево небето',
        'слънчево е!', 'лилав залез', 'сива буря',..... 
        Only the users from group "Special user", the superuser and the staff have 
        access to this  dropdown choice field in their 'edit_profile.html' pages. 
        The regular user profile's colour theme is set to the  default value of 1 
        and  if  the  user  is anonymous the colour theme is set to 0. 
   * -- There is a simple tag - my_simple_tag which extracts the profile's theme number
        from the  profile and keeps it in a hidden input field called 'colorTheme' 
        in 'color_theme.html' which is included in the 'base.html'.
   * -- Back in the JS file 'main.js' we extract the number in this field 
        from each html file as it in the 'base.html'. The  selected number is used as
        an index to the  list with all the colour themes and a certain colour theme 
        with different colours is selected. 
   * -- After that another  index  is  selected this  time  according  to the length    
        of the chosen list. And this  happens every time a page is reloaded.
   * -- the selected index is  used as an index to a list to choose from and a 
        colour is  chosen from the list.
   * -- Every time the page is reloaded the randomly selected  colour  from the  chosen
        palette is assigned to the body's background colour. 
   * -- Joy and happiness!!! Such a colourful function!
    
Colour themes:

![alt text](D:\Razni\IT\SoftUni\PYTHON\Python Web\quote_generator\astrology-api-stuff-packages\pics_for_github\background_colour_theme.jpg)
<img src="https://github.com/KaterinaMutafova/Astro-Quote-Generator-/blob/master/astrology-api-stuff-packages/pics_for_github/background_colour_theme.jpg">

![alt text](D:\Razni\IT\SoftUni\PYTHON\Python Web\quote_generator\astrology-api-stuff-packages\pics_for_github\0_colour_theme.JPG)
<img src="https://github.com/KaterinaMutafova/Astro-Quote-Generator-/blob/master/astrology-api-stuff-packages/pics_for_github/0_colour_theme.JPG">

![alt text](D:\Razni\IT\SoftUni\PYTHON\Python Web\quote_generator\astrology-api-stuff-packages\pics_for_github\1_colour_theme.JPG) 
<img src="https://github.com/KaterinaMutafova/Astro-Quote-Generator-/blob/master/astrology-api-stuff-packages/pics_for_github/1_colour_theme.JPG">

![alt text](D:\Razni\IT\SoftUni\PYTHON\Python Web\quote_generator\astrology-api-stuff-packages\pics_for_github\2_colour_theme.JPG) 
<img src="https://github.com/KaterinaMutafova/Astro-Quote-Generator-/blob/master/astrology-api-stuff-packages/pics_for_github/2_colour_theme.JPG">

![alt text](D:\Razni\IT\SoftUni\PYTHON\Python Web\quote_generator\astrology-api-stuff-packages\pics_for_github\3_colour_theme.JPG)
<img src="https://github.com/KaterinaMutafova/Astro-Quote-Generator-/blob/master/astrology-api-stuff-packages/pics_for_github/3_colour_theme.JPG">

![alt text](D:\Razni\IT\SoftUni\PYTHON\Python Web\quote_generator\astrology-api-stuff-packages\pics_for_github\4_colour_theme.JPG) 
<img src="https://github.com/KaterinaMutafova/Astro-Quote-Generator-/blob/master/astrology-api-stuff-packages/pics_for_github/4_colour_theme.JPG">

![alt text](D:\Razni\IT\SoftUni\PYTHON\Python Web\quote_generator\astrology-api-stuff-packages\pics_for_github\5_colour_theme.JPG) 
<img src="https://github.com/KaterinaMutafova/Astro-Quote-Generator-/blob/master/astrology-api-stuff-packages/pics_for_github/5_colour_theme.JPG">

![alt text](D:\Razni\IT\SoftUni\PYTHON\Python Web\quote_generator\astrology-api-stuff-packages\pics_for_github\6_colour_theme.JPG) 
<img src="https://github.com/KaterinaMutafova/Astro-Quote-Generator-/blob/master/astrology-api-stuff-packages/pics_for_github/6_colour_theme.JPG">











