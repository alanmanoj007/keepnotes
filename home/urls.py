from django.urls import path
from . import views

urlpatterns=[
    path('',views.fun,name='fun'),
    path('notes/<int:notes_id>',views.details,name='detail'),
    path('add/',views.add_note,name='add'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>', views.delete, name='delete')

]