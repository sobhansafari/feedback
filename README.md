# سیستم مدیریت فیدبک

یک پروژه ساده برای ثبت و مدیریت فیدبک‌ها با Flask و SQLite.

## قابلیت‌ها

- ثبت فیدبک با عنوان و متن
- مشاهده لیست فیدبک‌ها در داشبورد
- تغییر وضعیت فیدبک‌ها (ثبت شده، در حال بررسی، رسیدگی شده)

# نحوه اجرا


 1. کلون کردن پروژه
git clone https://github.com/sobhana/feedback-board.git
cd feedback-board

 2. ایجاد محیط مجازی
python -m venv venv
venv\Scripts\activate

 3. نصب وابستگی‌ها
pip install -r requirements.txt

 4. اجرا
python main.py


بعد از اجرا، در مرورگر باز کنید:

· صفحه ثبت فیدبک: http://127.0.0.1:5000
· داشبورد مدیریت: http://127.0.0.1:5000/admin

تکنولوژی‌ها

· Backend: Flask
· Database: SQLite + SQLAlchemy
· Frontend: HTML + Bootstrap

تصمیم‌های فنی

· استفاده از Flask به دلیل سادگی و سرعت توسعه
· SQLite برای دیتابیس سبک و بدون نیاز به نصب
· استفاده از SQLAlchemy برای مدیریت دیتابیس
· معماری REST API برای ارتباط فرانت‌اند و بک‌اند

اسکرین‌شات‌ها

screenshot1.png
screenshot2.png

نویسنده

[سبحان حاج صفری]





## 📌
