
# Importing the necessary modules
import os
import sys

# Defining the main function
def main():
    while True:
        # Printing the user prompt
        sys.stdout.write('$ ')
        sys.stdout.flush()
        
        # Getting the user input
        user_input = input()
        
        # Executing the user command
        os.system(user_input)

if __name__ == '__main__':
    main()