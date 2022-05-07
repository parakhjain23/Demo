from django.shortcuts import redirect, render
import mysql.connector as sql

# Create your views here.
fn = ''
ln = ''
em = ''
pwd = ''
def signupAction(request):
    global fn,ln,em,pwd
    if request.method=='POST':
        m=sql.connect(host='localhost',user='root',passwd='admin',database='python')
        cursor=m.cursor()
        d = request.POST
        for key,value in d.items():
            if key=='fname':
                fn = value
            if key=='lname':
                ln = value
            if key=='email':
                em = value
            if key=='pass':
                pwd = value

        cmd = "insert into users Values('{}','{}','{}','{}')".format(fn,ln,em,pwd)
        cursor.execute(cmd)
        m.commit()
        return render(request,'home.html')

    return render(request,'signup.html')

def loginAction(request):
    global em,pwd
    if request.method=='POST':
        m=sql.connect(host='localhost',user='root',passwd='admin',database='python')
        cursor=m.cursor()
        d = request.POST
        for key,value in d.items():
            if key=='email':
                em = value
            if key=='pass':
                pwd = value
        cmd = "select * from users where email='{}' and password='{}'".format(em,pwd)
        cursor.execute(cmd)
        tup = tuple(cursor.fetchall())
        if tup==():
            return render(request,'login.html',{'error':True})
        else:
        
            return render(request,'home.html')

    return render(request,'login.html')


