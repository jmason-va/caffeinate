from sys import argv

command = str(argv[1])

def print_menu():
	print
	print '///////////////////'
	print '// beverage menu //'
	print '/////////////////////////////////////////////////////////'
	print '/	    coffee-l: main menu                      \t/'
	print '/	          -+: adds coffee cup to daily total \t/'        
	print '/	          -c: clears daily total             \t/'
	print '/	          -a: clears all                     \t/'
	print '/	          -t: gets total                     \t/'
	print '/	          -w: adds water cup to daily total  \t/'
	print '/////////////////////////////////////////////////////////'
	print

def print_totals(coffee_daily_total, coffee_all_time_total, water_daily_total, water_all_time_total):
	print
	print
	print '/////////////////////////////////////////'
	print '/        water:   daily:     %d        \t/' % water_daily_total
	print '/                 all time:  %d        \t/' % water_all_time_total
	print '/        coffee:  daily:     %d        \t/' % coffee_daily_total
	print '/                 all time:  %d        \t/' % coffee_all_time_total	
	print '/////////////////////////////////////////'
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

def write_totals_file(coffee_daily_total, coffee_all_time_total, water_daily_total, water_all_time_total):
	infile = open('/Users/jmason/design/caffeinate/coffee_total.txt', 'w')
	infile.write(str(coffee_daily_total) + ',' + str(coffee_all_time_total) + ',' + str(water_daily_total) + ',' + str(water_all_time_total))
	infile.close()

def add_to_totals(type):
	totals = read_totals_file()
	if type == 'coffee':
		coffee_daily_total = int(totals[0]) + 1		
		coffee_all_time_total = int(totals[1]) + 1
		water_daily_total = int(totals[2])
		water_all_time_total = int(totals[3])

	if type == 'water':
		coffee_daily_total = int(totals[0])
		coffee_all_time_total = int(totals[1])
		water_daily_total = int(totals[2]) + 1
		water_all_time_total = int(totals[3]) + 1

	write_totals_file(coffee_daily_total, coffee_all_time_total, water_daily_total, water_all_time_total)
	print_totals(coffee_daily_total, coffee_all_time_total, water_daily_total, water_all_time_total)

def subtract_from_totals():
	totals = read_totals_file()
	coffee_daily_total = int(totals[0]) -1							
	coffee_all_time_total = int(totals[1]) -1	
	water_daily_total = int(totals[2]) -1
	water_all_time_total = int(totals[3]) -1 
	write_totals_file(coffee_daily_total, coffee_all_time_total, water_daily_total, water_all_time_total)
	print_totals(coffee_daily_total, coffee_all_time_total, water_daily_total, water_all_time_total)

def clear_daily_total():
	totals = read_totals_file()
	coffee_daily_total = 0							
	water_daily_total = 0
	coffee_all_time_total = int(totals[1])	
	water_all_time_total = int(totals[3]) 
	write_totals_file(coffee_daily_total, coffee_all_time_total, water_daily_total, water_all_time_total)
	print_totals(coffee_daily_total, coffee_all_time_total, water_daily_total, water_all_time_total)

def get_totals():
	totals = read_totals_file()
	coffee_daily_total = int(totals[0]) 
	coffee_all_time_total = int(totals[1]) 
	water_daily_total = int(totals[2]) 
	water_all_time_total = int(totals[3]) 
	print_totals(coffee_daily_total, coffee_all_time_total, water_daily_total, water_all_time_total)


def clear_totals():
	coffee_daily_total = 0							
	coffee_all_time_total = 0
	water_daily_total = 0
	water_all_time_total = 0
	write_totals_file(coffee_daily_total, coffee_all_time_total, water_daily_total, water_all_time_total)
	print_totals(coffee_daily_total, coffee_all_time_total, water_daily_total, water_all_time_total)



if command == 'add_coffee':
	add_to_totals('coffee')

if command == 'add_water':
	add_to_totals('water')

if command == 'new_day':
	clear_daily_total()

if command == 'get_totals':
	get_totals()

if command == 'clear_all':
	clear_totals()

if command == 'subtract_cup':
	subtract_from_totals()

if command == 'menu':
	print_menu()