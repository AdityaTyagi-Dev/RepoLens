from pathlib import Path

class DirectoryNotFound(Exception):
    pass

def check_items(path):
    if not (path and path.is_dir()):
        raise DirectoryNotFound("Directory path is not correct")
    
    directories = []
    files = []

    for item in path.rglob("*"):
        if item.is_dir():
            directories.append(str(item))

        elif item.is_file():
            files.append(str(item))

    output = {
        "directory" : directories,
        "file" : files
    }
    return output

if __name__ == "__main__":
    print(check_items(Path(input("Enter the path: "))))