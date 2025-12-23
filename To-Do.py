import csv
import msvcrt

# This program is a ToDo task manager
def main():
    choice = 0
    while choice != "1" or choice != "2" or choice != "3" or choice != "4":
        choice = input("Hello! What would you like to do? \n1. Add a new task\n2. View Tasks\n3. Mark a task completed\n4. Delete a task\nChoice: ")
        if choice == "1":
            addTask()
            #TODO
        elif choice == "2":
            viewTasks()
        #elif choice == "3":
         #   markTaskCompleted()
        #elif choice == "4":
            #deleteTask()
        else:
            print("Invalid choice. Please try again.")

def viewTasks():
    rows = []
    with open("data.csv", "r", newline = '') as f:
        # Assign contents to the object returned by DictReader
        contents = csv.DictReader(f)
        # Iterate through the row in the object
        for row in contents:
            print("Task: " + row["Task"], " - Status: " + row["Status"], sep = '')
            if any(row.values()):
                rows.append(row)
    if not rows:
        # Print no tasks and ask for a prompt to reloop
        print("You have nothing to do!\n")
    # Give the user time to read the tasks and status
    print("Press any key to continue...")
    msvcrt.getch()
# Add a task to the "data.txt" file
def addTask():
    task = input("Enter tasks name: ")

    with open("data.csv", "r") as f:
        if not f.read():
            with open("data.csv", "a") as writer:
                writer.write("Task,Status\n")

    # with will automatically close the file after executing
    with open("data.csv", "a") as f:
        f.write(task + ",Incomplete\n")
    return "The task has been added!"

if __name__ == "__main__":
    main()