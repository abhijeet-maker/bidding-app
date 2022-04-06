from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm

from .models import Company, PlacementBid


class CustomRegisterForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class BiddingCreationForm(forms.Form):
    placement_title = forms.CharField(label='Bid Title',max_length=255)
    #placement_slug = forms.SlugField(label='Bid ID')
    Company_CHOICES=[]
    #company=Company.objects.values('company_name')

    for company in Company.objects.values('company_name'):
        print("**************",company.get('company_name'))
        temp=[]
        temp.append(company.get('company_name'))
        temp.append(company.get('company_name'))
        x=tuple(temp)
        Company_CHOICES.append(x)
        temp.clear()
    print(Company_CHOICES)
    #company = list(Company.objects.all())
    #print("**************", company)
    #print("**************",company.get('company_name'))
    #placement_company = forms.ChoiceField(required=True, choices=Company_CHOICES)
    #queryset = Company.objects.all()
    placement_company = forms.ModelChoiceField(Company.objects.all(),label='Bidding Company')
    print(placement_company)


class BiddingConfirmationForm(ModelForm):
    class Meta:
        model = PlacementBid
        fields = ["user","placement","offer","confirmed"]
