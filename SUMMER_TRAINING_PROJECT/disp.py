from database import telephone as pl
def display():
     print( 'Number'.ljust(6), ' \t'    'Name'.ljust(18),      'gender',    '   age')
     for key in pl.keys():
         print (' {}   {} {}  {}'.format(key,pl[key][0].ljust(20),pl[key][1], pl[key][2])) 

