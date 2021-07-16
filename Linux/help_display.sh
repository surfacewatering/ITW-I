#!/bin/bash

printf "\t\t      UNIX PROJECT\n
\t\tUNIX Shell Programming\n
For performing a particular task, enter the given values\n 
In File Management you use various commands like cp, cat, ls, etc.\n
In Text Processing you use commands like grep, diff, wc.\n
In System Status Menu you use commands like ps, df, date, printenv.\n\n
Name		: Nikita Singh
Branch		: Computer Science and Engineering
Roll number	: 20075060
Email		: nikita.singh.cse20@itbhu.ac.in
Date		: 03/06/21\n\n
\t\tPress any key to go back to main program \n"
read value
clear
bash ./myhelp.sh $1
