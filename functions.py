FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """
    This function opens todo file and puts into list

    get_todos(...)
    :param filepath:
    :return:
    """
    # Old version which is not safer method
    # In case of error, it may not close the file
    # file = open("files/todos.txt", "r")
    # todos = file.readlines()
    # file.close()
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """
    This function writes todo items into todos file

    write_todos(...)
    :param todos_arg:
    :param filepath:
    """
    # Old version which is not safer method
    # In case of error, it may not close the file
    # file = open("files/todos.txt", "w")
    # file.writelines(todos)
    # file.close()

    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print(get_todos())
