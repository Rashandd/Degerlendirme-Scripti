from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from .models import Location, Question, Feedback
from django.conf import settings
from datetime import datetime


def feedback_form(request, id):
    # Lokasyonu al
    location = get_object_or_404(Location, id=id)

    # Lokasyona ait tüm soruları ve cevap seçeneklerini çek
    questions = Question.objects.filter(location=location).prefetch_related("options")

    if request.method == 'POST':
        # Formdan gelen verileri eşleştir
        responses = {
            q.text: request.POST.get(str(q.id)) for q in questions
        }


        x = Feedback.objects.create(location=location, responses=responses)
        if settings.SMTP_READY:
            x.sent = True
            x.save()
            send_mail(
                subject=f"Geri Bildirim: {location.name}",
                message=f"Tarih: {datetime.now().strftime('%d.%m.%Y %H:%M')}\nLokasyon: {location.name}\n\nCevaplar:\n" +
                        "\n".join([f"- {k}: {v}" for k, v in responses.items()]),
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=settings.FEEDBACK_MAIL_TO,
                fail_silently=False,
            )
        else:
            x.sent = False
            x.save()

        return render(request, 'thanks.html')

    # Sayfa açıldığında formu göster
    return render(request, 'form.html', {
        'location': location,
        'questions': questions
    })