from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render
from .forms import PrimeForm
from .utils import check_prime
from itertools import count, islice


class Nth_Prime(View):
    template_name = 'prime.html'
    form_class = PrimeForm



    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})


    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)
        if form.is_valid():
            nth = form.cleaned_data['nth_number']
            if nth == 1:
                return 2  
            counting = 1
            for number in count(3,2):
                if check_prime(number):
                    counting = counting+1
                    if counting == nth:
                        break;
            return render(request, self.template_name, {'form': form,'number':number})
        return render(request, self.template_name, {'form': form})
