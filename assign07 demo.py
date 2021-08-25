# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Working with pickling,
# saving to structured error handling.
# ChangeLog (Who,When,What):
# Morgan Farmer, 8/23/21 , Pickling & structured error handling
# <Your Name>,<Date>,Modified code to complete assignment 7
# Dev: Morgan Farmer, 08/18/21
# ---------------------------------------------------------------------------- #
import pickle
#import a list object
lstData = ['aaa','bbb']

objFile = open('seven','ab')
pickle.dump(lstData,objFile)
objFile.close()
#write to binary file
#ask user to input file and read it


# Error Handling
try:
    new_file_name = input('What do you want to name the file:')
    if new_file_name.isnumeric():
        raise Exception('Do not use numbers!')
    objectFile = open(new_file_name,'rb')
except Exception as e:
    print('There was an error!')
    print(e, e.__doc__, type(e), sep='\n')

# Pickling
#objectFile = open(input(new_file_name))
objFileData = pickle.load(objectFile)
objectFile.close()
print(objFileData)

