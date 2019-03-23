# file: equation.py
# module contains Polynomial, Quadratic classes
# from OOP y1 s2 lab7 task_5 UCU 2019.
class Polynomial:
	"""
	A class for representing and working with polynomials.
	"""
	def __init__(self, polynomials):
		"""
		A method for initialisation Polynomial object.
		:param polynomials: list
		"""
		self.polynomials = polynomials

	def __str__(self):
		"""
		Returns inf about Polynomial in str form.
		:return: str
		"""
		return "{}(coeffs={})".format(self.__class__.__name__,
									  self.polynomials)

	def degree(self):
		"""
		A method represents degree of polynomial.
		:return: int
		"""
		pol = self.polynomials[:]
		for coeff in self.polynomials:
			if coeff == 0:
				pol.remove(0)
			else:
				break
		return len(pol) - 1

	def coeff(self, num):
		"""
		A method returns returns the coefficient for x**i.
		:param num: int
		:return: int
		"""
		try:
			polynomials = list(reversed(self.polynomials))
			return polynomials[num]
		except BaseException:
			return 0
		
	def  evalAt(self, x):
		"""
		Returns the polynomial evaluated at that value of x
		:param x: int
		:return: int
		"""
		sum = 0
		for i, coeff in enumerate(reversed(self.polynomials)):
			sum += coeff * (x**i)
		return sum

	def __eq__(self, other):
		"""
		Method for comparison two polynomials
		:param other: object
		:return: bool
		"""
		if not isinstance(other, Polynomial)\
				and len(self.polynomials) > 1:
			return False
		elif len(self.polynomials) == 1:
			if self.polynomials[0] == other:
				return True
		if len(self.polynomials) == 0:
			if other.polynomials[0] == 0:
				return True
		if type(other.polynomials) is not list\
				or len(self.polynomials) < len(other.polynomials):
			return False
		pol = []
		if type(self.polynomials) is not list:
			for element in self.polynomials:
				pol.append(element)
		else:
			pol = self.polynomials[:]
		for i in range(len(pol)):
			if pol[i] != 0 and pol[0] != 0:
				break
			elif pol[i] != 0:
				try:
					pol.remove(0)
				except BaseException:
					continue
				break
			pol.remove(pol[i])
		pol_o = other.polynomials
		# there create n to go through pol_o
		n = 0
		for i in range(len(pol)):
			if pol[i] != pol_o[i]:
				return False
		return True

	def __hash__(self):
		"""
		Returns hash object of polynomial.
		"""
		return hash(repr(self.polynomials))

	def scaled(self, scale):
		"""
		A method returns new polynomial with all the coefficients
		multiplied on the given scale.
		:return: object
		"""
		return Polynomial([coeff * scale for coeff in
						   self.polynomials])

	def derivative(self):
		"""
		Returns a new polynomial that is the derivative
		of the original, using the power rule:
		More info: https://www.mathsisfun.com/calculus/power-rule.html
		:return: object
		"""
		new_lst = []
		for i, coeff in enumerate(self.polynomials[-1::-1]):
			new_lst.insert(0, i * coeff)
		# Removing 0 from polynomial
		new_lst.remove(0)
		return Polynomial(new_lst)

	def addPolynomial(self, other):
		"""
		A method for adding two polynomials.
		Returns new object.
		(2x**2 -3x + 5) + (4x - 3) == (2x**2 + x + 2)
		
		:param other: object of class Polynomial
		:return: object
		"""
		if isinstance(other, Polynomial) is False:
			return None
		new_lst = []
		# making copies
		polynomial_1 = self.polynomials[:]
		polynomial_2 = other.polynomials[:]

		# making lists of polynomials equal.
		if len(polynomial_1) < len(polynomial_2):
			while len(polynomial_1) != len(polynomial_2):
				polynomial_1.insert(0, 0)
		elif len(polynomial_1) > len(polynomial_2):
			while len(polynomial_1) != len(polynomial_2):
				polynomial_2.insert(0, 0)

		# finally adding them.
		for coeff_1, coeff_2 in zip(polynomial_1,
								    polynomial_2):
			new_lst.append(coeff_1 + coeff_2)
		return Polynomial(new_lst)

	def multiplyPolynomial(self, other):
		"""
		Class for multiplying polynomials.
		More info:
		https://www.mathsisfun.com/algebra/polynomials-multiplying.html
		:return: object
		"""
		if isinstance(other, Polynomial) is False:
			return None
		# making copies
		polynomial_1 = self.polynomials[:]
		polynomial_2 = other.polynomials[:]

		# making new abstract polynomial
		# the biggest degree is eq to sum of the biggest powers + 1.
		new_lst = [0 for i in range(len(polynomial_1) +\
									len(polynomial_2) - 1)]
		len_l = len(new_lst)
		for coeff_1 in polynomial_1:
			for coeff_2 in polynomial_2:
				degree_1 = list(reversed(polynomial_1)).index(
					coeff_1)
				degree_2 = list(reversed(polynomial_2)).index(
					coeff_2)
				new_degree = degree_1 + degree_2
				# defines new coeff new position
				new_lst[len_l - 1 - new_degree] += coeff_1 * coeff_2
		return Polynomial(new_lst)


class Quadratic(Polynomial):
	"""
	This class represents and operates with Quadratic equation.
	"""
	def __init__(self, polynomials):
		"""
		A method for representing quadratic equation.
		:param polynomials: list
		"""
		super().__init__(polynomials)
		if len(self.polynomials) != 3:
			raise ValueError
	 
	def __str__(self):
		"""
		A method for representing quadratic equation in str form.
		:return: str
		"""
		lst = self.polynomials
		return "Quadratic(a={}, b={}, c={})".format(lst[0],
													lst[1],
													lst[2])

	def discriminant(self):
		"""
		A method returns discriminant of equation.
		the discriminant is b**2 - 4ac
		:return: str
		"""
		# the list with coefficients
		lst = self.polynomials
		return lst[1]**2 - 4 * lst[0] * lst[2]

	def numberOfRealRoots(self):
		"""
		Method returns number of real roots.
		:return: int
		"""
		disc = self.discriminant()
		if disc < 0:
			return 0
		elif disc == 0:
			return 1
		else:
			return 2

	def getRealRoots(self):
		"""
		A method returns all roots of quadratic equation.
		:return: list
		"""
		a = self.polynomials[0]
		b = self.polynomials[1]
		c = self.polynomials[2]
		lst = self.polynomials
		disc = self.discriminant()
		if disc < 0:
			return []
		elif disc == 0:
			return [(- b) / 2 * a]
		else:
			return [((- b) - (disc) ** (1/2)) / 2 * a,
					((- b) + (disc) ** (1/2)) / 2 * a]
