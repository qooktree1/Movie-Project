from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = '__all__'


# 회원정보 변경
class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = get_user_model()
        fields = '__all__'