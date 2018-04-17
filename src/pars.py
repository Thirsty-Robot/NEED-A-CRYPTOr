import argparse

def func():
	parser = argparse.ArgumentParser()
	parser.add_argument("-dC", '--decrypt', help="Set tool mode to decrypt", action="store_true")
	parser.add_argument("-c", '--crypt', help="Set tool mode to crypt", action="store_true")
	parser.add_argument("-sF", '--saveFile', help="Save result in file", action="store_true")
	parser.add_argument("-f", "--file", help="Give file to work with", type=str)
	parser.add_argument("-s", "--string", help="Give string to decrypt", type=str)
	args = parser.parse_args()
	return args
