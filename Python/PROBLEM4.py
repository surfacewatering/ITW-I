#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Name:                   Nikita Singh
#Roll Number:            20075060
#Branch and section:     CSE Btech BA1
#Email:                  nikita.singh.cse20@itbhu.ac.in

                                     #PROBLEM 4

import pickle
import os
print('\t\tWelcome to Address Book\n1. Add_contact\n2. Display_contact\n3. Delete_contact\n4. Modify_contact\n5. Search_contact')
n=int(input('\nEnter choice(press 0 to exit): '))

def pickleinsert():
    with open('contacts.pickle','wb') as file:
        pickle.dump(contactlist,file,protocol=pickle.HIGHEST_PROTOCOL)
        
def pickleloadtolist():                   #list of dictionaries having values:name,email,phone
    file=open('contacts.pickle','rb')
    li=[]
    if(os.path.getsize('contacts.pickle')>0):
        li=pickle.load(file)
    return li

contactlist=[]
contactlist=pickleloadtolist()          
pickleinsert()

while n!=0:             
    if n==1:
        name=input('Enter contact name for insertion: ')
        email=input('Enter contact email: ')
        phone=int(input('Enter contact number: '))
        contactdet={'name':name,'email':email,'phone':phone}
        contactlist.append(contactdet)
        pickleinsert()
        print('\nContact successfully added.')
        
    elif n==2:
        contactlist=pickleloadtolist()
        if len(contactlist)!=0:
            for i in contactlist:
                print(f"\nName: {i['name']}\nEmail: {i['email']}\nContact Number: {i['phone']}")
        else:
            print('No such contact in address book.')
            
    elif n==3:
        contactlist=pickleloadtolist()
        if len(contactlist)==0:
            print('Address book empty. No contact to delete')
        else:
            val=input('Enter contact name: ')
            for i in contactlist:
                if i['name']==val:
                    contactlist.remove(i)
                    print('Contact Successfully Deleted.')
                    pickleinsert()
                    break
            else:
                print('No contact with this name to delete.')
                
    elif n==4:
        contactlist=pickleloadtolist()
        if len(contactlist)==0:
            print('Address book empty. No contact to modify')
        else:
            val=input('Enter contact name for modification: ')
            for i in range(len(contactlist)):
                if contactlist[i]['name']==val:
                    name_=input('Enter new name: ')
                    email_=input('Enter new email: ')
                    phone_=int(input('Enter new number: '))
                    contactdet={'name':name_,'email':email_,'phone':phone_}
                    contactlist[i]=contactdet
                    print('\nContact modified.')
                    pickleinsert()
                    break
            else:
                print('No contact with this name found')
                
    elif n==5:
        contactlist=pickleloadtolist()
        if len(contactlist)==0:
            print('Address book empty. No contact to search for.')
        else:
            val=input('Enter contact name to search for: ')
            for i in range(len(contactlist)):
                if contactlist[i]['name']==val:
                    print('Name: ',contactlist[i]['name'])
                    print('Email: ',contactlist[i]['email'])
                    print('Contact Number:',contactlist[i]['phone'])
                    break
            else:
                print('No contact with this name found')
        
    else:
        print('Invalid choice.')
    n=int(input('\nEnter choice: '))
print('\nGoodBye!')    


# In[ ]:




