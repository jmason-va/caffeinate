from sys import argv

command = str(argv[1])

def print_menu():
	print
	print '/////////////////'
	print '// coffee menu //'
	print '/////////////////////////////////////////////////////////'
	print '/	    coffee-l: main menu                      \t/'
	print '/	    -+: adds cup to daily total              \t/'        
	print '/	    -c: clears daily total                   \t/'
	print '/	    -a: clears all                           \t/'
	print '/	    -t: gets total                           \t/'
	print '/////////////////////////////////////////////////////////'
	print

def print_totals(daily_total, all_time_total):
	print
	print
	print '//////////////////////////////////////////'
	print '/	    daily total: %d       \t /' % daily_total
	print '/	    all time total: %d   \t /' % all_time_total
	print '//////////////////////////////////////////'
	print
	print

def read_totals_file():
	"""opens the coffee_total text file and returns a list of totals"""
	infile = open('/Users/jmason/design/caffeinate/coffee_total.txt', 'r')	
	totals = infile.read()					
	infile.close()

	if totals != '':
		totals=totals.split(',')				#split the counts into variables
	else:
		print "you're totals have been deleted!"
	return totals

def write_totals_file(daily_total, all_time_total):
	infile = open('/Users/jmason/design/caffeinate/coffee_total.txt', 'w')
	infile.write(str(daily_total) + ',' + str(all_time_total))
	infile.close()

def add_to_totals():
	totals = read_totals_file()
	daily_total = int(totals[0]) + 1		#first number a total that is reset daily
	all_time_total = int(totals[1]) + 1		#second number is all time total
	write_totals_file(daily_total, all_time_total)
	print_totals(daily_total, all_time_total)


def clear_daily_total():
	totals = read_totals_file()
	daily_total = 0							
	all_time_total = int(totals[1])	
	write_totals_file(daily_total, all_time_total)
	print_totals(daily_total, all_time_total)

def get_totals():
	totals = read_totals_file()
	daily_total = int(totals[0]) 
	all_time_total = int(totals[1]) 
	print_totals(daily_total, all_time_total)


def clear_totals():
	daily_total = 0							
	all_time_total = 0
	write_totals_file(daily_total, all_time_total)
	print_totals(daily_total, all_time_total)



if command == 'add_cup':
	add_to_totals()

if command == 'new_day':
	clear_daily_total()

if command == 'get_totals':
	get_totals()

if command == 'clear_all':
	clear_totals()

if command == 'menu':
	print_menu()