from django.core.exceptions import ValidationError


def validate_png(image):
    if not image.lower().endwith('.png'):
        raise ValidationError('Envie uma imagem png')