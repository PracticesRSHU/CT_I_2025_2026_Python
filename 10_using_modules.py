# import mypackage.func_lab4

# mypackage.func_lab4.hello()
# mypackage.func_lab4.hello()
# mypackage.func_lab4.hello()

import mypackage.func_lab4 as fl4

print(fl4.suma_number(3,4,5,6))

from mypackage.func_lab4 import info_user, suma_number
# import all functions from module
from mypackage.func_lab4 import *

info_user("admin","admin@admin.ua",18)

