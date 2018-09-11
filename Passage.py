import csv

class Passage:
	
	def __init__(self, start, end, ver):
		self.start = start
		self.end = end
		self.ver = ver
		self.text = getText(self.start, self.end, self.ver)
	

def getText(start, end, ver):
	file = 't_' + ver + '.csv'
	text = ''

	with open(file) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		next(csv_reader)
			
		for row in csv_reader:
			vid = int(row[0])
			if vid >= start and vid <= end:
				text += row[4]
				
		text = text.replace(".", ". ")
		text = text.replace("!", "! ")
		text = text.replace("?", "? ")
	return text

