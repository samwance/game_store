from django import forms
from .models import CartItem, WishlistItem


class CartForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['game', 'quantity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['game'].widget = forms.HiddenInput()
        self.fields['quantity'].widget = forms.NumberInput(attrs={'min': 1, 'step': 1})


class WishlistForm(forms.ModelForm):
    class Meta:
        model = WishlistItem
        fields = ['game']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['game'].widget = forms.HiddenInput()
