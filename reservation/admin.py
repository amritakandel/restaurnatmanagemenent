from django.contrib import admin
from reservation.models import Reservation
class ReservationAdmin(admin.ModelAdmin):
    list_display=('Name','Email','Phone','Date','Time','Guest')

admin.site.register(Reservation,ReservationAdmin)

# Register your models here.
