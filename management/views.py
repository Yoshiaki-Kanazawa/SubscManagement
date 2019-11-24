from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.views import generic
from .forms import SignupForm, AddServiceForm, UpdateForm, PasswordChangeForm
from .models import Service
from django.db.models import Sum
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse_lazy


class Signup(generic.CreateView):
    def post(self, request, *args, **kwargs):
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(to='/management')
        else:
            return render(request, 'management/signup.html', {'form': form})

    def get(self, request, *args, **kwargs):
        form = SignupForm()
        return render(request, 'management/signup.html', {'form': form})

class Management(generic.CreateView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = self.request.user
            services = Service.objects.filter(user__id = user.id)
            serviceNum = Service.objects.filter(user__id = user.id).count()
            result = Service.objects.filter(user__id = user.id).aggregate(monthTotal=Sum('price'))
            if result.get('monthTotal') == None:
                result['monthTotal'] = 0
            return render(request, 'management/management.html',
                {'services' : services, 'serviceNum': serviceNum, 'monthTotal': result.get('monthTotal')})
        else:
            return redirect(to='/accounts/login')

class AddService(generic.CreateView):
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            form = AddServiceForm(request.POST)
            if form.is_valid():
                service = Service(
                    user = self.request.user,
                    service_name = form.cleaned_data['servicename'],
                    price = form.cleaned_data['price'],
                    start_date = form.cleaned_data['startdate']
                    )
                service.save()
                user = self.request.user
                services = Service.objects.filter(user__id = user.id)
                return redirect('/management', {'services' : services})
            else:
                return render(request, 'management/addService.html', {'form': form})
        else:
            return redirect(to='/accounts/login')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            form = AddServiceForm()
            return render(request, 'management/addService.html', {'form': form})
        else:
            return redirect(to='/accounts/login')

class Detail(generic.CreateView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            serviceid = self.kwargs.get("serviceid")
            service = Service.objects.get(id = serviceid)
            form = UpdateForm(None, initial = {
                    'servicename': service.service_name,
                    'price': service.price,
                    'startdate': service.start_date
                })
            return render(request, 'management/detail.html',
                {'form': form, 'service': service, 'serviceid': serviceid})
        else:
            return redirect(to='/accounts/login')

class Update(generic.CreateView):
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            form = UpdateForm(request.POST)
            if form.is_valid():
                serviceid = self.kwargs.get("serviceid")
                service = Service.objects.get(id = serviceid)
                service.service_name = form.cleaned_data['servicename']
                service.price = form.cleaned_data['price']
                service.start_date = form.cleaned_data['startdate']
                service.save()
                return redirect(to='/management')
            else:
                return render(request, 'management/detail.html', {'form': form})
        else:
            return redirect(to='/accounts/login')

class Delete(generic.CreateView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            serviceid = self.kwargs.get("serviceid")
            Service.objects.get(id = serviceid).delete()
            return redirect(to='/management')
        else:
            return redirect(to='/accounts/login')

class UserDetail(generic.CreateView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            form = PasswordChangeForm()
            return render(request, 'management/userDetail.html', {'form': form})
        else:
            return redirect(to='/accounts/login')

class PasswordChange(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('management:password_change_done')
    template_name = 'management/password_change.html'

class PasswordChangeDone(PasswordChangeDoneView):
    template_name = 'management/password_change_done.html'

class UserDelete(generic.CreateView):
    def get(self, request, *args, **kwargs):
        logout(request)
        self.request.user.delete()
        return redirect(to='/accounts/login')