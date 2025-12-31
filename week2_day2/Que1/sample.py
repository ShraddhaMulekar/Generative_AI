with open("file.txt", "r") as file:
    content = file.readlines()
    print(content)

with open("file.txt", "w") as write_file:
    for line in content:
        if line.strip():
            write_file.write(line)
            print(line, write_file)