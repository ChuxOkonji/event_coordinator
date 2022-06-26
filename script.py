#!/usr/bin/env python3


guests = {}
def read_guestlist(file_name):
  text_file = open(file_name,'r')
  #twe define n so that it is not undefined when the whilw loop runs
  n = None
  while True:
    line_data = text_file.readline().strip().split(",")
    #n is not none if a value has been taken in by the generator using send()
    if n is not None:
        line_data = n.strip().split(',')
    if len(line_data) < 2:
    # If no more lines, close file
      text_file.close()
      break
    name = line_data[0]
    age = int(line_data[1])
    guests[name] = age
    #enable the generator function take in a value using send():
    n = yield name


guest_name = read_guestlist('guest_list.txt')

count = 0
for name  in guest_name:
    count += 1
    print(name)
    #After printing the first 10 names, print the value given via send()
    if count == 10:
        print(guest_name.send('Jane, 35'))

# Define a generator expression that uses the guest dictionary to retrieve a genarator of names of guests
# who are 21 and over
guest_21_and_over = (name for name in guests if guests[name] >= 21)

for name in guest_21_and_over:
    print(name)
