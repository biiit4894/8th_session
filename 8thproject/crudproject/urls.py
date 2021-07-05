from django.contrib import admin
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static
import crudapp.views
import accounts.views
import photo.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', crudapp.views.home, name="home"),
    path('crudapp/<int:crudapp_id>', crudapp.views.detail, name="detail"),
    path('accounts/', include('accounts.urls')),
    path('crudapp/new', crudapp.views.new, name='new'),
    path('crudapp/postcreate', crudapp.views.postcreate, name='postcreate'),
    path('photo/',photo.views.photo,name='photo'),

    path('crudapp/edit', crudapp.views.edit, name="edit"),
    path('crudapp/postupdate/<int:crudapp_id>', crudapp.views.postupdate, name='postupdate'),

    path('crudapp/postdelete/<int:crudapp_id>', crudapp.views.postdelete, name='postdelete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
