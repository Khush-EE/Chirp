# Chirp

Chirp was born out of a simple idea: to create a space where everyone can express themselves freely and authentically. In a world where information flows faster than ever, we wanted to design a platform that not only keeps up with the pace but also adds value to your social media experience. Whether it’s breaking news, viral trends, or heartfelt moments, Chirp is here to keep you in the loop.

# Installation

- First fork this repository
- Clone it in your local machine
- Then go to your project directory
```bash
cd Chirp
```

- Now lets create a virtual environment by the following commands. Run this commands one by one.
```bash
pip install virtualenv
python -m venv myenv
myenv\Scripts\activate
```

- Now there you will find one requirements.txt files which contains all the required packages and dependencies. To install it, run the following command
```bash

pip install -r requirements.txt
```

- Okay so now all the dependencies are installed in the environment. Now you will find another Chirp folder. Go there by
```bash
cd Chirp
```

- Now run the development server by the command
```bash
python manage.py runserver
```

- Now you can use chirp on your http://localhost:8000 port.

# Contributing In Frontend
All the html files are located in templates folder which is in home folder. All css and js files are located in static folder. The css page name is always same as its html name. You can edit them.

## Data Models
The data is stored in two SQL tables namely `users` and `chirps`, where user tables contains the users data and chirps contains all the post from various users (similar to tweets). In users table you have data fields
- username
- email
- profile_pic
- headline
- bio
- name
- password

And in chirps table, we have
- user
- content
- image
- datetime

You dont have to write any SQL, its already written in backend, you just need to use this fields to create an amazing UI. Some of this fields have been used in the templates. To use this variables, you have to enclose them in two curly braces like `{{user.username}}`.