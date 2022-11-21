from django.contrib import admin
from .models import rooms,room_state

# Register your models here.

#...................admin panel................#

class roomAdmin(admin.ModelAdmin):
    list_display = ['room_id','room_no']
 
class roomStateAdmin(admin.ModelAdmin):
    list_display = ['room_id_id','gas01','gas02','gas03','gas04','state']
 
#..............................................#

admin.site.register(rooms,roomAdmin)

admin.site.register(room_state,roomStateAdmin)

#..............................................#
