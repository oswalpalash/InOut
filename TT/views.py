from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from models import USERS,TASK,TRIP,TRIP_STATUS,TASK_STATUS
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from models import TRIP,TASK
def login(request):
	html = get_template('login.htm').render(Context({}))
	return HttpResponse(html)


def index(request):
    if request.method=="GET":
        tk = TASK.objects.all()
        tr = TRIP.objects.all()
        usert = USERS.objects.all()
        return render(request,'index.html',{'tk':tk,'tr':tr,'usert':usert})
    elif request.method == 'POST':
        #login data posted
        uid = request.POST.get('user')
        passw = request.POST.get('pass')
        try:
            USER_TEMP = USERS.objects.get(u_id=uid,passw=password)
        except:
            pass

def traveller(request):
    if request.user.is_authenticated():
        return render(request,'traveller.htm')

def listtrip(request):
    if request.user.is_authenticated():
        contt = TRIP.objects.filter(u_id=request.user)
        return render(request,'listtrip.htm',{'contt':contt})

def tasks(request):
    if request.user.is_authenticated():
        contt = TASK.objects.filter(u_id=request.user)
        return render(request,'listtask.htm',{'contt':contt})

def chat(request):
    if request.user.is_authenticated():
        contt = TASK.objects.all()
        usernam = request.user
        users = USERS.objects.all()
        return render(request,'chat.htm',{'contt':contt,'usernam':usernam,'users':users})

def fund(request,tripno):
    if(request.method=='GET'):
        tripdata = TRIP.objects.get(trip_id=tripno)
        print('here')
        taskd=TASK.objects.all()
        return render(request,'fund.htm',{'tripdata':tripdata,'taskd':taskd})
    elif (request.method=='POST'):
        pdata = request.POST.get()
        if request.POST['submit']=='submit':
            tripdata = TRIP.objects.get(trip_id=tripno)
            taskd=TASK.objects.all()
            if(request.POST.get('donate')==""):
                tasknum = request.POST.get('dropdownMenu1')
                taskfund = TASK.objects.get(tasknum).budget
                tripdata.u_id.balance = tripdata.u_id.balance-taskfund
                #mark task as done
                adding = TASK_STATUS
                adding.task_id(tasknum)
                adding.trip_id(tripno)
                adding.status_id(1)
                credadd=USERS.objects.get(u_id=TASK.objects.get(tasknum).u_id.u_id)
                credadd.credits=credadd.credits+100; #100credits added
                credadd.save()
                tripdata.save()
            else:
                tripdata.budget = tripdata.budget-request.POST.get('donate')
                print(request.POST)
                credadd=USERS.objects.get(u_id=request.user)
                credadd.credits=credadd.credits+0.1*tripdata.budget;
                credadd.save()
                tripdata.save()

            return render(request,'fund.htm',{'tripdata':tripdata,'taskd':taskd,'pdata':'pdata'})
        else:
            tripdata = TRIP.objects.get(trip_id=tripno)
            taskd=TASK.objects.all()
            return render(request,'fund.htm',{'tripdata':tripdata,'taskd':taskd,'pdata':'pdata'})