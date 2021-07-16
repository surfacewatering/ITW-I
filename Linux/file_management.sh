echo "        FILE AND DIRECTORY MANAGEMENT COMMANDS      "
echo "                                                    "
echo "1 --Display the contents of a file"
echo "2 --Remove a file"
echo "3 --Copy a file"
echo "4 --List a file"
echo "5 --Size of a file"
if [ "$1" == "1" ]
 then 
  echo "6 --Exit program;"
  echo ""
  echo "(THIS IS EXPERT MODE)"
else  
 echo "6 --Quit --Return to main Menu"
fi
echo ""
echo "        Enter your choice: "
read choice
while [ true ]
do
while [ $choice -ne 1 -a $choice -ne 2 -a $choice -ne 3 -a $choice -ne 4 -a $choice -ne 5 -a $choice -ne 6 ]
   do 
     echo "Enter a valid choice: "
     read choice
   done
	if [ $choice -eq 1 ]
	then
 	  echo "Enter the Path of File which you want to display contents of: "
  	  read file
  	  echo ""
  	  while [ ! -f $file  ]
   	  do 
  	      echo "Enter Valid Path: "
 	      read file
 	      echo ""
	  done  
	  cat $file
	  echo ""
	fi 
	if [ $choice -eq  2 ]
	then 
	  echo "Enter the path of file which you want to remove: " 
 	  read file
 	  echo ""
	  while [ ! -f $file1  ]
	  do 
	      echo "Enter Valid Path: "
   	  read file
   	  echo ""
   	  done  
	  rm $file
	  echo $file removed
	  echo ""
 	fi
	if [ $choice -eq 3 ]
 	then 
 	  echo "Enter the path of file which you want to copy: " 
  	  read file1
  	  echo ""
  	  while [ ! -f "$file1"  ]
  	  do 
  	      echo "Enter Valid Path: "
  	  read file1
  	  echo ""
  	  done  
  	      echo "Enter the Destination Path: "
  	  read file2
  	  echo ""
  	  while [ ! -d "$file2"  ]
  	  do 
 	      echo -n "Enter Valid Path: "
  	  read file2
  	  echo ""
  	  done  
  	  cp $file1 $file2
  	  echo "$file1 copied to $file2"
  	  echo ""
	fi 
	if [ $choice -eq  4 ]
	then 
	  echo "Enter the path of file which you want to list: "
	  read file
	  echo ""
 	  while [ ! -f $file1  ]
 	  do 
 	      echo "Enter Valid Path: "
 	  read file
 	  echo ""
 	  done  
 	  ls -l $file
 	fi
	if [ $choice -eq  5 ]
	then 
	  echo "Enter the path of file you want to display size of: "   
 	  read file
 	  echo ""
	  while [ ! -f $file1  ]
	  do 
	      echo "Enter Valid Path: "
	  read file
	  echo ""
	  done  
	  ls -sh $file | awk '{ if(NR==1) print $1 }'
	  echo ""
	 fi 
	if [ $choice -eq 6 ]
	then 
	  if [ "$1" == "1" ]
	   then 
	    echo "Exiting the file menu:"
	    exit 1
	  else
	   echo "Opening the main menu:"
	   clear
	   bash ./myhelp.sh
	   exit 1
	 fi
fi
echo "Enter your choice: "
   read choice      
done
