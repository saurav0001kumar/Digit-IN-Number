# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 18:30:48 2019

@author: SK
"""

n=int(input("\n-> Enter a number :"))
temp=n
print("\n-> Enter a digit to be counted in ",n," : ",end=" ")
d=int(input())
count=0
while n>0:
    if (n%10)==d:
        count+=1
    n=n//10
print("\n-> Occurence of digit ",d," in the number ",temp," is ",count," .")


input("\n\nPress Enter key to exit.")


    
