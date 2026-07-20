from typing import Any

from django import forms

from blog.models import BlogPost


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ["title", "content", "preview", "is_published"]
        widgets = {
            "is_published": forms.CheckboxInput(attrs={"type": "checkbox"}),
        }

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})
        self.fields["is_published"].widget.attrs.update({"class": "form-check"})
