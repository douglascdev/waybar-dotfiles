import sys
from pathlib import Path

todolist = Path("/home/douglas/.config/waybar/todolist")
match sys.argv[1]:
    case "new":
        with open(todolist, "w") as file:
            tasks = input("Tasks for today(comma separated): ").split(",")
            file.writelines([f'{t}\n' for t in tasks])
    case "pop":
        with open(todolist, "r+") as file:
            file.seek(0)
            tasks = file.read().splitlines()
            if len(tasks) > 0:
                tasks.pop(0)
            file.seek(0)
            for t in tasks:
                file.write(f'{t}\n')
            file.truncate()
    case "status":
        with open(todolist) as file:
            tasks = file.read().splitlines()
            if len(tasks) == 0:
                print("✔  All done!")
            else:
                print(f"🛠 {tasks[0]}")



