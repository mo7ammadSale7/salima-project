from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment ,AppRegs ,Category , MultiStepFormModel,MultiStepFormModelBr
from .forms import NewComment, PostCreateForm ,RegsForm ,MultiFormStep,MultiFormStepBr
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import CreateView, UpdateView, DeleteView ,ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import RegsForm
from django.http import HttpResponse 
from django.contrib import messages
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO

# from validate_email import validate_email
# import validate_email

def home(request):
    posts = Post.objects.all()

    
    context = {
        'title': 'الصفحة الرئيسية',
        'posts': posts,
        
    }
    return render(request, 'blog/index.html', context)


    # All Posts function
def allposts(request):
    posts = Post.objects.all()

    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_page)
    context = {
        'title': 'موضوعات متنوعه ',
        'posts': posts,
        'page': page,
    }
    return render(request, 'blog/all_posts.html', context)

# End Of All Posts function


# Application Form
            




        
        # TRY
        

        

        # 

        # try:
        #     if .objects.get(email=email):
        #         messages.add_message(request, messages.ERROR, 'Email is taken')
        #         context['has_error'] = True

        # except Exception as identifier:
        #     pass

        # try:
        #     if User.objects.get(username=username):
        #         messages.add_message(
        #             request, messages.ERROR, 'Username is taken')
        #         context['has_error'] = True

        # except Exception as identifier:
        #     pass
    #     context = {

    #         'data': request.POST,
    #         'has_error': False
    #     }
    #     if context['has_error']:
    #         return render(request, 'blog/formm.html', context, status=400)

    #     appregister = AppRegs.objects.create(companyName=companyName, 
    #                                         creationDate=creationDate,
    #                                         status=status,
    #                                         associatesNumber=associatesNumber,
    #                                         employeesNumber=employeesNumber,
    #                                         createdJobsNumber=createdJobsNumber,
    #                                         fullAddress=fullAddress,
    #                                         wilaya=wilaya,
    #                                         ownersEmail=ownersEmail,
    #                                         ownersLinkedin=ownersLinkedin,
    #                                         contactEmail=contactEmail,
    #                                         mobilePhoneNumber=mobilePhoneNumber,
    #                                         mainPhoneNumber=mainPhoneNumber)
        
    #     appregister.save()

    #     messages.add_message(request, messages.SUCCESS,
    #                                'Cogratulation')
    # else:
    #     form=RegsForm()                                
    # return redirect('home')
    #     # TRY
















    # if request.method == "POST":

    #     form = RegsForm (request.POST)

    #     if form.is_valid():

    #         appregister = AppRegs(companyName=form.cleaned_data['companyName'],
    #                         creationDate=form.cleaned_data['creationDate'],
    #                         status=form.cleaned_data['status'],
    #                         associatesNumber=form.cleaned_data['associatesNumber'],
    #                         employeesNumber=form.cleaned_data['employeesNumber'],
    #                         createdJobsNumber=form.cleaned_data['createdJobsNumber'],
    #                         fullAddress=form.cleaned_data['fullAddress'],
    #                         wilaya=form.cleaned_data['wilaya'],
    #                         ownersEmail=form.cleaned_data['ownersEmail'],
    #                         ownersLinkedin=form.cleaned_data['ownersLinkedin'],
    #                         contactEmail=form.cleaned_data['contactEmail'],
    #                         mobilePhoneNumber=form.cleaned_data['mobilePhoneNumber'],
    #                         mainPhoneNumber=form.cleaned_data['mainPhoneNumber'])
            
    #         appregister.save()
            
    #         return redirect('formm')
    # else:
    #     form = RegsForm ()
    # context = {'form': form}
        
    # return render(request, 'blog/formm.html',context)

        
            
       




   


    


# def adduser(request):
    
    
    

#     if request.method == "POST":
#         form = RegsForm (request.POST)
#         if form.is_valid():

            
#             appregister = AppRegs(companyName=form.cleaned_data['companyName'],
#                             creationDate=form.cleaned_data['creationDate'],
#                             status=form.cleaned_data['status'],
#                             associatesNumber=form.cleaned_data['associatesNumber'],
#                             employeesNumber=form.cleaned_data['employeesNumber'],
#                             createdJobsNumber=form.cleaned_data['createdJobsNumber'],
#                             fullAddress=form.cleaned_data['fullAddress'],
#                             wilaya=form.cleaned_data['wilaya'],
#                             ownersEmail=form.cleaned_data['ownersEmail'],
#                             ownersLinkedin=form.cleaned_data['ownersLinkedin'],
#                             contactEmail=form.cleaned_data['contactEmail'],
#                             mobilePhoneNumber=form.cleaned_data['mobilePhoneNumber'],
#                             mainPhoneNumber=form.cleaned_data['mainPhoneNumber'])
            
#             appregister.save()

#         return redirect('home')
	
 

    


def about(request):
    return render(request, 'blog/about.html', {'title': 'من أنا'})


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.filter(active=True)

    # check before save data from comment form
    if request.method == 'POST':
        comment_form = NewComment(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            # Deprecated line to prevent form to post data when refresh a page
            # comment_form = NewComment()
            return redirect('detail', post_id)
    else:
        comment_form = NewComment()

    context = {
        'title': post,
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    }

    return render(request, 'blog/detail.html', context)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # fields = ['title', 'content']
    template_name = 'blog/new_post.html'
    form_class = PostCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'blog/post_update.html'
    form_class = PostCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class PostDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



class CatListView(ListView):
    template_name = 'blog/category.html'
    context_object_name = 'catlist'



    def get_queryset(self):

        
        content = {

            'cat': self.kwargs['category'],
            'posts': Post.objects.filter(category__name=self.kwargs['category']),
        }

        return content

def category_list(request):

    category_list = Category.objects.all()
    

    context = {
        "category_list": category_list,
    }
    return context    

def application_list(request):
    
    application_list = AppRegs.objects.all()
    context = {
        "application_list": application_list,
    }
    return context    

def applist(request , app_id):
    applicationId = get_object_or_404(AppRegs,pk=app_id)
    # form=AppRegs.objects.all()
    
    context = {
        'applicationId': applicationId
    }
        
    return render(request, 'blog/table_data.html',context)     
    # return render(request, 'blog/application_detail.html',context)     
    # return render(request, 'blog/app_list.html',context)     

# الجدول الثاني
def multistipform_list(request):
    
    multistipform_list = MultiStepFormModel.objects.all()
    context = {
        "multistipform_list": multistipform_list,
    }
    return context   

def applistmultistipform(request , app_id):
    applicationId = get_object_or_404(MultiStepFormModel,pk=app_id)
    # form=AppRegs.objects.all()
    
    context = {
        'applicationIdmultistep': applicationId
    }
        
    return render(request, 'blog/table_dataMultistep.html',context)     

# الجدول الثالث
def multistipformBr_list(request):
    
    multistipformBr_list = MultiStepFormModelBr.objects.all()
    context = {
        "multistipformBr_list": multistipformBr_list,
    }
    return context   

def applistmultistipformBr(request , app_id):
    applicationId = get_object_or_404(MultiStepFormModelBr,pk=app_id)
    # form=AppRegs.objects.all()
    
    context = {
        'applicationIdmultistepBr': applicationId
    }
        
    return render(request, 'blog/table_dataMultistepBr.html',context) 


# نهايه الجدول الثالث


def admin_list(request):
    
    admin_list = AppRegs.objects.all()
    context = {
        "admin_list": admin_list,
    }
    return render(request,'blog/application_admin_detail.html',context)     







class FormmView(View):

                
    def get(self,request):
        return render (request , 'blog/formmV.html')

    def post(self,request):


        context={
            'data':request.POST,
            'has_error':False,
        }
        
        companyName = request.POST.get('companyName')
        creationDate = request.POST.get('creationDate')
        status = request.POST.get('status')
        associatesNumber = request.POST.get('associatesNumber')
        employeesNumber = request.POST.get('employeesNumber')
        createdJobsNumber = request.POST.get('createdJobsNumber')
        fullAddress = request.POST.get('fullAddress')
        wilaya = request.POST.get('wilaya')
        ownersEmail = request.POST.get('ownersEmail')
        ownersLinkedin = request.POST.get('ownersLinkedin')
        contactEmail = request.POST.get('contactEmail')
        mobilePhoneNumber = request.POST.get('mobilePhoneNumber')
        mainPhoneNumber = request.POST.get('mainPhoneNumber')

        try:
            if companyName == '':
                
                messages.add_message(request, messages.ERROR,
                                    'companyName is required' )
                context['has_error'] = True
        except Exception as identifier:  
            pass 

        try:
            if AppRegs.objects.get(companyName=companyName):
                    messages.add_message(request, messages.ERROR, 'اسم الشركه مستخدم سابقا')
                    context['has_error'] = True
        except Exception as identifier:
            pass  
        try:
            if fullAddress == '':
                
                messages.add_message(request, messages.ERROR,
                                    'fullAddress is required' )
                context['has_error'] = True
        except Exception as identifier:  
            pass 
  
        try:
            if fullAddress.isalnum() == False:
                
                messages.add_message(request, messages.ERROR,
                                    ' ادخل العنوان من ارقام وحروف فقط' )
                context['has_error'] = True
        except Exception as identifier:  
            pass   
        try:
            if status.isalpha() == False:
                
                messages.add_message(request, messages.ERROR,
                                    'Error in status name' )
                context['has_error'] = True
        except Exception as identifier:  
            pass  
        try:        
            if associatesNumber.isdigit() == False:
                messages.add_message(request, messages.ERROR,
                                    'من فضلك ادخل ارقام فقط لعدد الشركاء')
                context['has_error'] = True
        except Exception as identifier:
            pass
        try:        
            if employeesNumber.isdigit() == False:
                messages.add_message(request, messages.ERROR,
                                    ' من فضلك ادخل ارقام فقط لعدد الموظفين')
                context['has_error'] = True
        except Exception as identifier:
            pass
        try:        
            if createdJobsNumber.isdigit() == False:
                messages.add_message(request, messages.ERROR,
                                    'من فضلك ادخل ارقام فقط')
                context['has_error'] = True
        except Exception as identifier:
            pass

           
        try:        
            if AppRegs.objects.get(ownersEmail=ownersEmail):
                messages.add_message(request, messages.ERROR, 'ايميل مالك الشركه مستخدم سابقا')
                context['has_error'] = True
        except Exception as identifier:
            pass    
        try:        
            if ownersEmail == "":
                messages.add_message(request, messages.ERROR, ' من فضلك ادخل ايميل مالك الشركه  ')
                context['has_error'] = True
        except Exception as identifier:
            pass    


        if context['has_error']:


            return redirect('formmV')
        else:

            user = AppRegs.objects.create(creationDate=creationDate,wilaya=wilaya,ownersLinkedin=ownersLinkedin,contactEmail=contactEmail,mobilePhoneNumber=mobilePhoneNumber,mainPhoneNumber=mainPhoneNumber,companyName=companyName, associatesNumber=associatesNumber,ownersEmail=ownersEmail,employeesNumber=employeesNumber,createdJobsNumber=createdJobsNumber,status=status,fullAddress=fullAddress)   
            user.save()

            messages.success(request,"تم حفظ البيانات بنجاح برجاء متابعه صفحتك الشخصيه لمعرفه حاله الطلب وشكرا")
            return HttpResponseRedirect(reverse('home'))

            messages.error(request,"عفوا هناك خطأ عليك التاكيد من بياناتك وحاول مره أخري")
            return HttpResponseRedirect(reverse('formmV')) 

            # return redirect ('home')   

            # messages.add_message(request , messages.SUCCESS,'Congrtulation')



def multilistformmV(request):
    if request.method == 'POST':
        form = MultiFormStep(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('multilistformmV'))
    else:
        form = MultiFormStep()
    context = {'form':form}

    return render (request , 'blog/multilistformmV.html',context )    


def multilistformmV_save(request):

    if request.method == 'POST':

            
        Tname=request.POST.get('Tname')
        fname=request.POST.get('fname')
        You_are =request.POST.get('You_are')
        age=request.POST.get('age')
        wilaya=request.POST.get('wilaya')
        fullAddress=request.POST.get('fullAddress')
        Email=request.POST.get('Email')
        mainPhoneNumber=request.POST.get('mainPhoneNumber')
        webLink=request.POST.get('webLink')
        fbLink=request.POST.get('fbLink')
        ytubeLink=request.POST.get('ytubeLink')
        prjname=request.POST.get('prjname')
        file = request.FILES.get('file')
        file_CV = request.FILES.get('file_CV')
        file_Br = request.FILES.get('file_Br')
        prjfield=request.POST.get('prjfield')
        prjdetail=request.POST.get('prjdetail')
        prjprgress=request.POST.get('prjprgress')
        awards=request.POST.get('awards')

        
        try:
            multistepform=MultiStepFormModel(file_Br=file_Br,file_CV=file_CV,file=file,Tname=Tname,fname=fname,You_are=You_are,age=age,wilaya=wilaya,fullAddress=fullAddress,Email=Email,mainPhoneNumber=mainPhoneNumber,webLink=webLink,fbLink=fbLink,ytubeLink=ytubeLink,prjname=prjname,prjfield=prjfield,prjdetail=prjdetail,prjprgress=prjprgress,awards=awards)
            multistepform.save()
            messages.success(request,"تم حفظ البيانات بنجاح برجاء متابعه صفحتك الشخصيه لمعرفه حاله الطلب وشكرا")
            return HttpResponseRedirect(reverse('home'))
        
        except:
            messages.error(request,"عفوا هناك خطأ عليك التاكيد من بياناتك وحاول مره أخري")
            return HttpResponseRedirect(reverse('multilistformmV'))   
                
            
# def showmulstpform(request):

#     if request.method == 'POST':

#         form = MultiFormStep(request.POST)

#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('multilistformmV'))
#     else:
#         form = MultiFormStep()
#     context = {'form':form}

#     return render (request , 'blog/multilistformmV.html',context )    



# last form view (LABLE-INCUBATOR)

def multilistformmBr(request):
    if request.method == 'POST':
        form = MultiFormStepBr(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('multilistformmBr'))
    else:
        form = MultiFormStepBr()
    context = {'form':form}

    return render (request , 'blog/multilistformmBr.html',context )    


def multilistformmBr_save(request):

    if request.method == 'POST':

            
        Tname=request.POST.get('Tname')
        fname=request.POST.get('fname')
        You_are =request.POST.get('You_are')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        wilaya=request.POST.get('wilaya')
        fullAddress=request.POST.get('fullAddress')
        Email=request.POST.get('Email')
        mainPhoneNumber=request.POST.get('mainPhoneNumber')
        
        hadena_name=request.POST.get('hadena_name')
        legal_status=request.POST.get('legal_status')
        numemployees=request.POST.get('numemployees')
        creation_date=request.POST.get('creation_date')
        nif=request.POST.get('nif')
        nis=request.POST.get('nis')
        file = request.FILES.get('file')
        file_CV = request.FILES.get('file_CV')
        file_Br = request.FILES.get('file_Br')
        file_CNAS = request.FILES.get('file_CNAS')
        prjdesc=request.POST.get('prjdesc')
        file_dev = request.FILES.get('file_dev')
        listequip=request.POST.get('listequip')
        file_pres = request.FILES.get('file_pres')
        listincubated=request.POST.get('listincubated')
        file_cv_founder = request.FILES.get('file_cv_founder')

        try:
            multistepformBr=MultiStepFormModelBr(Tname=Tname,fname=fname,You_are=You_are,age=age,gender=gender,wilaya=wilaya,fullAddress=fullAddress,Email=Email,mainPhoneNumber=mainPhoneNumber,hadena_name=hadena_name,legal_status=legal_status,numemployees=numemployees,creation_date=creation_date,nif=nif,nis=nis,file=file,file_CV=file_CV,file_Br=file_Br,file_cv_founder=file_cv_founder,listincubated=listincubated,file_pres=file_pres,listequip=listequip,file_dev=file_dev,prjdesc=prjdesc,file_CNAS=file_CNAS)
            multistepformBr.save()
            messages.success(request,"تم حفظ البيانات بنجاح برجاء متابعه صفحتك الشخصيه لمعرفه حاله الطلب وشكرا")
            return HttpResponseRedirect(reverse('home'))
    
        except:

            messages.error(request,"عفوا هناك خطأ عليك التاكيد من بياناتك وحاول مره أخري")
            return HttpResponseRedirect(reverse('multilistformmBr')) 










def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None



data = {
	"company": "Dennnis Ivanov Company",
	"address": "123 Street name",
	"city": "Vancouver",
	"state": "WA",
	"zipcode": "98663",


	"phone": "555-555-2345",
	"email": "youremail@dennisivy.com",
	"website": "dennisivy.com",
	}

#Opens up page as PDF
class ViewPDF(View):
	def get(self, request, *args, **kwargs):

		pdf = render_to_pdf('blog/table_data.html', data)
		return HttpResponse(pdf, content_type='application/pdf')


#Automaticly downloads to PDF file
class DownloadPDF(View):
	def get(self, request, *args, **kwargs):
		
		pdf = render_to_pdf('blog/table_data.html', data)

		response = HttpResponse(pdf, content_type='application/pdf')
		filename = "Invoice_%s.pdf" %("12341231")
		content = "attachment; filename='%s'" %(filename)
		response['Content-Disposition'] = content
		return response


# def index(request):
#     	context = {}
# 	return render(request, 'app/index.html', context)






def uploadfile(request):

    if request.method == 'POST':

        form = MultiFormStep(request.POST , request.FILES)

        if form.is_valid():
            form.save()
            return redirect ('home')
    else:
        form = MultiFormStep()
    context = {'form':form}

    return render (request , 'blog/multilistformmV.html',context )    


def myform(request):

    if request.method == 'POST':

        form = RegsForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect ('home')

    else:
        form = RegsForm()
    return render (request , 'blog/myform.html' ,{'data':form})            