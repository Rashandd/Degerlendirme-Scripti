from django.contrib import admin
from .models import Location, Question, AnswerOption, Feedback
import qrcode
from django.http import HttpResponse
from io import BytesIO

@admin.action(description="QR Oluştur ve İndir")
def generate_qr_code(modeladmin, request, queryset):
    if queryset.count() == 1:
        location = queryset.first()
        domain = "example.com"
        url = f"https://{domain}/{location.id}/"
        img = qrcode.make(url)

        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        response = HttpResponse(buffer.getvalue(), content_type="image/png")
        response['Content-Disposition'] = f'attachment; filename=qr_{location.name.replace(" ", "_")}.png'
        return response
    else:
        modeladmin.message_user(request, "Lütfen sadece bir lokasyon seçin.")

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']
    actions = [generate_qr_code]

admin.site.register(Question)
admin.site.register(AnswerOption)
admin.site.register(Feedback)
