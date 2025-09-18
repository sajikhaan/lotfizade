#!/usr/bin/env bash
# خروجی از render میاد اینجا

# مطمئن شو pip و پکیج‌ها نصب هستن
pip install -r requirements.txt

# جمع‌آوری استاتیک‌ها
python manage.py collectstatic --noinput

# انجام مهاجرت‌های دیتابیس
python manage.py migrate --noinput
