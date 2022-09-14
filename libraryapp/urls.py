from django.urls import path
from . import views
urlpatterns=[
path('',views.index,name='index'),
path('signup',views.signup,name="signup"),
path('signin',views.signin,name="signin"),




path('create',views.create_view),
path('list/all',views.list_view),
path('detail/<id>',views.detail_view),
path('update/<id>',views.update_view),
path('delete/<id>',views.delete_view),



# path('geeky/',views.create_view),
# path('geeky/all',views.list_view),
# path('geeky/<id>',views.detail_view),
# path('geeky/<id>/update',views.update_view),
# path('geeky/<id>/delete',views.delete_view),

]