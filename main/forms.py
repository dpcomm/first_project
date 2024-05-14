from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

# class CustomUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = CustomUser
#         fields = UserCreationForm.Meta.fields + ('email',)  # 필요한 필드 추가

# class CustomAuthenticationForm(AuthenticationForm):
#     class Meta:
#         model = CustomUser
#         fields = ('username', 'password1', 'password2', 'first_name', 'phone_number')  # 사용할 필드 지정


from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=100, help_text='아이디를 입력해주세요.')
    password1 = forms.CharField(widget=forms.PasswordInput(), help_text='비밀번호를 입력해주세요.')
    password2 = forms.CharField(widget=forms.PasswordInput(), help_text='비밀번호를 확인해주세요.')
    first_name = forms.CharField(max_length=100, help_text='이름을 입력해주세요.')
    phone_number = forms.CharField(max_length=15, help_text='연락처를 입력해주세요.')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'phone_number')