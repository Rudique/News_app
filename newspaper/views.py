
from django.views import generic, View
from .models import NewsModel, CommentModel
from .forms import NewsForm, CommentForm
from django.shortcuts import render, HttpResponseRedirect

# Create your views here.


class NewsModelListView(generic.ListView):
    model = NewsModel
    template_name = 'newspaper/news_list.html'
    context_object_name = 'news_list'


class NewsFormView(View):

    def get(self, request):
        news_form = NewsForm()
        return render(
            request,
            'newspaper/news_add.html',
            context={
                'news_form': news_form
            })

    def post(self, request):
        news_form = NewsForm(request.POST)
        if news_form.is_valid():
            NewsModel.objects.create(**news_form.cleaned_data)
            return HttpResponseRedirect('/news')

        return render(request, "newspaper/news_add.html", context={'news_form': news_form})


class NewsFormEditView(View):
    def get(self, request, news_id):
        news_object = NewsModel.objects.get(id=news_id)
        news_form = NewsForm(instance=news_object)
        return render(request, 'newspaper/news_edit.html', context={"news_form": news_form, "news_id": news_id})

    def post(self, request, news_id):
        news_object = NewsModel.objects.get(id=news_id)
        news_form = NewsForm(request.POST, instance=news_object)
        if news_form.is_valid():
            news_object.save()
            return HttpResponseRedirect('/news')
        return render(
            request,
            'newspaper/news_edit.html',
            context={"news_form": news_form, "news_id": news_id}
        )


class NewsDetailView(generic.DetailView):
    model = NewsModel
    template_name = 'newspaper/news_detail.html'
    context_object_name = 'news_object'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        id = context['news_object'].id
        print(id)
        comments = CommentModel.objects.filter(article_id=id).all()
        context['comments'] = comments
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, pk):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.cleaned_data['article_id'] = pk
            CommentModel.objects.create(**comment_form.cleaned_data)
            url = '/news/' + str(pk)
            return HttpResponseRedirect(url)
