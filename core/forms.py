from django import forms
from .models import Contact, Subscribe
from captcha.fields import CaptchaField


class contactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = '__all__'


class subscribe(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = '__all__'