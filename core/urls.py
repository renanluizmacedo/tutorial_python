from django.urls import path
from .views import home,criar_post,editar_post,deletar_post,login_view,logout_view
from django.conf.urls.static import static 
from django.conf import settings
urlpatterns = [
    path('',home,name='home'),
    path('criar/',criar_post,name='criar_post'),
    path('editar/<int:id>/',editar_post,name='editar_post'),
    path('deletar/<int:id>/',deletar_post,name='deletar_post'),
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)