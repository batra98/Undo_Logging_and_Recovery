import sys


logs = []
disk = {}

start_checkpoint_location = -1
end_checkpoint_location = -1

output = ""

def undo_logging(start,end):

	committed = []

	for i in range(end,start,-1):

		if "COMMIT" in logs[i]:
			committed.append(logs[i].split(" ")[1])
		elif "START" in logs[i]:
			pass
		elif "END" in logs[i]:
			pass
		else:
			transaction,variable,value = logs[i].replace(" ","").split(",")
			# print(transaction,variable,value)
			if transaction not in committed:
				disk[variable] = convert_int(value)



	# print(committed)



def print_(elem):
	global output
	s = ""

	for i in sorted(elem):
		s += i + " "+str(elem[i])+" "

	s = s[:-1]

	output += s+"\n"

def recovery():
	global end_checkpoint_location,start_checkpoint_location

	if start_checkpoint_location > end_checkpoint_location:
		end_checkpoint_location = -1

	if start_checkpoint_location == -1 and end_checkpoint_location == -1:
		undo_logging(0,len(logs)-1)
	elif start_checkpoint_location != -1 and end_checkpoint_location != -1:
		undo_logging(start_checkpoint_location,len(logs)-1)
	elif start_checkpoint_location == -1 and end_checkpoint_location != -1:
		sys.exit("END CKPT WITHOUT START CKPT")
	elif start_checkpoint_location != -1 and end_checkpoint_location == -1:
		undo_logging(0,len(logs)-1)




def convert_int(x):
	try:
		return int(x)
	except:
		try:
			return float(x)
		except:
			sys.exit("Not an integer")


def read_file(file):
	global start_checkpoint_location,end_checkpoint_location
	line_no = 1
	# transaction_no = None

	with open(file,'r') as f:
		for line in f:
			if line_no == 1:
				variables = line.split()
				for i in range(0,len(variables),2):
					disk[variables[i]] = convert_int(variables[i+1])
			elif line.strip() == "":
				pass
			else:
				logs.append(line[1:-2])

			if "CKPT" in line.upper():
				if "END" in line.upper():
					end_checkpoint_location = line_no
				elif "START" in line.upper():
					start_checkpoint_location = line_no



			line_no += 1



if __name__ == "__main__":
	if len(sys.argv) != 2:
		sys.exit("Usage: python3 20171114_2.py <input_file>")

	args = sys.argv

	file = args[1]

	# print(file)

	try:
		read_file(file)
	except Exception as e:
		sys.exit(file+" does not exist")

	# print(logs)
	# print(start_checkpoint_location)
	# print(end_checkpoint_location)

	recovery()
	print_(disk)

	# print(output)

	out_file = open("20171114_2.txt","w")
	out_file.write(output)
	out_file.close()