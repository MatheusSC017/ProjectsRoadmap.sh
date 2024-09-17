import argparse
from Utils.commands import *

commands = {
    "add": (add_task, {}),
    "update": (update_task, {}),
    "delete": (delete_task, {}),
    "mark-in-progress": (update_status_task, {"old_status": "todo", "new_status": "in-progress"}),
    "mark-done": (update_status_task, {"old_status": "in-progress", "new_status": "done"}),
    "list": (list_tasks, {})
}

description = "Task tracker is a project used to track and manage your tasks. In this task, you will build a simple " \
              "command line interface (CLI) to track what you need to do, what you have done, and what you are " \
              "currently working on. This project will help you practice your programming skills, including working " \
              "with the filesystem, handling user inputs, and building a simple CLI application."

parser = argparse.ArgumentParser(prog="Task Tracker",
                                 description=description)
sub_parsers = parser.add_subparsers(dest="action")

add_task_sub_command = sub_parsers.add_parser("add", help="Add a new task")
add_task_sub_command.add_argument("description", type=str, help="Description of the task")

update_task_sub_command = sub_parsers.add_parser("update", help="Add a new task")
update_task_sub_command.add_argument("id", type=int, help="ID of the task")
update_task_sub_command.add_argument("description", type=str, help="Description of the task")

delete_task_sub_command = sub_parsers.add_parser("delete", help="Add a new task")
delete_task_sub_command.add_argument("id", type=int, help="ID of the task")

mark_in_progres_task_sub_command = sub_parsers.add_parser("mark-in-progress", help="Mark the task as in progress")
mark_in_progres_task_sub_command.add_argument("id", type=int, help="ID of the task")

mark_done_task_sub_command = sub_parsers.add_parser("mark-done", help="Mark the task as done")
mark_done_task_sub_command.add_argument("id", type=int, help="ID of the task")

list_tasks_sub_command = sub_parsers.add_parser("list", help="List the tasks")
list_tasks_sub_command.add_argument("status",
                                    type=str,
                                    nargs="?",
                                    choices=["todo", "in-progress", "done"],
                                    default=None,
                                    help="Status of the tasks to search")

args = parser.parse_args()
try:
    commands[args.action][0](args, **commands[args.action][1])
except Exception as e:
    print(f"An error occurred in the action {args.action}: {e}")
