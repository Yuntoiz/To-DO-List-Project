import json

DATA_DIRECTORY = 'data'

def load_json(name):
    """ This loads a JSON file from the directory told to."""
    with open(f"{DATA_DIRECTORY}/{name}.json", "r") as f:
        tasks = json.load(f)
    return tasks


def save_json(name=None, data=None):
    """This saves data to a JSON file in the directory commanded to."""
    with open(f"{DATA_DIRECTORY}/{name}.json", "w") as f:
        json.dump(data, f)
    return True


def search(sorted_tasks, search_key):
    """Searches for tasks that match the specified search key."""
    results = []
    for task in sorted_tasks:
        for value in task.values():
            if search_key in str(value):
                results.append(task)
                break
    return results
