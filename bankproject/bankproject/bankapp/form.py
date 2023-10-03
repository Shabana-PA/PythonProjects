from django import forms
from bankapp.models import Details, Branch, Material, District

class DetailsForm(forms.ModelForm):
    ACCOUNT_TYPE_CHOICES = [
        ('saving', 'Savings Account'),
        ('current', 'Current Account'),
    ]

    MATERIAL_CHOICES = [
        ('debit_card', 'Debit Card'),
        ('credit_card', 'Credit Card'),
        ('cheque_book', 'Cheque Book'),
    ]

    district = forms.ModelChoiceField(
        label='District',
        queryset=District.objects.all(),
        required=True
    )

    branch = forms.ModelChoiceField(
        label='Branch',
        queryset=Branch.objects.all(),
        required=True,
        help_text='Select a branch in the chosen district'
    )

    account_type = forms.ChoiceField(
        label='Account Type',
        choices=ACCOUNT_TYPE_CHOICES,
        required=True
    )

    materials_provide = forms.MultipleChoiceField(
        label='Materials Provided',
        choices=MATERIAL_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Details
        fields = ['name', 'dob', 'age', 'gender', 'phone_number', 'mail_id', 'address', 'district', 'branch', 'account_type', 'materials_provide']

    def __init__(self, *args, **kwargs):
        super(DetailsForm, self).__init__(*args, **kwargs)
        self.fields['branch'].queryset = Branch.objects.all()

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['branch'].queryset = Branch.objects.filter(district_id=district_id)
            except (ValueError, TypeError):
                pass

        elif self.instance.pk:
            self.fields['branch'].queryset = self.instance.district.branch_set.all()
class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['name']
