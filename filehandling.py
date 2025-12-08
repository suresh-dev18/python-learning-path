# file= open("sample.txt",mode='w+')
# file.write('this is sample file to test\n i want 2nd line as well')
# file.seek(0)
# print(file.read())
# file.close()

# file1=open("suresh_sample.txt",'a+')
# file1.write('\nfile with my name is there\nwhich contains nothing important')
# #file1.seek(5)
# file1.seek(0)
# print(file1.read())
# file1.close()

#with open
with open("myfile.txt",'w+') as file:
    file.write("practicing with open method 2nd time")
    file.seek(5)
    print(file.read())