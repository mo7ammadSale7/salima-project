from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.urls import reverse
from PIL import Image
from django.core.exceptions import ValidationError 

class Category(models.Model):

    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name
    

class Post(models.Model):
    title = models.CharField(max_length=100)
    category=models.ForeignKey(Category , on_delete=models.PROTECT , default=1)
    image = models.ImageField(default='default.jpg', upload_to='posts_pics')
    content = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    post_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        # return '/detail/{}'.format(self.pk)
        return reverse('detail', args=[self.pk])
        
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.width > 300 or img.height > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)    

    class Meta:
        ordering = ('-post_date', )


class Comment(models.Model):
    name = models.CharField(max_length=50, verbose_name='الاسم')
    email = models.EmailField(verbose_name='البريد الإلكتروني')
    body = models.TextField(verbose_name='التعليق')
    comment_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return 'علق {} على {}.'.format(self.name, self.post)

    class Meta:
        ordering = ('-comment_date',)




def validate_employees_Number(value): 
    if value > 0:

        return value 
    else: 
        raise ValidationError("please enter valid number")        

class AppRegs(models.Model):
    
    
    companyName = models.CharField(max_length=50,blank=True, null=True)
    creationDate = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=50,blank=True, null=True)
    associatesNumber = models.CharField(max_length=50,blank=True, null=True)
    employeesNumber = models.IntegerField(blank=True, null=True ,validators =[validate_employees_Number])
    createdJobsNumber = models.IntegerField(blank=True, null=True)
    fullAddress = models.CharField(max_length=50,blank=True, null=True)

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
    
    wilaya = models.CharField(max_length=100,choices = GEEKS_CHOICES,blank=True, null=True)
    ownersEmail = models.EmailField(blank=True, null=True)
    ownersLinkedin = models.URLField(blank=True, null=True)
    contactEmail = models.EmailField(blank=True, null=True)
    mobilePhoneNumber = models.CharField(max_length=50,blank=True, null=True)
    mainPhoneNumber = models.CharField(max_length=50,blank=True, null=True)
    
    
    def __str__(self):
        
        return self.companyName  

    def get_addmin_url(self):
        
        return reverse ('adminapp' , args=[self.pk])   



def user_directory_path(instance, filename): 

    
  
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename> 
    return 'user_{0}/{1}'.format(instance.user.id, filename) 

class MultiStepFormModel(models.Model):

   
    Founder_CHOICES = (

        ("Founder" , "Founder"),
        ("Co-founder" , "Co-founder"),
       
    )                                                                                           
    
    Secture_CHOICES = (

        ("Fintech" , "Fintech"),
        ("Cloud/Sass" , "Cloud/Sass"),
        ("Agritech (agriculture de précision)" , "Agritech (agriculture de précision)"),
        ("Economie circulaire (greentech)" , "Economie circulaire (greentech)"),
        ("E-learning/ Edtech" , "E-learning/ Edtech"),
        ("Govtech (e-administration)" , "Govtech (e-administration)"),
        ("IOT (internet des objets)" , "IOT (internet des objets)"),
        ("Legaltech" , "Legaltech"),
        ("Food tech" , "Food tech"),
        ("E-health (santé)" , "E-health (santé)"),
        ("Smart City" , "Smart City"),
        ("IOT (internet des objets)" , "IOT (internet des objets)"),
        ("Tourisme/voyage" , "Tourisme/voyage"),
        ("Energies renouvelables" , "Energies renouvelables"),
        ("Pharma" , "Pharma"),
        ("Education" , "Education"),
        ("Intelligence Artificielle" , "Intelligence Artificielle"),
        ("Réalité augmentée/virtuelle" , "Réalité augmentée/virtuelle"),
        ("E-services" , "E-services"),
        ("Economie sociale et solidaire." , "Economie sociale et solidaire."),
        ("Cybersecurity" , "Cybersecurity"),
        ("Electronique &amp; Composants" , "Electronique &amp; Composants"),
        ("Jeux/loisir" , "Jeux/loisir"),
        ("Autre" , "Autre"),
        
       
    )     


    Progress_CHOICES = (

        ("Concept/Idea" , "Concept/Idea"),
        ("prototype in development" , "prototype in development"),
        ("prototype ready" , "prototype ready"),
        ("ready product" , "ready product"),
       
    )          
    id=models.AutoField(primary_key=True)
    Tname=models.CharField(max_length=225)
    fname=models.CharField(max_length=225)
    You_are =models.CharField(max_length=225)
    age=models.CharField(max_length=225)
    
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

    wilaya=models.CharField(max_length=225)
    fullAddress=models.CharField(max_length=225)
    Email=models.CharField(max_length=225)
    mainPhoneNumber=models.CharField(max_length=225)
    webLink=models.CharField(max_length=225)
    fbLink=models.CharField(max_length=225)
    ytubeLink=models.CharField(max_length=225 ,null=True , blank=True)
    prjname=models.CharField(max_length=225)
    prjfield=models.CharField(max_length=225 )
    file=models.FileField(upload_to = 'uploads/' ,null=True , blank=True )
    file_CV=models.FileField(upload_to = 'uploads/',null=True , blank=True)
    file_Br=models.FileField(upload_to = 'uploads/',null=True , blank=True)
    prjdetail=models.CharField(max_length=225)
    prjprgress=models.CharField(max_length=225)
    awards=models.CharField(max_length=225)
    objects=models.Manager()




class MultiStepFormModelBr(models.Model):
    
   
    Founder_CHOICES = (

        ("Founder" , "Founder"),
        ("Co-founder" , "Co-founder"),
       
    )                                                                                           
    
    Secture_CHOICES = (

        ("Fintech" , "Fintech"),
        ("Cloud/Sass" , "Cloud/Sass"),
        ("Agritech (agriculture de précision)" , "Agritech (agriculture de précision)"),
        ("Economie circulaire (greentech)" , "Economie circulaire (greentech)"),
        ("E-learning/ Edtech" , "E-learning/ Edtech"),
        ("Govtech (e-administration)" , "Govtech (e-administration)"),
        ("IOT (internet des objets)" , "IOT (internet des objets)"),
        ("Legaltech" , "Legaltech"),
        ("Food tech" , "Food tech"),
        ("E-health (santé)" , "E-health (santé)"),
        ("Smart City" , "Smart City"),
        ("IOT (internet des objets)" , "IOT (internet des objets)"),
        ("Tourisme/voyage" , "Tourisme/voyage"),
        ("Energies renouvelables" , "Energies renouvelables"),
        ("Pharma" , "Pharma"),
        ("Education" , "Education"),
        ("Intelligence Artificielle" , "Intelligence Artificielle"),
        ("Réalité augmentée/virtuelle" , "Réalité augmentée/virtuelle"),
        ("E-services" , "E-services"),
        ("Economie sociale et solidaire." , "Economie sociale et solidaire."),
        ("Cybersecurity" , "Cybersecurity"),
        ("Electronique &amp; Composants" , "Electronique &amp; Composants"),
        ("Jeux/loisir" , "Jeux/loisir"),
        ("Autre" , "Autre"),
        
       
    )     


    Progress_CHOICES = (

        ("Concept/Idea" , "Concept/Idea"),
        ("prototype in development" , "prototype in development"),
        ("prototype ready" , "prototype ready"),
        ("ready product" , "ready product"),
       
    )          
    id=models.AutoField(primary_key=True)
    Tname=models.CharField(max_length=225)
    fname=models.CharField(max_length=225)
    You_are =models.CharField(max_length=225)
    age=models.CharField(max_length=225)
    gender=models.CharField(max_length=225)
    
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

    wilaya=models.CharField(max_length=225)
    fullAddress=models.CharField(max_length=225)
    Email=models.CharField(max_length=225)
    mainPhoneNumber=models.CharField(max_length=225)

    hadena_name=models.CharField(max_length=225)
    legal_status=models.CharField(max_length=225)
    numemployees=models.CharField(max_length=225 ,null=True , blank=True)
    creation_date=models.CharField(max_length=225)
    nif=models.CharField(max_length=225 )
    nis=models.CharField(max_length=225 )
    file=models.FileField(upload_to = 'uploads/incubator' ,null=True , blank=True )
    file_CV=models.FileField(upload_to = 'uploads/incubator',null=True , blank=True)
    file_Br=models.FileField(upload_to = 'uploads/incubator',null=True , blank=True)
    file_CNAS=models.FileField(upload_to = 'uploads/incubator',null=True , blank=True)
    prjdesc=models.CharField(max_length=225)
    file_dev=models.FileField(upload_to = 'uploads/incubator',null=True , blank=True)
    listequip=models.CharField(max_length=225)
    file_pres=models.FileField(upload_to = 'uploads/incubator',null=True , blank=True)
    listincubated=models.CharField(max_length=225)
    file_cv_founder=models.FileField(upload_to = 'uploads/incubator',null=True , blank=True)
    objects=models.Manager()


        





