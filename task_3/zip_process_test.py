from zip_processor import ZipProcessor
from zip_replace import ZipReplace
from scale_zip import ScaleZip

print("For replacing text in test_text.txt.zip enter\n"
	  "Word to raplace = Stryiska\n"
	  "Substitute word = Kozelnytska\n"
	  "File = test_text.txt.zip")
word_to_replace = input("Enter the word, which must be replaced: ")
substitute_word = input("Enter the substitute word: ")
filename = input("Enter the full name of zip file with text: ")
# testing ZipReplace
zipreplace = ZipReplace(word_to_replace, substitute_word)
ZipProcessor(filename, zipreplace).process_zip()

# testing ZipScale
print("Original size of img in test_img.jpg.zip is 2400 × 1606")
size = input("Enter the size for image scaling for example - '640 x 400'")
size.split("x").strip()
print(size)
zipscale = ScaleZip(size)
ZipProcessor("test_img.jpg.zip", zipscale).process_zip()





