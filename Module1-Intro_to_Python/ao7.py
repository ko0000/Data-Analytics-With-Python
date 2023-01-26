# Open the iris_data.csv file. It is in the data folder.
iris_file = open("iris.data")

# Read the first two lines of the Iris dataset and print them.
header = iris_file.readline()
row1 = iris_file.readline()

# Chop the line using the comma.
sepal_length, sepal_width, petal_length, petal_width, species = row1.strip().split(",")

# Now we can use the variables to print a formatted string.
print("Species: {}. Sepal length x width = {}cm x {}cm. Petal length x width = {}cm x {}cm.".format(species, sepal_length, sepal_width, petal_length, petal_width))

# Close the file.
iris_file.close()
