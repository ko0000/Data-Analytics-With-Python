#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 22:49:42 2023

@author: ko
"""

from sys import argv

class Project:
    def __init__(self, x):
        self.x = open(x, encoding= "UTF-8") 
    
    def max(q):
        maxiu= q[0]
        for x in q:
            if x >= maxiu:
                maxiu = x
            else:
                pass
        return maxiu
        
    def min(q):
        mini= q[0]
        for x in q:
            if x <= mini:
                mini = x
            else:
                pass
        return mini
    
    def aver(q):
        total = 0
        for x in q:
            total = total + int(x)
        averg = int(total)/len(q) 
        return averg    
    
def main():
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
    }
    covtype = open("./project/covtype.data", encoding="UTF-8")
    for x in covtype:
        y=x.strip().split(",")
        z=0
        for c in Data.keys():
            Data[c].append(y[z])
            if z <10:
                z=z+1
            else:
                pass
        if y[10]==1:
            
            
        elif y[11]==1:
            
        elif y[12]==1:
            
        elif y[13]==1:
    covtype.close()
    
    for c in Data.keys():
        print(c)
        print("MAX", max(Data[c]))
        print("Min", min(Data[c]))
        print("Average", aver(Data[c]))

if __name__ == "__main__":
    main()   

    
print(AREAS[1])

    
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