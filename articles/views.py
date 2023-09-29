from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from articles.models import Article
from .forms import articleForms
from random import randint
from django.template.loader import render_to_string, get_template


def home(request):

    my_list = [12,45,78,98,100,98]
    random_id = randint(1,4)
    article_obj = Article.objects.get(id = random_id)
    object_ls = Article.objects.all()
    context = {
        "object_list": object_ls,
        "my_list": my_list,
        "title" : article_obj.title,
        "id" : random_id,
        "content" : article_obj.content
    }
    

    html_str = render_to_string('articles\home_view.html', context = context)

    return HttpResponse(html_str)

@login_required
def article_create_view(request):
    context = {
        'form': articleForms()
        
    }
    if request.method == 'POST':
        form = articleForms(request.POST)
        if form.is_valid():
            Title = form.cleaned_data.get('title')
            Content = form.cleaned_data.get('content')
       
            obj = Article.objects.create(title=Title, content=Content)
            context = {
                'object': obj,
                'created':True,
                'form': form
            } 
            return render(request, 'articles\create.html',context = context) 
    return render(request, 'articles\create.html',context = context)  


def article_search_view(request, id = None):

    query_dict = request.GET #GET() will return a dictionary
    article_obj = None
    query = query_dict.get('q')
    if query is not None:
        article_obj = Article.objects.get(id = query)#<input type="text" name="q"/>
    context = {
        'object': article_obj,
        'id':id
    }
    return render(request, 'articles\search.html',context = context)



