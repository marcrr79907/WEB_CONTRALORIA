from django.forms import ModelForm
from .models import *


class ReportForm(ModelForm):
    class Meta:
        model = Reporte
        exclude = ['user_id']

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
