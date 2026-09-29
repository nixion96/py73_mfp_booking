from django.shortcuts import render, redirect
from booking_manager.models import Bookings


def main(request):
    context = {
        'title': 'Booking Service',
        'message': 'Hello. This is my firs booking service project !!!',
    }
    return render(request, 'booking_manager/booking_manager.html', context)

def services(request):
    serv = [
        {"id": 1, "name": "Haircut", "duration": 60, "price": 30, "category": "Hair","image":"https://plus.unsplash.com/premium_photo-1661645788141-8196a45fb483?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"},
        {"id": 2, "name": "Beard Trim", "duration": 30, "price": 15, "category": "Hair","image":"https://images.unsplash.com/photo-1503951914875-452162b0f3f1?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"},
        {"id": 3, "name": "Manicure", "duration": 45, "price": 25, "category": "Nails","image":"https://images.unsplash.com/photo-1632345031435-8727f6897d53?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"},
        {"id": 4, "name": "Massage", "duration": 90, "price": 50, "category": "Wellness","image":"https://plus.unsplash.com/premium_photo-1661407350987-9e9319ac11e6?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"},
        {"id": 5, "name": "Consultation", "duration": 30, "price": 20, "category": "Other","image":"https://images.unsplash.com/photo-1573497620053-ea5300f94f21?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"}
    ]
    return render(request, 'booking_manager/services.html',{'serv': serv})

def specialists(request):
    spec = [
        {"id": 1, "name": "Alice Brown", "speciality": "Hair Stylist", "experience": 5,"image":"https://images.unsplash.com/photo-1487412720507-e7ab37603c6f?q=80&w=1171&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"},
        {"id": 2, "name": "Bob Smith", "speciality": "Barber", "experience": 7,"image":"https://images.unsplash.com/photo-1564564321837-a57b7070ac4f?q=80&w=1176&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"},
        {"id": 3, "name": "Diana Green", "speciality": "Nail Artist", "experience": 3,"image":"https://images.unsplash.com/photo-1590649880765-91b1956b8276?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"},
        {"id": 4, "name": "Charlie White", "speciality": "Massage Therapist", "experience": 6,"image":"https://images.unsplash.com/photo-1600486913747-55e5470d6f40?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"}
    ]
    return render(request, 'booking_manager/specialist.html',{'spec': spec})

def booking(request):
    # book = [
    #     {"client": "John", "service": "Haircut", "date": "20.09.2026", "time": "12:00", "status": "confirmed"},
    #     {"client": "Anna", "service": "Manicure", "date": "20.09.2026", "time": "14:30", "status": "pending"},
    #     {"client": "Mike", "service": "Massage", "date": "21.09.2026", "time": "10:00", "status": "confirmed"},
    #     {"client": "Kate", "service": "Consultation", "date": "22.09.2026", "time": "16:00", "status": "cancelled"}
    # ]
    book = Bookings.objects.all().order_by('date', 'time')
    return render(request, 'booking_manager/booking_list.html',{'book': book})

def new_booking(request):
    if request.method == 'POST':
        Bookings.objects.create(
            client=request.POST.get('client'),
            service=request.POST.get('service'),
            date=request.POST.get('date'),
            time=request.POST.get('time'),
        )
        return redirect('booking_manager:booking')
    return render(request, 'booking_manager/new_booking.html')


