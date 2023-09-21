#Author: Jonathan Bankston
#KUID: 3097029
#Date: 2/16/23
#Lab: lab03
#Last modified: 2/17/23
#Purpose: This program finds out how many people are sick over a certain amount of days

def sick_ppl(days):
    d1, d2, d3 = 1, 5, 17
    count = 3
    if days <= 0:
        return "You cannot input less than 1 day"
    elif days == 1:
        return d1
    elif days == 2:
        return d2
    elif days == 3:
        return d3
    else:
        while count < days:
            more_days = d1 + d2 + d3
            d1 = d2
            d2 = d3
            d3 = more_days
            count = count + 1
        return more_days
  
print('THERES AN OUTBREAK!')

num_day = int(input('What day would you like a sick count for: '))
ans = sick_ppl(num_day)
if ans != "You cannont input less than 1 day":
  print(f"Total people with flu: {ans}")
else:
  print("You cannot input less than 1 day")

    


    
    

