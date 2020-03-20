# Payment using django-paypal
This is a payment gateway app created using django-paypal

Instructions to follow:
1) install django-paypal using pip install django-paypal
2) In your project go to settings.py and add 'paypal.standard.ipn' in the
   INSTALLED_APPS. This adds paypal application to your project.
3) In settings.py , add PAYPAL_RECEIVER_EMAIL='your paypal receiver email'.
   Note: This email is not fixed you can configure it later.
4) Add PAYPAL_TEST=True in settings.py to enable the paypal testing.
	 For paypal testing, you can use paypal sandbox account.
5) Now run migration by using 'python manage.py migrate' to sync paypal with the
   database.
6) add the url patterns in urls.py
7) Create views and templates for your app.
8) Check views.py and templates in payment app for futher details.
