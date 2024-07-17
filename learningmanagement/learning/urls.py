from django.urls import path
from .import views

urlpatterns=[
    path('',views.mainpage,name='mainpage'),
    
    path('instructormain/',views.instructormain,name='instructormain'),
    path('studentmain/',views.studentmain,name='studentmain'),
    path('instructorregister/',views.UserInstructorCreate,name='UserInstructorCreate'),
    path('UserInstructorLogins/',views.UserInstructorLogin,name='UserInstructorLogin'),
    path('studentregister/',views.UserStudentCreate,name='UserStudentCreate'),
    path('UserstudentLogins/',views.UserStudentLogin,name='UserStudentLogin'),
    path('courselist/',views.cource_list_view.as_view(),name='courcelist'),
    path('coursecreate/',views.cource_create_view.as_view(),name='cource_create_view'),
    path('courseDetail/<int:pk>/',views.cource_detail_view.as_view(),name='courcedetailview'),
    path('courseupdate/<int:pk>/',views.cource_update_view.as_view(),name='cource_update_view'),
    path('coursedlete/<int:pk>/',views.cource_delete_view.as_view(),name='cource_delete_view'),
    path('sign_out/',views.signout_page,name='signout_page'),
    
    path('assignmentList/',views.Assignment_list_view.as_view(),name="Assignment_list_view"),
    path('assignmentCreate/',views.Assignment_create_view.as_view(),name="Assignment_create_view"),
    path('assignmentdetail/<int:pk>',views.Assignment_detail_view.as_view(),name="Assignment_detail_view"),
    path('assignmentupdate/<int:pk>',views.Assignment_update_view.as_view(),name="Assignment_update_view"),
    path('assignmentdelete/<int:pk>',views.Assignment_delete_view.as_view(),name="Assignment_delete_view"),
    
    path('courselistviewforstudent/',views.course_list_view_for_student.as_view(),name='courseforstudent'),
    path('assignmentlistviewforstudent/',views.assignment_list_view_for_student.as_view(),name='assignmentforstudent'),
    path('assignmentdetailviewforstudent/<int:pk>/',views.assignment_detail_view_for_student.as_view(),name='assdetailstudent'),
    path('assignments/<int:pk>/submit/', views.solution_create_view_ofstudent.as_view(), name='solution-create'),

    
   
]