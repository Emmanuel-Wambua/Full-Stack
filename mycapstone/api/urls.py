from django.conf import settings
from django.conf.urls.static import static
from django.urls import path 
from . import views

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
         name="update")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
