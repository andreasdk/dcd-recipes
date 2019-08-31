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

"**_As a user, I want:_**"
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
- [Flask 1.0.2](http://flask.pocoo.org/)
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

**View All Recipes**
- On the recipes page, recipes cards are display from oldest to most recent. There is pagination, with a limit of 8 recipes per page. There is also a search bar which returns a list of recipes depending on the searched keyword. There is also a message for the user if their search results in no recipes being found.


##### back to [top](#table-of-contents)

---

## Technologies Used
- [Git](https://git-scm.com/) Used for version control of project code.
- [GitHub](https://github.com/) - Used to remotely store project code.
- [VS Code](https://code.visualstudio.com/) - The IDE I used for developing this project.
- [Imgbb](https://imgbb.com) to store all external images for this project.
- [Giphy](https://giphy.com/create/gifmaker) For creating the gifs used in this README.md file.
- [OBS](https://obsproject.com/) For recording screen captures of websites features for this README.md file.

### Libraries
- [Bootstrap 4.3.1](https://getbootstrap.com/) Used for its responsive design framework.
- [JQuery 3.4.0](https://jquery.com) Used for simplified DOM manipulation.
- [Google Fonts](https://fonts.google.com/) Used to import custom fonts.
- [FontAwesome](https://fontawesome.com/) For the icons used through the Whisk Recipes website.

### Front-End Technologies
- [HTML](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - Used to write markup text.
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3) - Used to creatwe custom styles


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