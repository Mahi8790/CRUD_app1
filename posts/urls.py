from django.urls import path
from posts import views

urlpatterns =[
    # path('time/',views.current_datetime, name = 'date and time'),

    # path('',views.hii_mahesh, name = 'hii_mahesh'),
    # path('',views.create_view, name = 'form'),
    # path('',views.list_view, name = 'list'),
    path ('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('retrieve', views.retrieve, name='retrieve'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name = 'update'),
    path(r'^delete_product/(?P<pk>[0-9]+)/$', views.delete, name = 'delete'),
]