import argparse


def create(name, text):
    """Return a created file with a user-defined name with the text given by the user."""
    f = open(name + ".txt", "w+")
    f.write(text)
    f.close()
    return f'Successfully created {name}.txt!'


def append(no_of_files, resulting_file):
    """Append the files identified by the user in a new file with the name given by the user."""
    f = open(resulting_file + ".txt", "w")
    for file in no_of_files:
        # f.write(open(input("Enter file name to append: ") + ".txt", "r").read())
        f.write(open(file+".txt","r").read())
    f.close()
    return f"Successfully appended files and created {resulting_file}.txt!"


def concat(file_to_concat,file_to_rewrite):
    """Concatenate the identified files into the given file."""
    f = open(file_to_rewrite+".txt","a")

    for file in file_to_concat:
        f.write(open(file+".txt","r").read())
    f.close()
    return f"Successfully concatenated files into {file_to_rewrite}.txt!"


def read(files):
    """Read the files identified."""
    text = ""
    for file in files:
        f = open(file+".txt","r")
        text += "\n"+f.read()
    return print(text)
    f.close()


parser = argparse.ArgumentParser()
parser.add_argument("files", nargs="*") # stores the names of files in a list.
parser.add_argument('-c','--create', action='store_true', help="Create new file.")
parser.add_argument('-a','--append', action='store_true', help="Append given files in a new file.")
parser.add_argument('-cat','--concat', action='store_true', help="Concatenates the text in the given files.")
parser.add_argument('-r','--read', action='store_true', help="Read the given file.")
args = parser.parse_args()

if args.create:
    name = input("Enter name of new file: ")
    text = input("Enter text to put in file: ")
    create(name, text)
elif args.append:
    no_of_files = (input("Enter files to append: ")).split(" ")
    resulting_file = input("Enter the name of the resulting file: ")
    append(no_of_files, resulting_file)
elif args.concat:
    file_to_concat = (input("Enter files to concat: ")).split(" ")
    file_to_rewrite = input("Enter file to rewrite: ")
    concat(file_to_concat, file_to_rewrite)
elif args.read:
    files = (input("Enter file/s to read: ")).split(" ")
    read(files)
