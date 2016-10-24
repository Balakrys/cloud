from django import forms

# from simplemathcaptcha.fields import MathCaptchaField

# class MyForm(forms.Form):
#     some_text_field = models.CharField(max_length=50)
#     captcha = MathCaptchaField()
class realform(forms.Form):
	username= forms.CharField()
	password= forms.CharField()
	message=forms.CharField()