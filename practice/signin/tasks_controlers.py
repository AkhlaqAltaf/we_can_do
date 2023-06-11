from django.shortcuts import render ,HttpResponse


class Task:

    def __init__(self,name,path,language,total_points , next):

        self.name = name
        self.path = path
        self.language = language
        self.total_points = total_points
        self.next = next

class TaskControler:


       
    head = None

    def insert_at_top(self,name,path,language,points):

        new_task = Task(name,path,language, points , self.head)

        self.head = new_task

    def task_at(self , index):

        if self.head is None:

            return "No Task Found"

        else:
            count = 0
            itr = self.head

            while  itr.next:
                
                if count == index -1:

                    return itr
                
                count +=1
                itr= itr.next
            return "This task Number is Not Present"    



    def task_manager(self):



        pass

    def view_task(self,index):

        
        print(".........................................Heloo World")
        task = self.task_at(self,index)
        
        dict = {'task_name':"...........S" ,'language':"............" , 'total_point':".............." ,'path':".........."}
        

        
        return dict

    


