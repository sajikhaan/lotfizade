# پروژه وبسایت تشریفات لطفی زاده

## راه‌اندازی در ویندوز
1. نصب پایتون 3.11 یا بالاتر
2. ایجاد محیط مجازی:
```bash
python -m venv .venv
.venv\Scripts\activate
```
3. نصب وابستگی‌ها:
```bash
pip install -r requirements.txt
```
4. اجرای مایگریشن‌ها:
```bash
python manage.py migrate
```
5. ساخت ادمین:
```bash
python manage.py createsuperuser
```
6. اجرای سرور:
```bash
python manage.py runserver
```
