#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Name:                   Nikita Singh
#Roll Number:            20075060
#Branch and section:     CSE Btech BA1
#Email:                  nikita.singh.cse20@itbhu.ac.in

                                     #PROBLEM 3

import pandas as pd
val={'ITEM': ['Chicken Strips','French Fries','Hamburger',
                         'Hotdog','Large Drink','Medium Drink',
                         'Milk Shake','Salad','Small Drink'] , 
                'PRICE(in $)': [3.50,2.50,4.00,3.50,1.75,
                          1.50,2.25,3.75,1.25]}

df=pd.DataFrame(val)
df.index+=1

print('Menu:','\n')
print(df,'\n')

while(True):
    s=input('Place order (press 0 to exit): ')
    if s=='0':
        break  
    elif s.isnumeric()==False:
        print('Invalid Input. Enter again.')
        continue
    add=0   
    li=[0,0,0,0,0,0,0,0,0]
    
    print("\nYour order list: ")
    
    for i in s:
        li[int(i)-1]+=1
        add+=df.loc[int(i),['PRICE(in $)']]
        
    for i in range(9):
        if li[i]!=0:
            print(f"{i+1} {val['ITEM'][i]} \t$({val['PRICE(in $)'][i]} X {li[i]})")
            
    print('\nYour order costs: $',*add,'\n',sep='')  
    
print('Hope you enjoyed your meal, have a great day!')


# In[ ]:





# In[ ]:




