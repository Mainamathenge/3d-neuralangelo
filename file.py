with open("requirements.txt") as file, open("requirements1.txt", "w") as file1:
    for line in file:
        if "tiny-cuda-nn" in line:
            continue
        file1.write(line)

