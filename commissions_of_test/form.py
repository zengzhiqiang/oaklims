from django.forms import ModelForm
from django import forms
from .models import Commission

class CommissionForm(ModelForm):
    '''送检单填写表单'''
    class Meta:
        model = Commission
        fields = [
            'commission_id',
            'sample_name',
            'sample_material',
            'sample_material_no',
            'sample_no',
            'product_id',
            'client',
            'test_item',
            'test_method',
            'test_require',
            'note'
        ]

class SearchForm(forms.Form):
    commission_id = forms.CharField(max_length=128, label="送检单编号")