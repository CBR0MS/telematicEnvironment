from django import forms 

class InterpretationForm(forms.Form):
  interp = forms.CharField(label='pass their message along', max_length=200)

class WhisperForm(forms.Form):
    whisper = forms.CharField(label='whisper something', max_length=200)