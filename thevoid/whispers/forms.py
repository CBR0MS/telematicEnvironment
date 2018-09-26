from django import forms 

class InterpretationForm(forms.Form):
  interp = forms.CharField(label='Whisper', max_length=200)

class WhisperForm(forms.Form):
    whisper = forms.CharField(label='Whisper', max_length=200)