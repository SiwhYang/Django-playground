from django import forms

class FormsName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)


#dijcldkcmvkldmvdkjskl