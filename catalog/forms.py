from decimal import Decimal
from typing import Any

from django import forms
from django.core.files.uploadedfile import UploadedFile
from PIL import Image

from catalog.models import Feedback, Product
from config.settings import FORBIDDEN_WORDS, PRODUCT_IMAGE_FILE_MAX_SIZE


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

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})

    @staticmethod
    def check_for_words(text: str, words_list: list[str]) -> list[str]:
        """
        check text for words in words_list

        :param text: str, text to check for words
        :param words_list: list(str), list of words
        :return: list(str), list of found words
        """
        words_found = list()
        for word in words_list:
            if word.lower() in text.lower():
                words_found.append(word)
        return words_found

    def clean_product_name(self) -> str:
        product_name: str = self.cleaned_data["product_name"]
        words_found = self.check_for_words(product_name, FORBIDDEN_WORDS)
        if words_found:
            raise forms.ValidationError(f"Product name not allowed this words: {", ".join(words_found)}")
        return product_name

    def clean_product_description(self) -> str:
        product_description: str = self.cleaned_data["product_description"]
        words_found = self.check_for_words(product_description, FORBIDDEN_WORDS)
        if words_found:
            raise forms.ValidationError(f"Product description not allowed this words: {", ".join(words_found)}")
        return product_description

    def clean_price(self) -> Decimal:
        price: Decimal = self.cleaned_data["price"]
        if price and price < 0:
            raise forms.ValidationError("Price cannot be less than 0")
        return price

    def clean_image(self) -> UploadedFile:
        uploaded_image: UploadedFile = self.cleaned_data["image"]
        if uploaded_image:
            with Image.open(uploaded_image) as img:
                allowed_formats = ["JPEG", "PNG"]
                if img.format not in allowed_formats:

                    raise forms.ValidationError(f"Image format not allowed: {img.format}. Upload a JPEG or PNG image.")

            # разделить на две функции???

            if uploaded_image.size:
                file_size_mb = round(uploaded_image.size / 1024 / 1024, 2)
            else:
                file_size_mb = 0

            if file_size_mb > PRODUCT_IMAGE_FILE_MAX_SIZE:
                raise forms.ValidationError(
                    f"Image file to large: {file_size_mb} MB! " f"Max allowed size is {PRODUCT_IMAGE_FILE_MAX_SIZE} MB"
                )
            uploaded_image.seek(0)
        return uploaded_image


class FeedbackForm(forms.ModelForm):
    """ """

    class Meta:
        model = Feedback
        fields = [
            "feedback_username",
            "feedback_phone",
            "feedback_message",
        ]
