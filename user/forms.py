from django import forms

from user.models import User

class UserUpdateForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('username','phone')
        error_messages = {
            'username': {
                'unique': 'Ya existe un usuario con ese nombre de usuario.'
            },
            'phone': {
                'unique': 'Ya existe un usuario con ese telefono.'
            }
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

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nombre_user', 'foto']
        widgets = {
            'nombre_user': forms.TextInput(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'})
        }
