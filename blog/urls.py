from django.urls import path
from . import views
from .views import PostCreateView, PostUpdateView, PostDeleteView , CatListView ,ViewPDF,DownloadPDF

urlpatterns = [
    path('', views.home, name='home'),
    path('new_post/', PostCreateView.as_view(), name='new_post'),
    path('allposts/', views.allposts, name='allposts'),
    path('about/', views.about, name='about'),
    # path('formm/', views.formm, name='formm'),

    path('pdf_view/', views.ViewPDF.as_view(), name="pdf_view"),
    path('pdf_download/', views.DownloadPDF.as_view(), name="pdf_download"),

    path('formmV/', views.FormmView.as_view(), name='formmV'),
    path('multilistformmV/', views.multilistformmV, name='multilistformmV'),
    path('multilistformmV_save/', views.multilistformmV_save, name='multilistformmV_save'),
    path('multilistformmBr/', views.multilistformmBr, name='multilistformmBr'),
    path('multilistformmBr_save/', views.multilistformmBr_save, name='multilistformmBr_save'),
    path('myform/', views.myform , name='myform'),

    path('uploadfile/', views.uploadfile, name='uploadfile'),

    path('adminapp/', views.admin_list, name='adminapp'),
    path('adminapp/<int:app_id>/', views.applist, name='adminapp'),
    path('applistmultistipform/<int:app_id>/', views.applistmultistipform, name='applistmultistipform'),
    path('applistmultistipformBr/<int:app_id>/', views.applistmultistipformBr, name='applistmultistipformBr'),

    # path('application/', views.adduser, name='application'),
    path('detail/<int:post_id>/', views.post_detail, name='detail'),
    path('category/<category>', CatListView.as_view(), name='category'),

    path('detail/<slug:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('detail/<slug:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
