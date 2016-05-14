from django.http import HttpResponse
from django.views.generic import View
from .forms import PrimeForm


class MyView(View):
	template_name = 'form_template.html'
	form_class = PrimeForm
    def get(self, request):
        # <view logic
        return HttpResponse('result')


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():            
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})