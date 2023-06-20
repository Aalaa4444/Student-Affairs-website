from dataclasses import field
from django import forms
from .models import studDetail
from django.utils import timezone
import django_filters

class addstudForm(forms.ModelForm):
    birthDate = forms.DateInput()
    class Meta:
        model = studDetail
        #phone=forms.IntegerField(max_length = 200)
        fields = ['STUDENT_ID', 'Fname', 'Lname', 'birthDate', 'gender','gpa' , 'level', 'status', 'depart', 'email', 'phone']
    def clean(self):
 
        # data from the form is fetched using super function
        super(addstudForm, self).clean()
         
        # extract the username and text field from the data
        Fname = self.cleaned_data.get('Fname')
        Lname = self.cleaned_data.get('Lname')
        
        gpa = self.cleaned_data.get('gpa')
        birthDate = self.cleaned_data.get('birthDate')
        STUDENT_ID = self.cleaned_data.get('STUDENT_ID')
        if birthDate.year<2000 or birthDate.year>2005:
            self._errors['birthDate'] = self.error_class(['invalid year, year should be between 2000 & 2005'])
        if STUDENT_ID<0 :
            self._errors['STUDENT_ID'] = self.error_class(['invalid ID'])
        if gpa<0.0 or gpa>4.0 :
            self._errors['gpa'] = self.error_class(['invalid gpa'])
        # conditions to be met for the username length
        if len(Fname) < 4:
            self._errors['Fname'] = self.error_class(['Minimum 5 characters required'])
        if len(Lname) <4:
            self._errors['Lname'] = self.error_class(['Minimum 5 characters required'])
 
        # return any errors if found
        return self.cleaned_data
class editstudForm(forms.ModelForm):
    birthDate = forms.DateInput()
    class Meta:
        model = studDetail
        #phone=forms.IntegerField(max_length = 200)
        fields = ['STUDENT_ID', 'Fname', 'Lname', 'birthDate', 'gender','gpa' , 'level', 'status', 'depart', 'email', 'phone']
    def __init__(self, *args, **kwargs):
        super(editstudForm, self).__init__(*args, **kwargs)
        self.fields['depart'].disabled = True
    def clean(self):
 
        # data from the form is fetched using super function
        super(editstudForm, self).clean()
         
        # extract the username and text field from the data
        Fname = self.cleaned_data.get('Fname')
        Lname = self.cleaned_data.get('Lname')
        
        gpa = self.cleaned_data.get('gpa')
        birthDate = self.cleaned_data.get('birthDate')
        STUDENT_ID = self.cleaned_data.get('STUDENT_ID')
        if birthDate.year<2000 or birthDate.year>2005:
            self._errors['birthDate'] = self.error_class(['invalid year, year should be between 2000 & 2005'])
        if STUDENT_ID<0 :
            self._errors['STUDENT_ID'] = self.error_class(['invalid ID'])
        if gpa<0.0 or gpa>4.0 :
            self._errors['gpa'] = self.error_class(['invalid gpa'])
        # conditions to be met for the username length
        if len(Fname) < 4:
            self._errors['Fname'] = self.error_class(['Minimum 5 characters required'])
        if len(Lname) <4:
            self._errors['Lname'] = self.error_class(['Minimum 5 characters required'])
 
        # return any errors if found
        return self.cleaned_data

class changeDepartForm(forms.ModelForm):
    birthDate = forms.DateInput()
    class Meta:
        model = studDetail
        #phone=forms.IntegerField(max_length = 200)
        fields = ['STUDENT_ID', 'Fname', 'Lname', 'depart']
    def __init__(self, *args, **kwargs):
        super(changeDepartForm, self).__init__(*args, **kwargs)
        self.fields['STUDENT_ID'].disabled = True
        self.fields['Fname'].disabled = True
        self.fields['Lname'].disabled = True

class changeStatusForm(forms.ModelForm):
    birthDate = forms.DateInput()
    class Meta:
        model = studDetail
        #phone=forms.IntegerField(max_length = 200)
        fields = ['STUDENT_ID', 'Fname', 'Lname', 'status']
    def __init__(self, *args, **kwargs):
        super(changeStatusForm, self).__init__(*args, **kwargs)
        self.fields['STUDENT_ID'].disabled = True
        self.fields['Fname'].disabled = True
        self.fields['Lname'].disabled = True


class studFilter(django_filters.FilterSet):
    Fname = django_filters.CharFilter(lookup_expr='icontains', field_name='Fname', label="Fname:")
    Lname = django_filters.CharFilter(lookup_expr='icontains', field_name='Lname', label="Lname:")
    STUDENT_ID = django_filters.CharFilter(lookup_expr='icontains', field_name='STUDENT_ID', label="STUDENT_ID:")

    class Meta:
        model = studDetail
        fields = ['Fname', 'Lname', 'STUDENT_ID']
        