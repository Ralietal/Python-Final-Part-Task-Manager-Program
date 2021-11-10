import datetime
import math

from datetime import date

# This program allows users whose names and passwords have been saved in the users txt files to:
# add task, view all task and view tasks of the logged-in individuals with the exception of the admin,
# who is allowed to register new users and read the tasks and users stat
# usernames are stored in the empty string "usernames"
# passwords are stored in the empty string "passwords"
# Login = False  boolean is meant to counter the true state of the login state
# printing lines below is just a control statement, this wont apply in normal real world, this is meant for ease of knowing which users,
# are registered

#  List of defined Functions       

# def reg_user is a function that gets called when admin wants to register a new user,
# this function is called as "r" in the program
# only the admin can register a new user
# admin get informed if the user is in the file.read and prompted to register another user    
def reg_user():
        if user_name == "admin":
            confirmation = False
            while confirmation == False:
                new_user = input("Please enter new user_name: \n")
                if new_user in lines:
                    print("Username already in use, choose another username")
                    confirmation = False
                else:
                    password = input("Please enter new user password: \n")
                    password_confirmantion = input("Please confirm your user password: \n")
                    if password != password_confirmantion:
                        print("Password dont match, please try again")
                        confirmation = False
 # only when the username and passwords are confirmed can the user write the text file
 # log in details are written in a specified format in the txt file, to ensure consistancy
                    else:   
                        print("Username and password confirmed")
                        file = open("user.txt","a")
                        file.write(f"\n{new_user}, {password}")
                        confirmation = True
                        login_details = user_name+","+" "+password
                        return login_details        
                        file.close()
        else:
            print("You dont have rights to register new user")
            
# def user_data is a function that hold all the usernames only without passwords,
def user_data():
        userS = []
        file = open("user.txt","r")
        lines = file.readlines()
        for line in lines:
           userN = line.strip().split(",")
           userS.append(userN)
        print(userS)
        return userS
    
# def add_task is a function that gets called when a user wants to add a task,
# this function is called as "a" in the program
# note \n is added at the end of the input variable to esnure lines writes below each other
def add_task():     
        excecutor_user_name = input("Enter the user_name of the person this task is assigned to: \n")
        task_title = input("Enter the task title: \n")
        task_description = input("Enter the task description: \n")
        task_due_day = input("Enter the day to complete the task: \n")
        task_due_month = input("Enter the month to complete the task as Oct for October or Nov for November: \n")
        task_due_year = input("Enter the year to complete the task: \n")
        task_due_date = task_due_day+task_due_month+task_due_year
        task_creation_date = date.today()
        task_creation_date = task_creation_date.strftime("%d%b%y")
        print(task_creation_date)
        task_complete = input("Mark the task as No: \n")
        task_completion_status = task_complete
        
        file = open("tasks.txt","a")
        file.write("\n"+ excecutor_user_name+","+task_title+","+task_description+","+task_due_date+","+task_creation_date+","+task_completion_status)
        task_addition = excecutor_user_name+","+task_title+","+task_description+","+task_due_date+","+task_creation_date+","+task_completion_status
        return task_addition
        file.close()
        
# def view_all function is a function that gets called when a user wants to view all the tasks
# this function is called as "va" in the program
# in this function taskNum counts the number of all task and display the number next to each task
def view_all():    
        taskNum =0
        file = open("tasks.txt","r")
        lines = file.readlines()
        for line in lines:
            taskNum+=1
            view_task = line.strip().split(",")  
            print("Task no     :"+(str(taskNum)))
            print("Task        :"+view_task[1])
            print("Assigned to :"+view_task[0])
            print("Date assigned:"+view_task[3])
            print("Due date     :"+view_task[4])
            print("Task complete?:"+view_task[5])
            print("Taskescription:"+view_task[2])
            
# def all_tasks function holds all tasks in the current text file,
# all_tasks _num counts all the project and display the number next to each task
# all tasks in current text file gets appended into an empty list to be called as indexes
def all_tasks():
    all_tasks_num = 0
    all_tasks_list = []
    file = open("tasks.txt","r")
    lines = file.readlines()
    for line in lines:
        all_tasks_num+=1
        all_tasks = line.strip().split(",")
        print("Task no     :"+str(all_tasks_num))
        print("Task        :"+all_tasks[1])
        print("Assigned to :"+all_tasks[0])
        print("Date assigned:"+all_tasks[3])
        print("Due date     :"+all_tasks[4])
        print("Task complete?:"+all_tasks[5])
        print("Task description:"+all_tasks[2])
        all_tasks_list.append(all_tasks)
        return all_tasks_list

# def view_mine_only function is a function that gets called when a user wants to view tasks assigned to them,
# this function is called when -1 is enetred under "vm" function in the program,
# in this function task_num counts the number of all task assigned to them and display them next to the task
# an emppty list is created to house all the tasks assgined to the signed in user,
# the logged-in user tasks are called from this list for viewing only
def view_mine_only():
    vmtask=[]
    task_num =0
    file = open("tasks.txt","r")
    lines = file.readlines()
    for line in lines:
        view_task = line.strip().split(",")
        if user_name == view_task[0]:
            task_num+=1
            print("Task no     :"+str(task_num))
            print("Task        :"+view_task[1])
            print("Assigned to :"+view_task[0])
            print("Date assigned:"+view_task[3])
            print("Due date     :"+view_task[4])
            print("Task complete?:"+view_task[5])
            print("Task description:"+view_task[2])
            vmtask.append(view_task)
            
# def view_mine function is a function that gets called when a user wants to view tasks assigned to them,
# this function is calle as "vm" in the program,
# in this function task_num counts the number of all task assigned to them and display them next to the task
# an emppty list is created to house all the tasks assgined to the signed in user,
# the logged-in user tasks are called from this list for viewing or edditing
# to edit the task, the task is called by it index because it in the list
# because the we start reading from zero, any displayed number is not the actual index number,
# but the actual index is input number minus 1 to get to the real number
def view_mine():
    vmtask=[]
    task_num =0
    file = open("tasks.txt","r")
    lines = file.readlines()
    for line in lines:
        view_task = line.strip().split(",")
        if user_name == view_task[0]:
            task_num+=1
            print("Task no     :"+str(task_num))
            print("Task        :"+view_task[1])
            print("Assigned to :"+view_task[0])
            print("Date assigned:"+view_task[3])
            print("Due date     :"+view_task[4])
            print("Task complete?:"+view_task[5])
            print("Task description:"+view_task[2])
            vmtask.append(view_task)
            
# the print spaces added below are for program neatnes and not part of the program
        
    print()                
    print("     TASK EDITING OPTION ")
    print()
    
# taskView is a variable given to the task to be edited
# vmtask[task] is a task indexed a number given by a user, while vmtask is a list containing the logged-in user,
# assigned projects
# below print statement is just a control statement to ensure that the called task is the same
# within taskView, index 5 is task status, hence taskView[5]
    
    task_number = int(input("Enter the number of the task to edit:\n"))
    task = task_number-1
    taskView = vmtask[task]
    print(f" This is the task to be edited: \n {taskView}")        
    task_complete = input("Do you want to mark the task complete Yes or No: \n")
    if task_complete == "Yes":
        taskView[5] = task_complete
        
# if the user opt not to assign a complete status to the task, the user is prompted if,
# they want to rea-assign the selected project to the new user
# if the user opt to edit the task and the tasks is not marked complete, a new user is assigned,
# new_user is postioned at index 0, hence taskView[0]

    if task_complete == "No":            
        user_edit = input("Do you want to re-assign the task to the other user: Yes or No :\n")
        if user_edit == "Yes":
            if taskView == vmtask[task]:            
                if user_edit == "Yes"and taskView[5] != "Yes":
                    new_user = input("Enter the new user to assign the task to:\n")
                    taskView[0]= new_user
                        
# if the user opt not to assign a new user status to the task, the user is prompted if,
# they want to change due date of the selected task
# if the user opt to edit the task and the tasks is not marked complete, due date get changed
  
        if user_edit == "No":
            if taskView == vmtask[task]:
                due_date_edit = input("Do you want to change the task due-date: Yes or No :\n")
                if due_date_edit == "Yes"and taskView[5] != "Yes":
                    print(f"Current due date {taskView[4]}")
                    task_due_day = input("Enter the day to complete the task: \n")
                    task_due_month = input("Enter the month in as eg Oct for October or Nov for November to complete the task: \n")
                    task_due_year = input("Enter the year to complete the task: \n")
                    task_new_due_date = (task_due_day+task_due_month+task_due_year)
                    print(task_new_due_date)
                    taskView[4]= task_new_due_date

        print()
        print("         ALL PROJECTS IN THE CURRENT TEXT FILE TASKS( BEFORE BEING EDITED) ARE DISPLAYED BELOW   ")
        print("         FROM THIS LIST CHOOSE THE PROJECT THAT YOU HAVE EDITTED TO REMOVE IT FROM THE TXT FILE")
        print()
        
# the below list displays all the projects in the text file before update
# a counter all_tasks_num is initiated and listed to count all the task and display the number next to the task
# an empty list (all_tasks_list []) is used to append all the task from the current text file called "tasks" in a list format

    all_tasks_num = 0
    all_tasks_list = []
    file = open("tasks.txt","r")
    lines = file.readlines()
    for line in lines:
        all_tasks_num+=1
        all_tasks = line.strip().split(",")        
        print("Task no     :"+str(all_tasks_num))
        print("Task        :"+all_tasks[1])
        print("Assigned to :"+all_tasks[0])
        print("Date assigned:"+all_tasks[3])
        print("Due date     :"+all_tasks[4])
        print("Task complete?:"+all_tasks[5])
        print("Task description:"+all_tasks[2])
        all_tasks_list.append(all_tasks)
        
# to remove the task, the task is called by its index because it in the list,
# because we start reading from zero, any displayed number is not the actual index number,
# but the actual index is input number minus 1 to get to the real number
# the print statements below are for control purposes to confirm the task to be removed
# taskAl is a number to be referenced a index for the task to be removed
# taskReplace is a variable assigned to a task in all_tasks_list indexed[taskAl]
# taskReplace is popped out of the all_tasks_list, not to duplicate it when an eddited task is,
# appended back into the task text file
    
    all_task_number = int(input(" Enter the number assigned to task that is the same as the edited to remove in text file:\n"))
    taskAl = all_task_number -1
    taskReplace = all_tasks_list[taskAl]
    print(f"task to replace {taskReplace}")
    poppedTask = all_tasks_list.pop(taskAl)
    print("This is popped",poppedTask) 
# below we loop through the updated all_tasks_list (where the edited task sibling has been poped),
# the remaining tasks indexed 0 and 1 are renamed 
    for line in all_tasks_list:
        alltasks_list = all_tasks_list[0]
        allTasks_list = all_tasks_list[1]
# after popping the task that has been eddited outside the tasks file, the updated list is written back in the tasks texfile,
# thereby overriding everything in that tasks text file
    file = open("tasks.txt","w")
    file.write(allTasks_list[0]+","+allTasks_list[1]+","+allTasks_list[2]+","+allTasks_list[3]+","+allTasks_list[4]+","+allTasks_list[5]+"\n")
    file.write(alltasks_list[0]+","+alltasks_list[1]+","+alltasks_list[2]+","+alltasks_list[3]+","+alltasks_list[4]+","+alltasks_list[5])
    file.close()
# a newly update task is being appended to the updated tasks text file here                            
    file = open("tasks.txt","a")
    file.write("\n"+taskView[0]+","+taskView[1]+","+taskView[2]+","+taskView[3]+","+taskView[4]+","+taskView[5])
    file.close()

# def display_statistics is a function called as "ds" to display statistics    
# only admin has access to display statistics
# statistics can be dispalyed as either taskOverview or user overview
def display_statistics ():  
    user_name =="admin"
    display_choice = input("Choose stats to display: T- for task Overview or U for userOverview \n")
    if display_choice == "T":                    
        print("        TASK OVERVIEW")
        print()
        file = open("tasks_overview.txt","r")
        lines = file.readlines()
        for line in lines:
            print(line)

    if display_choice == "U":
        print("        USER OVERVIEW")
        print()
        file = open("user_overview.txt","r")
        lines =file.readlines()
        for line in lines:
            print(line)
        return display_choice
    
# def generate_report is a function called "gr" used to generate reports before they can be displayed   
# only admin has access to generate the stats
# numerous counters has been generated and initialised to calculate the required information
# once the information is determined it is written in either tasks_overview txt file or user_overview txt file     
def generate_report():
        user_name == "admin"
        user_num = 0
        task_num = 0
        completed = 0
        incomplete = 0
        due_date = 0
        user0_complet_perc = 0
        user1_complet_perc = 0
        user2_complet_perc = 0        
        user3_complet_perc = 0
        user0_incomplet_perc = 0
        user1_incomplet_perc = 0
        user2_incomplet_perc = 0
        user3_incomplet_perc = 0        
        user0_due_date = 0
        user1_due_date = 0
        user2_due_date = 0
        user3_due_date = 0
        user0tasks = 0
        user1tasks = 0
        user2tasks = 0
        user3tasks = 0
# determination of number of the users
        file =open("user.txt","r")
        lines = file.readlines()
        for line in lines:
                user_num+=1
            
        file = open("user_overview.txt","a")
        file.write("Total number of users registered in taskmanager: "+str(user_num)+"\n")
        file.close()
        
# determination of the number of task
        file = open("tasks.txt","r")
        lines = file.readlines()
        for line in lines:
                task_num+=1
        
        file = open("tasks_overview.txt","a")
        file.write("Total number of task generated by taskmanager is: "+str(task_num)+"\n")
        file.close()
        
# determination of complete task
        file = open("tasks.txt","r")
        lines = file.readlines()
        for line in lines:
                complete = line.strip().split(",")
                if complete[5]== "Yes":
                        completed+=1
        
        file = open("tasks_overview.txt","a")
        file.write("Total number of completed task is: "+ str(completed)+"\n")
        file.close()
        
# determination of incomplete task
        file = open("tasks.txt","r")
        lines = file.readlines()
        for line in lines:
                incomplet = line.strip().split(",")
                if incomplet[5]=="No":
                        incomplete += 1    
        
        file = open("tasks_overview.txt","a")
        file.write("Total number of incomplete tasks is: "+str(incomplete)+"\n")
        file.close()
        
# determination of due projects:
        file = open("tasks.txt","r")
        lines = file.readlines()
        for line in lines:
                due = line.strip().split(",")
                if date.today().strftime("%d%b%Y")>= due[4]and due[5]=="No":
                        due_date+=1
            
        due_incomplete = due_date
        file = open("tasks_overview.txt","a")
        file.write("Total number of incomplete and due project is: "+str(due_incomplete)+"\n")
        file.close()

# determine percentage of due and incomplete project
# the calculation takes a float because of a division and is rounded 
        incompleteT = round(float(incomplete/task_num)*100)
        
        dueT = round(float(due_date/task_num)*100)
        
# append the output of the % calculation above to the task_overview files
        file = open("tasks_overview.txt","a")
        file.write("The percentage of incomplete projects is :"+str(incompleteT)+"%"+"\n")
        file.write("The percentage of due projects is :"+str(dueT)+"%")
        file.close()

# determine individual users stats
# an empty list is created to append only the usernames separated from the login details in user txt file
        userS = []
        file = open("user.txt","r")
        lines = file.readlines()
        for line in lines:
                userN = line.strip().split(",")
                userS.append(userN[0])
        print(userS[0])  
        
# the counters below determine the number of each user appearance therebey,
# indicating number of tasks assigned to each
        
        file = open("tasks.txt","r")
        lines = file.readlines()
        for line in lines:
                tasks_list = line.strip().split(",")
                if userS[0] in tasks_list:
                        user0tasks+=1
                        if date.today().strftime("%d%b%Y")>=tasks_list[4]and tasks_list[5]== "No":
                                 user0_due_date+=1            
                        if "No" in tasks_list[5]:
                                user0_incomplet_perc+=1
                        if "Yes" in tasks_list[5]:
                                user0_complet_perc+=1

                if userS[1] in tasks_list:
                        user1tasks+=1
                        if date.today().strftime("%d%b%Y")>=tasks_list[4]and tasks_list[5]== "No":
                                 user1_due_date+=1            
                        if "No" in tasks_list[5]:
                                user1_incomplet_perc+=1
                        if "Yes" in tasks_list[5]:
                                user1_complet_perc+=1
                if userS[2] in tasks_list:
                        user2tasks+=1
                        if date.today().strftime("%d%b%Y")>=tasks_list[4]and tasks_list[5]== "No":
                                 user2_due_date+=1            
                        if "No" in tasks_list[5]:
                                user2_incomplet_perc+=1
                        if "Yes" in tasks_list[5]:
                                user2_complet_perc+=1
                if userS[3] in tasks_list:
                        user3tasks+=1
                        if date.today().strftime("%d%b%Y")>=tasks_list[4]and tasks_list[5]== "No":
                                 user3_due_date+=1            
                        if "No" in tasks_list[5]:
                                user3_incomplet_perc+=1
                        if "Yes" in tasks_list[5]:
                                user3_complet_perc+=1 
      
# determine the % users overdue and incomplete tasks                
# in order to counter the mathematical error of impemissibility of divison by zero a,
# the below variable are set to zero and condition set to allow for non zero scenario                
        perc_incomp_due_user0 = 0
        perc_incomp_due_user1 = 0
        perc_incomp_due_user2 = 0
        perc_incomp_due_user3 = 0
              
        if user0tasks == 0:
                perc_incomp_due_user0 == 0
        else:    
                perc_incomp_due_user0 = round(float(user0_due_date/user0tasks)*100)
        if user1tasks == 0:
                perc_incomp_due_user1 == 0
        else:    
                perc_incomp_due_user1 = round(float(user1_due_date/user1tasks)*100)

        if user2tasks == 0:
                perc_incomp_due_user2 == 0
        else:
                perc_incomp_due_user2 = round(float(user2_due_date/user2tasks)*100)
        if user3tasks == 0:
                perc_incomp_due_user3 == 0
        else:    
                perc_incomp_due_user3 = round(float(user3_due_date/user3tasks)*100)
               
# % of total tasks assigned to this user
# total task used is the total number of projects in the file
# in order to counter the mathematical error of impemissibility of divison by zero a,
# the below variable are set to zero and condition set to allow for non zero scenario
        perc_task_user0 = 0
        perc_task_user1 = 0
        perc_task_user2 = 0
        perc_task_user3 = 0

        if user0tasks == 0:
                perc_task_user0 == 0
        else:
                perc_task_user0 = round(float(user0tasks/task_num)*100)
        if user1tasks == 0:
                perc_task_user1 == 0
        else:    
                perc_task_user1 = round(float(user1tasks/task_num)*100)
        if user2tasks == 0:
                perc_task_user2 == 0
        else:
                perc_task_user2 = round(float(user2tasks/task_num)*100)
        if user3tasks == 0:
                perc_task_user3 == 0
        else:
                perc_task_user3 = round(float(user3tasks/task_num)*100)
        
# determine the % task assigned to the user but incomplete
# in order to counter the mathematical error of impemissibility of divison by zero a,
# the below variable are set to zero and condition set to allow for non zero scenario                     
        perc_incompleted_user0 = 0
        perc_incompleted_user1 = 0
        perc_incompleted_user2 = 0
        perc_incompleted_user3 = 0
        
        if user0tasks == 0:
                perc_incompleted_user0 == 0
        else: 
                perc_incompleted_user0 =round(float(user0_incomplet_perc/user0tasks)*100)
        if user1tasks == 0:
                perc_incompleted_user1 == 0
        else:    
                perc_incompleted_user1 =round(float(user1_incomplet_perc/user1tasks)*100)
        if user2tasks == 0:
                perc_incompleted_user2 == 0
        else:
                perc_incompleted_user2 =round(float(user2_incomplet_perc/user2tasks)*100)
        if user3tasks == 0:
                perc_incompleted_user3 == 0
        else:
                perc_incompleted_user3 =round(float(user3_incomplet_perc/user3tasks)*100)
                          
# determine % of completed task assigned to the user              
# in order to counter the mathematical error of impemissibility of divison by zero a,
# the below variable are set to zero and condition set to allow for non zero scenario
        perc_completed_user0 = 0
        perc_completed_user1 = 0
        perc_completed_user2 = 0
        perc_completed_user3 = 0

        if user0tasks == 0:
                perc_completed_user0 == 0
        else:    
                perc_completed_user0 = round(float(user0_complet_perc/user0tasks)*100)
        if user1tasks == 0:
                perc_completed_user1 == 0
        else:
                perc_completed_user1 = round(float(user1_complet_perc/user1tasks)*100)
        if user2tasks == 0:
                perc_completed_user2 == 0
        else:    
                perc_completed_user2 = round(float(user2_complet_perc/user2tasks)*100)
        if user3tasks == 0:
                perc_completed_user3 == 0
        else:
                perc_completed_user3 = round(float(user3_complet_perc/user3tasks)*100)
        
# append the statistics assigned to the users to user_overview txt file
# each stats is calculated above and appended below for neatness of the code
# print space in between the users is also for code neatness
# \n at the end of the write sentence is to allow task to append below each other
                      
        file = open("user_overview.txt","a")
        file.write("STATISTICS FOR USER: " + str(userS[0]) + "\n")
        print()
        file.write("Number of tasks assigned:      "+ str(user0tasks)+"\n")
        file.write("Percentage tasks assigned:     "+ str(perc_task_user0)+"%"+"\n")
        file.write("Percentage tasks completed:    "+ str(perc_completed_user0)+"%"+"\n")
        file.write("Percentage tasks incomplete:   "+ str(perc_incompleted_user0)+"%"+"\n")
        file.write("Percentage incomplete&overdue  "+ str(perc_incomp_due_user0)+"%"+"\n")
        "\n"
        print()
        file.write("STATISTICS FOR USER: " + str(userS[1]) + "\n")
        print()
        file.write("Number of tasks assigned:      "+ str(user1tasks)+"\n")
        file.write("Percentage tasks assigned:     "+ str(perc_task_user1)+"%"+"\n")
        file.write("Percentage tasks completed:    "+ str(perc_completed_user1)+"%"+"\n")
        file.write("Percentage tasks incomplete:   "+ str(perc_incompleted_user1)+"%"+"\n")
        file.write("Percentage incomplete&overdue  "+ str(perc_incomp_due_user1)+"%"+"\n")
        "\n"
        print()
        file.write("STATISTICS FOR USER: " + str(userS[2]) + "\n")
        print()
        file.write("Number of tasks assigned:      "+ str(user2tasks)+"\n")
        file.write("Percentage tasks assigned:     "+ str(perc_task_user2)+"%"+"\n")
        file.write("Percentage tasks completed:    "+ str(perc_completed_user2)+"%"+"\n")
        file.write("Percentage tasks incomplete:   "+ str(perc_incompleted_user2)+"%"+"\n")
        file.write("Percentage incomplete&overdue  "+ str(perc_incomp_due_user2)+"%"+"\n")
        "\n"
        print()
        file.write("STATISTICS FOR USER: " + str(userS[3]) + "\n")
        print()
        file.write("Number of tasks assigned:      "+ str(user3tasks)+"\n")
        file.write("Percentage tasks assigned:     "+ str(perc_task_user3)+"%"+"\n")
        file.write("Percentage tasks completed:    "+ str(perc_completed_user3)+"%"+"\n")
        file.write("Percentage tasks incomplete:   "+ str(perc_incompleted_user3)+"%"+"\n")
        file.write("Percentage incomplete&overdue  "+ str(perc_incomp_due_user3)+"%"+"\n")
        file.close()
    
print("\n WELCOME TO THE TASK MANAGER PAGE: \n")

usernames = " "    
passwords = " "

Login = False      
file = open("user.txt","r")
lines = file.read()
print(lines)

# the initial state of the login is false and the user credentials will be requested
# login_details formated to resemble how they are read in the file
# if the login_details are not in the right combination in the file line, an error message is returned
# when the desired counter state of the login is attained the code runs

print("\n TO LOG_IN PLEASE ENTER USERNAME AND PASSWORD")
 
while Login == False:       
    user_name = input(" Please enter user name: ")
    password = input(" Please enter password: ")
    login_details = user_name+", "+password    
    if login_details not in lines:
        print("Incorrect login_details, please enter a correct details")
        Login = False    
    else:
        print(f"Welcome {user_name}!") 
        Login = True        
while Login == True:         
# when admin user is logged in an additional option of gr and ds are added and can only be viewed by the admin  
    if user_name =="admin":
        print("SUCCESFULLY LOGGED-IN: \n: Please select one of the following options: \n: r-register user: \n: a-add task: \n: va-view all task: \n: vm = view my task: \n: gr = generates report: \n: ds = display statistics: \n: e-exit")
        print(" ")
        print("To display statistics:i.e ds, FIRSTLY GENERATE REPORTS ONCE, ie gr")
        print("NB: Repeated statics generation will result in repeated display")
        choice = input("Select, r, a, va, vm, gr, ds or e: ")
    else:
# when any other user is logged-in an option of "gr" and "ds" is not provided        
        print("SUCCESFULLY LOGGED-IN: \n: Please select one of the following options: \n: r-register user: \n: a-add task: \n: va-view all task: \n: vm = view my task: \n: e-exit")
        choice = input("Select, r, a, va, vm, or e: ")
        
# this option only allows the admin to register new users        
    if choice == "r":
        
        reg_user()
        
    if choice == "a":
        
        add_task()
        
    if choice == "va":

        view_all()
            
    if choice == "vm":
        
        edit_option = input("To view-only and Return  to main Menu enter: -1 OR To view and edit enter: Yes \n")
        if edit_option =="-1":
            
            view_mine_only()
            
        else:                          
            view_mine()        

    if choice == "ds":
        
        display_statistics ()    
                        
    if choice == "gr":
        
        generate_report()
        
    if choice == "e":
        exit()


           
    
        
