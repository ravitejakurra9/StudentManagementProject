from django.urls import path

from StudentApp import views

urlpatterns=[
    path('',views.log_fun,name='log'),
    path('register',views.reg_fun,name='reg'), # it will redirect to register.html page
    path('regdata',views.regdata_fun), # it will create a superuser Account
    path('logdata',views.logdata_fun),# geit will read redirect
    path('home',views.home_fun,name='home'),# it will redirect to home page
    path('add_students',views.addstudent_fun,name='add'),
    path('readdata',views.readdata_fun),
    path('display',views.display_fun,name='display'),
    path('update/<int:id>',views.update_fun,name='update'),
    path('delete/<int:id>',views.delete_fun,name='delete'),
    path('log_out',views.logout_fun,name='log_out'),

]