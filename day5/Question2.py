sub_list=[1,1,5]

listy=[1,5,6,4,1,2,3,5]

flag = 0

if(set(sub_list).issubset(set(listy))):
 
	flag = 1
	

if (flag) : 
	
	print ("It's a match") 

else : 
	
	print ("It's Gone") 
