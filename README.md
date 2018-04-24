# Luna group project 

## History

So we have recently discovered that Yelp wants to move his current stack to a new one based on Python/Dajngo and ES6/React, they also want to replace his old fashioned Bootstrap UI framework with a supercool UI. 

For this herculean task they will hire a whole new team and selection process is starting now. A prototype following their wireframes is mandatory for all those that want to participate.

## Project specifications

### Docker integration

- Project can be developed inside a docker container
- Docker container has SSH access during development
- PyCharm can access the container python environment with a remote ssh interpreter
- PyCharm can run management commands with the _manage.py_ file inside the container.

### Testing

- Your code gets tested on **gitlab** every time you make a new commit
- Every endpoint has at least one or more tests executed when you run `$ python manage.py test`
- Tests are having a master test class that has basic functionality implemented.
- Tests cover not only success but also error messages that are expected from the API
- Tests cover also if a user has not rights to change or update data in the database. (test for right error messages)

### Permissions

- Implement object based permission check with the `GenericAPIView` or by calling `self.check_object_permissions(self.request, obj)` yourself inside the view where ever it's needed.
- Add `DEFAULT_PERMISSION_CLASSES` to make sure every endpoint needs an authentication without declearing it every time.

### Clean code

- Run `flake8` tests every time you commit on the **gitlab** runner server to make sure your stick to the PEP8 standard.
- Make sure you structure your code enought that every file is not lager than 100-200 lines.
- Keep your imports clean and short by using file imports instead of direct imports of classes and definitions.

### Documentation

- Activate the built-in docs package to make sure your API's can be viewed in a browser and have meaningfull documentation: [DRF custom documentation][drf-custom-docs]
- Make some good comment for each of your views so they get displayed in the docs frontend. (blockcomments - docstrings)

### Authentication

Implement a **JWT authentication** for DRF with this package: [JWT Authentication for DRF][jwt-auth]

### Features

This is a list of features that Yelp would like to see in all web prototypes:

#### General

* A user should be able to create a new account.
* A user should be able to update his profile: 
  * First name, last name, email and password.
* A user should be able to log in.
* A user should be able to log out.
* A user should be able to delete its account.

#### Anonymous user can do:

- View the list of the restaurants
- View the details of a restaurant
- View the contact page of your Luna project
- View the about page of your Luna project
- Search/Filter for restaurants by string or category
- Register himself on the website

#### Registered user can do:

- Create a restaurant
- Create a review of a restaurant
- View/Update/Delete a restaurant review of himself
- Like/Remove like a restaurant review
- Crate a comment on a restaurant review
- Like/Remove like a comment
- Update his userprofile
- Reset his password

#### A restaurant contains

- ID
- Name
- Address
- E-Mail
- Phone
- Logo
- Photos
- Categories
- Pricerange
- Website
- Opening hours

-----

**Details**

- Take reservations
- Delivery
- Take away
- Credit cards
- WIFI
- Nocie level
- Waiter service

#### A restaurant review contains

- ID
- Title
- Text-Content
- Raiting | 1-5 stars
- Date created
- Date modified
- User
- Restaurant
- Photos
- Likes

#### User contains

- ID
- First name
- Last name
- Username
- Address
- Email
- Phone
- Joined date
- Profile picture
- Photos
- Profile description

#### Comments on a review contains

- ID
- User
- Review
- Text content
- Date created
- Date modified
- Likes

### REST API backend endpoints

**Auth**

- `/api/auth/token/` **POST**: Get a new JWT by passing username and password
- `/api/auth/token/refresh/` **POST**: Get a new JWT by passing an old still valid JWT.
- `/api/auth/token/verify/` **POST**: Verify a token by passing the token in the body
- `/api/auth/password-reset/` **POST**: Reset users password by sending a validation code in a email
- `/api/auth/password-reset/validate/` **POST**: Validate password reset token and set new password for the user


[drf-custom-docs]: http://www.django-rest-framework.org/topics/documenting-your-api/#built-in-api-documentation
[jwt-auth]: https://github.com/davesque/django-rest-framework-simplejwt
[pagination-docs]: http://www.django-rest-framework.org/api-guide/pagination/