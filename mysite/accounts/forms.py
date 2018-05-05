from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from accounts.models import UserProfile



# defines a form for the user to signup
class SignupForm(UserCreationForm):
    email =forms.EmailField(required = True)
# define meta data that relates to class
    class Meta:
        model =User
        fields = (
                    'username',
                    'first_name',
                    'last_name',
                    'email',
                    'password1',
                    'password2'
                )
        ## save the data to itself
        def save(self,commit=True):
            user = super(SignupForm,self).save(commit = False)
            # clean django function
            user.first_name = self.clean_data['first_name']
            user.last_name = self.clean_data['last_name']
            user.email = self.clean_data['email']
## if you want to save the user data then saves to the database
            if commit:
                user.save()
            return user

class EditProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields =(
        'name',
        'email',
        'city',
        'bio',
        'favanime',
        'image',
        )
