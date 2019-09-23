# wedding


pip install bootstrap-admin
pip install django-richtextfield

connect database:
	'NAME': 'wedding_development',
    'USER': 'postgres',
    'PASSWORD': '12345678x@X',
    'HOST': 'localhost',
    'PORT': '5432',

#wedding: python manage.py makemigrations
#wedding: python manage.py migrate
#wedding: python manage.py runserver port

<div class="invitation-panel-content {{wedding.code.slug}}" %}>
                    <span class="" data-year="{{wedding.time_calendar|date:" Y "}}" data-month="{{wedding.time_calendar|date:" m "}}" data-day="{{wedding.time_calendar|date:" j "}}" data-minute="{{wedding.time_calendar|date:" i "}}" data-hour="{{wedding.time_calendar|date:" G "}}" id="wed_countdown_datetime"></span>
                </div>