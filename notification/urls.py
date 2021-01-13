from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = 'notification'
urlpatterns = [
    path('show/<int:notification_id>', views.show_notification, name='show'),
    path('delete/<int:notification_id>', views.delete_notification, name='delete'),

]+ static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)