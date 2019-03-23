# file: document_test.py
# module consists of tests for checking work of document.py module.
from task_4.document import Document, Cursor, Character
d = Document()
d.insert("h")
d.insert('e')
d.insert(Character('l', bold=True))
d.insert(Character('l', bold=True))
d.insert('o')
d.insert('\n')
d.insert(Character('w', italic=True))
d.insert(Character('o', italic=True))
d.insert(Character('r', underline=True))
d.insert('l')
d.insert('d')
print("Here is result of creating document:\n{}\n".format(d.string))

d.cursor.home()
d.delete()
d.insert('W')
print("Here is result of moving cursor to the beginning of page,"
	  "deleting char and inserting 'W'\n")
print(d.string)

# Moving cursor outside of the file (directly)
print("Length of document eq to {}".format(len(d.string)))
print("Moving cursor outside of the file and inserting 'Q': \n")
for i in range(len(d.string)):
	d.cursor.forward()
	print("Current pos of cursor {}".format(
		d.cursor.position
	))
print("\nInserting 'Q' in current position of cursor.")
d.insert("Q")
print(d.string)

# Moving cursor outside of the file (conversely)
print("\nMoving cursor outside of the file and inserting 'Q':\n")
for i in range(100):
	d.cursor.back()
	print("Current pos of cursor {}".format(
		d.cursor.position
	))
print("\nInserting 'Q' in current position of cursor.")
d.insert("Q")
print(d.string)

# Deleting char which doesn't exist
try:
	print("\nCurrent position of cursor: {}".format(d.cursor.position))
	print("Deleting char which doesn't exist:")
	d.delete()
except IndexError:
	print("<IndexError> raised")

# Savaing document without name
try:
	print("\nSavaing document without name:")
	d.save()
except FileNotFoundError:
	print("<FileNotFoundError> raised")

# Entering several chars.
try:
	print("\nEntering several chars.")
	d.insert("LSD")
except AssertionError:
	print("<AssertionError> raised")









# d.characters[0].underline = True
# print(d.string)

