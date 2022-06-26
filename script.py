#!/usr/bin/env python3


guests = {}
def read_guestlist(file_name):
  text_file = open(file_name,'r')
  while True:
    line_data = text_file.readline().strip().split(",")
    if len(line_data) < 2:
    # If no more lines, close file
      text_file.close()
      break
    name = line_data[0]
    age = int(line_data[1])
    guests[name] = age
    yield name

guest_name = read_guestlist('guest_list.txt')

count = 0
for name  in guest_name:
    count += 1
    if count == 10:
        guest_name.close()
    print(name)
