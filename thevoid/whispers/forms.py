from django import forms 

class InterpretationForm(forms.Form):
  interp = forms.CharField(label='Your interpretation', max_length=200)

class WhisperForm(forms.Form):
    whisper = forms.CharField(label='Your whisper', max_length=200)