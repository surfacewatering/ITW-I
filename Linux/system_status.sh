#!/bin/bash

echo "        SYSTEM STATUS COMMANDS"
echo ""
echo "1 --Display the current date and time"
echo "2 --Current disk usage"
echo "3 --List current local and enviornmental"
echo "4 --Display process status information"
if [ "$1" == "1" ]
then
	echo "5 --Exit Program"
	echo ""
	echo "(THIS IS EXPERT MODE)"
else
	echo "5 --Quit --Return to Main Menu"
fi	
echo ""
echo "        Enter your choice: "
read ch
while [ true ]
do
     while [ $ch -ne 1 -a $ch -ne 2 -a $ch -ne 3 -a $ch -ne 4 -a $ch -ne 5 ]
    	do 
    	echo "Enter a valid choice: "
     	read ch
     done
if [ $ch -eq 1 ]
then
    printf "\n"
    date +"%d/%h/%Y %R"
    printf "\n"
fi    
if [ $ch -eq 2 ]
then
    printf "\n"
    df
    printf "\n"
fi 
if [ $ch -eq 3 ]
then
     printf "\n"
     printenv
     printf "\n"
fi
if [ $ch -eq 4 ]
then
    printf "\n"
    ps -e
    printf "\n"
fi
if [ $ch -eq 5 ]
then
    if [ "$1" == "1" ]
    then
    	echo "Exiting system menu"
    	exit 1
    else
    	clear
    	echo "Opening the main menu:"
    	bash ./myhelp.sh
    	exit 1
    fi
fi
echo "Enter your choice: "
	read ch
done
