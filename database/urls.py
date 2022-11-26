from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('insert',views.index1,name='index1'),
    path('insert/user',views.user_insert,name='user_insert'),
    path('insert/content',views.content_insert,name='content_insert'),
    path('view',views.index2,name='index2'),
    path('view/user',views.user_data,name='user_data'),
    path('view/content',views.content_data,name='content_data'),
    path('delete',views.index3,name='index3'),
    path('delete/user',views.delete_user,name='delete_user'),
    path('delete/content',views.delete_content,name='delete_content'),
    path('update',views.index4,name='index4'),
    path('update/user',views.user_update,name='user_update'),
    path('update/content',views.content_update,name='content_update'),
]