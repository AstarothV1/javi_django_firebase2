from django.shortcuts import render
from django.views.generic import View

import firebase_admin

from firebase_admin import credentials
from firebase_admin import db
# Create your views here.

cred = credentials.Certificate("./django-javier-example-firebase-adminsdk-4njd3-b6a1715a19.json")

firebase_admin.initialize_app(cred, {'databaseURL': "https://django-javier-example-default-rtdb.firebaseio.com/"})  

class Sensibilidades(View):

    template_name = "index.html"

    ref = db.reference('Sensibilidades')

    data = ref.get()

    def get(self, request):
        return render(request, self.template_name, {"Sensibilidades": self.data})




