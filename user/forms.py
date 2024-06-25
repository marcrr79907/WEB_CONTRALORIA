from django import forms
from django.contrib.auth.models import  User


class UserUpdateForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('__all__')

        widgets = {
            'photo': forms.FileInput(attrs={'class': 'form-control'})
        }
        error_messages = {
            
        }
         
    # Manejo de usuario y modificacion de password
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()

            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)

        return data
