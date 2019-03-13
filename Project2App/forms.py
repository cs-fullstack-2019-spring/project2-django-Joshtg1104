from django import forms
from .models import WikiModel, RelatedContentModel, NewUserModel
from django.contrib.auth.models import User


class WikiForm(forms.ModelForm):
    class Meta:
        model = WikiModel
        exclude = ["wikiForeignKey"]


class RelatedContentForm(forms.ModelForm):
    class Meta:
        model = RelatedContentModel
        exclude = ["relatedForeignKey"]


class NewUserForm(forms.ModelForm):
    class Meta:
        model = NewUserModel
        exclude = ["userForeignKey"]

        def clean_password1(self):
            password1Data = self.cleaned_data.get("password1")
            password2Data = self.cleaned_data.get("password2")
            print(password1Data)
            print(password2Data)
            if str(password1Data) != str(password2Data):
                raise forms.ValidationError("Password does not match")
            return password1Data

        def clean_username(self):
            usernameData = self.cleaned_data.get("username")
            print(usernameData)
            if User.objects.filter(username=usernameData).exists():
                raise forms.ValidationError("Username already in use")
            return usernameData
