from newapp.models import user_model
from django  import forms

class user_form(forms.ModelForm):

    class Meta:
        model = user_model
        fields = ('title','description','due_date')
        '''
        widgets = {
            'title': forms.CharField(attrs= {'placeholder':'Enter the Title'}),
            'description': forms.CharField(attrs= {'placeholder':'Enter the descriptions'}),
            'due_date' : forms.DateField(attrbs={'placeholder' : 'M D Y'}),
        }
       '''