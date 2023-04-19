from django.shortcuts import render , redirect
from django.views.generic import View
from .models import Room
# Create your views here.


class MapView(View):
    def get(self,request,option=None):
        if option:
            if option == "horario":
                return render(request, 'map.html',{"option":option})
            elif option == "bagagem":
                return render(request, 'map.html',{"option":option})
            elif option == "duvidas":
                return render(request, 'map.html',{"option":option})
            
        else:
            return render(request, 'map.html')
        
    def post(self,request):
        choice_cod = request.POST["escolha"]  
        if(choice_cod == "doc"):
            return redirect("map", choice_cod)
        elif(choice_cod == "horario"):
            return redirect("map", choice_cod)
        elif(choice_cod == "bagagem"):
            return redirect("map", choice_cod)
        elif(choice_cod == "duvidas"):
            return redirect("map", choice_cod)
        elif(choice_cod == "doc"):
            return redirect("map", choice_cod)
       


        
def homepage(request):
    rooms = Room.objects.all()
    return render(request, 'home.html', {'rooms': rooms})