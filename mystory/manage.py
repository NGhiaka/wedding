from django.contrib.auth.models import User
# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication
# Create user and save to the database
user = User.objects.create_user('admin', 'nghiacntt09@gmail.com', '12345678x@X')

# Update fields and then save again
user.first_name = 'Nghĩa'
user.last_name = 'Linh'
user.save()