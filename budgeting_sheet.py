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
		for key, value in self.my_dict.iteritems():
			amount_spent_for_key = 0
			for v in value:
				amount_spent_for_key += float(value[v])
			print(key + ": $" + repr(amount_spent_for_key))
		print("Your total spending is: $" + repr(self.total_spendings) + "\n")
		
	def get_budget(self):
		print("===AMOUNT YOU HAVE LEFT===")
		leftover = float(self.initial_budget) - self.total_spendings
		print(leftover)
		print("")

	def read_file(self, user_sheet):
		text_file = []
		with open(user_sheet, "r") as f:
			text_file = f.read()
			text_file = text_file.split("\n")
		return text_file

		
	def set_dict(self, sheet_content):
		print("")
		for i in sheet_content:
			temp = []
			temp = i.split(" ")
			print(temp) #fixme: delete this after this function is perfect
			self.total_spendings += float(temp[2])
			if temp[0] not in self.my_dict:
				self.my_dict[temp[0]] = {}
				self.my_dict[temp[0]][temp[1]] = temp[2]
			elif temp[0] in self.my_dict and temp[1] in self.my_dict: #fixme: how to i add acen hotel 57 and acen hotel 2 together?
				self.my_dict[temp[0]][temp[1]] += temp[2]
			else:
				self.my_dict[temp[0]][temp[1]] = temp[2]

	def print_results(self):
		print("===HISTORY===")
		for key, value in self.my_dict.iteritems():
			print(key + ":")
			print value
			print("")
		self.get_total_spendings()
		self.get_budget()

#main:
print("\n***********SUMMER BUDGET SHEET!!!!!*************\n")

#set initial budget and call Budget class
user_init_budget = raw_input("What is your total budget? \n")
b = Budget(user_init_budget)
b.get_initial_budget()
#read user given sheet
user_sheet = raw_input("What is the name of your budget sheet? \n")
sheet_content = b.read_file(user_sheet)
b.set_dict(sheet_content)
#spit out results
b.print_results()


print("\n**********************************************************\n")