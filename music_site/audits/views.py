from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib.auth.decorators import login_required
from django.db import connection

# Create your views here.

@login_required
def index(request):
    user = request.user
    audits = custom_sql_dictfetchall(
        """
            SELECT date, time, action, entity, entityid, username, email FROM audit JOIN auth_user
                ON audit.user_id = auth_user.id
        """
    )

    return render(
        request, 
        'audits.html',
        {
            'user': user,
            'audits': audits,
        }
    )

def custom_sql_dictfetchall(query):
    "Return all rows from a cursor as a dict"
    with connection.cursor() as cursor:
        cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))     
            for row in cursor.fetchall()
        ]
