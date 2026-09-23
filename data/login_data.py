INVALID_LOGIN_DATA = [
    (
        "invalid_user",
        "secret_sauce",
        "Username and password do not match",
    ),
    (
        "standard_user",
        "wrong_password",
        "Username and password do not match",
    ),
    (
        "",
        "secret_sauce",
        "Username is required",
    ),
    (
        "standard_user",
        "",
        "Password is required",
    ),
]