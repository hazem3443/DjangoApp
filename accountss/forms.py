from django.forms import ModelForm, Textarea
from django import forms
from .models import Order
from django.utils.translation import gettext_lazy as _

class OrderForm(ModelForm): 
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields["customer"].choices = [("", "please choose value"),] + list(self.fields["customer"].choices)[1:]        
        self.fields["product"].choices = [("", "please choose value"),] + list(self.fields["product"].choices)[1:]        
        self.fields["status"].choices = [("", "please choose value"),] + list(self.fields["status"].choices)[1:]        

    class Meta:
        model = Order
        
        # fields = '__all__' #['customer','product']
        # def __init__(self, *args, **kwargs):
        #     super(OrderForm, self).__init__(*args, **kwargs)
        #     self.fields['customer'].empty_label = "hellow"
        fields = '__all__'
        # widgets = {
        #     'customer': ModelChoiceField(attrs={'cols': 80, 'rows': 20}, emp),
        # }
        
        labels = {
            'customer': _('الزبون'),
            'product': _('المنتج'),
            'status': _('حالة المنتج'),
        }
        # help_texts = {
        #     'customer': _('Some useful help text.'),
        # }
        error_messages = {
            'required': 'This field is required',
            'invalid': 'hazem hellos',
            'caps': 'This field if case sensitive',
        } 

