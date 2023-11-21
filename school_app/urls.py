from django.urls import path
from school_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.HomePage.as_view(),name='homepage'),
    path('StudentList/',views.StudentList.as_view(),name='student_list'),
    path('AddStudent/',views.AddStudent.as_view(),name='add_student'),
    path('UpdateStudent/<int:pk>/',views.UpdateStudent.as_view(),name='update_student'),
    path('DeleteStud/<int:pk>/',views.delete_student,name='delete_student'),
    path('ContactUs/',views.ContactUsPage.as_view(),name='contact_us')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)