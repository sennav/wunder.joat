#!/usr/bin/python

import os
import json

from collections import defaultdict
from datetime import datetime

END = '\033[0m'
WHITE = '\033[37m'
GREEN = '\033[32m'


def get_color_str(text, color):
    return f'{color}{text}{END}'


def print_color(text, color):
    print(get_color_str(text, color))


def get_map_by_task_id(items):
    items_map = defaultdict(list)
    for item in items:
        task_id = item['task_id']
        items_map[task_id].append(item)
    return items_map


def get_date_from_iso_str(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%fZ')
    return date_obj.strftime("%H:%M %d-%m-%Y")


def print_task(task, subtask_map, reminder_map):
    reminders = reminder_map[task['id']]
    task_str = get_color_str(f'• {task["title"]}', WHITE)
    if 'due_date' in task:
        due_date = datetime.strptime(
            task["due_date"],
            '%Y-%m-%d'
        )
        task_str += f' - Due: [{due_date.strftime("%d-%m-%Y")}]'

    if len(reminders) > 0:
        task_str += ' Reminders: ('
    reminders_date_str = [
        get_date_from_iso_str(reminder['date']) for reminder in reminders
    ]
    task_str += ', '.join(reminders_date_str)
    if len(reminders) > 0:
        task_str += ')'
    print(task_str)

    for subtask in subtask_map[task['id']]:
        if subtask["completed"]:
            print_color(f'  √ {subtask["title"]}', GREEN)
            continue
        print(f'  • {subtask["title"]}')


def main():
    tasks_str = os.getenv('TASKS', "[]")
    subtasks_str = os.getenv('SUBTASKS', "[]")
    reminders_str = os.getenv('REMINDERS', "[]")
    tasks = json.loads(tasks_str)
    subtasks = json.loads(subtasks_str)
    reminders = json.loads(reminders_str)

    subtask_map = get_map_by_task_id(subtasks)
    reminder_map = get_map_by_task_id(reminders)
    for task in tasks:
        print_task(task, subtask_map, reminder_map)


if __name__ == '__main__':
    main()
