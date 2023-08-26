
from django.shortcuts import render,redirect
import pyrebase


# Remember the code we copied from Firebase.
#This can be copied by clicking on the settings icon > project settings, then scroll down in your firebase dashboard
config={
  "apiKey": "AIzaSyDSVcx9cSHYuZScK31puUnzSe1-0P34iw0",
  "authDomain": "django-backend-v1.firebaseapp.com",
  "projectId": "django-backend-v1",
  "databaseURL":"https://django-backend-v1-default-rtdb.firebaseio.com/",
  "storageBucket": "django-backend-v1.appspot.com",
  "messagingSenderId": "833002413671",
  "appId": "1:833002413671:web:d3a82eeee83b5625efbec2",
  "measurementId": "G-17KVRP3KRM"
}

#here we are doing firebase authentication
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()



def index(request):
        car=[]
        key=[]
        all_users = database.child("Users").get()
        
        for users in all_users.each():
                car.append(users.val())
                key.append(users.key())
                data={
                        'car':car,
                        'key1':key
                        }
                

        return render(request, 'index.html',data)


def insert(request):
        return render(request,'insert.html')

def data(request):
        msg = {
            'name':"Inserted",
            }
        if request.method =='POST':
                name = request.POST.get('name')
                framework = request.POST.get('framework')
                stack = request.POST.get('stack')
                database.child('Users').push({"name":name,"framework":framework,"stack":stack})
                # return render(request,'insert.html',msg)
                return redirect('/')
        
def delete(request,id):
           database.child('Users').child(id).remove()
           return redirect('/')

def edit(request,id):
           lis=[]
           lis.append(database.child('Users').child(id).get().val())
           data={
             'dat':lis,
             'id':id
           }
           
           return render(request, 'update.html',data)


def update(request):
        msg = {
            'name':"updated",
            }
        if request.method =='POST':
                idd= name = request.POST.get('idd')
                name = request.POST.get('name')
                framework = request.POST.get('framework')
                stack = request.POST.get('stack')
                database.child('Users').child(idd).update({"name":name,"framework":framework,"stack":stack})
                # return render(request,'insert.html',msg)
                return redirect('/')