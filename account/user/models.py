from django.contrib.auth.models import User

class User(User):
        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS = ['first_name', 'last_name', 'password', 'username']

        def __str__(self):
            return self.email



