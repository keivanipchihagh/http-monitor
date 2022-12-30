# http-monitor
Real-Time HTTP monitor service written in Python


## Endpoints
### Authentication
-  `[POST] /auth/api/signup`

    - Registers the user and returns the same form back as the response.
    - Request Body:
        ```
        {
            "firstname": "Keivan",
            "lastname": "Ipchi Hagh",
            "username": "keivanipchihagh",
            "email": "keivanipchihagh@gmail.com",
            "password": "1234",
        }
        ```

- `[POST] /auth/api/signin`
    - Logins the user and returns the token and expiry date of the token as the response.
    - Request Body:
        ```
        {
            "username": "keivanipchihagh",
            "password": "1234",
        }
        ```

- `[POST] /auth/api/signout`
    - Logsout the user and returns an empty response with 204 response code.
    - Request Header:
        ```
        {
            "Authorization": "Token d418e09d53b1cc8e9a99221de1dd97382034ffccba402eb291e4f552eea76c02"
        }
        ```

- `[POST] /auth/api/signout-all`
    - Logsout the user from everywhere and returns an empty response with 204 response code.
    - Request Header:
        ```
        {
            "Authorization": "Token d418e09d53b1cc8e9a99221de1dd97382034ffccba402eb291e4f552eea76c02"
        }
        ```