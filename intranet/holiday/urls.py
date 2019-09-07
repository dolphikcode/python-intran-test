from django.conf.urls import url
from holiday import views

# SET THE NAMESPACE!
app_name = 'vacation'

urlpatterns = [
    # url(r'^$',views.index,name='index'),
    url(r'^form', views.form, name="form"),
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
]