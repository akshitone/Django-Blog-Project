from django import forms
from .models import BlogPost

class BlogForm(forms.Form):
    title   = forms.CharField()
    slug    = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)

class BlogModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'slug', 'content']

    def valid_title(self, *args, **kwargs):
        title = self.cleared_data.get("title")
        query = BlogPost.objects.filter(title__iexact=title)
        if query.exists():
            raise forms.ValidationError("This title has already been used. Please try another title for blog.")
        return title