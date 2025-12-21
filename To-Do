# This program is a ToDo task manager
def main():
    choice = 0
    while choice != "1" or choice != "2" or choice != "3" or choice != "4":
        choice = input("Hello! What would you like to do? \n1. Add a new task\n2. View Tasks\n3. Mark a task completed\n4. Delete a task\nChoice: ")
        if choice == "1":
            addTask()
            #TODO
        #elif choice == "2":
         #   viewTasks()
        #elif choice == "3":
         #   markTaskCompleted()
        #elif choice == "4":
            #deleteTask()
        else:
            print("Invalid choice. Please try again.")

# Add a task to the "data.txt" file
def addTask():
    task = input("Enter tasks name: ")
    with open("data.txt", "a") as f:
        f.write(task + "\n")
    return "The task has been added!"

if __name__ == "__main__":
    main()