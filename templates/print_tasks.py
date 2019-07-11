#!/usr/bin/python

import os
import json

from collections import defaultdict

END = '\033[0m'
WHITE = '\033[37m'
GREEN = '\033[32m'


def print_color(text, color):
    print(f'{color}{text}{END}')


def get_subtask_map(subtasks):
    subtasks_map = defaultdict(list)
    for subtask in subtasks:
        task_id = subtask['task_id']
        subtasks_map[task_id].append(subtask)
    return subtasks_map


def main():
    tasks_str = os.getenv('TASKS')
    subtasks_str = os.getenv('SUBTASKS')
    tasks = json.loads(tasks_str)
    subtasks = json.loads(subtasks_str)

    subtask_map = get_subtask_map(subtasks)

    for task in tasks:
        print_color(f'• {task["title"]}', WHITE)
        for subtask in subtask_map[task['id']]:
            if subtask["completed"]:
                print_color(f'  √ {subtask["title"]}', GREEN)
                continue
            print(f'  • {subtask["title"]}')


if __name__ == '__main__':
    main()
