array_result = []
result = ''
alphabet = [ 'a','b','c','d', 'e', 'f','g','h','i','j',
    	'k','l','m','n','o','p','q','r','s','t','u',
		'v','w','x','y','z'
		]

index = 0;

class Algorithm:
	def __init__(self, to_crypt):
		self.array = alphabet
		self.to_crypt = to_crypt

	def StringCrypt(self):
		self.to_crypt = self.to_crypt.lower()
		for i in self.to_crypt:
			i = alphabet.index(i)+13
			if (i > 24):
				i = i-26
			array_result.append(alphabet[i])

		result = ''.join(array_result)
		print ('\nResult: ' +result)
		return result

	def FileCrypt(self):
		print ('\nFile content: ')
		
		with open(self.to_crypt, 'r') as file:
			for line in file:
				print (line)

	def StringDecrypt(self):
		self.to_crypt = self.to_crypt.lower()

		for i in self.to_crypt:
			i = alphabet.index(i)-13
			array_result.append(alphabet[i])

		result = ''.join(array_result)
		print ('\nResult: '+result)