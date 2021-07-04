from django.forms import ModelForm
from .models import DigitalFiles
class DigitalFilesForm(ModelForm):
    class Meta:
        model=DigitalFiles
        fields=('Name','Surname','Email','Title','Description','Field','FileUpload',)
