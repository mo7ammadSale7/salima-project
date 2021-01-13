from django import forms
from django.forms import ModelForm

from .models import Comment, Post ,MultiStepFormModel ,MultiStepFormModelBr ,AppRegs
from django.core.exceptions import ValidationError 
from django.utils.translation import ugettext_lazy as _


class NewComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class PostCreateForm(forms.ModelForm):
    title = forms.CharField(label='عنوان التدوينة')
    content = forms.CharField(label='نص التدوينة', widget=forms.Textarea)
    image = forms.ImageField(label='اختار صوره للموضوع ')

    class Meta:
        model = Post
        fields = ['title', 'content' , 'category','image',]




def is_compName(x,y):

    return sorted(x) == sorted(y)

class DateInput(forms.DateInput):
    
    input_type = 'date'
    

class RegsForm(forms.ModelForm):
    
    # def clean_companyName(self):
        
    #     companyName = self.cleaned_data.get('companyName')
    #     if (companyName == ""):
    #         raise forms.ValidationError('This field can not be left blank')
    #     return companyName

    



    companyName = forms.CharField(
                                  widget=forms.TextInput(attrs=
                                                          {'class':'form-control' , 
                                                           'placeholder':'companyName',
                                                           
                                                           }),max_length=50,required=True,label='اسم الشركه')
    
    creationDate = forms.DateField(widget=DateInput(attrs=
                                                          {'class':'form-control' , 
                                                          'placeholder':'ادخل التاريخ',
                                                           }), label="تاريخ الإنشاء")
    
    status = forms.CharField(max_length=50,
                                  widget=forms.TextInput(attrs=
                                                          {'class':'form-control' , 
                                                           'placeholder':'SARL/EURL/SPA...etc.',}))
    
    
    associatesNumber = forms.CharField(max_length=50,
                                  widget=forms.TextInput(attrs=
                                                          {'class':'form-control' , 
                                                           'placeholder':"Nombre d 'associées",}))
    
    
    employeesNumber=forms.CharField(max_length=50,
                                  widget=forms.TextInput(attrs=
                                                          {'class':'form-control' , 
                                                           'placeholder':"Nombre d'employés",}))
    
    
    
    createdJobsNumber=forms.CharField(max_length=50,
                                  widget=forms.TextInput(attrs=
                                                          {'class':'form-control' , 
                                                           'placeholder':"عدد الوظائف التي أنشأتها شركتك",}))
    
    
    
    fullAddress=forms.CharField(max_length=50,
                                  widget=forms.TextInput(attrs=
                                                          {'class':'form-control' , 
                                                           'placeholder':" العنوان الكامل",}))

    GEEKS_CHOICES = (

        ("أدرار" , "أدرار"),
        ("الشلف" , "الشلف"),
        ("الأغواط" , "الأغواط"),
        ("أم البواقي" , "أم البواقي"),
        ("باتنة" , "باتنة"),
        ("بجاية" , "بجاية"),
        ("بسكرة" , "بسكرة"),
        ("بشار" , "بشار"),
        ("البليدة" , "البليدة"),
        ("البويرة" , "البويرة"),
        ("تمنراست" , "تمنراست"),
        ("تبسة" , "تبسة"),
        ("تلمسان" , "تلمسان"),
        ("تيارت" , "تيارت"),
        ("تيزي وزو" , "تيزي وزو"),
        ("الجزائر" , "الجزائر"),
        ("الجلفة" , "الجلفة"),
        ("جيجل" , "جيجل"),
        ("سطيف" , "سطيف"),
        ("سعيدة" , "سعيدة"),
        ("سكيكدة" , "سكيكدة"),
        ("سيدي بلعباس" , "سيدي بلعباس"),
        ("عنابة" , "عنابة"),
        ("قالمة" , "قالمة"),
        ("قسنطينة" , "قسنطينة"),
        ("المدية" , "المدية"),
        ("مستغانم" , "مستغانم"),
        ("المسيلة" , "المسيلة"),
        ("معسكر" , "معسكر"),
        ("ورقلة" , "ورقلة"),
        ("وهران" , "وهران"),
        ("البيض" , "البيض"),
        ("إليزي" , "إليزي"),
        ("برج بوعريريج" , "برج بوعريريج"),
        ("بومرداس" , "بومرداس"),
        ("الطارف" , "الطارف"),
        ("تيندوف" , "تيندوف"),
        ("تيسمسيلت" , "تيسمسيلت"),
        ("وادي سوف" , "وادي سوف"),
        ("سوق أهراس" , "سوق أهراس"),
        ("تيبازة" , "تيبازة"),
        ("عين الدفلى" , "عين الدفلى"),
        ("النعامة" , "النعامة"),
        ("عين تيموشنت" , "عين تيموشنت"),
        ("غرداية" , "غرداية"),
        ("غليزان" , "غليزان"),
    )                                                       
    
    
    wilaya=forms.ChoiceField(choices = GEEKS_CHOICES ,
                                widget=forms.Select(attrs=
                                                          {'class':'form-control' , 
                                                           'placeholder':"الولاية",})) 
                                 
    
    ownersEmail=forms.CharField(max_length=50,
                                  widget=forms.EmailInput(attrs=
                                                          {'class':'form-control' , 
                                                           'placeholder':" عنوان البريد الإلكتروني للمدير ",}))
    
    
    ownersLinkedin=forms.URLField(max_length=50,
                                  widget=forms.TextInput(attrs=
                                                          {'class':'form-control' , 
                                                           'placeholder':"لينكدين المدير ",}))
    
    
    
    contactEmail=forms.CharField(max_length=50,
                                  widget=forms.EmailInput(attrs=
                                                          {'class':'form-control' , 
                                                           'placeholder':" عنوان البريد الإلكتروني للاتصال",}))
    
    
    
    mobilePhoneNumber=forms.CharField(max_length=50,
                                  widget=forms.TextInput(attrs=
                                                          {'class':'form-control' , 
                                                           'placeholder':"الهاتف المحمول",}))
    mainPhoneNumber=forms.CharField(max_length=50,
                                  widget=forms.TextInput(attrs=
                                                          {'class':'form-control' , 
                                                           'placeholder':"الهاتف الرئيسي",}))  

    class Meta:
        model = AppRegs
        fields = '__all__'

    def clean_companyName(self):
        companyName = self.cleaned_data.get('companyName')

        if not companyName:
            raise forms.ValidationError('sorry field is required')
        return companyName



class MultiFormStep(forms.ModelForm):

    class Meta:
        model =   MultiStepFormModel
        fields = ('file', 'file_CV','file_Br')
        
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__()    


        # def clean(self):
        #     super(MultiStepFormModel, self).clean()
        #     Tname = self.cleaned_data.get('Tname')
        #     fname = self.cleaned_data.get('fname')
            
        #     if len(Tname) < 5 :
        #         self._errors['Tname'] = self.error_class([
        #         'Minimum 5 characters required'])

        #     if len(fname) < 10 :  
        #         self._errors['fname'] = self.error_class([
        #     'Post Should Contain a minimum of 10 characters'])

        #     return self.cleaned_data


class MultiFormStepBr(forms.ModelForm):

    class Meta:
        model =   MultiStepFormModelBr
        fields = ('file', 'file_CV','file_Br','file_CNAS','file_dev','file_pres','file_cv_founder')
        
    