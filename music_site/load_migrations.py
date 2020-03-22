import os

os.chdir("music_site")
os.system("python manage.py makemigrations")
os.system("python manage.py migrate")
print(" - Migrations Done!")