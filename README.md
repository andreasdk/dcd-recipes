# [Whisk Recipes](https://whisk-recipes.herokuapp.com/)

<img src="https://i.ibb.co/bWW5sNd/home.png" alt="Whisk Home Page" width="800">

---

## Table of Contents
1. [**UX**](#ux)
    - [**User Stories**](#user-stories)
    - [**Design**](#design)
        - [**Framework**](#framework)
        - [**Color Scheme**](#color-scheme)
        - [**Icons**](#icons)
        - [**Typography**](#typography)
    - [**Wireframes**](#wireframes)

2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features Left to Implement**](#features-left-to-implement)

3. [**Technologies Used**](#technologies-used)
    - [**Libraries**](#Libraries)
    - [**Front-End Technologies**](#front-end-technologies)
    - [**Back-End Technologies**](#back-end-technologies)

4. [**Testing**](#testing)
    - [**Validators**](#validators)
    - [**Compatibility**](#compatibility)
    - [**Known Issues**](#known-issues)

5. [**Deployment**](#deployment)
    - [**Local Deployment**](#local-deployment)
    - [**Remote Deployment**](#remote-deployment)

6. [**Credits**](#credits)
    - [**Content**](#content)
    - [**Media**](#media)
    - [**Code**](#code)
    - [**Acknowledgements**](#acknowledgements)

---

## UX

This project is the assessment of the Python/Flask/MongoDB modules for the Full Stack Software Development degree at [Code Institute](https://codeinstitute.net/). I chose to create a web application that allows users to store and easily access cooking recipes. Each user should be able to  **C**reate, **R**ead, **U**pdate, and **D**elete (**CRUD**) their own recipes.

### User Stories

"**As a user, I want:**"
- *to view the site* on my preferred device (mobile, tablet, desktop).
- *to create my own profile*
- *to add recipes to the website*
- *to edit my recipes*
- *to delete my recipes*
- *to change my password*
- *to see a list of my own recipes*
- *to search for recipes using keywords*
- *to view recipes* without needing to sign up.

### Design

This site was built using Bootstrap, as well as refactored designs I used in my previous milestones. On the homepage, recipes page and account page, recipes are displayed as cards that when clicked, lead to the individual recipe page.

#### Framework

- [Bootstrap 4.3.1](https://getbootstrap.com//)
    - I chose Bootstrap for its ease of use, its minimal use of classes compared to other front-end libraries, and its ability to be easily customized.
- [jQuery 3.3.1](https://code.jquery.com/jquery/)
    - I am using the version of jQuery recommended with Bootstrap for features like the navbar.
- [Flask 1.1.1](http://flask.pocoo.org/)
    - I've used the Python framework to create routes, functions and templates for the back-end of the website.

#### Color Scheme

I used a charcoal color for the navbar and header, and then a mid green color (#57ba98) as the primary color for headings, buttons, and backgrounds. My goal was to use different tones of one color as the primary colors so that the overall design is cohesive.

- ![#57BA98](https://placehold.it/15/57BA98/57BA98) `#57BA98` (**mid-green** - *primary-color*)
- ![#65CCB8](https://placehold.it/15/65CCB8/65CCB8) `#65CCB8` (**light green** - *primary-color-light*)
- ![#3B945E](https://placehold.it/15/3B945E/3B945E) `#3B945E` (**dark green** - *primary-color-dark*)
- ![#ff0000](https://placehold.it/15/ff0000/ff0000) `#ff0000` (**red** - *secondary-color*)
- ![#f7f7f7](https://placehold.it/15/f7f7f7/f7f7f7) `#f7f7f7` (**light grey** - *grey-color-light-1*)
- ![#777](https://placehold.it/15/777/777) `#777` (**dark grey** - *grey-color-dark-1*)
- ![#999](https://placehold.it/15/999/999) `#999` (**dark grey** - *grey-color-dark-2*)
- ![#333](https://placehold.it/15/333/333) `#333` (**charcoal grey** - *grey-color-dark-3*)
- ![#fff](https://placehold.it/15/fff/fff) `#fff` (**white** - *white-color*)

#### Icons
- [Font Awesome](https://fontawesome.com/)
    - I used Font Awesome icons for the navbar, footer, search bar, and recipe page. I used them in the navbar to give a visual clue as to what page each link leads to. In the footer, the icons direct to my GitHub and LinkedIn accounts.

#### Typography

- I specified two fonts from [Google Fonts](https://fonts.google.com/) in my CSS variables. Roboto Condensed is used as the primary font of the website, and Cabin is used paragraphs and form labels. I chose only two so that the website content would be easily readable.
    - [Roboto Condensed](https://fonts.google.com/specimen/Roboto+Condensed)
    - [Cabin](https://fonts.google.com/specimen/Cabin)

##### back to [top](#table-of-contents)


---

## Features

### Existing Features

<img src="https://media.giphy.com/media/dBxUpnPh0icOHWI81v/giphy.gif" alt="Navbar Desktop" width="800">

**Navbar**
- The navbar is displayed on the homepage, recipes page, search page, single recipe page and the account page. In its logged out state, it displays links to the home page, the recipes page, the login page, and the register page. Each link has an icon to give a visual clue as to the linked page content. On desktop,
the links have a hover effect which causes the background and text color to invert via a right side sliding animation. On smaller tablet and mobile screens, the navbar is accessed via a toggler and the nav links are centred.

<img src="https://i.ibb.co/YDGVMYJ/navbardefault.png" alt="Navbar Default Desktop" width="800">

- Visitors who are not logged in, or who have no account see the following navbar links.
    1. Home
    2. Recipes
    3. Login
    4. Register 

<img src="https://i.ibb.co/fNfj6Z2/navbarsignedin.png" alt="Navbar Signed In Desktop" width="800">

- Logged in users see the following navbar links.
    1. Home
    2. Recipes
    3. Add A Recipe
    4. Account
    5. Logout 
        
<img src="https://media.giphy.com/media/VHwnNiRIzFC1Itd7ux/giphy.gif" alt="Successful User Registration" width="800">

**Account Registration**
- A user can register an account by creating a username and a password. The username must be unique and be between 2 and 20 characters long. The username input field has a red bottom border while unvalidated, which changes to the primary color (#57BA98) when validated. The same validation style applies to the password fields, which must match in order for a registration to be successful. If the username is not unique or the passwords do not match, the website will redirect to the register page, and a flash message appears to guide the user. This page does not have a navbar, but can be closed by clicking the close icon in the top right corner. This redirects to the homepage.

<img src="https://media.giphy.com/media/ZXYNyebaOurWYNpjnH/giphy.gif" alt="Successful User Login" width="800">

**Account Login**
- A user can  log in to their account by inputting their username and password. The username input field has a red bottom border while unvalidated, which changes to the primary color (#57BA98) when validated. The same validation style applies to the password field. Validation in the login form means that both fields must be filled in. If the user inputs the wrong username and/or password, they are redirected back to the form. A flash message appears to give them feedback about why login was not successful. This page does not have a navbar, but can be closed by clicking the close icon in the top right corner. This redirects to the homepage.

<img src="https://media.giphy.com/media/l2vVm0Xx1m65RiIuBo/giphy.gif" alt="Successful User Password Change" width="800">

**Change Password**
- A user can  change their password by inputting their current password, and then inputting and confirming their new password.The username input fields have the same validation style as the register and login forms. Validation in the password change form means that all fields must be filled in. If the user inputs the wrong current pasword and/or the new passwords do not match, they are redirected back to the form. A flash message appears to give them feedback about why the form submission was not successful. This page does not have a navbar, but can be closed by clicking the close icon in the top right corner. This redirects to the user account page.

<img src="https://media.giphy.com/media/StjNcaawUBAUmyDSPY/giphy.gif" alt="User Logout" width="800">

**Account Logout**
- When a user logs in, the login and registration links no longer appear on the navbar. Instead, the user sees links to add a recipe, to view their account page, and to log out. On clicking logout, the session is ended and the user is redirected to the homepage.

<img src="https://media.giphy.com/media/kILsAv77Z7IueoCIiJ/giphy.gif" alt="View All Recipes" width="800">

**View All Recipes**
- On the recipes page, recipes cards are display from oldest to most recent. There is pagination, with a limit of 8 recipes per page. There is also a search bar which returns a list of recipes depending on the searched keyword. There is also a message for the user if their search results in no recipes being found. A user can click on a recipe card to be directed to the individual recipe page.

<img src="https://media.giphy.com/media/WSqmi1HcIzzBljep18/giphy.gif" alt="View A Single Recipe" width="800">

**View A Single Recipe**
- A user can click on a recipe card from the homepage, the recipes page, and the search page to access a single recipe. A recipe display the recipe name, meal type, diet type if entered, prep and cooking time, recipe image, ingredients and directions.

<img src="https://media.giphy.com/media/RIeof95NXLp0kW2qMO/giphy.gif" alt="View A Single Recipe" width="800">

**Search For Recipes**
- On the recipes page, a user can search the recipes collection by entering a keyword. They are then directed to the search page, with the results of their search. This page has pagination with a maximum of 8 results per page. The page automatically scrolls to the search results section.

**Create A Recipe**
- A logged in user is able to create a recipe by clicking on the 'Add Recipe' link in the navbar. They are then invited to fill in a recipe form with the relevant recipe data.

**Update A Recipe**
- A logged in user who is also the author of a given recipe is able to update that recipe by clicking on the 'Update Recipe' button on the recipe page. Only the logged in author can see this button. They are then invited to edit the recipe via the recipe form, pre-filled with the relevant recipe data.

**Delete A Recipe**
- A logged in user who is also the author of a given recipe is able to delete that recipe by clicking on the 'Delete Recipe' button on the recipe page. Only the logged in author can see this button. Clicking this button removes the recipe from the database. Users is redirected to the homepage upon deletion of a recipe.


### Features Left to Implement

Due to time constraints, there are some additional features I wasn't able to implement.

**Search From Select**
- Currently a user can search by inputting keywords to a search bar. I would also like to implement searching by choosing an option from a select element. These could be based on the meal-type and diet-type select fields.

**Delete Account**
- I would like for a user to be able to delete their account and thus remove all their recipes from the database.

##### back to [top](#table-of-contents)

---

## Technologies Used
- [Git](https://git-scm.com/) Used for version control of project code.
- [GitHub](https://github.com/) - Used to remotely store project code.
- [VS Code](https://code.visualstudio.com/) - The IDE I used for developing this project.
- [Imgbb](https://imgbb.com) to store all external images for this project.
- [Giphy](https://giphy.com/create/gifmaker) For creating the gifs used in this README.md file.
- [OBS](https://obsproject.com/) For recording screen captures of websites features for this README.md file.
- [Convertio](https://convertio.co/mp4-webm/) Used to convert the homepage header video to webm format.

### Libraries
- [Bootstrap 4.3.1](https://getbootstrap.com/) Used for its responsive design framework.
- [JQuery 3.4.0](https://jquery.com) Used for simplified DOM manipulation.
- [Google Fonts](https://fonts.google.com/) Used to import custom fonts.
- [FontAwesome](https://fontawesome.com/) For the icons used through the Whisk Recipes website.

### Front-End Technologies
- [HTML](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - Used to write markup text.
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3) - Used to create custom styles.


### Back-End Technologies
- **Python**    
    - [Python 3.6.8](https://www.python.org/) - Used as the back-end programming language.
    - [MongoDB Atlas](https://www.mongodb.com/) - The database used to store website backend data.
    - [PyMongo 3.8.0](https://api.mongodb.com/python/current/) - Used for interacting with MongoDB database from Python.
    - [WTForms 2.2.1](https://pypi.org/project/WTForms/) - I used WTForms to handle form rendering and validation.
    - [Python dotenv](https://github.com/theskumar/python-dotenv) - Gets and sets values in the .env file.
- **Flask**
    - [Flask 1.1.1](http://flask.pocoo.org/) - To construct and render templates.
    - [Werkzeug 0.15.5](https://werkzeug.palletsprojects.com/en/0.15.x/) - Used for generating and verifying password hashing.
    - [Flask Blueprints](http://flask.pocoo.org/docs/1.0/blueprints/) - I used Blueprints to split the app into modules.
    - [Jinja 2.10.1](http://jinja.pocoo.org/docs/2.10/) - To display back-end data in the front-end.
- **Heroku**
    - [Heroku](https://www.heroku.com) - This app is hosted via Heroku.


##### back to [top](#table-of-contents)

---

## Testing

I manually tested the website with debugger.
```python
debug=True
```
Whenever the app crashed, debugger displayed an error message that made it clear what was causing the error. I was able to resolve issues by going back to the routes and templates and examining the relevant code.

**User Registration**
I created my own account and tested website features with it. I can log in, update my password, add, edit, and delete my own recipes. I also made test accounts to see if it was possible to delete or edit another user's recipes from another account.

**Add A Recipe**
I made dummy recipes to test the create recipe function. I tested submitting a recipe with no image to see if the placeholder image would appear, and it does. I attempted to submit the form without some required fields, but it wasn't possible.

**Update A Recipe**
I tested a number of recipes to make sure the edit recipe function was working correctly. When the form is successfully validated, the recipe updates with the new data.

**Delete A Recipe**
I tested the delete function on dummy recipes, and it removes the selected recipe from the database.

**Read A Recipe**
Individual recipes were tested by clicking on the recipe cards. The recipe data is successfully displayed on screen. The ingredient and directions arrays are successfully iterated over and displayed as lists.

**Pagination**
- Default Pagination
    - Recipe card per page successfully limited to 8
    - Current page link is disabled
    - Correct number of page buttons appear
    - Each page buttons links to the correct page
    - Each page displays correct page URL
    - When more recipes are added to DB, more page numbers are subsequently added to pagination

- Search Pagination
    - Recipe cards per page successfully limited to 8
    - No pagination is results == 0
    - 1 paginated page if result = 1
    - 1 paginated page if results < 8
    - Correct number of pagination buttons if results > 8


**Search**
To test the search function, I searched with keywords that should have returned results as well as searching with irrelevant keywords. I also tested the pagination to make sure the search keywords carried over to the selected page, and that the window automatically scrolled to the search results on the selected page.

### Validators


**HTML**
- [W3C HTML Validator](https://validator.w3.org) - WC3 does not understand the Jinja templating language, so throws up errors for that. It also does not currently understand loading="lazy" as this is a new Chrome feature since version 76. Other than the Jinja errors, the code is validated.


**CSS**

**JavaScript**
-[Esprima](https://esprima.org/demo/validate.html)
 -"Code is syntactically valid."
 -There is only one line of JS in this app, for scrolling to the search results in the search pagination

## Deployment

### Local Deployment

To run this project locally, you need the following:
- An IDE. I used [Visual Studio Code](https://code.visualstudio.com/) but you are free to use one of your choice.

The following **must be installed** on your machine:
- [PIP](https://pip.pypa.io/en/stable/installing/)
- [Python 3](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) to create your own database.

### Instructions
- Save a copy of this GitHub repository by clicking the 'Clone or download' button at the top of the page, then on 'Download ZIP'. Extract the ZIP file to the folder you will be working in. Alternatively, if you have Git installed locally, you can clone the repository with the following command:
    - `git clone https://github.com/andreasdk/dcd-recipes`.
- Open a terminal window and change directory (cd) to the directory you extracted the files in.
- Create a **.env** file with the connection to your MongoDB database, and a secret key. It should look something like this:
```
MONGO_URI='Your Mongo URI Details'
SECRET_KEY='Your secret key' 
```  
- Create a **.flaskenv** file, specifying the following:
    - `FLASK_APP=run.py`
    - `FLASK_ENV=development`
- Install all required modules with the command:
    - `sudo -H pip3 -r requirements.txt`
- Create a new database on MongoDB and name it whisk. In the database, create the following two collections:

**USER**
```
_id: <ObjectId>
username: <String>
pass: <String>
user_avatar: <String>
user_recipes: <Array>
```
**RECIPES**
```
_id: <ObjectId>
recipe_name: <String>
description: <String>
meal_type: <String>
diet_type: <String>
prep_time: <String>
time: <String>
image: <String>
ingredient_name: <Array>
directions: <Array>
author: <ObjectId>
```

- You can now run the application by running the following command:
    - `flask run`
    - The website will run now on *localhost* `http://127.0.0.1:5000`


### Remote Deployment

The app can be deployed via [Heroku](https://www.heroku.com/). To deploy, you need to do the following:

- In the terminal, create a `requirements.txt` file using the command `pip freeze > requirements.txt`.
- In the terminal, create a `Procfile` by running the `echo web: python app.py > Procfile` command.
- Push these files to your GitHub repository.
- Create a new app on [Heroku dashboard](https://dashboard.heroku.com/apps), give it a name and set the region to whichever is closest to you.
- Link the Heroku app to your GitHub repository.
- Set the config vars as follows:

| Key | Value |
 --- | ---
DEBUG | FALSE
IP | 0.0.0.0
MONGO_URI | `mongodb+srv://<username>:<password>@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority`
PORT | 5000
SECRET_KEY | `<your_secret_key>`

The MONGO_URI and SECRET_KEY should match the ones in your **.env** file.

- Click 'Deploy' in the Heroku Dashboard, and select 'enable automatic deployment'.

- It should now be possible to launch the app via Heroku.

##### back to [top](#table-of-contents)

## Credits

### Content

- [BBC Good Food](https://www.bbcgoodfood.com/) - All recipes added by me on the website, as well as recipe images come from this website.

### Media

The website images (excluding the recipe images) were taken from the following sources:

- **Recipe Placeholder Image** : [Google Image Search](http://i0.wp.com/cdn11.bigcommerce.com/s-571px4/images/stencil/original/products/1559/4041/WD413_Chef_Face_and_Hat_Wall_Decal_Art_Kitchen_Decor_Red_Room_Pic__57934.1464377687.JPG?c\u003d2\u0026imbypass\u003don?strip=all)
- **User Avatars** : [Iconfinder](https://www.iconfinder.com)
- **Register, Login, Change Password form bg-image** : [Unsplash](https://unsplash.com/photos/QnNqGoCnBg0)
- **Mockup images used in README** : [techsini](https://techsini.com/multi-mockup/)

The homepage header video came from:
- **Coverr** : [Coverr](https://coverr.co/videos/Pinangat%20Making)

### Code

- **Navbar animation, user registration form styles, heading styles, utilities styles, search bar styles** [Jonas Schmedtman Advanced CSS & Sass](https://www.udemy.com/advanced-css-and-sass)
- **Flask Tutorials** - [Corey Schafer](https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH)
- **The Flask Mega-Tutorial** - [Miguel Grinberg](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- **Search Function** [johnnycistudent](https://github.com/johnnycistudent/recipe-app)

### Acknowledgements

- [Tim Nelson](https://github.com/TravelTimN)
    - Fellow Code Institute student who helped me out a lot building routes.
- Slack Users **Shane Muirhead, John_Lynch_Alumnus**
    - Code Institute students who were very reactive on Slack to help out when I asked questions.


##### back to [top](#table-of-contents)