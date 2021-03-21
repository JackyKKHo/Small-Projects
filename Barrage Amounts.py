# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 17:26:39 2021

@author: Jacky
"""

import numpy as np
   
import time
import random
 
Displayed: while loops, using for loops in a list
Modularising functions
Evaluation of time

def Barrage_Amnt(Max,Spawns,Hp,n=10000):
   start = time.time() 
   Number = [] 
   def Stack(Max,Spawns,Hp):
       count = 0
       Stack_hp = [Hp]*Spawns #A stack of monsters with full hitpoints
       while sum(Stack_hp) != 0: #While the stack still has alive monsters 
           Damage = np.random.randint(0,(Max+1),len(Stack_hp)) #roll a hit for each spawn 
           Stack_hp = [max(i,0) for i in (Stack_hp - Damage)] #
           count += 1
       Number.append(count)
    
   for i in range(n):
        Stack(Max,Spawns,Hp)
   end = time.time()
   print("Amount of Barrages per Monster is:", np.mean(Number)/Spawns)
   print(f"Runtime of the program is {end - start}")
  
   
   
Barrage_Amnt(30,8,120)
 


       

#Situation for more than 9 spawns, at most 9 can be targeted at a time.
def Barrage_BigAmnt(Max,Spawns,Hp,n=100):  
 start = time.time()
 Number = []  
 def BigStack(Max,Spawns,Hp):  #Modularise function #this one has an extra loop. rmeove if possible
  
      count = -1 
      Stack_Hp = [Hp]*Spawns 
      while Stack_Hp != []:
     
        Damage =  np.random.randint(0,(Max+1),min(9,len(Stack_Hp))) #Roll Damage for up to 9 targets, or less if there are less than 9 alive.
        Targets =random.sample(range(min(Spawns,len(Stack_Hp))),min(9,len(Stack_Hp))) #Chooses which targets.
        for i in range(len(Targets)):
         Stack_Hp[Targets[i]] = (Stack_Hp[Targets[i]]-Damage[i]) 


        for item in Stack_Hp: #Removes any monsters with less than 0 hp.
         if item <=0:
             Stack_Hp.remove(item)
        count +=1            
     
      Number.append(count)   #Check for how many barrages to kill the stack.


 for i in range(n):
        BigStack(Max,Spawns,Hp)
 end = time.time()   
 print("Amount of Barrages per Monster is:", np.mean(Number)/Spawns)
 print(f"Runtime of the program is {end - start}")
Smokes

Barrage_BigAmnt(43,12,185,1000)

  Greater nech:
       Barrage_BigAmnt(43,7,205,10000)
       Barrage_Amnt(43,7,205,10000)
 
   Dust devil:
       Barrage_BigAmnt(43,8,105,1000)
       Barrage_Amnt(43,8,105,100000)
      
#Need to check why the two formulas give different answers       

#extensions:  add dart dps
#any other dynamic situations like death spawns
   
 
       
  