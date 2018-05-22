#2018 budget sheet
import os

class Budget:
	#private variables
	total_spendings = 0	#total spendings private variable
	budget = 0	#amount I can spend after spendings
	my_dict = {}	#dictionary for sheet. ex: acen: mcdonalds: 5.08

	def __init__(self, user_init_budget):
		self.initial_budget = user_init_budget

	def get_initial_budget(self):
		print("Your initial budget was: $" + repr(self.initial_budget) + "\n")

	def get_total_spendings(self):
		print("===TOTAL SPENDINGS===")
		for key in self.my_dict:
			amount_spent_for_key = 0
			for v in self.my_dict[key]:
				amount_spent_for_key += float(self.my_dict[key][v])
			print(key + ": $" + repr(round(amount_spent_for_key, 2)))
		print("Your total spending is: $" + repr(self.total_spendings) + "\n")
		
	def get_budget(self):
		print("===AMOUNT YOU HAVE LEFT===")
		leftover = float(self.initial_budget) - self.total_spendings
		print(leftover)
		print("")

	def read_file(self, user_sheet):
		text_file = []
		if not os.path.exists(user_sheet):
			print("Creating new sheet...")
			new_sheet = open(user_sheet, 'w')

		else:
			with open(user_sheet, "r") as f:
				text_file = f.read()
				text_file = text_file.split("\n")
		return text_file

		
	def set_dict(self, sheet_content):
		print("")
		if len(sheet_content) == 0:
			print("Theres nothing on this sheet!")
		else:
			for i in sheet_content:
				temp = []
				temp = i.split(" ")
				print(temp) #fixme: delete this after this function is perfect
				self.total_spendings += float(temp[2])
				if temp[0] not in self.my_dict:
					self.my_dict[temp[0]] = {}
					self.my_dict[temp[0]][temp[1]] = temp[2]
				elif temp[0] in self.my_dict and temp[1] in self.my_dict[temp[0]]: #fixme: how to i add acen hotel 57 and acen hotel 2 together?
					total = self.my_dict[temp[0]][temp[1]]
					total = float(total) + float(temp[2])
					self.my_dict[temp[0]][temp[1]] = repr(total)
				else:
					self.my_dict[temp[0]][temp[1]] = temp[2]

	def print_results(self):
		print("===HISTORY===")
		for key in self.my_dict:
			print("***" + key + "***")
			for value in self.my_dict[key]:
				print(value + ": $" + self.my_dict[key][value])
			print("")
		self.get_total_spendings()
		self.get_budget()

	def add_event(self, user_sheet):
		usr_event = raw_input("Please type in the title of the event, the reason for spending, and the amount you spent.\n(ex: chicago burger 8.50)\n")
		event_divided = []
		event_divided = usr_event.split(" ")
		if len(event_divided) == 3:
			with open(user_sheet, "a") as f:
				if os.stat(user_sheet).st_size == 0: #how to fix this
					f.write(usr_event)
				else:
					f.write("\n" + usr_event)
			print("Succesfully updated your sheet.")
		else:
			print("Sorry! incorrect format!")



#main:
print("\n***********SUMMER BUDGET SHEET!!!!!*************\n")

#set initial budget and call Budget class
num = 1
while num == 1:
	user_init_budget = raw_input("What is your total budget? \n")
	try:
		val = int(user_init_budget)
		num = 2
		b = Budget(user_init_budget)
		b.get_initial_budget()
	except ValueError:
		print("Please type in a number!")
		num = 1
#read user given sheet
user_sheet = raw_input("What is the name of your budget sheet? (ex: sheet.txt)\n")
sheet_content = b.read_file(user_sheet)
if not sheet_content:
	print(user_sheet + " is empty!\n")
else:
	b.set_dict(sheet_content)
	b.print_results()

#allow user to log more information
repeat = 'h'
while repeat != 'n':
	usr_decision = raw_input("Would you like to log a spending event? (y or n)\n")
	if usr_decision == 'y':
		b.add_event(user_sheet)
	elif usr_decision == 'n':
		print("Thank you for using the budget sheet!!!!!\n")
		repeat = 'n'
	else:
		print("That is an incorrect option!")



print("\n**********************************************************\n")