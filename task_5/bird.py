# file: bird.py
# this module contains the class from OOP s2 t5 UCU 2019.
class Bird:
	"""
	A class for representing birds.
	"""
	def __init__(self, name, can_fly=True, eggs=0):
		"""
		A method for initialisation Bird object.
		:param name: str
		:param can_fly: bool
		"""
		self.name = name
		self.can_fly = can_fly
		self.eggs = eggs

	def fly(self):
		"""
		A method for representing whether the bird can fly.
		:return: str
		"""
		if self.can_fly is True:
			return "I can fly!"
		else:
			return "No flying for me."

	def countEggs(self):
		"""
		A method for counting eggs.
		:return: int
		"""
		return self.eggs
	
	def __repr__(self):
		"""
		A method for representation situation with bird.
		:return: str
		"""
		if self.eggs == 1:
			return "{} has 1 egg".format(self.name)
		else:
			return "{} has {} eggs".format(self.name, self.eggs)

	def layEgg(self):
		"""
		A method for adding (laying) eggs.
		:return: None
		"""
		self.eggs += 1

class Penguin(Bird):
	"""
	Class for representing penguin.
	"""
	def swim(self):
		"""
		A method for representing whether the bird can swim.
		:return: str
		"""
		return "I can swim!"

	def fly(self):
		"""
		A method for representing whether the bird can fly.
		:return: str
		"""
		return "No flying for me."

class MessengerBird(Bird):
	"""
	Class for representing bird's messages.
	"""
	def __init__(self, name, message=""):
		"""
		A method for representing message.
		:param name: str
		:param message: str
		"""
		super(MessengerBird, self).__init__(name)
		self.message = message

	def deliverMessage(self):
		"""
		A method for delivering messages.
		:return: str
		"""
		return self.message
