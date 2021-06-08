from django.forms import ModelForm

from task.models import Gmail


class GmailForm(ModelForm):
    class Meta:
        model = Gmail
        fields =['reciever','subject','body']
