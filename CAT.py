# open, read file then concat multiple files to another file

##for x in ["A","B","C"]:
##    f = open("{}.txt".format(x), "w")
##    f.write(x)
##    f.close()
##
##files = [open("A.txt","r"),open("B.txt","r"),open("C.txt","r")]
##f1 = open("D.txt", "w")
##for file in files:
##    f1.write(file.read())
##f1.close()

response=-1
while response != 0:
    if response == 1:
        name = input("Please enter name of file: ")
        text = input("Please enter text:\n")
        f = open(name+".txt","w")
        f.write(text)
        f.close()
        print("Success!")
        response=3
        #do stuff
    elif response == 2:
        no_of_files = int(input("How many files to append? "))
        res_name = input("Please enter the name of the resulting file: ")
        f = open(res_name+".txt","w")
        for n in range(no_of_files):
            f.write(open(input("Enter file name to append: ")+".txt","r").read())

        f.close()
        print("Success!")
        response=3
        #do stuff
    elif response == 0:
        break
    else:
        print("Commands\n1: Create File\n2: Append File\n0: Exit")
        response = int(input("Please enter command: "))
print("Thanks!")
