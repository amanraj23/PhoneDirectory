from modify import modification as m
from add import add_items as a
from delete import delete_items as d
from disp import display as l 

while 1:
    print('\n\n\n     PHONEBOOK')
    print('    ------------\n')
    print('\n MENU :-')
    print('\n 1. Display Number list \n 2. Add New numbers \n 3. Modify person details \n 4. Delete number with their details \n 5. Exit')
    ch=int(input(' \n Enter your choice : '))
    if ch==1:
        l()
    elif ch==2:
        a()
    elif ch==3:
        m()
    elif ch==4:
        d()
    elif ch==5:
        break
    else:
        print(' \n wrong choice !!')