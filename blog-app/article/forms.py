from django import forms

from .models import Article, Comment
from ckeditor.widgets import CKEditorWidget

class ArticleForm(forms.ModelForm):

    content = forms.CharField(widget=CKEditorWidget)

    class Meta:

        model = Article
        fields = ["title", "content"]