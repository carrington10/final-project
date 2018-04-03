from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreationForm(UserCreationForm):
    class meta:
        ## create fields for account form
        fields = ("username","email","password1","password2")
        model = User

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            self.fields["username"].label = "Display name"
            self.fields["email"].label = "Email Address"
