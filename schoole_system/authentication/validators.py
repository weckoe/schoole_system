from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions

MAX_UPLOAD_PHOTO_WIDTH = 200
MAX_UPLOAD_PHOTO_HEIGHT = 200


def user_image_resolution_check(image):
    image_width, image_height = get_image_dimensions(image)
    if image_width != MAX_UPLOAD_PHOTO_WIDTH or image_height != MAX_UPLOAD_PHOTO_HEIGHT:
        raise ValidationError(f'Image resolution must be {MAX_UPLOAD_PHOTO_WIDTH}x{MAX_UPLOAD_PHOTO_HEIGHT}')