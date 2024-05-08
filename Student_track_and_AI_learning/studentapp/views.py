import datetime
import smtplib
from email.mime.text import MIMEText
import nltk
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.db.models import Count, Sum, Q
from studentapp.models import *

from django.core.mail import send_mail

def main_index(request):
    auth.logout(request)
    return render(request,'main_index.html')
def login(request):
    auth.logout(request)
    return render(request,'login_index.html')

def logincode(request):
    uname=request.POST['textfield']
    pwd=request.POST['textfield2']
    try:
        ob=login_table.objects.get(username=uname,password=pwd)
        if ob.type == 'admin':
            ob1 = auth.authenticate(username="admin", password="admin")
            if ob1 is not None:
                auth.login(request,ob1)
                request.session['lid'] = ob.id
            return HttpResponse('''<script>alert('welcome');window.location='/admin'</script>''')
        elif ob.type == 'staff':
            ob1 = auth.authenticate(username="admin", password="admin")
            if ob1 is not None:
                auth.login(request,ob1)
                request.session['lid'] = ob.id
                obb=staff_table.objects.get(LOGIN=ob.id)
                request.session['class']=obb.Class
            return HttpResponse('''<script>alert('welcome');window.location='/staff'</script>''')
        elif ob.type == 'parent':
            ob1 = auth.authenticate(username="admin", password="admin")
            if ob1 is not None:
                auth.login(request,ob1)
                request.session['lid'] = ob.id
            return HttpResponse('''<script>alert('welcome');window.location='/parent'</script>''')
        elif ob.type == 'expert':
            ob1 = auth.authenticate(username="admin", password="admin")
            if ob1 is not None:
                auth.login(request,ob1)
                request.session['lid'] = ob.id
            return HttpResponse('''<script>alert('welcome');window.location='/expert'</script>''')
        else:
            return HttpResponse('''<script>alert('invalid username&password');window.location='/'</script>''')
    except:
        return HttpResponse('''<script>alert('invalid username&password');window.location='/'</script>''')

def logout(request):
    auth.logout(request)
    return render(request,'login_index.html')

@login_required(login_url='/')
def admin(request):
    return render(request,'homepage/index.html')


@login_required(login_url='/')
def managestaff(request):
    # ob=staff_table.objects.all()
    ob=staff_table.objects.all().order_by('-id')
    return render(request,'homepage/manage staff.html',{'val':ob})


@login_required(login_url='/')
def searchstaff(request):
    name=request.POST['textfield']
    ob=staff_table.objects.filter(fname__icontains=name)
    return render(request,'homepage/manage staff.html',{'val':ob})

@login_required(login_url='/')
def editstaff(request,id):
    ob=staff_table.objects.get(id=id)
    request.session['sid']=id
    cls = [1, 2, 3, 4]
    ob1 = staff_table.objects.filter(LOGIN__type='staff')
    lis = []
    for i in ob1:
        if i.Class not in lis:
            lis.append(i.Class)
    op = []
    for i in cls:
        if i not in lis:
            op.append(i)
    print(ob1, "============")
    # cls=['1','2','3','4']
    # for i in ob:
    #     for k in cls:
    #         if i.Class not in k:
    #             print(i.Class)
    return render(request,"homepage/edit_staff.html",{"i":ob,"s":op})

@login_required(login_url='/')
def deletestaff(request,id):
    ob=staff_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>;window.location='/managestaff#about'</script>''')

@login_required(login_url='/')
def addstaff(request):
    cls=[1,2,3,4]
    ob=staff_table.objects.filter(LOGIN__type='staff')
    lis=[]
    for i in ob:
        if i.Class not in lis:
            lis.append(i.Class)
    op=[]
    for i in cls:
        if i  not in lis:
            op.append(i)
    print(ob,"============")

    return render(request,"homepage/add staff.html",{"s":op})



@login_required(login_url='/')
def addedstaff(request):


    ft=request.POST['textfield']
    ln=request.POST['textfield2']
    gn=request.POST['gender']
    pl=request.POST['textfield4']
    po=request.POST['textfield5']
    pin=request.POST['textfield6']
    ph=request.POST['textfield7']
    em=request.POST['textfield8']
    pic=request.FILES['file']
    fs=FileSystemStorage()
    fn=fs.save(pic.name,pic)
    ty=request.POST['select']
    print(ty,"===================================")
    if ty=="1":
        cls= request.POST['select']
    elif ty == "2":
        cls=0
    else:
        cls=0
    un= request.POST['textfield10']
    ps= request.POST['textfield11']
    ox=staff_table.objects.filter(email=em)
    if len(ox) == 0:
        oy=staff_table.objects.filter(ph_no=ph)
        if len(oy) == 0:

            ob=login_table()
            ob.username=un
            ob.password=ps
            ob.type="staff"
            ob.save()
            # send_mail('STUDENT TRACK & AI LEARNING', "YOUR PASSWORD IS  -" + str(ps), 'nksalha2@gmail.com', [em],
            # #           fail_silently=False)
            # try:
            #     gmail = smtplib.SMTP('smtp.gmail.com', 587)
            #     gmail.ehlo()
            #     gmail.starttls()
            #     gmail.login('nksalha2@gmail.com', 'eqxddvxzcirleiwt')
            #     print("login=======")
            # except Exception as e:
            #     print("==================================================")
            #     print(e)
            #     ob.delete()
            #     return HttpResponse('''<script>alert('couldnot setup mail');window.location='/managestaff'</script>''')
            # msg = MIMEText("Your username :"+un+"\n Your password id : " + str(ps))
            # print(msg)
            # msg['Subject'] = 'STUDENT TRACKING'
            # msg['To'] = em
            # msg['From'] = 'nksalha2@gmail.com'
            # try:
            #     gmail.send_message(msg)
            # except Exception as e:
            #     print(e)
                # return HttpResponse('''<script>alert('couldn't setup mail');window.location='/managestaff'</script>''')
            print("ok====")
            ub=staff_table()
            ub.fname=ft
            ub.lname=ln
            ub.gender=gn
            ub.place=pl
            ub.post=po
            ub.pin=pin
            ub.ph_no=ph
            ub.email=em
            ub.photo=fn
            ub.Class=cls
            ub.LOGIN=ob
            ub.save()
            print("==============================================================")


            return HttpResponse('''<script>;window.location='/managestaff#about'</script>''')
        else:
            return HttpResponse('''<script>alert("phone number is already exist");window.location='/managestaff#about'</script>''')
    else:
        return HttpResponse('''<script>alert("email is already exist");window.location='/managestaff#about'</script>''')


@login_required(login_url='/')
def updatestaff(request):
    if 'file' in request.FILES:
        ft = request.POST['textfield']
        ln = request.POST['textfield2']
        gn = request.POST['gender']
        pl = request.POST['textfield4']
        po = request.POST['textfield5']
        pin = request.POST['textfield6']
        ph = request.POST['textfield7']
        em = request.POST['textfield8']
        pic = request.FILES['file']
        fs = FileSystemStorage()
        fn = fs.save(pic.name, pic)
        ty = request.POST['select']
        print(ty, "===================================")
        if ty == "1":
            cls = request.POST['select']
        elif ty == "2":
            cls = 0
        else:
            cls = 0
        ub=staff_table.objects.get(id=request.session['sid'])
        ub.fname = ft
        ub.lname = ln
        ub.gender = gn
        ub.place = pl
        ub.post = po
        ub.pin = pin
        ub.ph_no = ph
        ub.email = em
        ub.photo = fn
        ub.Class = cls
        ub.save()
        return HttpResponse('''<script>alert;window.location='/managestaff#about'</script>''')
    else:
        ft = request.POST['textfield']
        ln = request.POST['textfield2']
        gn = request.POST['gender']
        pl = request.POST['textfield4']
        po = request.POST['textfield5']
        pin = request.POST['textfield6']
        ph = request.POST['textfield7']
        em = request.POST['textfield10']
        ty = request.POST['select']
        print(ty, "===================================")
        if ty == "1":
            cls = request.POST['select']
        elif ty == "2":
            cls = 0
        else:
            cls = 0
        ub = staff_table.objects.get(id=request.session['sid'])
        ub.fname = ft
        ub.lname = ln
        ub.gender = gn
        ub.place = pl
        ub.post = po
        ub.pin = pin
        ub.ph_no = ph
        ub.email = em
        ub.Class = cls

        ub.save()
        return HttpResponse('''<script>;window.location='/managestaff#about'</script>''')



@login_required(login_url='/')
def manageexpert(request):
    ob=expert_table.objects.all().order_by('-id')
    return render(request,'homepage/manage expert.html',{'val': ob})

@login_required(login_url='/')
def searchexpert(request):
    name=request.POST['textfield']
    ob=expert_table.objects.filter(fname__icontains=name)
    return render(request,'homepage/manage expert.html',{'val':ob})

@login_required(login_url='/')
def deleteexpert(request,id):
    ob=expert_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>;window.location='/manageexpert#about'</script>''')

@login_required(login_url='/')
def editexpert(request,id):
    ob=expert_table.objects.get(id=id)
    request.session['eid']=id


    return render(request,"homepage/edit_expert.html",{"i":ob})

@login_required(login_url='/')
def addexpert(request):
    return render(request,'homepage/add expert.html')

@login_required(login_url='/')
def addedexpert(request):
    ft=request.POST['textfield']
    ln=request.POST['textfield2']
    pl=request.POST['textfield3']
    po=request.POST['textfield4']
    pin=request.POST['textfield5']
    pic=request.FILES['file']
    fs=FileSystemStorage()
    fn=fs.save(pic.name,pic)
    ph = request.POST['textfield6']
    em=request.POST['textfield9']
    un= request.POST['textfield7']
    ps= request.POST['textfield8']

    ox = expert_table.objects.filter(email=em)
    if len(ox) == 0:
        oy = expert_table.objects.filter(ph_no=ph)
        if len(oy) == 0:


            ob=login_table()
            ob.username=un
            ob.password=ps
            ob.type="expert"
            ob.save()


            ub=expert_table()
            ub.fname=ft
            ub.lname=ln
            ub.place=pl
            ub.post=po
            ub.pin=pin
            ub.photo=fn
            ub.ph_no=ph
            ub.email=em
            ub.LOGIN=ob
            ub.save()
            return HttpResponse('''<script>;window.location='/manageexpert#about'</script>''')
        else:
            return HttpResponse('''<script>alert("Phone number is already exist");window.location='/manageexpert#about'</script>''')
    else:
        return HttpResponse('''<script>alert("Email is already exist");window.location='/manageexpert#about'</script>''')


@login_required(login_url='/')
def updateexpert(request):
    if 'file' in request.FILES:
        ft=request.POST['textfield']
        ln=request.POST['textfield2']
        pl=request.POST['textfield3']
        po=request.POST['textfield4']
        pin=request.POST['textfield5']
        pic=request.FILES['file']
        fs=FileSystemStorage()
        fn=fs.save(pic.name,pic)
        ph = request.POST['textfield6']
        em = request.POST['textfield9']




        ub=expert_table.objects.get(id=request.session['eid'])
        ub.fname=ft
        ub.lname=ln
        ub.place=pl
        ub.post=po
        ub.pin=pin
        ub.photo=fn
        ub.ph_no=ph
        ub.email=em

        ub.save()
        return HttpResponse('''<script>;window.location='/manageexpert#about'</script>''')
    else:
        ft = request.POST['textfield']
        ln = request.POST['textfield2']
        pl = request.POST['textfield3']
        po = request.POST['textfield4']
        pin = request.POST['textfield5']
        ph = request.POST['textfield6']
        em = request.POST['textfield9']

        ub = expert_table.objects.get(id=request.session['eid'])
        ub.fname = ft
        ub.lname = ln
        ub.place = pl
        ub.post = po
        ub.pin = pin
        ub.ph_no = ph
        ub.email=em

        ub.save()
        return HttpResponse('''<script>;window.location='/manageexpert#about'</script>''')

@login_required(login_url='/')
def viewparent(request):
    ob=parent_table.objects.all().order_by('-id')
    return render(request,'homepage/view parent.html',{'val':ob})

@login_required(login_url='/')
def parentsearch(request):
    name=request.POST['textfield']
    ob=parent_table.objects.filter(fname__icontains=name)
    return render(request,'homepage/view parent.html',{'val':ob})




@login_required(login_url='/')
def staff(request):
    return render(request,'Staff/staff_index.html')

@login_required(login_url='/')
def mng_attendence(request):
    ob=staff_table.objects.get(LOGIN__id=request.session['lid'])
    result=attendence_table.objects.filter(PARENT__Class=ob.Class).values('PARENT').order_by('PARENT').annotate(count=Count('attendence'),sum=Sum('attendence'))
    print(result)
    for i in result:
        pob=parent_table.objects.get(id=i['PARENT'])
        i['sn']=pob.fname+" "+pob.lname
        i['p']=round((i['sum']/i['count'])*100,2)
    d1=datetime.datetime.now().strftime("%Y-%m-%d")
    return render(request,'Staff/manage attendence.html',{'val':result,"d1":d1})

@login_required(login_url='/')
def s_mng_attendence(request):
    d=datetime.datetime.now().strftime("%Y-%m-%d")
    dx=datetime.datetime.now().strftime("%Y-%m-%d")



    fd=request.POST['textfield']
    td=request.POST['textfield2']
    ob=staff_table.objects.get(LOGIN__id=request.session['lid'])
    result = attendence_table.objects.filter(PARENT__Class=ob.Class,date__range=(fd,td)).values('PARENT').order_by('PARENT').annotate(count=Count('attendence'),sum=Sum('attendence'))
    print(result)
    for i in result:
        pob=parent_table.objects.get(id=i['PARENT'])
        i['sn']=pob.fname+" "+pob.lname
        i['p']=round((i['sum']/i['count'])*100,2)
    return render(request,'Staff/manage attendence.html',{'val':result,"f":fd,"t":td,'d1':d})

@login_required(login_url='/')
def add_attendence(request):
    ob=staff_table.objects.get(LOGIN__id=request.session['lid'])
    d=datetime.datetime.now().strftime("%Y-%m-%d")
    obp=parent_table.objects.filter(Class=ob.Class)
    return render(request,'Staff/add attendence.html',{"s":"0",'d1':d})

@login_required(login_url='/')
def addedattendence(request):
    btn=request.POST['Submit']
    if btn=="Search":
        date=request.POST['textfield']
        cls=request.POST['select']
        ob=attendence_table.objects.filter(STAFF__LOGIN__id=request.session['lid'],date=date,PARENT__Class=cls)
        if len(ob)==0:
            ob=staff_table.objects.get(LOGIN__id=request.session['lid'])
            obp=parent_table.objects.filter(Class=cls).order_by('fname','lname')
            return render(request, 'Staff/add attendence.html',{"val":obp,"d":date,"s":"0"})
        else:
            return render(request, 'Staff/add attendence.html', {"val": ob, "d": date, "s": "1"})
    elif btn=="Save":
        date=request.POST['textfield']
        ob = staff_table.objects.get(LOGIN__id=request.session['lid'])
        obp = parent_table.objects.filter(Class=ob.Class)
        pdata=request.POST.getlist('checkbox')
        print(pdata)
        for i in obp:
            att=0
            if str(i.id) in pdata:
                att=1
            ob1=attendence_table()
            ob1.STAFF=ob
            ob1.PARENT=i
            ob1.date=date
            ob1.attendence=att
            ob1.save()
        return HttpResponse('''<script>alert('Attendance added');window.location='/mng_attendence#about'</script>''')
    else:
        date = request.POST['textfield']
        ob = attendence_table.objects.filter(STAFF__LOGIN__id=request.session['lid'], date=date)
        pdata=request.POST.getlist('checkbox')
        for i in ob:
            att = 0
            if str(i.id) in pdata:
                att = 1
            ob1 = attendence_table.objects.get(id=i.id)

            ob1.attendence = att
            ob1.save()
        return HttpResponse('''<script>alert('Attendance updated');window.location='/mng_attendence#about'</script>''')

@login_required(login_url='/')
def mng_DA(request):
    ob=daily_activities.objects.filter(STAFF__LOGIN__id=request.session['lid']).order_by('-id')
    return render(request,'Staff/manage DA.html',{'val': ob})

@login_required(login_url='/')
def search_DA(request):
    dt=request.POST['textfield']
    ob=daily_activities.objects.filter(date=dt,STAFF__LOGIN=request.session['lid'])
    return render(request,'Staff/manage DA.html',{'val': ob})

@login_required(login_url='/')
def editda(request,id):
    ob=daily_activities.objects.get(id=id)
    request.session['did']=id
    return render(request,"Staff/edit_DA.html",{"i":ob})

@login_required(login_url='/')
def deleteda(request,id):
    ob=daily_activities.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>;window.location='/mng_DA#about'</script>''')

@login_required(login_url='/')
def add_DA(request):
    d=datetime.datetime.now().strftime("%Y-%m-%d")
    return render(request,'Staff/Add DA.html',{'d1':d})


@login_required(login_url='/')
def addedDA(request):
    # dt=request.POST['textfield']
    ac=request.POST['textfield2']
    det=request.POST['textfield3']
    ub=daily_activities()
    ub.date=datetime.datetime.today()
    ub.activity=ac
    ub.details=det
    ub.STAFF=staff_table.objects.get(LOGIN__id=request.session['lid'])
    ub.save()
    return HttpResponse('''<script>;window.location='/mng_DA#about'</script>''')


@login_required(login_url='/')
def updateda(request):
    # dt=request.POST['textfield']
    ac=request.POST['textfield2']
    det=request.POST['textfield3']
    ub = daily_activities.objects.get(id=request.session['did'])
    # ub.date=dt
    ub.activity=ac
    ub.details=det
    ub.save()
    return HttpResponse('''<script>;window.location='/mng_DA#about'</script>''')

@login_required(login_url='/')
def mng_parent(request):
    ob = parent_table.objects.all().order_by('-id')
    return render(request,'Staff/mng parent.html',{'val':ob})

@login_required(login_url='/')
def searchparent(request):
    name=request.POST['textfield']
    ob=parent_table.objects.filter(fname__contains=name)
    return render(request,'Staff/mng parent.html',{'val':ob})

@login_required(login_url='/')
def editparent(request,id):
    ob=parent_table.objects.get(id=id)
    request.session['pid']=id
    return render(request,"Staff/edit_parent.html",{"i":ob})

@login_required(login_url='/')
def deleteparent(request,id):
    ob=parent_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>;window.location='/mng_parent#about'</script>''')

@login_required(login_url='/')
def add_parent(request):
    return render(request,'Staff/add parent.html')

@login_required(login_url='/')
def addedparent(request):
    ft=request.POST['textfield']
    ln=request.POST['textfield2']
    ph=request.POST['textfield3']
    em=request.POST['textfield4']
    pn=request.POST['textfield5']
    cl=request.POST['select']
    db=request.POST['textfield7']
    gn=request.POST['gender']
    pl=request.POST['textfield9']
    po=request.POST['textfield10']
    pin=request.POST['textfield11']
    pic=request.FILES['file']
    fs=FileSystemStorage()
    fn=fs.save(pic.name, pic)
    un=request.POST['textfield12']
    ps=request.POST['textfield13']

    ox = parent_table.objects.filter(email=em,ph_no=ph,fname=ft,lname=ln)
    if len(ox) == 0:

        ob=login_table()
        ob.username=un
        ob.password=ps
        ob.type="parent"
        ob.save()

        ub=parent_table()
        ub.fname=ft
        ub.lname=ln
        ub.ph_no=ph
        ub.email=em
        ub.parent_name=pn
        ub.Class=cl
        ub.DOB=db
        ub.gender=gn
        ub.place=pl
        ub.post=po
        ub.pin=pin
        ub.photo=fn
        ub.LOGIN=ob
        ub.save()
        return HttpResponse('''<script>;window.location='/mng_parent#about'</script>''')
    else:
        return HttpResponse('''<script>alert("This student is already exist");window.location='/mng_parent#about'</script>''')
        
@login_required(login_url='/')
def updateparent(request):
    if 'file' in request.FILES:
        ft = request.POST['textfield']
        ln = request.POST['textfield2']
        ph = request.POST['textfield3']
        em = request.POST['textfield4']
        pn = request.POST['textfield5']
        cl = request.POST['select']
        db = request.POST['textfield7']
        gn = request.POST['gender']
        pl = request.POST['textfield9']
        po = request.POST['textfield10']
        pin = request.POST['textfield11']
        pic = request.FILES['file']
        fs = FileSystemStorage()
        fn = fs.save(pic.name, pic)

        ub=parent_table.objects.get(id=request.session['pid'])

        ub.fname = ft
        ub.lname = ln
        ub.ph_no = ph
        ub.email = em
        ub.parent_name = pn
        ub.Class = cl
        ub.DOB = db
        ub.gender = gn
        ub.place = pl
        ub.post = po
        ub.pin = pin
        ub.photo = fn
        ub.save()
        return HttpResponse('''<script>;window.location='/mng_parent#about'</script>''')
    else:
        ft = request.POST['textfield']
        ln = request.POST['textfield2']
        ph = request.POST['textfield3']
        em = request.POST['textfield4']
        pn = request.POST['textfield5']
        cl = request.POST['select']
        db = request.POST['textfield7']
        gn = request.POST['gender']
        pl = request.POST['textfield9']
        po = request.POST['textfield10']
        pin = request.POST['textfield11']

        ub = parent_table.objects.get(id=request.session['pid'])

        ub.fname = ft
        ub.lname = ln
        ub.ph_no = ph
        ub.email = em
        ub.parent_name =pn
        ub.Class = cl
        ub.DOB = db
        ub.gender = gn
        ub.place = pl
        ub.post = po
        ub.pin = pin

        ub.save()
        return HttpResponse('''<script>window.location='/mng_parent#about'</script>''')

@login_required(login_url='/')
def view_leave(request):
    ob=leave.objects.filter(STAFF__LOGIN__id=request.session['lid']).order_by('-id')
    return render(request, 'Staff/view Leave req.html',{'val': ob})

@login_required(login_url='/')
def seach_leave(request):
    dt=request.POST['textfield']
    ob=leave.objects.filter(date=dt,STAFF__LOGIN=request.session['lid'])
    return render(request,'Staff/view Leave req.html',{'val': ob})

@login_required(login_url='/')
def updgrade(request):
    ob=parent_table.objects.filter(Class=request.session['class'])
    return render(request, 'Staff/upgrade student.html',{'val':ob})

@login_required(login_url='/')
def upgradepost(request,id):
    ob=parent_table.objects.get(id=id)
    ob.Class=ob.Class+1
    ob.save()
    return HttpResponse('''<script>;window.location='/mng_parent#about'</script>''')


@login_required(login_url='/')
def change_pw(request):
    return render(request,'Staff/change pwd.html')

@login_required(login_url='/')
def changepwd(request):
    cp=request.POST['textfield']
    np=request.POST['textfield2']
    cmp=request.POST['textfield3']
    ob=login_table.objects.get(password=cp,id=request.session['lid'])
    if ob is not None:
        if np==cmp:
            ob.password=np
            ob.save()
            return HttpResponse('''<script>alert('Password  Changed');window.location='/staff'</script>''')
        else:
            return HttpResponse('''<script>alert('Password  Mismatched');window.location='/staff'</script>''')
    else:
        return HttpResponse('''<script>alert('Invalid User');window.location='/staff'</script>''')

@login_required(login_url='/')
def parent(request):
    return render(request,'Parent/parent_index.html')

# @login_required(login_url='/')
def date_fn(y,m):
    import calendar

    # Get the current year and month
    current_year = int(y)  # You can change this to any specific year
    current_month = int(m)  # You can change this to any specific month (1 for January, 2 for February, ..., 12 for December)

    # Get the list of all dates in the specified month
    month_calendar = calendar.monthcalendar(current_year, current_month)
    op=[]
    # Print all the dates in the month
    for week in month_calendar:
        for day in week:
            if day != 0:
                op.append(f"{current_year}-{current_month:02d}-{day:02d}")
    return op

@login_required(login_url='/')
def view_attendence1(request):
    y=datetime.datetime.now().strftime("%Y")
    m=datetime.datetime.now().strftime("%m")
    op=date_fn(y,m)
    oplist=[]
    for i in op:
        result1 = attendence_table.objects.filter(PARENT__LOGIN__id=request.session['lid'],date=i)
        if len(result1)==0:
            oplist.append(-1)
        elif result1[0].attendence==1:
            oplist.append(1)
        else:
            oplist.append(0)
    print(oplist)
    return render(request,"sample.html",{"y":y,"m":m,"l":oplist})

@login_required(login_url='/')
def view_attendence(request):
  try:
        result = attendence_table.objects.filter(PARENT__LOGIN__id=request.session['lid']).values('PARENT').order_by('PARENT').annotate(
            count=Count('attendence'), sum=Sum('attendence'))
        print(result)
        result1 = attendence_table.objects.filter(PARENT__LOGIN__id=request.session['lid'])
        for i in result1:
            val = parent_table.objects.get(LOGIN__id=i.PARENT.LOGIN.id)
            name=val.fname+" "+val.lname
        print(result1)

        twd=result[0]['count']
        tpd=result[0]['sum']
        tad=twd-tpd
        per=round((tpd/twd)*100,2)
        return render(request,"Parent/view attendence.html",{"d":name,"val":result1,"twd":twd,"tpd":tpd,"tad":tad,"per":per})
  except:
      result = attendence_table.objects.filter(PARENT__LOGIN__id=request.session['lid']).values('PARENT').order_by(
          'PARENT').annotate(
          count=Count('attendence'), sum=Sum('attendence'))
      print(result)
      result1 = attendence_table.objects.filter(PARENT__LOGIN__id=request.session['lid'])

      twd = result[0]['count']
      tpd = result[0]['sum']
      tad = twd - tpd
      per = round((tpd / twd) * 100,2)
      return render(request, "Parent/view attendence.html",
                    {"d": 0, "val": result1, "twd": twd, "tpd": tpd, "tad": tad, "per": per})

@login_required(login_url='/')
def search_attendance(request):
    y=int(request.POST['select'])
    m=int(request.POST['select1'])

    # y = int(datetime.datetime.now().strftime("%Y"))
    # m = int(datetime.datetime.now().strftime("%m"))
    print(m,y)
    op = date_fn(y, m)
    print(op)
    oplist = []
    for i in op:
        result1 = attendence_table.objects.filter(PARENT__LOGIN__id=request.session['lid'], date=i)
        if len(result1) == 0:
            oplist.append(-1)
        elif result1[0].attendence == 1:
            oplist.append(1)
        else:
            oplist.append(0)
    print(oplist)
    return render(request, "sample.html", {"y": int(y), "m": int(m), "l": oplist})



@login_required(login_url='/')
def view_DA(request):
    ob1=parent_table.objects.get(LOGIN__id=request.session['lid'])
    ob=daily_activities.objects.filter(STAFF__Class=ob1.Class)
    return render(request,'Parent/view DA.html',{'val': ob})

@login_required(login_url='/')
def searchDA(request):
    dt=request.POST['textfield']
    i=parent_table.objects.get(LOGIN_id=request.session['lid'])
    cls=i.Class
    j=daily_activities.objects.filter(date=dt,STAFF__Class=cls)
    return render(request,'Parent/view DA.html',{'val': j})



@login_required(login_url='/')
def view_SM(request):
    ob1 =parent_table.objects.get(LOGIN__id=request.session['lid'])
    ob=study_material.objects.filter(Class=ob1.Class).order_by('-id').order_by('-id')
    return render(request, 'Parent/view Study material.html', {'val': ob})

@login_required(login_url='/')
def searchSM(request):
    dt=request.POST['textfield']
    i=parent_table.objects.get(LOGIN_id=request.session['lid'])
    cls=i.Class
    j=study_material.objects.filter(date=dt,Class=cls)
    return render(request,'Parent/view Study material.html',{'val': j})

@login_required(login_url='/')
def chat_staff(request):
    return render(request,'Parent/chat with staff.html')

@login_required(login_url='/')
def ask_doubt_reply(request):
    ob=doubt_table.objects.filter(PARENT__LOGIN=request.session['lid']).order_by('-id')
    return render(request,'Parent/ask doubt&send reply.html',{'val':ob})

@login_required(login_url='/')
def ask_doubt(request):
    ob=expert_table.objects.all()
    return render(request,'Parent/Askdoubt.html',{'val':ob})


@login_required(login_url='/')
def adddoubt(request):
    doubt = request.POST['textfield']
    id = request.POST['select']
    ub=doubt_table()
    ub.doubt = doubt
    ub.reply='pending'
    ub.EXPERT=expert_table.objects.get(id=id)
    ub.PARENT=parent_table.objects.get(LOGIN=request.session['lid'])
    ub.date=datetime.datetime.now().strftime("%Y-%m-%d")
    ub.save()
    return HttpResponse('''<script>;window.location='/ask_doubt_reply#about'</script>''')

@login_required(login_url='/')
def search_doubt(request):
    dt=request.POST['textfield']
    ob=doubt_table.objects.filter(date=dt,PARENT__LOGIN=request.session['lid'])
    return render(request,'Parent/ask doubt&send reply.html',{'val':ob})

@login_required(login_url='/')
def sendleave(request):
    d = datetime.datetime.now().strftime("%Y-%m-%d")
    return render(request,'Parent/send_leave_req.html',{'d1':d})

@login_required(login_url='/')
def addleave(request):
    try:
        dt = request.POST['textfield']
        rs = request.POST['textfield2']
        obp=parent_table.objects.get(LOGIN=request.session['lid'])
        sob=staff_table.objects.filter(Class=obp.Class)[0]
        ub=leave()
        ub.date=dt
        ub.reason=rs
        ub.STAFF=sob
        ub.PARENT=parent_table.objects.get(LOGIN=request.session['lid'])
        ub.save()
        return HttpResponse('''<script>alert('leave added');window.location='/sendleave#about'</script>''')
    except:
        return HttpResponse('''<script>alert('Failed');window.location='/sendleave#about'</script>''')

@login_required(login_url='/')
def insert_test(request):
    ans=request.POST['textfield']
    sm=request.session['smid']
    ty=request.session['ty']
    cnt=request.session['cnt']
    ob = dataset.objects.filter(type=ty, STUDYMATERIAL__id=sm)
    obc=chatbot()
    obc.PARENT=parent_table.objects.get(LOGIN__id=request.session['lid'])
    obc.DATASET=ob[cnt]
    obc.answer=ans
    obc.date=datetime.datetime.today()
    obc.save()
    cnt=cnt+1
    request.session['cnt']=cnt
    val = []
    for i in range(cnt):
        r={"q":ob[i].question,"t":"q","qn":i+1}
        val.append(r)
        obr=chatbot.objects.get(date=datetime.datetime.today(),DATASET__id=ob[i].id,PARENT__LOGIN__id=request.session['lid'])
        r={"q":obr.answer,"t":"a"}
        val.append(r)
    try:
        val.append({"q":ob[cnt].question,"t":"q","qn":cnt+1})
        return render(request, "Parent/send answer.html", {"v": val,"ty":ty})
    except:
        return HttpResponse("<script>alert('level "+request.session['ty']+" completed');window.location='/view_SM#about'</script>")

@login_required(login_url='/')
def attendtest(request,id):
    r={"e":0,"m":0,"h":0}
    sm=id
    request.session['smid']=id
    obr = chatbot.objects.filter(DATASET__STUDYMATERIAL__id=sm, PARENT__LOGIN__id=request.session['lid'], DATASET__type='Easy')
    datelist = []
    for j in obr:
        if j.date not in datelist:
            datelist.append(j.date)
    print(datelist)
    for j in datelist:

        obr = chatbot.objects.filter(DATASET__STUDYMATERIAL__id=sm, PARENT__LOGIN__id=request.session['lid'], DATASET__type='Easy', date=j)

        mark = 0
        for k in obr:
            if k.answer == k.DATASET.answer:
                mark = mark + 1
        mark= mark/len(obr)
        if r['e']<mark:
            r['e']=mark
    obr = chatbot.objects.filter(DATASET__STUDYMATERIAL__id=sm, PARENT__LOGIN__id=request.session['lid'], DATASET__type='Medium')
    datelist = []
    for j in obr:
        if j.date not in datelist:
            datelist.append(j.date)
    for j in datelist:
        row={}
        obr = chatbot.objects.filter(DATASET__STUDYMATERIAL__id=sm, PARENT__LOGIN__id=request.session['lid'], DATASET__type='Medium', date=j)
        row['ty'] = 'Medium'

        mark = 0
        for k in obr:
            if k.answer == k.DATASET.answer:
                mark = mark + 1
        mark = mark/len(obr)
        if r['m']<mark:
            r['m']=mark
    obr = chatbot.objects.filter(DATASET__STUDYMATERIAL__id=sm, PARENT__LOGIN__id=request.session['lid'], DATASET__type='Hard')
    datelist = []
    for j in obr:
        if j.date not in datelist:
            datelist.append(j.date)
    for j in datelist:

        obr = chatbot.objects.filter(DATASET__STUDYMATERIAL__id=sm, PARENT__LOGIN__id=request.session['lid'], DATASET__type='Hard', date=j)

        mark = 0
        for k in obr:
            if k.answer == k.DATASET.answer:
                mark = mark + 1
        mark = mark/len(obr)
        if r['h']<mark:
            r['h']=mark
    request.session['cnt']=0
    if r['e']<0.6:
        request.session['ty']="Easy"
        ob=dataset.objects.filter(type='Easy',STUDYMATERIAL__id=sm)
        val=[{"q":ob[0].question,"t":"q","qn":"1"}]
        return render(request,"Parent/send answer.html",{"v":val,"ty":"Easy"})


    elif r['m']<0.6:
        request.session['ty']="Medium"

        ob = dataset.objects.filter(type='Medium', STUDYMATERIAL__id=sm)
        val = [{"q": ob[0].question, "t": "q", "qn": "1"}]
        return render(request,"Parent/send answer.html",{"v":val,"ty":"Medium"})
    else:
        request.session['ty']="Hard"
        ob = dataset.objects.filter(type='Hard', STUDYMATERIAL__id=sm)
        val = [{"q": ob[0].question, "t": "q", "qn": "1"}]
        return render(request,"Parent/send answer.html",{"v":val,"ty":"Hard"})




@login_required(login_url='/')
def expert(request):
    return render(request,'Expert/expert_index.html')


@login_required(login_url='/')
def mng_SM(request):
    ob=study_material.objects.filter(EXPERT__LOGIN__id=request.session['lid']).order_by('-id')
    return render(request, 'Expert/Manage study material.html', {'val': ob})

@login_required(login_url='/')
def search_SM(request):
    dt=request.POST['textfield']
    ob=study_material.objects.filter(date=dt,EXPERT__LOGIN=request.session['lid'])
    return render(request,'Expert/Manage study material.html',{'val': ob})

@login_required(login_url='/')
def editsm(request,id):
    ob=study_material.objects.get(id=id)
    request.session['sid']=id
    return render(request,"Expert/edit_SM.html",{"i":ob})

@login_required(login_url='/')
def updatesm(request):
    if 'file' in request.FILES:
        cl = request.POST['select']
        nm = request.POST['textfield']
        sm = request.FILES['file']
        fs = FileSystemStorage()
        fn = fs.save(sm.name, sm)
        ub = study_material.objects.get(id=request.session['sid'])
        ub.Class = cl
        ub.name = nm
        ub.date = datetime.datetime.now().strftime("%Y-%m-%d")

        ub.study_material = fn

        ub.save()

        return HttpResponse('''<script>;window.location='/mng_SM#about'</script>''')
    else:
        cl = request.POST['select']
        nm = request.POST['textfield']

        ub = study_material.objects.get(id=request.session['sid'])
        ub.Class = cl
        ub.name = nm
        ub.date = datetime.datetime.now().strftime("%Y-%m-%d")

        ub.save()

        return HttpResponse('''<script>;window.location='/mng_SM#about'</script>''')

@login_required(login_url='/')
def deleteSM(request,id):
    ob=study_material.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>;window.location='/mng_SM#about'</script>''')


@login_required(login_url='/')
def add_SM(request):
    ob = study_material.objects.filter(EXPERT__LOGIN__id=request.session['lid']).order_by('-id')
    return render(request, 'Expert/Add studymaterial.html', {'val': ob})

@login_required(login_url='/')
def addedSM(request):
    cl=request.POST['select']
    nm=request.POST['textfield']
    sm=request.FILES['file']
    fs = FileSystemStorage()
    fn = fs.save(sm.name, sm)
    ub=study_material()
    ub.Class=cl
    ub.name=nm
    ub.date=datetime.datetime.now().strftime("%Y-%m-%d")

    ub.study_material=fn
    ub.EXPERT=expert_table.objects.get(LOGIN__id=request.session['lid'])
    ub.save()
    return HttpResponse('''<script>;window.location='/mng_SM#about'</script>''')


@login_required(login_url='/')
def mng_ques(request):
    ob = dataset.objects.all()
    return render(request, 'Expert/Manage questions.html', {'val': ob})

@login_required(login_url='/')
def add_ques(request):
    ob=study_material.objects.filter(EXPERT__LOGIN=request.session['lid']).order_by('-id')
    return render(request,'Expert/Add questions.html',{'val': ob})

@login_required(login_url='/')
def addedques(request):
    sm=request.POST['select']
    qa=request.POST['textfield']
    an=request.POST['textfield2']
    tp=request.POST['select2']

    ub=dataset()
    ub.STUDYMATERIAL=study_material.objects.get(id=sm)
    ub.question=qa
    ub.answer=an
    ub.type=tp


    ub.save()
    return HttpResponse('''<script>;window.location='/mng_ques#about'</script>''')

@login_required(login_url='/')
def deleteQA(request,id):
    ob=dataset.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>;window.location='/mng_ques#about'</script>''')



@login_required(login_url='/')
def viewresult_par(request):
    ob1 = parent_table.objects.get(LOGIN__id=request.session['lid'])
    ob = study_material.objects.filter(Class=ob1.Class).order_by('-id').order_by('-id')

    return render(request, 'Parent/view marks_parent.html', {'val':ob})

@login_required(login_url='/')
def searchresult_par(request):
    sm=request.POST['select']
    request.session['sm']=sm
    result=[]
    i=parent_table.objects.get(LOGIN__id=request.session['lid'])
    obr = chatbot.objects.filter(DATASET__STUDYMATERIAL__id=sm, PARENT__id=i.id, DATASET__type='Easy')
    datelist = []
    for j in obr:
        if j.date not in datelist:
            datelist.append(j.date)
    print(datelist)
    for j in datelist:
        row = {"name": i.fname + " " + i.lname}
        obr = chatbot.objects.filter(DATASET__STUDYMATERIAL__id=sm, PARENT__id=i.id, DATASET__type='Easy', date=j)
        row['ty'] = 'Easy'
        row['date'] = j
        mark = 0
        for k in obr:
            try:
                x = float(k.answer)
                if k.answer == k.DATASET.answer:
                    mark = mark + 1
            except:
                m = mark_generation(k.answer, k.DATASET.answer)
                if m >= 0.5:
                    mark = mark + 1
        row['mark'] = str(mark) + "/" + str(len(obr))
        row['s']=str(mark) + "-" + str(len(obr))+"-Easy"
        result.append(row)
    obr = chatbot.objects.filter(DATASET__STUDYMATERIAL__id=sm, PARENT__id=i.id, DATASET__type='Medium')
    datelist = []
    for j in obr:
        if j.date not in datelist:
            datelist.append(j.date)
    for j in datelist:
        row = {"name": i.fname + " " + i.lname}
        obr = chatbot.objects.filter(DATASET__STUDYMATERIAL__id=sm, PARENT__id=i.id, DATASET__type='Medium', date=j)
        row['ty'] = 'Medium'
        row['date'] = j
        mark = 0
        for k in obr:
            try:
                x = float(k.answer)
                if k.answer == k.DATASET.answer:
                    mark = mark + 1
            except:
                m = mark_generation(k.answer, k.DATASET.answer)
                if m >= 0.5:
                    mark = mark + 1
        row['mark'] = str(mark) + "/" + str(len(obr))
        row['s'] = str(mark) + "-" + str(len(obr)) + "-Medium"
        result.append(row)
    obr = chatbot.objects.filter(DATASET__STUDYMATERIAL__id=sm, PARENT__id=i.id, DATASET__type='Hard')
    datelist = []
    for j in obr:
        if j.date not in datelist:
            datelist.append(j.date)
    for j in datelist:
        row = {"name": i.fname + " " + i.lname}
        obr = chatbot.objects.filter(DATASET__STUDYMATERIAL__id=sm, PARENT__id=i.id, DATASET__type='Hard', date=j)
        row['ty'] = 'Hard'
        row['date'] = j
        mark = 0
        for k in obr:
            try:
                x = float(k.answer)
                if k.answer == k.DATASET.answer:
                    mark = mark + 1
            except:
                m = mark_generation(k.answer, k.DATASET.answer)
                if m >= 0.5:
                    mark = mark + 1
        row['mark'] = str(mark) + "/" + str(len(obr))
        row['s'] = str(mark) + "-" + str(len(obr)) + "-Hard"
        result.append(row)
    ob1 = parent_table.objects.get(LOGIN__id=request.session['lid'])
    ob = study_material.objects.filter(Class=ob1.Class).order_by('-id').order_by('-id')

    return render(request, 'Parent/view marks_parent.html', {'val': ob,"val1":result,'sm1':int(sm)})
    # return render(request,'Parent/view marks_parent.html',{'val':result})

@login_required(login_url='/')
def viewresult(request):
    ob=study_material.objects.filter(EXPERT__LOGIN__id=request.session['lid'])
    return render(request,'Expert/view marks.html',{'val':ob})

@login_required(login_url='/')
def searchresult(request):
    sm=request.POST['select']
    ob=chatbot.objects.filter(DATASET__STUDYMATERIAL__id=sm)
    listp=[]
    for i in ob:
        listp.append(i.PARENT.id)
    obp=parent_table.objects.filter(id__in=listp)
    result=[]
    for i in obp:

        obr=chatbot.objects.filter(DATASET__STUDYMATERIAL__id=sm,PARENT__id=i.id,DATASET__type='Easy')
        datelist=[]
        for j in obr:
            if j.date not in datelist:
                datelist.append(j.date)
        print(datelist)
        for j in datelist:
            row = {"name":i.fname+" "+i.lname}
            obr = chatbot.objects.filter(DATASET__STUDYMATERIAL__id=sm, PARENT__id=i.id, DATASET__type='Easy',date=j)
            row['ty']='Easy'
            row['date']=j
            mark=0
            for k in obr:
                try:
                    x=float(k.answer)
                    if k.answer==k.DATASET.answer:
                        mark=mark+1
                except:
                    m=mark_generation(k.answer,k.DATASET.answer)
                    if m>=0.5:
                        mark=mark+1
            row['mark']=str(mark)+"/"+str(len(obr))
            result.append(row)
        obr = chatbot.objects.filter(DATASET__STUDYMATERIAL__id=sm, PARENT__id=i.id, DATASET__type='Medium')
        datelist = []
        for j in obr:
            if j.date not in datelist:
                datelist.append(j.date)
        for j in datelist:
            row = {"name": i.fname + " " + i.lname}
            obr = chatbot.objects.filter(DATASET__STUDYMATERIAL__id=sm, PARENT__id=i.id, DATASET__type='Medium', date=j)
            row['ty'] = 'Medium'
            row['date'] = j
            mark = 0
            for k in obr:
                try:
                    x = float(k.answer)
                    if k.answer == k.DATASET.answer:
                        mark = mark + 1
                except:
                    m = mark_generation(k.answer, k.DATASET.answer)
                    if m >= 0.5:
                        mark = mark + 1
            row['mark'] = str(mark) + "/" + str(len(obr))
            result.append(row)
        obr = chatbot.objects.filter(DATASET__STUDYMATERIAL__id=sm, PARENT__id=i.id, DATASET__type='Hard')
        datelist = []
        for j in obr:
            if j.date not in datelist:
                datelist.append(j.date)
        for j in datelist:
            row = {"name": i.fname + " " + i.lname}
            obr = chatbot.objects.filter(DATASET__STUDYMATERIAL__id=sm, PARENT__id=i.id, DATASET__type='Hard', date=j)
            row['ty'] = 'Hard'
            row['date'] = j
            mark = 0
            for k in obr:
                try:
                    x = float(k.answer)
                    if k.answer == k.DATASET.answer:
                        mark = mark + 1
                except:
                    m = mark_generation(k.answer, k.DATASET.answer)
                    if m >= 0.5:
                        mark = mark + 1
            row['mark'] = str(mark) + "/" + str(len(obr))
            result.append(row)
    obsm=study_material.objects.filter(EXPERT__LOGIN__id=request.session['lid'])
    return render(request,'Expert/view marks.html',{'val':obsm,"v":result,'sm1':int(sm)})



@login_required(login_url='/')
def mng_sugges(request):
    ob = suggestion_table.objects.filter(EXPERT__LOGIN__id=request.session['lid']).order_by('-id')
    return render(request,'Expert/Manage suggestions.html',{'val': ob})

@login_required(login_url='/')
def add_sugges(request):
    return render(request,'Expert/Add suggestions.html')

def addedsugges(request):
    ty = request.POST['select']
    mk = request.POST['textfield']
    sug = request.POST['textfield2']

    ub = suggestion_table()
    ub.EXPERT=expert_table.objects.get(LOGIN__id=request.session['lid'])
    ub.suggestion=sug
    ub.mark=mk
    ub.type=ty

    ub.save()
    return HttpResponse('''<script>;window.location='/mng_sugges#about'</script>''')


def deletesug(request,id):
    ob = suggestion_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>;window.location='/mng_sugges#about'</script>''')


@login_required(login_url='/')
def view_sugges(request,id):
    id=id.split("-")
    p=(int(id[0])/int(id[1]))*100
    print(p)
    ob = suggestion_table.objects.filter(mark__lte=p,type=id[2]).order_by("-mark")
    print(ob)
    marklist=[]
    sm=request.session['sm']
    result = []
    i = parent_table.objects.get(LOGIN__id=request.session['lid'])
    obr = chatbot.objects.filter(DATASET__STUDYMATERIAL__id=sm, PARENT__id=i.id, DATASET__type=id[2])
    datelist = []
    for j in obr:
        if j.date not in datelist:
            datelist.append(j.date)
    print(datelist)
    for j in datelist:

        obr = chatbot.objects.filter(DATASET__STUDYMATERIAL__id=sm, PARENT__id=i.id, DATASET__type=id[2], date=j)

        mark = 0
        for k in obr:
            try:
                x = float(k.answer)
                if k.answer == k.DATASET.answer:
                    mark = mark + 1
            except:
                m = mark_generation(k.answer, k.DATASET.answer)
                if m >= 0.5:
                    mark = mark + 1
        mark = (int(mark) /len(obr))*100
        marklist.append(mark)

    avgmark=sum(marklist)/len(marklist)
    print(avgmark,"avgmark")
    print(p,"p")
    sug=""
    if len(marklist)>=2:
        if len(marklist)>0:
            if p<=avgmark:
                sug="This mark is below your average performance"
            else:
                sug="This mark is above your average performance"
    if len(marklist) > 2:
        markdiff=[]
        for j in range(0,len(marklist)-1):
            markdiff.append(marklist[j+1]-marklist[j])
        print(marklist)
        print(markdiff)
        k=0
        j=0
        for i in markdiff:
            if i<0:
                k=k+abs(i)
            else:
                j=j+i
        print(k,j)
        if k>j:
            sug=sug+". Your total perfomance is dropping"
        elif k==j:
            sug=sug+". Your total perfomance is constant"
        else:
            sug=sug+". Your total perfomance is increasing"


    if len(ob)>0:
        return render(request,'Parent/view suggestions.html',{'val': [ob[0]],"s":sug})
    else:
        return render(request, 'Parent/view suggestions.html', {'val':[],"s":sug})


@login_required(login_url='/')
def view_doubt_reply(request):
    ob =doubt_table.objects.filter(EXPERT__LOGIN=request.session['lid']).order_by('-id')
    return render(request,'Expert/view doubts &send reply.html',{'val': ob})

@login_required(login_url='/')
def searchdoubt(request):
    dt=request.POST['textfield']
    ob=doubt_table.objects.filter(date=dt,EXPERT__LOGIN=request.session['lid'])
    return render(request,'Expert/view doubts &send reply.html',{'val':ob})


@login_required(login_url='/')
def reply(request,id):
    request.session['cid']=id
    return render(request,'Expert/reply.html')


@login_required(login_url='/')
def sendreply(request):
    rm=request.POST['textfield']
    ub=doubt_table.objects.get(id=request.session['cid'])
    ub.reply=rm
    ub.save()
    return HttpResponse('''<script>;window.location='/view_doubt_reply#about'</script>''')



#================================================================================================
@login_required(login_url='/')
def chatwithparent(request):
    ob = parent_table.objects.all()
    return render(request,"Staff/fur_chat.html",{'val':ob})



@login_required(login_url='/')
def chatview(request):
    ob = parent_table.objects.all()
    d=[]
    for i in ob:
        r={"name":i.fname+" "+i.lname,'photo':i.photo.url,'email':i.email,'loginid':i.LOGIN.id}
        d.append(r)
    return JsonResponse(d, safe=False)



@login_required(login_url='/')
def coun_insert_chat(request,msg,id):
    print("===",msg,id)
    ob=chat_table()
    ob.from_id=login_table.objects.get(id=request.session['lid'])
    ob.to_id=login_table.objects.get(id=id)
    ob.message=msg
    ob.date=datetime.datetime.now().strftime("%Y-%m-%d")
    ob.save()

    return JsonResponse({"task":"ok"})
    # refresh messages chatlist


@login_required(login_url='/')
def coun_msg(request,id):

    ob1=chat_table.objects.filter(from_id=id,to_id=request.session['lid'])
    ob2=chat_table.objects.filter(from_id=request.session['lid'],to_id=id)
    combined_chat = ob1.union(ob2)
    combined_chat=combined_chat.order_by('id')
    res=[]
    for i in combined_chat:
        res.append({"from_id":i.from_id.id,"msg":i.message,"date":i.date,"chat_id":i.id})

    obu=parent_table.objects.get(LOGIN__id=id)


    return JsonResponse({"data":res,"name":obu.fname+" "+obu.lname,"photo":obu.photo.url,"user_lid":obu.LOGIN.id})
#=============================================================================================

#================================================================================================
@login_required(login_url='/')
def chatwithstaff(request):

    ob1 = parent_table.objects.get(LOGIN__id=request.session['lid'])
    ob = staff_table.objects.filter(Class=ob1.Class)
    return render(request,"Parent/fur_chat.html",{'val':ob})


#
#
@login_required(login_url='/')
def chatviews(request):
    ob1 = parent_table.objects.get(LOGIN__id=request.session['lid'])
    ob = staff_table.objects.filter(Class=ob1.Class)
    d=[]
    for i in ob:
        r={"name":i.fname+i.lname,'photo':i.photo.url,'email':i.ph_no,'loginid':i.LOGIN.id}
        d.append(r)
    return JsonResponse(d, safe=False)


#
#
@login_required(login_url='/')
def coun_insert_chats(request,msg,id):
    print("===",msg,id)
    ob=chat_table()
    ob.from_id=login_table.objects.get(id=request.session['lid'])
    ob.to_id=login_table.objects.get(id=id)
    ob.message=msg
    ob.date=datetime.datetime.now().strftime("%Y-%m-%d")
    ob.save()
#
    return JsonResponse({"task":"ok"})
#     # refresh messages chatlist
#
#
@login_required(login_url='/')
def coun_msgs(request,id):

    ob1=chat_table.objects.filter(from_id=id,to_id=request.session['lid'])
    ob2=chat_table.objects.filter(from_id=request.session['lid'],to_id=id)
    combined_chat = ob1.union(ob2)
    combined_chat=combined_chat.order_by('id')
    res=[]
    for i in combined_chat:
        res.append({"from_id":i.from_id.id,"msg":i.message,"date":i.date,"chat_id":i.id})

    obu=staff_table.objects.get(LOGIN__id=id)


    return JsonResponse({"data":res,"name":obu.fname,"photo":obu.photo.url,"user_lid":obu.LOGIN.id})
# #=============================================================================================


#=============================================================================================
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

num=['0','1','2','3','4','5','6','7','8','9']
def mark_generation(ans,oans):


    ps = PorterStemmer()


    stop_words = set(stopwords.words('english'))

    word_tokens = word_tokenize(ans.lower())


    filtered_sentence = []

    for w in word_tokens:
        if w not in stop_words:
            lis = []
            my_string = w
            only_characters = ""

            for char in my_string:
                if char.isalpha():
                    if char != "-" and char != "-" and char not in num:
                        only_characters += char
                    else:
                        lis.append(only_characters)
                        only_characters = ""
                elif char == " ":
                    lis.append(only_characters)
                    only_characters = ""
            else:
                lis.append(only_characters)

            for ww in lis:
                if len(ww) >= 3:
                    w = ps.stem(w)

                    filtered_sentence.append(w)
    word_tokens = word_tokenize(oans.lower())


    filtered_sentence1 = []

    for w in word_tokens:
        if w not in stop_words:
            lis = []
            my_string = w
            only_characters = ""

            for char in my_string:
                if char.isalpha():
                    if char != "-" and char != "-" and char not in num:
                        only_characters += char
                    else:
                        lis.append(only_characters)
                        only_characters = ""
                elif char == " ":
                    lis.append(only_characters)
                    only_characters = ""
            else:
                lis.append(only_characters)

            for ww in lis:
                if len(ww) >= 3:
                    w = ps.stem(w)

                    filtered_sentence1.append(w)

    X_set = set(filtered_sentence)
    Y_set = set(filtered_sentence1)
    l1=[]
    l2=[]
    # form a set containing keywords of both strings
    rvector = X_set.union(Y_set)
    for w in rvector:
        if w in X_set:
            l1.append(1)  # create a vector
        else:
            l1.append(0)
        if w in Y_set:
            l2.append(1)
        else:
            l2.append(0)
    c = 0

    # cosine formula
    for i in range(len(rvector)):
        c += l1[i] * l2[i]
    cosine = c / float((sum(l1) * sum(l2)) ** 0.5)
    print("similarity: ", cosine)
    return cosine

#========================================================================================================