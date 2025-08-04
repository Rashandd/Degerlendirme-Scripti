# 🧼 Temizlik QR Geri Bildirim Sistemi

Fiziksel alanlara (WC, otopark, yemekhane vb.) yerleştirilen QR kodlar sayesinde kullanıcıların temizlik durumu hakkında geri bildirim göndermesini sağlayan bir Django tabanlı web uygulamasıdır.

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![Django](https://img.shields.io/badge/Django-4.x-green.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)

---

## 🚀 Özellikler

- 📌 Lokasyon bazlı QR kodlar (UUID ile güvenli)
- 📋 Admin panelden soru ve cevap tanımı
- 🧠 Her soru için dropdown veya serbest metin girişi
- 📨 Geri bildirimler anında e-posta ile bildirilir
- 🧾 Admin panelde tek tıkla QR oluşturma ve indirme
- 🗂️ Feedback verileri veritabanında saklanır

---

## ⚙️ Kurulum
```bash
git clone https://github.com/Rashandd/Degerlendirme-Scripti
cd Degerlendirme-Scripti
```
```bash
# Python 3.10 ve üzeri gereklidir
python -m venv venv  # Sanal ortam oluşturma
source venv/bin/activate  # Windows: venv\Scripts\activate
```
```bash
pip install -r requirements.txt # Gerekli paketleri yükleme
```

```commandline
# .env dosyasını oluşturun ve aşağıdaki değişkenleri ekleyin
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=seninmailin@gmail.com
EMAIL_HOST_PASSWORD=uygulama_sifresi
FEEDBACK_MAIL_TO=temizlik@firma.com,yonetici@firma.com
SITE_DOMAIN=example.com
```


```commandline
# Veritabanı ayarlarını yapın 
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
# Sunucuyu başlatın
python manage.py runserver
```

---

## 🛠 Admin Panelden Veri Girişi

Geri bildirim sisteminin çalışması için admin panelden önce **lokasyon**, sonra her lokasyona özel **soru** ve gerekirse **seçenek** girilmelidir.

---

### 🏢 1. Lokasyon (Location) Ekleme

1. Admin paneline giriş yap /admin
2. Sol menüden **Locations** seçeneğine tıkla
3. Sağ üstteki **Add Location** butonuna tıkla
4. `name` alanına lokasyon adını yaz (örnek: WC Kat 1, Otopark A Blok)
5. **Kaydet** butonuna tıkla

> Her lokasyona sistem otomatik olarak benzersiz bir `UUID` verir (QR için kullanılır)

---
### ❓ 2. Soru (Question) Ekleme

1. Sol menüden **Questions** seçeneğine tıkla
2. Sağ üstteki **Add Question** butonuna tıkla
3. `location` seç → bu soru hangi lokasyona ait?
4. `text` alanına soruyu yaz (örnek: Zemin durumu nasıl?)
5. `input type` seç:
   - `select`: kullanıcıya önceden tanımlı seçenekleri gösterir (Temiz, Kirli, vb.)
   - `text`: kullanıcı serbest metin girişi yapar
6. **Kaydet** butonuna tıkla

---

### ✅ 3. (Opsiyonel) Soruya Seçenek (AnswerOption) Ekleme

> Sadece `select` türündeki sorular için geçerlidir.

1. `Questions` ekranında eklediğin soruya tıkla
2. Aşağıda “Answer options” alanı göreceksin
3. Her satıra bir seçenek gir (örnek: Temiz, Kirli, Eksik vs.)
4. İstediğin kadar satır ekleyebilirsin
5. En alttan **Save** (Kaydet) butonuna bas

---

### 📋 Örnek:

**Location:** WC Bahçelievler  
**Question 1:** Zemin durumu nasıl? → input type: `select` → seçenekler: Temiz, Kirli  
**Question 2:** Açıklama eklemek ister misiniz? → input type: `text`

---
