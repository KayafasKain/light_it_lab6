import re

class StringCalculator:
	def add(self, string):
		if len(string) == 0:
			return 0

		if "," not in string and "\n" not in string:				
			return int(string)


		delims = re.search("(?<=\/\/)\#+(?=\\n)", string)
		
		if delims:
			string = string[delims.span()[1]:]
			values = re.split(delims.group(0), string)
		else:
			values = re.split("\n|,",string)


		result = 0		
		err_message = ""
		for val in values:
			if int(val) >= 0:
				if int(val) < 1000:
					result += int(val)
			else:
				err_message += val + ","


		if len(err_message) > 0:
			return "отрицательные числа запрещены: " + err_message[:-1]
		return result	