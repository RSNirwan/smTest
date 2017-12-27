from django import forms

from .models import User

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['user_name',]

	#add validation for user_name. only [a-z][A-Z][0-9] allowed
	def clean_user_name(self):
		ascii_list = list(range(97,123)) + list(range(65,91)) + list(range(48,58))
		user_name = self.cleaned_data.get('user_name')
		for char in user_name:
			if char not in ascii_list:
				raise forms.ValidationError('Only following characters allowed: [a-z][A-Z][0-9]')
		return user_name