from django.contrib import admin
from .models import (
    School, Student, Teacher,
    Place, Restaurant, Supplier,
    Champion, Supporter, Midliner,
)

class ChampionAdmin(admin.ModelAdmin):
    list_display = ('name', 'champion_type', 'rank',)
    list_editable =  ('rank',)

admin.site.register(School)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Place)
admin.site.register(Restaurant)
admin.site.register(Supplier)
admin.site.register(Champion, ChampionAdmin)
admin.site.register(Supporter)
admin.site.register(Midliner)
