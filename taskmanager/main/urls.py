from django.urls import path
from . import views

urlpatterns = [
    path('', views.authorizations), 
    path('main', views.main),
    path('signin', views.signin),
    path('student', views.student),
    path('prepod', views.prepod),
    path('jurnal', views.jurnal),
    path('prepodprof', views.prepodprof),
    path('select_prof', views.select_prof),
    path('spisok', views.spisok),
    path('jurnali', views.jurnali),
    path('addgroup', views.addgroup),
    path('addurok', views.addurok),
    path('edit', views.edit),
    path('osebe', views.osebe),
    path('ocenka', views.ocenka),
]