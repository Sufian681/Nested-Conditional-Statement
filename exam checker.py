medical = input("did you have a medical cause (y or no) : ")
attendence = int(input("enter the attendance : "))
if medical == "y" :
    print("you are allowed")
    
else :
    if attendence >= 75 :
        print("you are allowed")
        
    else : 
        print("you are not allowed")
