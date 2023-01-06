from django import forms
# from .models import PostModel

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = PostModel

#         fields = [
#             "title",
#             "description",
#         ]
from .models import Details

class detailsform(forms.ModelForm):
    class Meta:
        model=Details
        fields="__all__"