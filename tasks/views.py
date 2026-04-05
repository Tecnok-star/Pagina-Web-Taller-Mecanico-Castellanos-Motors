from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Este decorador (@) es el primer nivel de "Roles y Privilegios". 
# Le dice a Django: "Expulsa a los visitantes anónimos, solo usuarios con cuenta pueden ver esto".
@login_required
def panel_inicio(request):
    return render(request, 'inicio.html')
