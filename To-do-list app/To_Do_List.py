# Add task
task = []
def add():
    try:
        while True:
            print('''    1. add more 
            2. save and exit''')
            choose = int(input())
            if choose == 1:
                task.append(input("Enter task: "))
            else:
                save()
                print("Tasks saved:", task)
                break
    except:
        print("Enter correct value")
        pass

def overwrite():
    path = "data.txt"
    with open(path , "w") as file:
        data = '\n'.join(task)
        file.write(data)

# View task
def view():
    file = open("data.txt" , "r")
    print(file.read())

# load 
def load():
    task.clear()
    with open ("data.txt" , "r") as f :
        try:
            for line in f:
                task.append(line.strip())
        except FileNotFoundError:
            pass
# mark as completed
def mark():
    view()
    load()
    choose = int(input("Choose the number of task you want to mark completed : "))
    if choose >= 1 and choose <= len(task) :
        task[choose - 1] =(task[choose - 1]  + " : Completed")
        overwrite()
    else:
        print("Enter valid number")

# Delete the task
def delete():
    load()
    view()
    print("Select no. of task to delete")
    choose = int(input())
    if choose >= 1 and choose <= len(task) :
        task.remove(task[choose-1])
        overwrite()

# save file
def save():
    path = "data.txt"
    with open(path , "a") as file:
        data = '\n'.join(task)
        file.write(data)


# Exit Program
print('''
Select options from below(1 to 5) :
      
1. Add Your Task
2. View Your Task
3. Mark task as Completed
4. Delete Your task
5. Save And Exit
      ''')

choose = int(input())
if choose == 1 :
    add()
elif choose == 2 :
    view()
elif choose == 3 :
    mark()
elif choose == 4 :
    delete()
else:
    print("Enter a valid input")