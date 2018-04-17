import os
import sys
from algorithm import Algorithm
import pars
import time

args = pars.func()
os.system('cls')

print ('============================================================================================================================================')
print ('============================================================================================================================================')
print ('@@@  @@@  @@@@@@@@  @@@@@@@@  @@@@@@@               @@@@@@               @@@@@@@  @@@@@@@   @@@ @@@  @@@@@@@   @@@@@@@   @@@@@@   @@@@@@@   ')
print ('@@@@ @@@  @@@@@@@@  @@@@@@@@  @@@@@@@@             @@@@@@@@             @@@@@@@@  @@@@@@@@  @@@ @@@  @@@@@@@@  @@@@@@@  @@@@@@@@  @@@@@@@@  ')
print ('@@!@!@@@  @@!       @@!       @@!  @@@             @@!  @@@             !@@       @@!  @@@  @@! !@@  @@!  @@@    @@!    @@!  @@@  @@!  @@@  ')
print ('!@!!@!@!  !@!       !@!       !@!  @!@             !@!  @!@             !@!       !@!  @!@  !@! @!!  !@!  @!@    !@!    !@!  @!@  !@!  @!@  ')
print ('@!@ !!@!  @!!!:!    @!!!:!    @!@  !@!  @!@!@!@!@  @!@!@!@!  @!@!@!@!@  !@!       @!@!!@!    !@!@!   @!@@!@!     @!!    @!@  !@!  @!@!!@!   ')
print ('!@!  !!!  !!!!!:    !!!!!:    !@!  !!!  !!!@!@!!!  !!!@!!!!  !!!@!@!!!  !!!       !!@!@!      @!!!   !!@!!!      !!!    !@!  !!!  !!@!@!    ')
print ('!!:  !!!  !!:       !!:       !!:  !!!             !!:  !!!             :!!       !!: :!!     !!:    !!:         !!:    !!:  !!!  !!: :!!   ')
print (':!:  !:!  :!:       :!:       :!:  !:!             :!:  !:!             :!:       :!:  !:!    :!:    :!:         :!:    :!:  !:!  :!:  !:!  ')
print (' ::   ::   :: ::::   :: ::::   :::: ::             ::   :::              ::: :::  ::   :::     ::     ::          ::    ::::: ::  ::   :::  ')
print ('::    :   : :: ::   : :: ::   :: :  :               :   : :              :: :: :   :   : :     :      :           :      : :  :    :   : :  ')
print ('============================================================================================================================================')
print ('By. Thirsty-Robot')
print ('============================================================================================================================================\n')

if (args.crypt):
	if (args.string):
		start_time = time.time()

		print('[+] Time started: ',start_time)
		print('\n[+] Encrypting word: '+args.string)

		object1 = Algorithm(args.string)
		result = object1.StringCrypt()

		end = time.time()

		print('\n[+] Finish time: ',end)

		if(args.saveFile):
			with open('result.txt', 'w') as file:
				file.write(result)
				file.close()

			print ('[+] Saved in file')

	if (args.file):
		object1 = Algorithm(args.file)
		object1.FileCrypt()


if (args.decrypt):
	start_time = time.time()

	print('[+] Time started: ',start_time)
	print('\n[+] Decrypting word: '+args.string)

	object1 = Algorithm(args.string)
	object1.StringDecrypt()

	end = time.time()

	print('\n[+] Finish time: ',end)
