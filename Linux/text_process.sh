#!/bin/bash

echo "        TEXT PROCESSING COMMANDS"
echo ""
echo "1 --Search a file for a pattern"
echo "2 --Count lines, words, and characters in specified files"
echo "3 --Display line differences between two files"
if [ "$1" == "1" ]
then
	echo "4 --Quit --Exit Program"
	echo ""
	echo "(THIS IS EXPERT MODE)"
else
	echo "4 -- Quit -- Return to Main Menu"
fi
echo ""
echo "Enter your choice: "
read val
while [ true ]
do
if [ $val -eq 1 ]
then
    echo "Enter file to check for pattern: "
    read filename
    echo "Enter pattern to search for: "
    read pattern
    echo ""
    grep -E $pattern $filename
    echo ""
fi    
if [ $val -eq 2 ]
then
    echo "Enter filename for counting: "
    read filename
    echo "Number of line: "
    wc -l $filename | awk '{ print $1 }'
    echo "Number of words: "
    wc -w $filename | awk '{ print $1 }'
    echo "Number of characters: "
    wc -c $filename | awk '{ print $1 }'
    echo ""
fi    
if [ $val -eq 3 ]
then
    echo "Enter files to display line differences in: "
    read filename
    echo ""
    diff ${filename[0]} ${filename[1]}
    echo ""
fi 
if [ $val -eq 4 ]
then
	if [ "$1" == "1" ]
	then
    	echo "Exiting Program"
   	exit 1
  	else
  	echo "Opening the main menu:"
  	clear
        bash ./myhelp.sh
        exit 1
        fi
fi    
echo "Enter your choice: "
read val
done
