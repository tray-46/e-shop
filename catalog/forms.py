from django import forms

from catalog.models import Feedback, Product


class ProductForm(forms.ModelForm):
    """ """
    class Meta:
        model = Product
        fields = [
            "product_name",
            "product_description",
            "image",
            "product_category",
            "price",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})

class FeedbackForm(forms.ModelForm):
    """ """
    class Meta:
        model = Feedback
        fields = [
            "feedback_username",
            "feedback_phone",
            "feedback_message",
        ]
