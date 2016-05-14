from django import forms

class PrimeForm(forms.Form):
    nth_number =  forms.IntegerField(required=True)

    def clean_nth_number(self):
        data = self.cleaned_data['nth_number']
        if data < 1 :
            raise forms.ValidationError("Number must be greate the 0")
        return data
