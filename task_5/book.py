# file: book.py
# this module contains Book Class from OOP lab7 semester 2 ucu 2019.
class Book:
	"""
	A class for representing the book.
	"""
	def __init__(self, title, author, num_p, curr_p=1):
		"""
		Method for initialization Book object.
		:param title: str
		:param author: str
		:param num_p: int
		:param curr_p: int
		"""
		# p - page/pages
		self.title = title
		self.author = author
		self.num_p = num_p
		self.curr_p = curr_p
		self.book_marked_page = None

	def __str__(self):
		"""
		Method for representing Book object in str form.
		:return: str
		"""
		string = "{}<{} by {}:".format(self.__class__.__name__,
									   self.title,
									   self.author)
		if self.num_p == 1:
			string += " {} page, " \
					  "currently on page {}".format(self.num_p,
													self.curr_p)
		else:
			string += " {} pages, " \
					  "currently on page {}".format(self.num_p,
													self.curr_p)
		if self.book_marked_page is not None:
			string += ", page {} bookmarked>".format(
				self.book_marked_page)
			return string
		else:
			string += ">"
			return string

	def turnPage(self, num):
		"""
		A method for changing current page.
		:param num: int
		:return: None
		"""
		if 0 < self.curr_p + num < self.num_p:
			self.curr_p = self.curr_p + num
		elif num > 0:
			self.curr_p = self.num_p
		else:
			self.curr_p = 1

	def getCurrentPage(self):
		"""
		A method returns current page.
		:return: int
		"""
		return self.curr_p

	def getBookmarkedPage(self):
		"""
		Returns bookmarked page. If in the book is not bookmarked
		page returns None.
		:return: int or bool
		"""
		return self.book_marked_page

	def placeBookmark(self):
		"""
		The method for setting bookmark on the current page.
		:return: None
		"""
		self.book_marked_page = self.curr_p

	def turnToBookmark(self):
		"""
		Turns to the page with bookmark.
		:return: None
		"""
		if self.book_marked_page is not None:
			self.curr_p = self.book_marked_page

	def removeBookmark(self):
		"""
		A method for removing bookmarks.
		:return: None
		"""
		self.book_marked_page = None

	def __eq__(self, other):
		"""
		Method for comparing books. If two books has the same title,
		author and num of pages - they are equal. Otherwise - they
		are not.
		:param other: object
		:return: bool
		"""
		if self.title == other.title and self.author == other.author\
			    and self.num_p == other.num_p\
				and self.curr_p == other.curr_p\
				and self.book_marked_page == other.book_marked_page:
			return True
		else:
			return False
