from sys import argv

script, file, destination = argv

files = open(file).read()

ain = open(destination, "w")

ain.write(files)


destination.close()
