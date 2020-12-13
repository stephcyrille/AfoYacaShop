from datetime import date

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def calculate_age(birthDate):
    today = date.today()
    age = today.year - birthDate.year -((today.month, today.day) < (birthDate.month, birthDate.day))
    return age


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

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name'].lower()
        if len(first_name) <= 3:
            raise ValidationError("First name must have at least 3 letters")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name'].lower()
        if len(last_name) <= 3:
            raise ValidationError("Last name must have at least 3 letters")
        return last_name

    def clean_birth_date(self):
        birth_day = self.cleaned_data['birth_date']
        tab_date = (birth_day.isoformat()).split('-')
        day = int(tab_date[2])
        month = int(tab_date[1])
        year = int(tab_date[0])
        age = calculate_age(date(year, month, day))

        if age <= 16:
            raise ValidationError("User must have at least 17 years old")
        return birth_day

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email already exists")
        return email

    def save(self, commit=False):
        str_password = self.cleaned_data['password']
        user = User.objects.create_user(
            self.cleaned_data['email'],
            self.cleaned_data['email'],
            str_password
        )
        user.refresh_from_db()  # load the profile instance created by the signal
        user.userprofile.first_name = self.cleaned_data.get('first_name')
        user.userprofile.last_name = self.cleaned_data.get('last_name')
        user.userprofile.birth_date = self.cleaned_data.get('birth_date')
        user.userprofile.gender = self.cleaned_data.get('gender')
        user.save()
        return user
