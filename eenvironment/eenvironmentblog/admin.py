from django.contrib import admin
from .models import Post,ArieNaturala, DateGeografice, DateHidrografice, DateSpeologice, DateForestiere, DateBiodiversitate, Petition
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
admin.site.register(Post)
#admin.site.register(ArieNaturala)
admin.site.register(DateGeografice)
admin.site.register(DateHidrografice)
admin.site.register(DateSpeologice)
admin.site.register(DateForestiere)
admin.site.register(DateBiodiversitate)

class ArieNaturalaAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        try:
            obj.save()
        except ValidationError as e:
            list(messages.get_messages(request))
            for message in e.messages:
                self.message_user(request, message, level=messages.ERROR)
            return
        list(messages.get_messages(request))
        self.message_user(request, f'Obiectul arie naturală "{obj.nume_arie}" a fost modificat cu succes.', level=messages.SUCCESS)

    def response_change(self, request, obj):
        if "_save" in request.POST:
            return HttpResponseRedirect(request.path)
        return super().response_change(request, obj)

admin.site.register(ArieNaturala, ArieNaturalaAdmin)
admin.site.register(Petition)