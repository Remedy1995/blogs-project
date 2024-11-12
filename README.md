Step 1: Clone the Repository
You can clone the repository by running:

bash
Copy code
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
Step 2: Create and Activate a Virtual Environment
you should create and activate a virtual environment:

bash
Copy code
python -m venv env
# Activate the virtual environment
# On Windows
env\Scripts\activate
# On macOS/Linux
source env/bin/activate
Step 3: Install the Project Dependencies
Inside the activated virtual environment, install dependencies:

bash
Copy code
pip install -r requirements.txt

Step 5: Run Migrations
you should run the Django migrations to set up the database:

python manage.py migrate

Step 6 : Run the Django Server:
After installing the dependencies, you can run the Django app with:


python manage.py runserver
This will start the Django development server, and you should be able to access the app via http://127.0.0.1:8000/ in their browser.


Blogs
This is an API documentation guide for creating,deleting,updating and viewing blogs.
These are the various methods supported on the API's. The API leverages on a token based authentication in making requests to the API's.

﻿
Test using any API testing tool like Postman 
POST
signup
http://localhost:8000/blogs/signup/
This endpoint creates a new user using these parameters username,email,password and role

﻿

Body
raw (json)
json
{
    "username":"John1",
    "password" :"12345",
    "email" : "john@gmail.com",
     "role" :"user"
}
POST
login
http://localhost:8000/blogs/login/
This endpoint authenticates a user using a username and password that was used to signup.
A token will be generated after successful login that will be used to make further requests

﻿

Body
raw (json)
json
{
    "username":"John1",
    "password" :"12345"
}
POST
create-blog
http://localhost:8000/blogs/create-blogs/
This endpoint creates a new blog using the specified parameters in the request body and a token that was generated after successful logiin. The token should be appended in the Authorization tab as a bearer token for the request

﻿

Authorization
Bearer Token
Token
<token>
Body
raw (json)
json
{
       "title" : "Ananse The Wise King",
        "slug" : "ananse-the-wise-king",
         "author": "Micheal Ansah",
         "content":"Once upon a time",
         "categories": "Stories"
}
GET
all-blogs
http://localhost:8000/blogs/all-blogs/
This endpoint lists all blogs using a token that was generated after successful login. The token should be appended in the Authorization tab as a bearer token for the request

﻿

Authorization
Bearer Token
Token
<token>
DELETE
delete-blog
http://localhost:8000/blogs/delete-blog/4
This endpoint delete a blog using a specified id in the url and a token that was generated after successful login. The token should be appended in the Authorization tab as a bearer token for the request

﻿

Authorization
Bearer Token
Token
<token>
PUT
update-blog
http://localhost:8000/blogs/update-blog/5
This endpoint updates a blog using the specified parameters in the request body, a specified id in the url and a token that was generated after successful login.The token should be appended in the Authorization tab as a bearer token for the request

﻿

Authorization
Bearer Token
Token
<token>
Body
raw (json)
json
{
       "title" : "Mary the Seer",
        "slug" : "mary-the-seer",
         "author": "Jonas Abekah",
         "content":"Mary lives in the world",
         "categories": "Folktales"
}
GET
view-a-blog
http://localhost:8000/blogs/blogs/5
This endpoint views a blog using the specified id in the url and a token that was generated after successful login. The token should be appended in the Authorization tab as a bearer token for the request

﻿

Authorization
Bearer Token
Token
<token>