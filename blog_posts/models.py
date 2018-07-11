from django.db import models

# Create your models here.
# - * - codificação: utf-8 - * -
from  __future__  import unicode_literals

de modelos de importação django.db

# Crie seus modelos aqui.
class  blog_posts ( models . Model ):
    title = models.CharField ( max_length = 400 )
    tag = models.CharField ( max_length = 50 )
    author = models.CharField ( max_length = 120 )

    def  __unicode__ ( self ):
        retorno  auto .title

    def  get_post_url ( self ):
        retorno reverso ( ' post_edit ' , kwargs = { ' pk ' : self .pk})