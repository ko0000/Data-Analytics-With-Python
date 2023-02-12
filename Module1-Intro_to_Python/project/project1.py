#!/usr/bin/env python3 type, parameter, data type method and what they do and what they return. 
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 22:49:42 2023
Title; Project1
@author: Itsuhiro ko
Course: AFS505
----------
Usage: python project1.py <PATH to covtype.data>
----------
Output: report_stat.txt 
    This output file contains the Max, min and Average numbers of each column in the data.
    Then, the same statistic for individual wilderness area is appended
"""


from sys import argv  #this allow the commandline input of the file

"""
  There are two global variable(dic): AREAS and COLUMNS
"""

AREAS = {
    0: 'All',
    1: 'Rawah Wilderness Area',
    2: 'Neota Wilderness Area',
    3: 'Comanche Peak Wilderness Area',
    4: 'Cache la Poudre Wilderness Area'
}

COLUMNS = {
    0: 'Elevation',
    1: 'Aspect',
    2: 'Slope',
    3: 'Horizontal_Distance_To_Hydrology',
    4: 'Vertical_Distance_To_Hydrology',
    5: 'Horizontal_Distance_To_Roadways',
    6: 'Hillshade_9am',
    7: 'Hillshade_Noon',
    8: 'Hillshade_3pm',
    9: 'Horizontal_Distance_To_Fire_Points'
}

"""
The following three functions are only used for calculating the status in the entire dataset input. 
For each wilderness area statistics, the code is different. 
"""

def get_max(q):
    """ 
    The "get_max" fucntion is used for geting the maximum value from a list of number

    Parameters
    ----------
    q : a list of number. The number can be string. This function will covert the string into int

    Returns
    -------
    maxiu: This is the maximum value from the list of number

    """
    maxiu= q[0]
    for x in q:
        if int(x) >= maxiu:
            maxiu = int(x)
    return maxiu
    
def get_min(q):
    """ 
    The "get_min" fucntion is used for geting the minimum value from a list of number

    Parameters
    ----------
    q : a list of number. The number can be string. This function will covert the string into int

    Returns
    -------
    mini: This is the minimum value from the list of number

    """
    mini= q[0]
    for x in q:
        if x <= mini:
            mini = x
        else:
            pass
    return mini

def get_aver(q):
    """ 
    The "get_aver" fucntion is used for geting the mean value from a list of number

    Parameters
    ----------
    q : a list of number. The number can be string. This function will covert the string into int

    Returns
    -------
    averg: This is the mean value of the list of number

    """
    total = 0
    for x in q:
        total = total + int(x)
    averg = int(total)/len(q) 
    return averg    
    
def main():
    """ 
    The "main" fucntion is: 1, geting the value from the first 10 column in the input file and sorted into a list
    2, getting the max, min, and mean value of the first 10 column for each wilderness area. Indicated in column 11-14
    
    Parameters
    ----------
    argv : a csv file input by the user

    Output
    ----------
    report_stat.txt:
        
    This output file will be created in the same working folder. 
    The first part of the file contains the Max, min and Average numbers of each column in the data.
    Then, the same statistic for individual wilderness area is appended

    """
    Data={
          "Elevation":[], 
          "Aspect":[],
          "Slope":[],
    "Horizontal_Distance_To_Hydrology":[],
    "Vertical_Distance_To_Hydrology":[],
    "Horizontal_Distance_To_Roadways":[],
    "Hillshade_9am":[],
    "Hillshade_Noon":[],
    "Hillshade_3pm":[],
    "Horizontal_Distance_To_Fire_Points":[],
    }  # a list of each coumn in the data were created
    
    covtype = open(argv[1]) #user input file is given here
    my_file1 = open("report_stats.txt", "w")  #the output file is created and opened
    #for loop reads the input file line by line and split the each line value by ","into a list
    for line in covtype:
        column=line.strip().split(",")
        z=0
        # In the next for loop, each column data is appended into the DATA list
        for key in Data.keys():
            Data[key].append(float(column[z]))
            #the following if statement is to make sure that the code only get first 10 column.
            #this is not nessasary, but it is part of my logic when making this code. 
            if z <10:
                z=z+1
    # this for loop loops over each column of the DATA list, and then using the get_max get_min, and get_aver functions made above
    #to get the statictics of each coumn in the inputdata
    for value in Data.keys():
        print('─' * 50, "All", '─' * 28, "\n",\
              value, "\n", \
              "Max:", get_max(Data[value]),"\n",\
                  "Min:", get_min(Data[value]),"\n",\
                      "Average", get_aver(Data[value]),"\n", file= my_file1)
    my_file1.close()
    
    
    """
    This is the second part of the main function
    In this part, each wilderness area statistics were calculated and output into the same output file
    """
    
    my_file1 = open("report_stats.txt", "a")
    for area in AREAS.keys():
        #exclude the "0:"ALL"" to prevent any error in this code
        if area != 0:
            #print the name of each wilderness area to the output file
            print('─' * 50, AREAS[area], '─' * 28, file= my_file1) 
            #Then looping over the 10 column of input data
            for col in COLUMNS.keys():
                # defining the "big" for max value in each column of data, "small" for min value, 
                #math" for sum, "number_line" track the number of line that belongs to the single area
                # big is negative infinity, small is positive infinity
                big = float('-inf')  
                small = float('inf')
                math = 0
                number_line = 0
                #return the readline to the first line
                covtype.seek(0)
                #looping over the covtype data row by row
                for line in covtype:
                    #saperate each line into column list of number
                    column=line.strip().split(",")
                    #defining the column that indicates the area code. area code start at column 11
                    that_col=int(area) + 9
                    # if the area code col is 1, then we want to keep working on this data. if not, move on to next row
                    if float(column[int(that_col)])==1:
                        #counting the number of row belong to this area
                        number_line = number_line + 1
                        #change the list item from str to float
                        item = float(column[col])
                        #if the list item is large, then "big" variable will be substituted with the new number(item)
                        if item >big:
                            big = item
                        #if small ....    
                        if item <small:
                            small = item
                        # this sum up all the item number in the designated area
                        math = math + item
                    else:
                        continue
                # this line is to avoid the "Division by zero error"
                if number_line==0:
                    continue
                else:
                    mean= math / number_line #doing the average math
                    # then print out the title of the column, max,min,average number
                    #then looping to the next column 
                    print(COLUMNS[col], "\n",\
                          "MAX",big, "\n",\
                          "Min",small, "\n",\
                          "Average", mean, "\n",\
                          file= my_file1)
                          
    covtype.close()
    my_file1.close()

# this if statement ensures that when the user used this script, the script will run the main fucntion, without creating any global variable
if __name__ == "__main__":
    main()   




    


