from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class AddEndUserForm(forms.Form):
    first_name = forms.CharField(label="Nom", max_length=150,
                                 widget=forms.TextInput(
                                     attrs={"class": "input100", "autocomplete": "off", "required": "true"})
                                 )
    last_name = forms.CharField(label="Prenom", max_length=150,
                                widget=forms.TextInput(
                                    attrs={"class": "input100", "autocomplete": "off", "required": "true"})
                                )
    birth_date = forms.DateField(label="Nom d'utilisateur",
                                 widget=forms.DateInput(
                                     attrs={"class": "input100", "type": "date", "required": "true"})
                                 )
    email = forms.EmailField(label="Adresse email",
                             widget=forms.EmailInput(
                                 attrs={"class": "input100", "autocomplete": "off", "required": "true"})
                             )
    password = forms.CharField(label="Mot de passe", max_length=150,
                               help_text="Le mot de passe doit être composé d'une majuscule, "
                                         "un chiffre et un symbole au minimum",
                               widget=forms.PasswordInput(
                                   attrs={"class": "input100", "autocomplete": "off", "required": "true"})
                               )
