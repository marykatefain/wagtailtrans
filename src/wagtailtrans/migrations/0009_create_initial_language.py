# Generated by Django 2.1.7 on 2019-02-22 15:13

from django.conf import settings
from django.db import migrations
from django.utils import translation


def create_initial_language(apps, schema_editor):
    Language = apps.get_model('wagtailtrans.Language')

    # Only run if there are no languages already (new build)
    if not Language.objects.exists():
        # The value of LANGUAGE_CODE may not be an entry in LANGUAGES.
        # For example, LANGUAGE_CODE may be "en-us" but LANGUAGES may only contain "en".
        # This converts the LANGUAGE_CODE into a supported variant if it isn't in LANGUAGES.
        language_code = translation.get_supported_language_variant(settings.LANGUAGE_CODE)

        Language.objects.create(
            code=language_code,
            is_default=True,
            live=True
        )


def nooperation(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailtrans', '0008_verbose_names'),
    ]

    operations = [
        migrations.RunPython(create_initial_language, nooperation),
    ]
