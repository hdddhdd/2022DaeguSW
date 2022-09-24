from django.views.generic import ListView, DetailView
from .models import Post, CompanyName, Training
from django.shortcuts import render

class PostList(ListView):
    model = Post
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['company_names'] = CompanyName.objects.all()
        
        return context


class PostDetail(DetailView):
    model = Training

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['company_names'] = CompanyName.objects.all()
        
        return context


class trainingList(ListView):
    model = Training
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(trainingList, self).get_context_data()
        context['companyName'] = CompanyName.objects.all()
        
        return context


def trainingList_page(request, slug):
    companyName = CompanyName.objects.get(slug=slug)

    return render(
        request,
        'cooperation/training_list.html',
        {
            'training_list': Training.objects.filter(companyName=companyName),
            'categories': CompanyName.objects.all(),
            'no_category_post_count': Training.objects.filter(companyName=None).count(),
            'companyName': companyName,
        }

    )

class CompanySearch(PostList):
    paginate_by = None
    
    def get_queryset(self):
        q = self.kwargs['q']
        post_list = Post.objects.filter(companyName__contains=q).distinct()

        return post_list

    def get_context_data(self, **kwargs):
        context = super(CompanySearch, self).get_context_data()
        q = self.kwargs['q']
        context['search_info'] = f': {q} ({self.get_queryset().count()}))'

        return context
