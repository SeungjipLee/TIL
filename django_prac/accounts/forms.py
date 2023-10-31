from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email')

class CustomUserChangeFrom(UserChangeForm):
    class Meta(UserChangeForm):
        model = get_user_model()
        fields=('first_name', 'last_name', 'email',)
