from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class customize(UserCreationForm):
    nickname = forms.CharField(required=False,max_length=20)
    phone = forms.CharField(required=True, max_length=11)
    # birth = models.DateField(blank=True)
    Verification_problem = forms.CharField(required=False, max_length=100)  # 验证问题
    Verification_answer = forms.CharField(required=False, max_length=50)  # 验证答案

    class Meta:
        model = User
        # fields = ('__all__')
        fields = ('username','nickname','phone','email','Verification_problem','Verification_answer','password1','password2')