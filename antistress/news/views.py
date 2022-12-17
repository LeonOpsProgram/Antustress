from django.shortcuts import render, redirect
from .models import Test
from .forms import TestForm
from django.views.generic import DetailView, UpdateView, DeleteView


def test_home(request):
    test = Test.objects.order_by('id')
    return render(request, 'news/test_home.html', {'tests': test})


class NewsDetailView(DetailView):
    model = Test
    template_name = 'news/details_test.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Test
    template_name = 'news/create_test.html'
    context_object_name = 'update'

    form_class = TestForm


class NewsDeliteView(DeleteView):
    model = Test
    success_url = '/news/'
    template_name = 'news/test-delete.html'



def create_test(request):
    error = ''
    if request.method == "POST":
        form = TestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неккорктна'
    form = TestForm
    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'news/create_test.html', data)


def test_work(request):
    tests = Test.objects.order_by('id')
    return render(request, 'news/test_work.html', {'tests': tests})
# def create_test(request):
#     return render(request, 'news/create_test.html')
