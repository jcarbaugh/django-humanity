from django.core.exceptions import ValidationError
from django import forms
import base64
import random

OPERATIONS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
}

def generate_question():
    q = "%i %s %i" % (
        random.randint(10, 20),
        random.choice(OPERATIONS.keys()),
        random.randint(1, 10),
    )
    return q

def is_correct_answer(question, answer):
    try:
        parts = question.split(' ')
        nums = (int(parts[0]), int(parts[2]))
        op = OPERATIONS[parts[1]]
        return op(*nums) == int(answer)
    except ValueError:
        return False

class HumanityQuestionField(forms.Field):
    
    def __init__(self, *args, **kwargs):
        super(HumanityQuestionField, self).__init__(*args, **kwargs)
    
    def clean(self, value):
        value = base64.b64decode(value or '')
        return super(HumanityQuestionField, self).clean(value)

class HumanityForm(forms.Form):
    
    def __init__(self, *args, **kwargs):
        super(HumanityForm, self).__init__(*args, **kwargs)
        q = generate_question()
        params = {
            'initial': base64.b64encode(q),
            'widget': forms.HiddenInput,
        }
        
        label = q
        data = args[0] if len(args) > 0 else kwargs.get('data', None)
        if data:
            label = base64.b64decode(data.get('humanity_question', ''))
        
        self.fields['humanity_question'] = HumanityQuestionField(**params)
        self.fields['humanity_answer'] = forms.CharField(
            label="To prove your humanity, solve %s =" % label,
            required=False,
            widget=forms.TextInput(attrs={'size': '2'}),
        )
        
    def clean(self):
        
        q = self.cleaned_data['humanity_question']
        a = self.cleaned_data.get('humanity_answer', '')
        
        if not is_correct_answer(q, a):
            raise ValidationError("You are a robot!")
