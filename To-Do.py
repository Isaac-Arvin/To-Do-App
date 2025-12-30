import csv
import msvcrt
import os

# This program is a ToDo task manager
def main():
    # call choiceMade to recieve an input and match it to a function
    while (True):
        match choiceMade():
            case 1:
                addTask()
            case 2:
                viewTasks()
            case 3:
                markTaskComplete()
            case 4:
                deleteTask()
            case 5:
                return

def choiceMade():
    choice = 0
    menu = (
        "Hello! What would you like to do? \n" 
        "1. Add a new task \n" 
        "2. View Tasks \n" 
        "3. Mark a task completed \n" 
        "4. Delete a task \n" 
        "5. Close program \n"
        "Choice: ")

    while True:
        choice = input(menu)
        try:
            choice = int(choice)
        except ValueError:
            continue

        if choice in {1, 2, 3, 4, 5}:
            return choice

        clearScreen()
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
        clearScreen()
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

def markTaskComplete():
    x = 0

    while x == 0:
        lines = []  # reset each loop so you don't duplicate rows

        with open("data.csv", "r", newline='') as f:
            contents = csv.DictReader(f)

            n = 0  # number of INCOMPLETE tasks shown to the user
            for line in contents:
                if any(line.values()):
                    lines.append(line)

                if line["Status"] == "Incomplete":
                    n += 1
                    print(f"Task {n}: {line['Task']} - Status: {line['Status']}")

        if n == 0:
            clearScreen()
            print("You have nothing to do!\n")
            return

        try:
            x = int(input("What task would you like to mark complete? "))
        except ValueError:
            x = 0

        if x < 1 or x > n:
            clearScreen()
            print(f"Enter a valid option between 1 and {n}!")
            print("Press any key to continue...")
            msvcrt.getch()
            x = 0

    # Write back out, updating the x-th INCOMPLETE task
    with open("data.csv", "w", newline='') as f:
        f.write("Task,Status\n")

        incomplete_count = 0
        for value in lines:
            if value["Status"] == "Incomplete":
                incomplete_count += 1
                if incomplete_count == x:
                    value["Status"] = "Complete"

            f.write(value["Task"] + "," + value["Status"] + "\n")

def deleteTask():
    taskList = []
    n = 1
    delete = 0
    counter = 1

    with open("data.csv", "r", newline = '') as f:
        tasks = csv.DictReader(f)
        clearScreen()
        print("Which task would you like to remove? ")

        for task in tasks:
            if not task["Task"] == "Task":
                print(f"Task {counter}: {task["Task"]} - {task["Status"]}")
                taskList.append(task)
                counter += 1
        while delete < 1 or delete > len(taskList):
            try:
                delete = int(input("Choice: "))
            except:
                continue

            print("Please enter a valid response! ")

            for z in taskList:
                print(f"Task {taskList.index(z)+1}: {z["Task"]} - {z["Status"]}")

    with open("data.csv", "w") as f:
        f.write("Task,Status\n")
        for task in taskList:
            if n != delete:
                f.write(task["Task"] + "," + task["Status"] + "\n")
                n = n + 1
            else:
                n = n + 1
    print("Task deleted! Press any key to continue...")
    msvcrt.getch()

def clearScreen():
    print("\033c", end="")
    
def ensure_file(path):
    if not os.path.exists(path):
        with open(path, "w") as f:
            pass

if __name__ == "__main__":
    ensure_file("data.csv")
    main()