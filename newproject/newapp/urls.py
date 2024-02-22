from django.urls import path
from . import views



urlpatterns=[
    path('',views.myfunction,name='index'),
    path('adds/<int:a>/<int:b>//',views.add,name='add'),
    path('i',views.index,name='index'),
    path('print',views.print,name='print'),
    path('create',views.create,name='create'),
    path('list',views.list,name='list'),
    path('edit',views.edit,name='edit'),
    path('new',views.new,name='new'),
    path('new/<int:movie_id>',views.detail,name='detail'),
    path('add/',views.add_movie,name='add_movie'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),





    



]

