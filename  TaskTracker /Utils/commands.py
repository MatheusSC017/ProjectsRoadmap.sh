from datetime import datetime
import json


def add_task(args):
    task_tracker = read_task_tracker()

    with open("tasks.json", "w") as tasks_file:
        new_task = {
            "description": args.description,
            "status": "todo",
            "createdAt": datetime.now().isoformat(),
            "updatedAt": datetime.now().isoformat(),
        }

        new_task_id = max([int(task_id) for task_id in task_tracker.keys()]) + 1 if len(task_tracker.keys()) > 0 else 1

        task_tracker[new_task_id] = new_task
        json.dump(task_tracker, tasks_file, indent=4)
        print("Task added successfully (ID: 1)")


def update_task(args):
    task_tracker = read_task_tracker()

    if str(args.id) in task_tracker.keys():
        task_tracker[str(args.id)]["description"] = args.description
        task_tracker[str(args.id)]["updatedAt"] = datetime.now().isoformat()

        with open("tasks.json", "w") as tasks_file:
            json.dump(task_tracker, tasks_file, indent=4)

        print("Task updated successfully")
    else:
        print("Task not found")


def delete_task(args):
    task_tracker = read_task_tracker()

    if str(args.id) in task_tracker.keys():
        del task_tracker[str(args.id)]

        with open("tasks.json", "w") as tasks_file:
            json.dump(task_tracker, tasks_file, indent=4)

        print("Task deleted successfully")
    else:
        print("Task not found")


def update_status_task(args, old_status, new_status):
    task_tracker = read_task_tracker()

    if str(args.id) in task_tracker.keys():
        if task_tracker[str(args.id)]["status"] == old_status:
            task_tracker[str(args.id)]["status"] = new_status
            task_tracker[str(args.id)]["updatedAt"] = datetime.now().isoformat()

            with open("tasks.json", "w") as tasks_file:
                json.dump(task_tracker, tasks_file, indent=4)

            print(f"Task {new_status}")
        else:
            print(f"Invalid status change, only tasks in state {old_status} can be changed to {new_status}")
    else:
        print("Task not found")


def list_tasks(args):
    task_tracker = read_task_tracker()
    task_tracker = [{"id": task_id, **task_info}
                    for task_id, task_info in task_tracker.items()
                    if args.status is None or args.status == task_info["status"]]
    print("ID | Description | Status | CreatedAt | UpdatedAt")
    for task in task_tracker:
        print(f"{task['id']} | {task['description']} | {task['status']} | {task['createdAt']} | {task['updatedAt']}")


def read_task_tracker():
    try:
        with open("tasks.json", "r") as tasks_file:
            return json.load(tasks_file)
    except FileNotFoundError:
        open("tasks.json", "x")
    except json.decoder.JSONDecodeError:
        print("Task not found")
    return {}

