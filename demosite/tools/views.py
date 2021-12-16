from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class testView(View):
    def get(self, request):
        data = [{
            "key01": "value01",
            "key02": "value02",
            "key03": "value03",
            "key04": "value04",
            "key05": "value05",
        }]
        return JsonResponse({"data": data})

    def post(self, request):
        data = [{
            "key01": "value01",
            "key02": "value02",
            "key03": "value03",
            "key04": "value04",
            "key05": "value05",
        }]
        return JsonResponse({"data": data})
