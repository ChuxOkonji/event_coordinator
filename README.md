Project: Event Coordinator

Assuming you are starting up your own event coordination business and want to create a Python application using generators to help manage your events.

This project will utilize  generators by managing and coordinating customer events for your business.

Provided is a guest list of names and their ages that are within the file guest_list.txt.

-- Within the file script.py, there is a defined function called read_guestlist() that will read in the guestlist file line by line. This function will separate the name and age values and store them into variables named name and age respectively.

--This function was then modified to be a generator function so that each guest name is yielded for every iteration of the generator object.

--The generator function was further modified so that the generator object can take in a value using the send() method. To accomplish this:
   - We first define a variable n, before the while loop and set it to None, this variable will hold the data fed into the generator using send()
   - If n is not None, the line_data variable stores the value inputed with send(), with the strip() and split() methods applied as is with the data read from the .txt file.
   - The variable n is set to yield at the end of the while loop. This is so that we can maintain a single yield statement. So that whether or  not input is given via send(), the name variable yielded.

The for loop prints the first 10 names from the guest_list, and then prints the name given through send(), and then the remaining names on guest_list

A generator expression is defined that uses the guests dictionary to retrieve a generator of names of guest who are 21 and over. Note that the data fed through send() earlier is included in the dictionary.

We assume that our events will have 3 tables with five seats each. Three generator functions are created to represent each table. Each generator yields a tuple of ('food name', 'Table table label', 'Seat number')

Finally, we want to assign a table and seat number to each guest. To achieve this, we pipeline generators-- a new generator we create will take as input any of the generators we created earlier that yielded the food/seat number. This new generator will also take in as input the guests dictionary.
This generator function will yield a tuple of the guest name and the next value from the inputed generator 
