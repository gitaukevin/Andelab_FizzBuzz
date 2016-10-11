#this defines the function find_max_min
def find_max_min(sample_data):
	Min_Number= min (sample_data) #first variable with max values of the parameter sample data
	Max_Number= max (sample_data)#secon variable with min values of the parameter sample_data
	lists=[] #lists an empty list we'll use to store our output
	if Min_Number == Max_Number:
	  return [len(sample_data)] #We return the value in case the value minimum == maximum
	else:  
	  return lists.append([Min_Number,Max_Number]) #we insert the values in the lists