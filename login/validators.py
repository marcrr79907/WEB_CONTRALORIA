from django.core.exceptions import ValidationError

def valid_foto(value):
    if (not value.name.endswith('.jpg') and not value.name.endswith('.png') and not value.name.endswith('.gif') and not value.name.endswith('.jpeg')):
        raise ValidationError("Archivos permitidos: .jpg, .jpeg, .png, .gif")