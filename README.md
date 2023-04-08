# API for Yatube
REST API for the Yatube project - a social network for reading and publishing posts and comments.

The API is only available to authenticated users. Authentication in the project is done using TokenAuthentication (JWT token authentication).

Authenticated users are allowed to modify and delete their own content; otherwise, access is read-only.

It works with all modules of the Yatube social network: posts, comments, groups, followers.

Supports GET, POST, PUT, PATCH, DELETE methods.

Provides data in JSON format.

The full documentation (redoc.yaml) is available at http://localhost:8000/redoc/.

## Technologies:
- python 3.9
- Django 2.2
- djangorestframework 3.12.4
- Simple-JWT

## How to run the project:

Clone the repository and navigate to it in the command line:

```
git clone https://github.com/ya-yura/api_final_yatube.git
```

```
cd api_final_yatube
```

Create and activate a virtual environment:

```
python3.9 -m venv venv
```

```
source env/scripts/activate
```

Install dependencies from the requirements.txt file:
```
pip install -r requirements.txt
```

Run migrations:

```
python manage.py migrate
```

Run the project:

```
python manage.py runserver
```

## Request examples
The following endpoints are available in the project:

### Working with JWT tokens
```
/api/v1/jwt/create/
```
This endpoint accepts a POST request with a username and password.
```
{
    "username": "User",
    "password": "Password"
}
```
It returns a JWT token and a refresh token for refreshing the token.
```
{
    "refresh": "token_refresh",
    "access": "token_string"
}
```

```
/api/v1/jwt/refresh/
```
This endpoint accepts a POST request with a refresh token and returns a new access token.
```
{
    "access": "token_string"
}
```

```
/api/v1/jwt/verify/
```
This endpoint accepts a POST request to verify the validity of a JWT token.

###  Working with posts
```
/api/v1/posts/
```
GET request will return a list of all posts.
```
[
    {
        "id": 1,
        "author": "User",
        "image": "http://127.0.0.1:8000/media/posts/temp.jpeg",
        "text": "1 запись обновлена еще раз обновлена",
        "pub_date": "2022-12-05T06:39:10.579986Z",
        "group": 1
    },
    {
        "id": 4,
        "author": "User",
        "image": null,
        "text": "4 запись",
        "pub_date": "2022-12-05T06:58:06.532989Z",
        "group": 2
    }
]
```
It's possible to limit the number of posts.
- limit - the number of posts
- offset - the page number to start displaying from

POST request with post data
```
{
    "text": "5 запись",
    "group": 1
}
```
will create a new post.
```
{
    "id": 5,
    "author": "User1",
    "image": null,
    "text": "5 запись",
    "pub_date": "2022-12-06T08:59:47.470180Z",
    "group": 1
}
```
To add an image, it's necessary to pass it as a base64-encoded string.


```
/api/v1/posts/{id}/
```
GET request will return a post by id.

```
/api/v1/posts/5/
```
PUT and PATCH (partial update) requests
```
{
    "text": "5 запись обновлена",
    "group": 1
}
```
will update the post.
```
{
    "id": 5,
    "author": "User1",
    "image": null,
    "text": "5 запись обновлена",
    "pub_date": "2022-12-06T08:59:47.470180Z",
    "group": 1
}
```
Only the author of the post can update it.

DELETE request will delete a post by id. Only the author of the post can delete it.


###  Working with comments
```
/api/v1/posts/{post_id}/comments/
```
A GET request will return a list of all comments to the post with the specified post_id.
A POST request
```
/api/v1/posts/5/comments/
```
```
{
    "text": "Комментарий к пятому посту"
}
```
will create a new comment.
```
{
    "id": 19,
    "author": "User1",
    "text": "Комментарий к пятому посту",
    "created": "2022-12-06T09:19:42.024854Z",
    "post": 5
}
```

```
/api/v1/posts/{post_id}/comments/{id}/
```
A GET request will return the comment with the specified id to the post with the specified post_id.
PUT and PATCH (partial update) request
```
/api/v1/posts/5/comments/19/
```
```
{
    "text": "Комментарий к пятому посту обновлен"
}
```
will update the comment.
```
{
    "id": 19,
    "author": "User1",
    "text": "Комментарий к пятому посту обновлен",
    "created": "2022-12-06T09:19:42.024854Z",
    "post": 5
}
```
DELETE request deletes a publication. 
Editing and deleting a post is only available to the author of the post.


###  Working with communities
```
/api/v1/groups/
```
GET request returns a list of available communities.

```
/api/v1/groups/{id}/
```
GET request returns information about the community by ID.


###  Working with subscriptions
```
/api/v1/follow/
```
GET request returns all subscriptions of the requesting user.

```
/api/v1/follow/?search=User
```
Search subscriptions of the requesting user by User.

POST request with
```
{
  "following": "Username"
}
```
creates a subscription to the user with the given Username.
