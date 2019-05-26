from django import forms

from .models import Details, General


class GeneralForm(forms.ModelForm):
    class Meta:
        model = General
        fields = "__all__"


class DetailForm(forms.ModelForm):
    class Meta:
        model = Details
        general = forms.ModelChoiceField(queryset=General.objects.all(), widget=forms.BaseModelFormSet, required=False)
        fields = ['procesor', 'pamiec', 'pamiec_ram', 'bateria']
        # fields = "__all__"
