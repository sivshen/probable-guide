#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sesw213
#
# Created:     13/07/2016
# Copyright:   (c) sesw213 2016
# Licence:     <your licence>
#-----------------------------------------------------------------------------

password= "will"

for i in range(2):
    p= input("enter pass")
    j=2
    if(p==password):
        print("welcome")
        break
    else:
        print("wrong",j-1)
        continue
print("again")


