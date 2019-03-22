import sys
import os

class ZipReplace:
	"""
	A class for replacing string in zip file.

	Methods
	-------
	process(zipprocessor)
	    Perform a search and replace on all files in the temporary
	    directory.
	    
	Attributes
	----------
	search_string : str
	    The string to find and replace.
	replace_string : str
	    Substitute string.
	"""
	def __init__(self, search_string, replace_string):
		"""
		Method for representing substitute string and string
		for replacing.
		:param search_string: str
		:param replace_string: str
		"""
		self.search_string = search_string
		self.replace_string = replace_string

	def process(self, zipprocessor):
		"""
		Perform a search and replace on all files in the temporary
	    directory.
		"""
		for filename in os.listdir(zipprocessor.temp_directory):
			with open(zipprocessor._full_filename(filename)) as file:
				contents = file.read()
				contents = contents.replace(self.search_string,
											self.replace_string)
			with open(zipprocessor._full_filename(filename), "w") as file:
				file.write(contents)
