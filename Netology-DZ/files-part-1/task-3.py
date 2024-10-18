filenames = ["1.txt", "2.txt", "3.txt"]

files_data = dict[str, list[str]]()
for filename in filenames:
    with open(filename) as file:
        files_data[filename] = file.readlines()

with open("task-3-result.txt", "w") as file:
    for file_name in sorted(files_data, key=lambda file_name: len(files_data[file_name])):
        _ = file.write(file_name + "\n")
        _ = file.write(f"{len(files_data[file_name])}\n")
        _ = file.writelines(files_data[file_name])
