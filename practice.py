import math

def compose(f, g):
	"""
	Composes two functions into a function of the form f(g).

	Args:
		f: a function, assumed to receive only one argument
		g: a function, can receive any amount of arguments

	Returns:
		a function which can be called with one argument and
		returns the result of the composition of f and g, f(g).
	"""
	def h(*x):
		"""
		Composition of two functions passed in compose frame.

		Args:
			*x: a list of values which are suitable as arguments to g

		Returns:
			a call on composition of f and g with all arguments in *x
		"""
		return f(g(*x))
	return h

# ------------------------------------------------------------------------- #
#																			#
# Question 1: Currying and Composing										#
# ------------------------------------------------------------------------- #
def power_curry_1(x):
	"""
	Higher-order currying function for exponeniation.
	Sets our base for powers but doesn't restrict us to
	a specified exponent yet.

	Args:
		x: number, base to be exponenitiated

	Returns:
		a function which when called returns the desired power of x
	"""
	def curried(n):
		"""
		Function with the base of the power set in the power_curry frame.
		
		Args:
			n: exponent of the power

		Returns:
			the power of x to the n
		"""

		product = ________
		for i in range(________):
			product = ________
		return ________

	return ________

def power_curry_2(n):
	"""
	Higher-order currying function for exponeniation.
	Sets our exponent for powers but doesn't restrict us to
	a specified base yet.

	Args:
		n: exponent of the power

	Returns:
		a function which when called returns the desired power of x
	"""
	def curried(x):
		"""
		Function with the exponent of the power
		set in the power_curry frame.
		
		Args:
			x: number, base to be exponenitiated

		Returns:
			the power of x to the n
		"""

		product = ________
		for i in range(________):
			product = ________
		return ________

	return ________

def square(x):
	"""
	Defines the square function using a
	call to one of the power_curry functions.

	Args:
		x: number to be squared

	Returns:
		the square of x
	"""
	return ________

def quart(x):
	"""
	Defines the quart function (x ** 4)
	using the square function and a call
	to the compose function.

	Args:
		x: number to be quarted

	Returns:
		the fourth power of x
	"""
	return compose(________, ________)(________)

def stnd_nrm(x):
	"""
	Using the compose function, produce a function which returns
	the value of the standard normal curve valued at x.
	The standard normal curve is of the form f(x) = exp(-x^2) / sqrt(2*pi)

	Args:
		x: x-value of where to evaluate the standard normal curve
	
	Returns:
		y-value of the standard normal curve at x
	"""
	return compose(lambda y: ________, lambda y: ________)(________)

# ------------------------------------------------------------------------- #
#																			#
# Question 2: Lambdas														#
# ------------------------------------------------------------------------- #
# lambda(x) which encodes the cube function
cube = ________

# lambda(x,y) that concatantes two strings
concat = ________

# lambda(x) which returns a function lambda(y) which returns a function
# lambda(z) which returns a tuple of the values passed into
# the three of these functions
triple_factory = ________

# lambda(n) which returns a function lambda(x) which returns
# the inverse power of x to the n
inverse_pow = ________

# lambda(x,y) which emulates the NAND logic gate without if/elif/else statements
nand = ________

# lambda(x,y) which emulates the NOR logic gate without if/elif/else statements
nor = ________

# lambda(x,y) which emulates the XOR logic gate without if/elif/else statements
xor = ________

# lambda(x,y) which emulates the XNOR logic gate without if/elif/else statements
xnor = ________

# ------------------------------------------------------------------------- #
#																			#
# Question 3: Accumulations													#
# ------------------------------------------------------------------------- #
def accumulate(term, operation, base, n):
	"""
	Accumulates a total value by operating on succesive terms given for an
	index with the initial total value equal to a designated base (base is
	determined by the operation usually).

	Args:
		term: function which returns a numerical value determined by the
			index passed in as an argument
		operation: two argument function which produces a value by comining
			them in some mathematical procedure
		base: initial total value; critical in ensuring we have return a
			correct final total value (e.g. if operation=mul, base=0 would
			always result in a return of 0)
		n: index to which the accumulation is to be taken up to (indexing
			goes from 0 to n)

	Returns:
		a number which is the total accumulation of the terms with the operation
	"""
	total = ________
	for i in range(________):
		total = ________
	return ________

def sum(term, n):
	"""
	Representation of a sum up to a specified index given some sequence.

	Args:
		term: functional form of a sequence accpeting one argument
			which represents the term index
		n: index the sequence is to be summed up to

	Returns:
		a sum of terms
	"""
	return accumulate(________, ________, ________, ________)

def zeta_approx(s):
	"""
	Approximates the zeta function with respect to s up to the 500th term.
	The zeta function Z(s) = sum of (1/n)^s from n=1 to ∞.
	Using your defined sum function, come up with a proper term function,
	using only a lambda function, for the sum. Do not use ** notation, must
	use previous abstractions of powers. Make sure your sum doesn't diverge!

	Args:
		s: exponent to which each term is being raised

	Returns:
		an approximation of Z(s)
	"""
	return sum(________, ________)

def product(term, n):
	"""
	Representation of a procut up to a specified index given some sequence.

	Args:
		term: functional form of a sequence accpeting one argument
			which represents the term index
		n: index the sequence is to be prodcutted up to

	Returns:
		a procut of terms
	"""
	return accumulate(________, ________, ________, ________)

def factorial(n):
	"""
	Implement the factorial of n, n!, using product by defining a term function.
	Remember when defining your term that indexing in product begins at 0.

	Args:
		n: a nonnegative integer

	Returns:
		nth factorial
	"""
	return product(________, n)

def choose(n, k):
	"""
	A choose function returns how many ways there are to choose k items
	from n choosable, distinct items. I.e. how many different hands of 4 cards
	are there from a deck of cards? choose(52, 4).

	Implement the choose function nCk = n! / k! * (n - k)!.
	Be careful when defining using factorial, n! gets really big really
	fast. The better method will be to use a product with a suitable
	term function. If k < 0 or k > n, choose(n, k) = 0.
	For more info: https://en.wikipedia.org/wiki/Binomial_coefficient

	Args:
		n: nonnegative integer
		k: nonnegative integer
	
	Returns:
		the choose function evaluated for n and k
	"""
	if ________:
		return 0
	elif ________:
		return 1
	return product(________, ________)

# ------------------------------------------------------------------------- #
#																			#
# Question 4: Polynomials													#
# ------------------------------------------------------------------------- #
def polynomial(_a_):
	"""
	Produces a function which when called with a
	number, x, returns the value of plugging x into
	the polynomial specified by _a_.

	Args:
		_a_: a list of coefficients for a polynomial,
			with the number at index i of _a_ representing
			the coeffecient of the ith power of x
			e.g. _a_ = [1, 2, 3] represents the polynomial
			1 + 2x + 3x^2

	Returns:
		a function which takes one value and plugs it into
		the polynomial specified by _a_
	"""

	def plug_in(x):
		"""
		Applies the x to the polynomial _a_.

		Args:
			x: number

		Returns:
			in a sense, f(x) where f is the polynomial
			that _a_ is representing
		"""
		return sum([________ for i in range(________)])
	return plug_in

def diff_polynomial(_a_):
	"""
	Produces a function which when called with a
	number, x, returns the value of plugging x into
	the derivative of a polynomial specified by _a_.

	Args:
		_a_: a list of coefficients for a polynomial,
			with the number at index i of _a_ representing
			the coeffecient of the ith power of x
			e.g. _a_ = [1, 2, 3] represents the polynomial
			1 + 2x + 3x^2

	Returns:
		a function which takes one value and plugs it into
		the derivative of the polynomial specified by _a_

	HINT: form a new polynomial which is the derivative of
	_a_ by manipulating _a_
	HINT: the derivative of _a_[n+1] * x^(n+1) = _a_[n+1] * (n+1) * x^n
	"""
	return polynomial([________ for i in range(________)])

# ------------------------------------------------------------------------- #
#																			#
# Question 5: Newton's Method												#
# ------------------------------------------------------------------------- #
def improve(update, close, guess):
	"""
	Given an initial guess, continue to "update" the guess until
	the guess is determined to be close enough.

	Args:
		update: a function used to update guess, takes one argument
		close: a function to determine if our guess is close enough
			to the desired answer
		guess: can be any value, estimate we are trying to improve

	Returns:
		final value for guess after it has been deemed "close enough"
	"""
	while ________:
		guess = ________
	return ________

def newton_update_compse(f, df):
	"""
	Composes an update function which when called with a guess,
	returns the next iteration for the guess provided by the
	Newton's Method formula.

	Args:
		f: function whose roots we are searching for, takes one
			numerical argument
		df: first derivative of f, takes one numerical argument

	Returns:
		an update function which takes one argument
	"""
	def update(x):
		"""
		Applies the Newton's Method formula to x to get a new and
		improved x-estimate for the root of. HINT: requires the
		use of f, df and x.

		Args:
			x: current guess for root of f

		Returns:
			a new and more accurate guess for the root of f
		"""
		return ________ if df(x) != 0 else ________

	return ________

def find_root_compose(f, df, h):
	"""
	Composes a function, close, which when provided with a guess, x, determines
	if -h <= f(x) <= h.
	Produces a function which finds the root of f by applying our
	newton_update and close functions and an initial guess to our improve function.

	Args:
		f: function whose roots we want to find
		df: first derivative of f
		h: uncertainty we are allowing in the y-distance of our guess for f's root;
			assumed to be a small positive number

	Returns:
		a function which takes an initial guess for the root of f and returns an
		approximate, if not accurate, estimate of a local root of f
	"""
	assert h > 0

	def close(x):
		return ________
	def find_root(guess):
		return ________

	return ________

def find_poly_compose(_a_, h):
	"""
	Finds the root of a polynomial specified by the list of coefficients
	and within the uncertainty range h. Assumes polynomial and
	diff_polynomial have been correctly filled out.

	Args:
		_a_: list of coefficients
		h: allowed uncertainty

	Returns:
		a function finds the root for specifically a polynomial
	"""
	return ________

def sqrt(a):
	"""
	Finds the sqrt of a number by using Newton's Method.
	HINT: the roots of a x^2 - a are ±√(a)

	Args:
		a: number to be square rooted

	Returns:
		square root of a
	"""
	return ________

def fractional_power(x, a, b):
	"""
	Determines the result of taking x to the (a / b) power.
	Not allowed to use ** notation or the built in pow function.
	HINT: the root of f(c) = c^b - d is d ^ (1 / b)
	HINT: your defined power_curry functions will come in use for raising
	the power to the ath power

	Args:
		x: number to exponentiated
		a: positive integer
		b: positive integer
	
	Returns:
		x ^ (a / b) with considerable accuracy
	"""
	return ________


# ------------------------------------------------------------------------- #
#																			#
# Question 5: Docstring Practice											#
# ------------------------------------------------------------------------- #

# Define and write a function named "pair_reversal" which switches the position
# of each character in a string with its corresponding adjacent character.
# Include a docstring which conforms to the Google docstring format providing
# details about the function
# Ex: "abcdef" --> "badcfe"		"123456789" --> "214365879"
