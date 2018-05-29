import datetime
from django.views.generic.edit import FormView
from .forms import WorkDescriptionForm
# Create your views here.


class Durations(object):

    def get_current_week_date(self):
        today = datetime.datetime.now().date()
        dates = [today + datetime.timedelta(days=i) for i in \
                 range(0 - today.weekday(), 5 - today.weekday())]
        return dates


class Home(FormView):
    form_class = WorkDescriptionForm
    template_name = "index.html"
    success_url = "/work/"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super().form_valid(form)
