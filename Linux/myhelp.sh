EXPERTorNO=1
if [ "$#" -eq "0" ]
  then
  	EXPERTorNO=0
  	 printf "         UNIX HELP MAIN MENU\n
 	                                      
1 --File and Directory Management Commands\n
2 --Text Processing Commands\n
3 --System Status Commands\n
4 --Exit
 	                                      
 	 Enter your choice:\n"
 	 read choice
 		 while [ $choice -ne 1 -a $choice -ne 2 -a $choice -ne 3 -a $choice -ne 4 ]
 		  do
 		    echo "Enter a valid choice: "
 		    read choice
 		  done
 	 if [ $choice -eq 1 ]
   	 then
 	   echo "Opening the File management commands sub-menu "
 	   clear
 	   bash ./file_management.sh $EXPERTorNO
 	 elif [ $choice -eq 2 ]
 	 then
 	   echo "Opening the Text Processing commands sub-menu "
 	   clear
 	   bash ./text_process.sh $EXPERTorNO
 	 elif [ $choice -eq 3 ]
 	 then
     	   echo "Opening the System Status commands sub-menu "
  	   clear
  	   bash ./system_status.sh $EXPERTorNO
 	 else
 	   echo "Exiting the program"
 	   exit 1
	 fi
elif [ "$1" != "help" -a "$1" != "status" -a "$1" != "text" -a "$1" != "file" ]
 then
  	 echo "Enter a valid argument"
  	 echo "Exiting the Program"
  	 exit 1
elif [ "$1" == "file" ]
 then
    	 echo "Opening the File management commands sub-menu "
   	 clear
   	 bash ./file_management.sh $EXPERTorNO
elif [ "$1" == "text" ]
 then
  	 echo "Opening the Text Processing commands sub-menu "
  	 clear
  	 bash ./text_process.sh $EXPERTorNO
elif [ "$1" == "status" ]
 then
  	 echo "Opening the System Status commands sub-menu "
  	 clear
  	 bash ./system_status.sh $EXPERTorNO
elif [ "$1" == "help" ]
 then
  	 echo "About the program"
 	 clear
  	 bash ./help_display.sh
fi
