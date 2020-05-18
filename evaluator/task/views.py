from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .forms import CompanyForm, InformationForm
from .models import Information, Companie


class InputView(CreateView):
    """
    The view that registers the company
    """
    template_name = 'input.html'
    form_class = CompanyForm
    success_url = reverse_lazy('info')


class InfoView(CreateView):
    """
    A view that inserts information performance
    """
    template_name = 'info.html'
    form_class = InformationForm
    success_url = reverse_lazy('result')


def result(request):
    """
    a view that gives off the information inserted, graphically
    :param request:
    :return:
    """
    template_name = 'result.html'
    information = Information.objects.all()
    company = Companie.objects.all()
    # info = get_object_or_404(information)
    # # danger = range(0, 49)
    # # medium = range(50, 69)
    # # high = range(70, 100)
    # # # color = {}
    # #
    # # def coloring():
    # #     if Information.score == danger:
    # #         color = "red"
    # #
    # #     elif Information.score == medium:
    # #         color = ""
    # #
    # #     elif Information.score == high:
    # #         color = "green"
    #
    # # if Information.score == danger:
    # #     color = "red"
    # #
    # # elif Information.score == medium:
    # #     color = ""
    # #
    # # elif Information.score == high:
    # #     color = "green"
    # #
    # # return color
    # # color = print (Color)
    # # danger = range(0, 49)
    # # # medium = range(50, 69)
    # # high = range(70, 100)
    # context = {
    #     "color": {
    #         "red": info.score in danger,
    #         "green": info.score in high,
    #     },
    context = {
        'Information': information,
        # 'color': Information.color(information),
        'Company': company,
    }

    return render(request, template_name, context)


# class ResultView(ListView):
#     template_name = 'result.html'
#     model = Information
#     context_object_name = 'Information'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         pass
