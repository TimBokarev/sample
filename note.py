

file = open("notes.txt", "r")
current_text = file.read()
file.close()

added_text = input ('add text: ')
c = 'print'

if added_text == c :
   file = open("notes.txt", "r")
   print(file.read())
   file.close()

file = open("notes.txt", "w")

file.write(current_text + added_text)

file.close() 

------------------------

file.write(current_text + added_text)
file.write(current_text + added_text)
file.write(current_text + added_text)