from django import forms


class PostSearchForm(forms.Form):
    queried = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['queried'].widget.attrs.update({'class': 'form-control'})
