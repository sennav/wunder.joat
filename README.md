# Wunder CLI

Config files for a joat based cli, you don't know what is joat? 😱
get your shit together and go [read about joat!](https://github.com/sennav/joat)

## Instalation

```
joat install sennav/wunder.joat
```

Or just clone this repo in your home folder with under the folder `.wunder.joat` and create a symlink in your path name `wunder` pointing to your `joat` binary.

## Usage

It's used like a regular CLI, here's the help with the commands:

```
wunder 0.0.0 (joat 0.0.1)
Your Name <your@email.com>
Describe your extension

USAGE:
    wunder [SUBCOMMAND]

FLAGS:
    -h, --help       Prints help information
    -V, --version    Prints version information

SUBCOMMANDS:
    auto_complete     Create auto complete script
    create_subtask    perform a subtask request
    create_task       perform a create task request (POST)
    done              mark a task as done
    help              Prints this message or the help of the given subcommand(s)
    list              get list by name
    list_id           get list by id
    lists             get lists
    subtask           create a subtask
    subtasks          list subtasks
    tasks             get tasks for list
    tasks_id          get tasks by list id
    todo              create a task
    undo              unmark a task as done
    update_task       update a task (PATCH)

```

## Config

You need to set the following environment variables:
* `WUNDER_CLIENT_ID` - your wunderlist client id, google how to get one :)
* `WUNDER_CLIENT_SECRET` - your wunderlist client secret, google how to get one :)
* `WUNDER_LIST_ID` - optionally you can define a default todo list to work on.
