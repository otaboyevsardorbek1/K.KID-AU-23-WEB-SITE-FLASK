# Universitet Web Dasturi

Bu loyiha universitet talabalarining baholarini, kurslarini, va boshqa ma'lumotlarini kuzatib borish uchun ishlab chiqilgan web ilovadir. Dasturda turli foydalanuvchilar uchun alohida panellar mavjud: admin, student, ota-ona, kurator va starisa. Har bir foydalanuvchi o'z roliga mos ravishda tizimga kirib, kerakli ma'lumotlarni ko‘rishi va boshqarishi mumkin.

## Texnologiyalar

- **Backend:** Flask (Python)
- **Ma'lumotlar bazasi:** SQLAlchemy (SQL)
- **Frontend:** HTML, CSS, JavaScript
- **SMS xabarnomalar:** Twilio (yoki boshqa SMS API)
- **Autentifikatsiya:** Flask-Login

## Funksiyalar

1. **Foydalanuvchi ro'yxatga olish va autentifikatsiya:**
   - Foydalanuvchilar (admin, student, ota-ona, kurator, starisa) tizimga ro‘yxatdan o‘tishi va login qilishlari mumkin.
   - Flask-Login yordamida sessiyalar boshqariladi.

2. **Admin paneli:**
   - Admin foydalanuvchilarni qo‘shish, o‘chirish, va tahrirlash imkoniyatiga ega.
   - Universitetdagi barcha ma'lumotlarni boshqarish.

3. **Student paneli:**
   - Talabalar o‘z baholarini va boshqa ma'lumotlarini ko‘rishlari mumkin.

4. **Ota-ona paneli:**
   - Ota-onalar farzandlarining baholarini va o‘qish holatini ko‘rishlari mumkin.

5. **Kurator va Starisa panellari:**
   - Kuratorlar va starisalar guruhdagi talabalar baholarini kuzatib borishlari, o‘qish jarayonini boshqarishlari mumkin.

6. **SMS xabarnomalar:**
   - Foydalanuvchilarga (masalan, o‘zgartirishlar haqida) SMS yuborish imkoniyati.

7. **Sessiya nazorati:**
   - Talabalar va o‘qituvchilar uchun testlar, kurslar, va baholarni kuzatish tizimi.

8. **Universitet ma'lumotlari:**
   - Universitet o‘qituvchilari, kurslari, dars jadvali va boshqa kerakli ma'lumotlarni ko‘rsatish.

## Foydalanish

### 1. **Virtual muhitni yaratish:**

**Bash** (Linux/Mac):
```bash
python3 -m venv venv
source venv/bin/activate
