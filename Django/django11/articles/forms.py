from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

class UsersForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("username", "password1", "password2")
        
        
class zzUserChangeForm(UserChangeForm):
    class Mata:
        model = get_user_model()
        fields = '__all__'