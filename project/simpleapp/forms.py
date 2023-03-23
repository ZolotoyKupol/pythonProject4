from django import forms
from django.core.exceptions import ValidationError

from .models import Posts

class PostsForm(forms.ModelForm):
    description = forms.CharField(min_length=20)

    class Meta:
        model = Posts
        fields = [
            'name',
            'description',
            'category',
        ]

    # def clean(self):
    #     cleaned_data = super().clean()
    #     description = cleaned_data.get("description")
    #     name = cleaned_data.get("name")

        # if name == description:
        # #     raise ValidationError(
        # #         "Описание не должно быть идентично названию."
        # #     )
        # #
        # return cleaned_data