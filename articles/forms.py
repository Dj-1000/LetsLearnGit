from django import forms

class articleForms(forms.Form):
    title = forms.CharField(max_length=50)
    content = forms.CharField()

    def clean_title(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title')
        return title
    
    def clean(self):
        cleaned_data = self.cleaned_data
        return cleaned_data