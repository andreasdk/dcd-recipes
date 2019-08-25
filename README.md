# [Whisk Recipes](https://whisk-recipes.herokuapp.com/)

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
- *see a list of my own recipes*
- *to view recipes* without needing to sign up.

### Design

This site was built using Bootstrap, as well as refactored designs I used in my previous milestones. On the homepage, recipes page and account page, recipes are displayed as cards that, when clicked, lead to the individual recipe page.

#### Framework

- [Bootstrap 4.3.1](https://getbootstrap.com//)
    - I chose Bootstrap for its ease of use, its minimal use of classes compared to other front-end libraries, and its ability to be easily customized.
- [jQuery 3.3.1](https://code.jquery.com/jquery/)
    - I am using the version of jQuery recommended with Bootstrap for features like the navbar.
- [Flask 1.0.2](http://flask.pocoo.org/)
    - I've used the Python framework to create routes, functions and templates for the back-end of the website.