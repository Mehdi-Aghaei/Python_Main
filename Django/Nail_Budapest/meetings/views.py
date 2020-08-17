from django.shortcuts import render, get_object_or_404, redirect
from .models import Appointment
from django.forms import modelform_factory


def home(request):
    return render(request, 'meetings/home.html')


def meeting(request):
    "Show All appointments"
    appointment = Appointment.objects.all()
    context = {"meetings": appointment}
    return render(request, 'meetings/meeting.html', context)


def detail(request, id):
    meeting = get_object_or_404(Appointment, pk=id)
    context = {"meeting": meeting}
    return render(request, 'meetings/detail.html', context)


MeetingForm = modelform_factory(Appointment, exclude=[])


def new_app(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        context = {"form": form}
        if form.is_valid():
            form.save()
            return redirect("appointment")

    else:
        form = MeetingForm()
        context = {"form": form}

    return render(request, 'meetings/new_app.html', context)
