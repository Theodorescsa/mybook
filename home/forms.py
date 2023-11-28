from django import forms
from .models import BookModel
from category.models import CategoryBookModel
from ckeditor.widgets import CKEditorWidget
from customer.models import CustomerModel

class BookForms(forms.Form):
    
    category_name = forms.ModelMultipleChoiceField(queryset=CategoryBookModel.objects.all(),widget=forms.CheckboxSelectMultiple)
    
    book_name = forms.CharField(max_length=500)
    quantity_page = forms.IntegerField()
    author = forms.CharField(max_length=100)
    price = forms.IntegerField()
    birth = forms.DateField()
    description = forms.CharField(widget=CKEditorWidget())
    link_image = forms.ImageField()
    saved_books  = forms.ModelMultipleChoiceField(queryset=BookModel.objects.all(),widget=forms.CheckboxSelectMultiple)
    def save(self):
        model = BookModel(
            
            category_name = self.cleaned_data["category_name"],
           
            book_name = self.cleaned_data["book_name"],
            quantity_page = self.cleaned_data["quantity_page"],
            author = self.cleaned_data["author"],
            price = self.cleaned_data["price"],
            birth = self.cleaned_data["birth"],
            description = self.cleaned_data["description"],
            link_image = self.cleaned_data["link_image"],
        )
        model.save()
        customer = CustomerModel.objects.create(
            saved_books = self.cleaned_data['saved_books'],
            
        )
        customer.save()
class BookModelForms(forms.ModelForm):
    class Meta():
        model = BookModel
        fields = ["category_name","book_name","quantity_page","author","price","birth","description","link_image","color_card"]
    category_name = forms.ModelMultipleChoiceField(queryset=CategoryBookModel.objects.all(),widget=forms.CheckboxSelectMultiple)
    description = forms.CharField(widget=CKEditorWidget())
