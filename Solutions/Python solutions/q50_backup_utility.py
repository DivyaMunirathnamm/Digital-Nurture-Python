import shutil

copied = set()

try:
    source = "sample.txt"
    destination = "backup/sample.txt"

    if source not in copied:
        shutil.copy(source, destination)
        copied.add(source)

        with open("backup.log", "a") as log:
            log.write(f"Copied {source}\n")

except FileNotFoundError:
    print("File Not Found")

except PermissionError:
    print("Permission Denied")