from django.shortcuts import render

# Create your views here.
from django.views.generic import View

from django.http import JsonResponse

class AboutView(View):
    def get(self,request):
        response_data={
            "institution":"luminartechnolab",
            "service":"software development training"
        }
        return JsonResponse(response_data)

class Courseview(View):
    def get(self,respect):
        response_data= [

 {
          "id": 1,
          "title": "Python Full Stack Development",
          "duration": "5 Months",
          "technologies": ["Python", "Django", "React", "MySQL"]
      },
      {
          "id": 2,
          "title": "Data Science & AI",
          "duration": "4 Months",
          "technologies": ["Python", "Machine Learning", "Generative AI"]
      }
      
    ]
        return JsonResponse(response_data,safe=False)


        

