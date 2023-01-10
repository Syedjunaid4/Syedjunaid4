# Python3 program to print the season
# name based on the month number
def findseason (M) :
	
	# Taken all the possible
	# month numbers in the list.
	list1 = [[12 , 1 , 2], [3 , 4 , 5],
			[6 , 7 , 8], [9 , 10 , 11]]
			
	# Matching the month number
	# with the above list entries
	if M in list1[0] :
		print ( "WINTER" )
	elif M in list1[1] :
		print ( "SPRING" )
	elif M in list1[2] :
		print ( "SUMMER" )
	elif M in list1[3] :
		print ( "AUTUMN" )
	else :
		print ( "Invalid Month Number" )

# Driver Code
M = 5
print("For Month number:", M);
findseason ( M )

M = 10
print("For Month number:", M);
findseason ( M )

# This code is contributed by Abhishek
