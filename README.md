# cat.py

## Requirements
Python 3

## What is it?
This is a Python program that implements the different functions of the unix command, **cat**.

## What can it do?
This program contains the following functions:
  
  **Create**: This function creates new text files with the text given by the user.
  
  **Read**: This function allows the user to read the content of the identified files.
  
  **Concat**: This function allows the user to concatenate the content of the given files
          into the chosen files.
  
  **Append**: This function appends the given list of files into a new file with a
          user-defined filename.
          
## Reminders
In cases where **_more than one_ file** will be included in the command, always remember to 
input the desired resulting file **_in the end_** before inputting the function to be called.
Otherwise, just input the single file name before the command to be called.

For example:

  **Goal**: 
  
  To append the files file1.txt, file2.txt, and file3.txt into a new file called 
  file4.txt.
  
  
  **Command**:
  
  \> python cat.py file1 file2 file3 file4 -a
  
