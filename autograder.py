import unittest, sys
from graderlib import test_case
import practice as module
import math

"""
Dictionary of allowed question test requests
	Dictionary of functions in practice part
	of this question test
		Function to be tested: list of lists
		which correspond to a test input for
		this function and an expected output
			Tuple of tuples: each tuple inside
			main tuple represents inputs to
			a call: i.e. first tuple represents
			inputs into actual function, 2nd
			tuple are the inputs passed into
			returned function if one is expected,
			etc. Reflected by change in graderlib
"""
question_inputs = {
	"q1": {
		"power_curry_1": [
			[((2,), (4,)), 16],
			[((4,), (3,)), 64],
			[((3,), (5,)), 243]
		],
		"power_curry_2": [
			[((4,), (2,)), 16],
			[((3,), (4,)), 64],
			[((5,), (3,)), 243]
		],
		#"compose": [
		#	[((lambda x: 1 / math.sqrt(2 * math.pi) * math.exp(x), lambda x: - x * x), (1,)), 0.14676266317373993],
		#	[((lambda x: 2 * x, lambda b, x: str(x) + '!' if b else str(x) + '?'), (True, 4)), '4!4!'],
		#	[((lambda x: 2 * x, lambda b, x: str(x) + '!' if b else str(x) + '?'), (False, 4)), '4?4?']
		#],
		"square": [
			[((1,),), 1],
			[((2,),), 4],
			[((3,),), 9],
			[((4,),), 16]
		],
		"quart": [
			[((1,),), 1],
			[((2,),), 16],
			[((3,),), 81],
			[((4,),), 256]
		]
	},
	"q2": {
		"cube": [
			[((1,),), 1],
			[((2,),), 8],
			[((3,),), 27],
			[((4,),), 64]
		],
		"concat": [
			[(("a", "b"),), "ab"],
			[(("dogs ", "cats"),), "dogs cats"]
		],
		"triple_factory": [
			[(("a",), (2,), ("c")), ("a", 2, "c")],
			[(("o",), (1,), ("o")), ("o", 1, "o")],
			[(("e",), (3,), ((1, 2, 3),)), ("e", 3, (1, 2, 3))],
		],
		"inverse_pow": [
			[((2,), (3,)), 1 / 9],
			[((3,), (2,)), 1 / 8]
		],
		"nand": [
			[((False, False),), True],
			[((False, True),), True],
			[((True, False),), True],
			[((True, True),), False],
		],
		"nor": [
			[((False, False),), True],
			[((False, True),), False],
			[((True, False),), False],
			[((True, True),), False],
		],
		"xor": [
			[((False, False),), False],
			[((False, True),), True],
			[((True, False),), True],
			[((True, True),), False],
		],
		"xnor": [
			[((False, False),), True],
			[((False, True),), False],
			[((True, False),), False],
			[((True, True),), True],
		]
	},
	"q3": {
		"sum": [
			[((lambda n: n, 100),), 1 / 2 * 100 * 101]
		],
		"zeta_approx": [
			[((0,),), 500],
			[((1,),), 6.79282342999052],
			[((2,),), 1.642936065514894],
			[((3,),), 1.202054907155594],
			[((4,),), 1.0823232310524604]
		],
		"product": [
			[((lambda x: (x - 1/2) / (x + 1/2) if x > 0 else 1, 10),), 1 / 21]
		],
		"factorial": [
			[((0,),), 1],
			[((1,),), 1],
			[((2,),), 2],
			[((3,),), 6],
			[((4,),), 24],
			[((5,),), 120],
			[((6,),), 720]
		],
		"choose": [
			[((4,2),), 6],
			[((10, 4),), 210],
			[((20, 5),), 15504]
		]
	},
	"q4": {
		"polynomial": [
			[(([1, 1, 1, 1],), (1,)), 4],
			[(([1, 2, 3, 4],), (2,)), 49],
			[(([1, 4, 9, 16],), (3,)), 526],
		],
		"diff_polynomial": [
			[(([1, 1, 1, 1],), (1,)), 6],
			[(([1, 2, 3, 4],), (2,)), 62],
			[(([1, 4, 9, 16],), (3,)), 490],
		]
	},
	"q5": {
		"find_root_compose": [
			[((module.polynomial([-1, 0, 1]), module.diff_polynomial([-1, 0, 1]), 0.0000000000000001), (2,)), 1],
			[((module.polynomial([0, -2, -1, 1]), module.diff_polynomial([0, -2, -1, 1]), 0.0000000000000001), (1,)), -1],
			[((module.polynomial([0, -2, -1, 1]), module.diff_polynomial([0, -2, -1, 1]), 0.0000000000000001), (1 / 2,)), 0],
			[((module.polynomial([0, -2, -1, 1]), module.diff_polynomial([0, -2, -1, 1]), 0.0000000000000001), (3 / 2,)), 2],
		],
		"fractional_power": [
			[((2, 1, 2),), 2 ** (1 / 2)],
			[((3, 1, 2),), 3 ** (1 / 2)],
			[((7, 1, 2),), 7 ** (1 / 2)],
		]
	}
}

def run_test(questions):
	for question in questions:
		# test is the instance of our TestCase class with all of our
		# desired question, specified by argv[1], functions to be tested.
		test = test_case(module, question, question_inputs)

		# not test corresponds to a requested question test which
		# doesn't exist
		if not test:
			return

		# adds our TestCase to the global attributes so that unittest
		# will find it when it searches for TestCases to run
		globals()[test.__name__] = test

	# Displays which questions are being tested
	plural = ('s ' if len(questions) > 1 else ' ')
	q_string = ', '.join([questions[i][1:] for i in range(len(questions))])
	print('\nRunning Test' + plural + 'for Question' + plural + q_string)
	print()


	"""
	argv='q' allows the program to use the command line arguments
	as the question input. q is a dummy attribute class of __main__
	so that the unittest will run that as the passed in command
	arguments, then our program can access the actual command args
	without them messing up the unittest! DO NOT make the value for
	argv more than one character: no clue why, but the unittest main
	function tries to split the argv value into single characters so
	unless we have each of those individual characters defined as
	dummy attribute classes of __main__ (which there's no reason to
	do so), so leave argv='q'.
	"""
	unittest.main(argv='q')

def main():
	# Test all questions.
	if len(sys.argv) == 1:
		run_test([question for question in question_inputs])
	# Test one specific question specified
	# by the single argument passed in.
	elif len(sys.argv) == 2:
		run_test([sys.argv[1]])
	# Too many arguments.
	else:
		run_test([sys.argv[i] for i in range(1, len(sys.argv))])

if __name__ == '__main__':
	main()
