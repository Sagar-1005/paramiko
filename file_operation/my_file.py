import os

# print(os.getcwd())
# # os.chdir('..')
# print(os.getcwd())
# print(os.listdir())
# print(os.system('ls -larth'))

files=os.listdir()
for file in files:
    try:
        with open(file) as file_data:
            print(file_data.read())
    except:
        print('Not a file')