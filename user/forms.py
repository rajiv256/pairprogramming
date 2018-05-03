from django import forms
from dal import autocomplete
from user.models import Topic


class TopicForm(forms.ModelForm):

    topic = forms.ModelChoiceField(
        query_set = Topic.objects.all(),
        widget    = autocomplete.ModelSelect2(url='autocomplete', attrs={'data-minimum-input-length': 2, 'data-placeholder': 'Autocomplete ...',},)

    )

    class Meta:
        model     = Topic
        fields    = '__all__'
