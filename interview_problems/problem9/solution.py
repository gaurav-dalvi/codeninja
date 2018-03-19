from datetime import datetime

class Customer(object):

	def __init__(self,date, id, event):
		self.date = date
		self.id = id
		self.event = event

	def print_customer(self):
		print self.date, self.id, self.event

def parse_file(data):
	temp = []
	for line in data:
		temp.append(line.split(','))

	customers = []
	for i in xrange(len(temp)):
		cdate = datetime.strptime(temp[i][0] , '%Y-%m-%d').date()
		c = Customer(cdate, temp[i][1], temp[i][2])
		customers.append(c)
	
	return customers

def purchase_older_90days(person, customer_map):

	count = 0
	purchase_array = customer_map[person.id][1]
	for i in xrange(len(purchase_array)):
		if abs((person.date - purchase_array[i]).days) > 90:
			count += 1
	return count


def solution(customers):
	
	customer_map = {}
	for person in customers:
		if person.event == 'FRAUD_REPORT':
			if person.id not in customer_map.keys():
				customer_map[person.id] = [[person.date],[]]
			else:
				temp = customer_map[person.id]
				temp[0].append(person.date)
		else: # event is PURCHASE

			# if there is no history
			if person.id not in customer_map.keys():
				customer_map[person.id] = [[], [person.date]]
				print person.date.strftime('%Y-%m-%d') + ',' + person.id + ',NO_HISTORY'

			else:
				customer_map[person.id][1].append(person.date)
				if len(customer_map[person.id][0]) > 0:
					# If there is any FRAUD then count from hashmap and output it.
					print person.date.strftime('%Y-%m-%d') + ',' + person.id + ',FRAUD_HISTORY:'+ str(len(customer_map[person.id][0]))
				else:
					count = purchase_older_90days(person, customer_map)
					# to check if there is ATLEAST one PURCHASE more than 90 days old
					if count > 0:
						print person.date.strftime('%Y-%m-%d') + ',' + person.id + ',GOOD_HISTORY:'+ str(count)
					else:
						print person.date.strftime('%Y-%m-%d') + ',' + person.id + ',UNCONFIRMED_HISTORY:'+ str(len(customer_map[person.id][1])- 1)

if __name__ == '__main__':
	
	with open('test') as file:
		data = file.readlines()

	content = [x.strip() for x in data] 
	customers = parse_file(content)
	solution(customers)


