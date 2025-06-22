from django.shortcuts import render,redirect
from .models import menu,reservations
from .forms import reservation_form,MenuItemForm
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from rest_framework import viewsets
from .serializers import MenuItemSerializer
from .permissions import IsManagerOrReadOnly
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def home(request):
    return render(request,"home.html")
def about(request):
    return render(request,"about.html")
@csrf_exempt
def book(request):
    form = reservation_form()
    if request.method == "POST":
        form = reservation_form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            # Check if this date and time are already booked
            existing = reservations.objects.filter(date=cd['date'], time=cd['time'])
            if existing.exists():
                return JsonResponse({'error': 'This time slot is already booked!'}, status=400)

            # Save reservation
            lf = reservations(
                name=cd['name'],
                reservation_slot=cd['reservation_slot'],
                date=cd['date'],
                time=cd['time'],
            )
            lf.save()

            return JsonResponse({'message': 'success'}, status=200)

    return render(request, "book.html", {"form": form})
def menu_view(request):
    menuv = menu.objects.all()
    return render(request,"menu.html",{"menu":menuv})
def menu_item(request,pk):
    item = menu.objects.get(pk=pk)
    return render(request,"menu_item.html",{"item":item})

def is_manager(user):
    return user.is_staff  # or check for a "Manager" group


def menu_item_list(request):
    items = menu.objects.all()
    return render(request, 'menu.html', {'items': items})
@login_required
@user_passes_test(is_manager)
def menu_item_create(request):
    form = MenuItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('menu')
    return render(request, 'menu_item_form.html', {'form': form})
@login_required
@user_passes_test(is_manager)
def menu_item_update(request, pk):
    item = get_object_or_404(menu, pk=pk)
    form = MenuItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('menu')
    return render(request, 'menu_item_form.html', {'form': form})
@login_required
@user_passes_test(is_manager)
def menu_item_delete(request, pk):
    item = get_object_or_404(menu, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('menu')
    return render(request, 'menu_item_confirm_delete.html', {'item': item})
def custom_logout_view(request):
    logout(request)
    return redirect('login') 
class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = menu.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsManagerOrReadOnly]
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Delete the token to force a logout
        try:
            request.user.auth_token.delete()
        except:
            pass
        return Response({"detail": "Logged out successfully."}, status=status.HTTP_200_OK)
@csrf_exempt
def get_booked_slots(request):
    date = request.GET.get('date')
    if not date:
        return JsonResponse({'error': 'Date not provided'}, status=400)

    booked = reservations.objects.filter(date=date).values_list('time', flat=True)
    times = [str(t)[:5] for t in booked]  # Convert time to 'HH:MM'
    return JsonResponse({'booked_times': times})