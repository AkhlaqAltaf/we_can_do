from django.shortcuts import render , HttpResponse

from .tasks_controlers import TaskControler as tc
 
import datetime 
from signin.models import *
from django.contrib import messages
def index(request):
   
        
        return render(request, 'index.html')

def home(request):
     return render(request , 'home.html')

def about(request):
    return HttpResponse("This is MY About Page..........")
  
def task(request):
   
    data = tc.view_task(tc, 1)
    return render(request , "tasks.html",data)

def contact_us(request):
    if request.method == "POST":
        print("Yes Here is POST Request")
        email = request.POST.get('email')
        print(email)
        message = request.POST.get('message')

        print(message)
        date_time = datetime.datetime.today()
        contact = Contact(email = email , message = message,date_time = date_time)

        contact.save() 
        messages.success(request, "Success Fully Submitted.")

    return render(request , 'contact_us.html')
    


def show_message(request):

     

     for data in Contact.objects.all():
          
        print(data.email)

     print(dict)     
     return render(request, 'show_message.html' ,dict)     


def mcq_quiz(request):
    mcqs = MCQ.objects.all()
    return render(request, 'quiz.html', {'mcqs': mcqs})



def quiz_submission(request):
    if request.method == 'POST':
        score = 0
        for key in request.POST:
            if key.isdigit():
                mcq = MCQ.objects.get(pk=key)
                selected_option = request.POST[key]
                print("answer is ."+selected_option )
                if selected_option == mcq.answer:
                    print(score, "your Score")
                    score += 1
        return HttpResponse(f'Your score is {score}')