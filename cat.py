import argparse


def create(defined_name, input_text):
    """Return a created file with a user-defined name with the text given by the user."""
    f = open(defined_name, "w+")
    f.write(input_text)
    f.close()
    return f'Successfully created {defined_name}!'


def append(list_of_files, result):
    """Append the files identified by the user in a new file with the name given by the user."""
    f = open(result, "w")
    for file in list_of_files:
        f.write(open(file, "r").read())
    f.close()
    return f"Successfully appended files and created {result}!"


def concat(concat_file, rewrite_file):
    """Concatenate the identified files into the given file."""
    f = open(rewrite_file, "a")

    for file in concat_file:
        f.write(open(file, "r").read())
    f.close()
    return f"Successfully concatenated files into {rewrite_file}!"


def read(desired_files):
    """Read the files identified."""
    text_in_file = ""
    for file in desired_files:
        f = open(file, "r")
        text_in_file += "\n"+f.read()
        f.close()
    return print(text_in_file)


parser = argparse.ArgumentParser()
parser.add_argument('-c', '--create', action='store_true', help="Create new file.")
parser.add_argument('-a', '--append', action='store_true', help="Append given files in a new file.")
parser.add_argument('-cat', '--concat', action='store_true', help="Concatenates the text in the given files.")
parser.add_argument('-r', '--read', action='store_true', help="Read the given file.")
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
