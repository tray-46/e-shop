from django import forms
from config.settings import FORBIDDEN_WORDS

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

    @staticmethod
    def check_for_words(text, words_list):
        words_found = list()
        for word in words_list:
            if word in text.lower():
                words_found.append(word)
        return words_found

    def clean_product_name(self):
        product_name = self.cleaned_data["product_name"]
        words_found = self.check_for_words(product_name, FORBIDDEN_WORDS)
        if words_found:
            raise forms.ValidationError(f"Product name not allowed this words: {", ".join(words_found)}")
        return product_name

    def clean_product_description(self):
        product_description = self.cleaned_data["product_description"]
        words_found = self.check_for_words(product_description, FORBIDDEN_WORDS)
        if words_found:
            raise forms.ValidationError(f"Product description not allowed this words: {", ".join(words_found)}")
        return product_description

class FeedbackForm(forms.ModelForm):
    """ """
    class Meta:
        model = Feedback
        fields = [
            "feedback_username",
            "feedback_phone",
            "feedback_message",
        ]
