#caffeinate
##a simple command line program to keep track of coffee intake

###the paths in coffee.py and .bash_profile will need to be changed

add the following to your .bash_profile
`
\#coffee commands
alias coffee-l='python ~/design/caffeinate/coffee.py menu'
alias coffee-+='python ~/design/caffeinate/coffee.py add_cup'
alias coffee-c='python ~/design/caffeinate/coffee.py new_day'
alias coffee-d='python ~/design/caffeinate/coffee.py clear_all'
alias coffee-t='python ~/design/caffeinate/coffee.py get_totals'
`
