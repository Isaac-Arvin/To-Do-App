import csv
import msvcrt
import os

# This program is a ToDo task manager
def main():
    choice = 0
    while choice != "1" or choice != "2" or choice != "3" or choice != "4":
        choice = input("Hello! What would you like to do? \n1. Add a new task\n2. View Tasks\n3. Mark a task completed\n4. Delete a task\nChoice: ")
        if choice == "1":
            addTask()
        elif choice == "2":
            viewTasks()
        elif choice == "3":
            markTaskComplete()
        #elif choice == "4":
            #deleteTask()
        else:
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
    
def clearScreen():
    print("\033c", end="")
    
if __name__ == "__main__":
    main()