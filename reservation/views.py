from django.shortcuts import render, redirect
from core.models import Hotel, Reservation

from datetime import datetime


def book(request, id):
    return render(request, template_name="reservation/book.html", context={"id": id})


def checkout(request):
    hotel = Hotel.objects.get(id=request.GET["hotel"])
    fromDate = request.GET["fdate"]
    toDate = request.GET["tdate"]
    total_days = datetime.strptime(toDate, "%Y-%m-%d") - datetime.strptime(
        fromDate, "%Y-%m-%d"
    )
    if request.method == "POST":
        Reservation.objects.create(
            user=request.user,
            days=total_days.days,
            start_date=fromDate,
            end_date=toDate,
            payed=total_days.days * hotel.price,
            hotel=hotel
        )
        return redirect("/")

    return render(
        request,
        template_name="reservation/checkout.html",
        context={
            "hotel": hotel,
            "fromDate": fromDate,
            "toDate": toDate,
            "days": total_days.days,
            "price": total_days.days * hotel.price,
        },
    )


def controlFlow(request):
    user = request.user
    reservations = Reservation.objects.filter(user=user)
    return render(
        request,
        template_name="reservation\control_flow.html",
        context={"res": reservations},
    )


def removeReserve(request, id):
    Reservation.objects.get(id=id).delete()
    print(id)
    return redirect("/reservation/control-flow/")