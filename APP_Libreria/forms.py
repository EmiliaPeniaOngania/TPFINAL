from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm, User


class UserRegistrationForm(UserCreationForm):
     email=forms.EmailField()
     password1 =forms.CharField(label='Constraseña',widget=forms.PasswordInput)
     password2 =forms.CharField(label='Repetir Contraseña',widget=forms.PasswordInput)
    
class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_text = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    last_name =forms.CharField(label='Apellido')
    first_name=forms.CharField(label='Nombre')
    email=forms.EmailField()
    
    class Meta:
        model = User
        fields = ['last_name','first_name','email']
        help_text = {k:"" for k in fields}

class AvatarForm(forms.Form):
    imagen= forms.ImageField()

class InformacionAdicionalForm(forms.Form):
    descripcion_personal= forms.CharField(max_length=200)
    pagina_web=forms.URLField(max_length=200)

class ReseniaForm(forms.Form):
    nombre_libro = forms.CharField(max_length=64)
    puntaje = forms.IntegerField()
    reseña = forms.CharField(max_length=280)

class ImagenForm(forms.Form):
    nombre_libro= forms.CharField(max_length=64)
    imagen= forms.ImageField()