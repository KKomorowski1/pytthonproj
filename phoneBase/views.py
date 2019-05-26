from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.views import generic
from django.views.generic import DeleteView, UpdateView

from phoneBase.forms import DetailForm, GeneralForm
from .models import General, Details


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'phoneBase/index.html'
    context_object_name = 'phone_list'

    def get_queryset(self):
        return General.objects.all()


class DetailView(generic.DetailView):
    model = General
    template_name = 'phoneBase/details.html'


class PhoneDelete(DeleteView):
    model = General
    success_url = '/phoneBase/'


class PhoneUpdate(UpdateView):
    model = General
    fields = "__all__"
    success_url = '/phoneBase/'


class DetailsUpdate(UpdateView):
    model = Details
    fields = ['procesor', 'pamiec', 'pamiec_ram', 'bateria']
    success_url = '/phoneBase/'
    template_name = 'phoneBase/updateDetail.html'


def phone_save(request):
    if request.method == 'POST':
        general_form = GeneralForm(request.POST)
        details_form = DetailForm(request.POST)

        if general_form.is_valid() and details_form.is_valid():
            general = general_form.save()
            details = details_form.save(False)

            details.general = general
            details_form.full_clean()
            details.save()

            return redirect('/phoneBase/')
        else:
            return render(request, 'phoneBase/add.html', {'general_form': general_form, 'details_form': details_form},
                          {'error_message': "Coś poszło nie tak... spróbuj ponownie."})
    else:
        general_form = GeneralForm
        details_form = DetailForm
        args = {}
        args.update(csrf(request))
        args['general_form'] = general_form
        args['details_form'] = details_form

        return render(request, 'phoneBase/add.html', args)
