# Talabalar va Kuratorlar Ma'lumotlari Boshqaruvi

Ushbu loyiha talabalar, kuratorlar, starisalar va boshqa foydalanuvchi turlari uchun ma'lumotlarni yig'ish va ko'rsatish uchun ishlab chiqilgan Flask asosidagi web ilovasi. Loyiha foydalanuvchilarga o'z guruhidagi talabalar va guruh rahbarlari (kuratorlar, starisalar) bilan bog'lanish va ma'lumotlarni tezkor va oson ko'rish imkonini beradi.

## Funksiyalar

- **Talabalar**: O'z guruhidagi barcha talabalar haqida ma'lumotlarni ko'rish.
- **Kuratorlar**: O'z guruhidagi talabalar va rahbarlari (starisalar) haqida ma'lumotlarni boshqarish.
- **Starisalar**: O'z guruhidagi talabalar va kuratorlar bilan aloqalar.
- **Admin**: Foydalanuvchilarni boshqarish, guruhlar va tizim sozlamalarini o'zgartirish.
- **Ma'lumotlarni Tezkor Yig'ish**: Ma'lumotlar aniq va oson tartibda ko'rsatiladi.
- **Quvi Interface**: Foydalanuvchilar uchun intuitiv va foydalanishga qulay dizayn.

## Texnologiyalar

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS (Bootstrap bilan)
- **Ma'lumotlar bazasi**: SQLite (yoki boshqa SQL ma'lumotlar bazasi)
- **Foydalanuvchi autentifikatsiyasi**: Flask-Login
- **Shablonlar**: Jinja2

## Loyiha Yaratilishi

1. **Flask** serverini ishga tushurish uchun `flask run` buyruğidan foydalaning.
2. **Ma'lumotlar bazasini yaratish**: 
   - Ma'lumotlar bazasi va foydalanuvchilarni yaratish uchun:
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
