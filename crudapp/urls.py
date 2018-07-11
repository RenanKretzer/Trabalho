"" "
Configuração do URL Crudapp
A lista `urlpatterns` encaminha os URLs para as visualizações. Para mais informações, consulte:
     https://docs.djangoproject.com/en/1.11/topics/http/urls/
 "" "
do URL de importação django.conf.urls , inclua
de admin de importação django.contrib
de crudapp.views import home

urlpatterns = [
    url ( r ' ^ admin / ' , admin.site.urls),
    url ( r ' ^ blog_posts / ' , include ( ' blog_posts.urls ' , espaço de nomes = ' blog_posts ' )),
    url ( r ' ^ $ ' , home, name = ' home ' ),
]