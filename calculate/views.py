from django.shortcuts import render
from calculate.forms import CalForm
from django.views.generic import TemplateView

# def CalculateView(request):
#     form = CalculateForm(request.POST or None)
#     if form.is_valid():
#         form = CalculateForm()
#         print(form.fields['number'])

#     context = {
#         'form':form
#     }

#     return render(request, 'index.html', context=context)


class HomeView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        form = CalForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = CalForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            number = form.cleaned_data['number']

            result = number*number

            form = CalForm()

            args = {'form':form, 'result':result, 'name':name}

            return render(request, self.template_name, args)