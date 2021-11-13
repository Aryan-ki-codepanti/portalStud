from base.models import MarkSheet
from django.forms import ModelForm

class MarkSheetForm(ModelForm):
    class Meta:
        model = MarkSheet
        fields = "__all__"
        exclude = ("student",)
