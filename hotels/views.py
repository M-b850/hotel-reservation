from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from core.models import Hotel


class Index(View):
    def get(self, request):
        hotels = Hotel.objects.all()
        return render(
            request, template_name="hotels/list.html", context={"hotels": hotels}
        )
