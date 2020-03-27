from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .forms import CompanyForm, InformationForm
from .models import Information


class InputView(CreateView):
    template_name = 'input.html'
    form_class = CompanyForm
    success_url = reverse_lazy('info')


class InfoView(CreateView):
    template_name = 'info.html'
    form_class = InformationForm
    success_url = reverse_lazy('result')


class ResultView(ListView):
    template_name = 'result.html'
    model = Information
    context_object_name = 'Information'

    # def get(self, request, *args, **kwargs):
    #     if self.model.score >= :
    #         color = 'red'
    #     else:
    #         color = 'green'
    #
    #     return color

# def result(request):
#     template_name = 'result.html'
#     information = Information
#
#     color = ''
#     if request.method == 'GET':
#         if information.score == 70:
#             color = 'red'
#         else:
#             color = 'green'
#         return color
#
#     return render(request, template_name)
