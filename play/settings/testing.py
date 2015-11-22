from .production import *
from model_mommy.generators import gen_image_field

MOMMY_CUSTOM_FIELDS_GEN = {
    'django_resized.ResizedImageField': gen_image_field ,
}

