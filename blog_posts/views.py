from django.shortcuts import render

# Create your views here.
# - * - codificação: utf-8 - * -
from  __future__  import unicode_literals

de django.shortcuts import render, redirecionar, get_object_or_404
de django.forms import ModelForm

de blog_posts.models import blog_posts
# Crie suas visualizações aqui.

classe  PostsForm ( ModelForm ):
    classe  Meta :
        model = blog_posts
        fields = [ ' id ' , ' title ' , ' author ' ]

def  post_list ( request , template_name = ' blog_posts / post_list.html ' ):
    posts = blog_posts.objects.all ()
    data = {}
    data [ ' object_list ' ] = mensagens
    return render (request, template_name, data)

def  post_create ( pedido , template_name = ' blog_posts / post_form.html ' ):
    form = PostsForm (request. POST  ou  None )
    if form.is_valid ():
        form.save ()
        return redirect ( ' blog_posts: post_list ' )
    return render (request, template_name, { ' form ' : form})

def  post_update ( solicitação , pk , template_name = ' blog_posts / post_form.html ' ):
    post = get_object_or_404 (blog_posts, pk = pk)
    form = PostsForm (request. POST  ou  None , instance = post)
    if form.is_valid ():
        form.save ()
        return redirect ( ' blog_posts: post_list ' )
    return render (request, template_name, { ' form ' : form})

def  post_delete ( solicitação , pk , template_name = ' blog_posts / post_delete.html ' ):
    post = get_object_or_404 (blog_posts, pk = pk)
    if request.method == ' POST ' :
        post.delete ()
        return redirect ( ' blog_posts: post_list ' )
    return render (request, template_name, { ' objeto ' : post})