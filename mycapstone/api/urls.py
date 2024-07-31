from django.conf import settings
from django.conf.urls.static import static
from django.urls import path 
from . import views
from knox import views as knox_views

urlpatterns = [
    path("aot/", views.AttackTitanListCreate.as_view(), name="attacktitan-view-create"),
    path("aot/<int:pk>/",
         views.AttackTitanRetrieveUpdateDestroy.as_view(),
         name="update"),
    path("mha/", views.MyHeroListCreate.as_view(), name="myhero-view-create"),
    path("mha/<int:pk>/",
         views.MyHeroRetrieveUpdateDestroy.as_view(),
         name="update"),
    path("jjk/", views.JujutsuKaisenListCreate.as_view(), name="jujutsukaisen-view-create"),
    path("jjk/<int:pk>/",
         views.JujutsuKaisenRetrieveUpdateDestroy.as_view(),
         name="update"),
    path('register/',views.RegisterView.as_view(),name='register'),
    path('login/',views.LoginView.as_view(),name='login'),
    path('logout/',views.KnoxLogoutView.as_view(),name='logout'),
    path('logoutall/',knox_views.LogoutAllView.as_view(),name='logoutall'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
