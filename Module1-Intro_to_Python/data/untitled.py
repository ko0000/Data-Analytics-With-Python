from sys import argv
name, files = argv
def get_next_line(x):
    file=open(x, encoding="UTF-8")
    line1=file.read()
    key, value = line1[2].split("=")
    print(key)
get_next_line(files)