from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from .models import CustomUser

class Cucf(UserCreationForm):
    class Meta:
        model= CustomUser
        fields= UserCreationForm.Meta.fields + ("age",)

class Cuchangef(UserChangeForm):
    class Meta:
        model = CustomUser
        fields= UserChangeForm.Meta.fields
