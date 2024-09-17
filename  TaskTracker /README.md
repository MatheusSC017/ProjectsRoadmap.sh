# Task Tracker

Task tracker is a project used to track and manage your tasks. In this task, you will build a simple command line interface (CLI) to track what you need to do, what you have done, and what you are currently working on. This project will help you practice your programming skills, including working with the filesystem, handling user inputs, and building a simple CLI application.

Project suggested by Roadmap.sh and project description available at https://roadmap.sh/projects/task-tracker

## Basic commands

### Add task
> python3 main.py <description: string>

### Update task
> python3 main.py update <id: int> <description: string>

### Delete task
> python3 main.py delete <id: int>

## Update Status commands
For the commands below, status transitions will only be allowed for the sequence todo -> in-progress -> done

### Mark in progress a task
> python3 main.py mark-in-progress <id: int>

### Mark done a task
> python3 main.py mark-done <id: int>

## List tasks
Command to list the task, the status argument is optional and is used as a filter for the task tracker

> python main.py list <status: str(todo, in-progress, done)?>
