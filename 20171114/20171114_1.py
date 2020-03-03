import sys

transactions = {}
disk = {}
memory = {}
trans_ids = []
output = ""


temp_var_map = {}
temp_var = {}

operators = ["+","-","*","/"]


def convert_int(num):
	try:
		return int(num)
	except:
		try:
			return float(num)
		except:
			sys.exit("Not an integer")

def process(command):
	command = command.split("(")
	variable = command[1].split(",")[0]
	value = command[1].split(",")[1]
	value = value.split(")")[0]
	return (value,variable)

def print_(elem):
	global output
	s = ""

	for i in sorted(elem):
		s += i + " "+str(elem[i])+" "

	s = s[:-1]
	output += s+"\n"


def process_2(command,operator):
	result = command.split(":")[0]
	temp = command.split("=")[1]

	val1 = temp.split(operator)[0]
	val2 = temp.split(operator)[1]

	return (result,val1,val2)







def log(current_transaction,x,start):

	global output

	if start >= len(transactions[current_transaction]):
		return 1

	commands = transactions[current_transaction][start:start+x]
	# print(commands)

	if start == 0:
		output += "<START "+current_transaction+">"+"\n"
		print_(memory)
		print_(disk)


	
	for command in commands:
		command = command.strip().replace(" ","")

		# print(command)
		# print(temp_var)
		
		if "READ" in command.upper():
			value,variable = process(command)

			if variable not in temp_var_map.keys():
				temp_var_map[variable] = value
				temp_var[value] = disk[variable]
				memory[variable] = disk[variable]

			else:
				
				temp_var[value] = memory[variable]
				temp_var_map[variable] = value


		elif "WRITE" in command.upper():
			value,variable = process(command)

			output += "<"+current_transaction+", "+variable+", "+str(memory[variable])+">"+"\n"
			memory[variable] = convert_int(temp_var[value])

			print_(memory)
			print_(disk)

		elif "OUTPUT" in command.upper():
			variable = command.split("(")[1]
			variable = variable.split(")")[0]
			disk[variable] = memory[variable]

		else:
			for operator in operators:
				if operator in command:
					result,val1,val2 = process_2(command,operator)
					break

			# print(result,val1,val2,operator)
			# result,val1,val2,op = process_2(command)
			if val2 not in temp_var.keys():
				if operator == "+":
					temp_var[result] = temp_var[val1]+convert_int(val2)
				elif operator == "-":
					temp_var[result] = temp_var[val1]-convert_int(val2)
				elif operator == "*":
					temp_var[result] = temp_var[val1]*convert_int(val2)
				elif operator == "/":
					temp_var[result] = float(temp_var[val1])/float(convert_int(val2))
			else:
				# print("in")
				if operator == "+":
					temp_var[result] = temp_var[val1]+temp_var[val2]
				elif operator == "-":
					temp_var[result] = temp_var[val1]-temp_var[val2]
				elif operator == "*":
					temp_var[result] = temp_var[val1]*temp_var[val2]
				elif operator == "/":
					temp_var[result] = temp_var[val1]/temp_var[val2]


	if start+x >= len(transactions[current_transaction]):
		output += "<COMMIT "+current_transaction+">"+"\n"
		print_(memory)
		print_(disk)

	return 0




			
		



def main(x):
	complete = False
	i = 0
	count_finished = 0

	current_transaction = trans_ids[i]
	# print(current_transaction)
	start = 0
	while not complete:
		count_finished += log(current_transaction,x,start)
		i += 1

		if i%len(transactions) == 0:
			start += x
			i = 0

		current_transaction = trans_ids[i]

		if count_finished >= len(transactions):
			complete = True

	# print(output)


	

	

def read_file(file):
	line_no = 1
	transaction_no = None

	with open(file,'r') as f:
		for line in f:
			if line_no == 1:
				variables = line.split()
				for i in range(0,len(variables),2):
					disk[variables[i]] = convert_int(variables[i+1])
			elif line.strip() == "":
				pass
			elif line.split(" ")[0][0] == 'T':
				transaction_id,number_of_commands = line.strip().split()

				if transaction_id in trans_ids:
					sys.exit("Repeated Transaction ID")
				else:
					trans_ids.append(transaction_id)
					transactions[transaction_id] = list()
			else:
				transactions[transaction_id].append(line[:-1])
				



			line_no += 1

	# print(disk)
	# print(transactions)






if __name__ == "__main__":
	if len(sys.argv) != 3:
		sys.exit("Usage: python3 20171114_1.py <input_file> x")

	args = sys.argv

	file = args[1]

	try:
		x = convert_int(args[2])
	except Exception as e:
		sys.exit("x is not an integer")

	
	try:
		read_file(file)
	except Exception as e:
		sys.exit(file+" does not exist")

	main(x)

	out_file = open("20171114_1.txt","w")
	out_file.write(output)
	out_file.close()



