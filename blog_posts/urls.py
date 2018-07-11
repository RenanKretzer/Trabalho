
"" "
Configuração da URL do crudapp
A lista `urlpatterns` encaminha os URLs para as visualizações. Para mais informações, consulte:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"" "
from django.conf.urls import url
de admin de importação django.contrib
das visualizações de importação de blog_posts

urlpatterns = [
    url ( r ' ^ admin / ' , admin.site.urls),
    url ( r ' ^ $ ' , views.post_list, name = ' post_list ' ),
    url ( r ' ^ new $ ' , views.post_create, nome = ' post_new ' ),
    url ( r ' ^ edit / ( ? P <pk> \ d + ) $ ' , views.post_update, name = ' post_edit ' ),
    url ( r ' ^ delete / ( ? P <pk> \ d + ) $ ' , views.post_delete, nome = ' post_delete ' ),
]