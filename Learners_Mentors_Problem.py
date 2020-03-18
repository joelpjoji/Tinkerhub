'''THIS PROGRAM IS TO EXECUTED IN PYTHON 3'''
class Learner_Mentor:
	
    info = {}
    def addStacks(self,name):
        Stack=input("\nThe available Options are : Python, C , C++ , Java , Web \n\nEnter a Option you are Interested/Experted in: ")
        self.info[name] = [None, None, None]
        if name in self.info:
            self.info[name][0] = Stack
        return
      
    def setMentorOrLearner(self,name):
        Title = int(input("\nAre you a \n1 : Mentor\n2 : Learner\n\nEnter your choice : "))        
        if name in self.info:
            self.info[name][1] = Title
        return
        

    def setAvailableTime(self,name):
        if self.info[name][1] == 1 :
            time_available=int(input("\nEnter Your Available Time(In Hours)Per Day : ")) 
            if name in self.info:
                self.info[name][2] = time_available
        return
    
    def getMentor(self,Stack,time):
        flag = 0
        print("\nThe available Mentors are : ")
        for Mentor in self.info:
            if self.info[Mentor][0] == Stack and self.info[Mentor][2] >= time:
                print("{} ".format(Mentor))
                flag = 1
        if flag == 0:
            print("None")
        return
obj = Learner_Mentor()
while True:

	print("\n****************Welcome****************")
	print("\n1:Enter the details of a participant")
	print("\n2:Check the availablity of Mentors")
	print("\n3:Exit")
	choice = int(input("\nEnter Your Choice : "))
	if(choice == 1):
		
		name = input("\nEnter Your Name : ")
		obj.addStacks(name)
		obj.setMentorOrLearner(name)
		obj.setAvailableTime(name)
		
	elif(choice == 2):
		Stack=input("\n The available Stacks are : Python , C , C++ , Java , Web \n\n Enter The Option That You Are Interested In : ")
		time=int(input("Enter The Time That You Need (In Hours)Per Day : "))
		obj.getMentor(Stack,time)
	elif(choice == 3):
		print("\n Exiting. . . \n****************Thank You***************")
		break
	else:
		print("INVALID CHOICE !")
		
	flag = input("\nYor Details Have Been Recorded \n\n Do you want to continue (Y/N)? ")
	if(flag == 'n' or flag == 'N'):
		print("\n Exiting. . . \n****************Thank You***************")
		go = False
