from django import forms
from .models import MenuCatagory  # Make sure this model is correctly imported

class MenuForm(forms.Form):
    name = forms.CharField(
        max_length=200,
        label='Menu Name',
        widget=forms.TextInput(attrs={'class': 'form-control name', 'placeholder': 'Enter menu name'})
    )
    description = forms.CharField(
        label='Menu Description',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter description'})
    )
    price = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        label='Menu Price',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter price'})
    )
    catagory = forms.ModelChoiceField(
        queryset=MenuCatagory.objects.all(),
        label='Menu Category',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    available = forms.BooleanField(
        label='Available',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    type = forms.ChoiceField(
        choices=(('food','food'),('deal','deal')),
        label='Type',
        widget=forms.Select(attrs={'class':'form-control'})
    )
    image = forms.ImageField(
        label='Menu Image',
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )
