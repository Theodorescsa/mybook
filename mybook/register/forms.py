from django import forms
from django.contrib.auth.models import User
from customer.models import CustomerModel
class RegisterFormModel(forms.Form):
    first_name = forms.CharField(max_length=100,label='Firstname')
    last_name = forms.CharField(max_length=100,label='Lastname')
    email = forms.EmailField(label="Email")
    username = forms.CharField(max_length=100,required=True,label='Username')
    password1 = forms.CharField(label="Password",required=True,widget=forms.PasswordInput)
    password2 = forms.CharField(label="Nhap lai mat khau", required=True,widget=forms.PasswordInput)
    phone_number = forms.CharField(label="So dien thoai")
    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']    
            password2 = self.cleaned_data['password2']        
            if password1 and password1 == password2:
                return password2
        raise forms.ValidationError("mat khau khong hop le hoac khong khop")
    
    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username = username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("Usename da ton tai")
        
    def save(self):
        user = User.objects.create_user(
            # first_name = self.cleaned_data['first_name'],
            # last_name = self.cleaned_data['last_name'],
            # email = self.cleaned_data['email'],
            username = self.cleaned_data['username'],
            password = self.cleaned_data['password1'],
        )
        customer = CustomerModel.objects.create(
            user = user,
            first_name = self.cleaned_data['first_name'],
            last_name = self.cleaned_data['last_name'],
            phone_number = self.cleaned_data['phone_number'],
            email = self.cleaned_data['email'],
        )
        customer.save()
        
    
    