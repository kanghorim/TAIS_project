import json
from django.http import JsonResponse
import cx_Oracle as ora
import pandas as pd
from django.shortcuts import render
from django.db.models import Count
from tai.models import TACHART
import pandas as pd
# Create your views here.


def tai(request):
    sub = request.GET.get('name')
    #월별
    sql2 = "select occur_mn, COUNT(*) from TAI_TACHART where OCCUR_PROVIN = '{}' group by occur_mn order by occur_mn".format(sub)
    # .format(sub)
    print('sql2 :',sql2)
    conn = connections()
    cs = conn.cursor()
    cs.execute(sql2)
    rows = cs.fetchall()
    print('rs :', rows)
    context = {'result':rows}
    with open('static/data2.json', 'w') as f : 
        json.dump(rows, f, indent=4)
    
    #지역별
    sql1 = "select OCCUR_PROVIN,count(OCCUR_PROVIN) from TAI_TACHART group by OCCUR_PROVIN"
    print('sql1 :',sql1)
    conn = connections()
    cs = conn.cursor()
    cs.execute(sql1)
    rows = cs.fetchall()

    with open('static/data1.json', 'w') as f : 
        json.dump(rows, f, indent=4)
    
    #시간별
    sql3 = "select occur_hr, COUNT(*) from TAI_TACHART where OCCUR_PROVIN = '{}' group by occur_hr order by occur_hr".format(sub)
    # .format(sub)
    print('sql3 :',sql3)
    conn = connections()
    cs = conn.cursor()
    cs.execute(sql3)
    rows = cs.fetchall()

    with open('static/data3.json', 'w') as f : 
        json.dump(rows, f, indent=4)
    
    #연령별  
    sql4 = "select * from(select ATTACKER_HUMAN_AGE, count(*) from TAI_TACHART where OCCUR_PROVIN = '{}' group by ATTACKER_HUMAN_AGE order by count(*)desc) where rownum <= 5".format(sub)
    # .format(sub)
    print('sql4 :',sql4)
    conn = connections()
    cs = conn.cursor()
    cs.execute(sql4)
    rows = cs.fetchall()

    with open('static/data4.json', 'w') as f : 
        json.dump(rows, f, indent=4)



    
    return render(request, 'tai/tai.html')

def tai2(request):
    
    sql = "select occur_mn, COUNT(*) from TAI_TACHART where OCCUR_PROVIN = '강남구' group by occur_mn order by occur_mn"
    print('sql :',sql)
    conn = connections()
    cs = conn.cursor()
    cs.execute(sql)
    rows = cs.fetchall()
    print('rs :', rows)
    
    context = {'result':rows}
    with open('static/data2.json', 'w') as f : 
        json.dump(rows, f, indent=4)
        
        
    return render(request, 'tai/tai2.html')

def tai3(request):
    return render(request, 'tai/tai.html')

def tai4(request):
    return render(request, 'tai/tai.html')




def connections():
    try:
        conn=ora.connect('ora_user01/1234@localhost:1521/orcl')
    except Exception as e:
        print('예외 발생')
    return conn

def chart_data(request):
    # city = request.GET.get('occur_city')
    sql = "select occur_mn, COUNT(*) from TAI_TACHART where OCCUR_PROVIN = '강서구' group by occur_mn order by occur_mn"
    print('sql :',sql)
    conn = connections()
    cs = conn.cursor()
    cs.execute(sql)
    rows = cs.fetchall()
    print('rs :', rows)
    
    context = {'result':rows}
    with open('static/data7.json', 'w') as f : 
        json.dump(rows, f, indent=4)
        
    return JsonResponse(context)

    
    
    

