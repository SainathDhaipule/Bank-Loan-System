from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.db import models
from loanApp.models import loanCategory



#class LoanCategoryForm(forms.ModelForm):
    #class Meta:
        #interest_rate = forms.DecimalField(label='Interest Rate (%)', min_value=0, max_value=100, decimal_places=2)
     #   model = loanCategory
      #  fields = ('loan_name', 'interest_rate_per_annum')  # Assuming the field name is 'interest_rate_per_annum'




class LoanCategoryForm(forms.ModelForm):
    class Meta:
        model = loanCategory
        fields = ('loan_name', 'interest_rate')
    
class loanCategory(models.Model):
    loan_name = models.CharField(max_length=100)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)  # Add this line

    def __str__(self):
        return self.loan_name


class AdminLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')
