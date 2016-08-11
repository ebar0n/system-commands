import subprocess

from django.views.generic import TemplateView

OPTIONS = {
    '1': 'pwd',
    '2': 'ls -la',
    '3': 'free -m',
    '4': 'df -h',
}


class IndexView(TemplateView):

    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['result'] = ''

        option = self.request.POST.get('option')
        if option in OPTIONS:
            cmd = subprocess.getstatusoutput(OPTIONS.get(option))
            context['result'] = cmd[1].split('\n')

        return context

    def post(self, request, *args, **kwargs):
        return super(IndexView, self).get(self, request, *args, **kwargs)
