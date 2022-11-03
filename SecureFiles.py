#!/usr/bin/env python3
import os
import base64
import random
import magic
from banner import *
banner()

menu = {1:"Image",2:"Text file",3:"Audio file",4:"Video",5:"Other files"}
def encrypt(source_file,choice):
	file = open("./files/"+source_file,"rb")
	data = file.read()
	b_array = bytearray(data)
	key = input("Enter Key to encrypt {}: ".format(menu[choice]))
	random.seed("CH4R4NU"+key)
	for i in range(len(b_array)):
		k = random.getrandbits(8)
		b_array[i] = b_array[i] ^ k
	file.close()
	b64_array = base64.b64encode(b_array)
	if "." in source_file:
		ext = "."+source_file.split(".")[-1]
		file = open("./files/"+source_file.strip(ext)+"_encrypted"+ext,"wb")
	else:
		file = open("./files/"+source_file+"_encrypted","wb")
	file.write(b64_array)
	print("\tThe {} is encrypted and saved in files directory..".format(menu[choice]))

def decrypt(source_file,choice):
	file = open("./files/"+source_file,"rb")
	data = file.read()
	b_array = bytearray(base64.b64decode(data))
	key = input("Enter Key to decrypt image : ")
	random.seed("CH4R4NU"+key)
	for i in range(len(b_array)):
		k = random.getrandbits(8)
		b_array[i] = b_array[i] ^ k 
	file.close()
	if "." in source_file:
		ext = "."+source_file.split(".")[-1]
		source_file = "./files/"+source_file.strip(ext)+"_decrypted"+ext
		file = open(source_file,"wb")
	else:
		source_file = "./files/"+source_file+"_decrypted"
		file = open(source_file,"wb")
	file.write(b_array)
	isdecrypted(source_file,choice)

def check_file(file):
	if not os.path.isfile("./files/"+file):
		print("File not found. ")
		exit(1)
def isdecrypted(file,choice):
	print("-"*50)

	typ = magic.from_file(file,mime=True)

	if ("text" in typ) and choice == 7:
		print("Text File is decrypted and saved in files directory..:-)")
	elif ("image" in typ) and choice == 6:
		print("Image is decrypted and saved in files directory..:-)")
	elif ("audio" in typ) and choice == 8:
		print("Audio file is decrypted and saved in files directory..:-)")
	elif ("video" in typ) and choice == 9:
		print("Video is decrypted and saved in files directory..:-)")
	elif ("text/plain" in typ ) and choice == 10:
		print("File is decrypted and saved in files directory..:-)")
	else:
		print("The key is wrong...")
		exit(1)
	print("-"*50)

def main():
	print("""
File Encrypter and Decrypter Menu
---------------------------------------------
Copy and paste the file in the "files" directory...
		1. Encrypt Image files      
		2. Encrypt Text files		
		3. Encrypt Audio files		
		4. Encrypt Video files		
		5. Encrypt other files		
		6. Decrypt Image files		
		7. Decrypt Text files		
		8. Decrypt Audio files		
		9. Decrypt Video files		
		10. Decrypt other files		
		0. Exit						
---------------------------------------------
		""")
	choice = int(input("Choose your option[0/1-10] : "))
	
	if choice == 1:
		file = input("Enter image name : ")
		check_file(file)
		encrypt(file,1)
	elif choice == 2:
		file = input("Enter Text file name : ")
		check_file(file)
		encrypt(file,2)
	elif choice == 3:
		file = input("Enter Audio file name : ")
		check_file(file)
		encrypt(file,3)
	elif choice == 4:
		file = input("Enter Video file name : ")
		check_file(file)
		encrypt(file,4)
	elif choice == 5:
		file = input("Enter File name : ")
		check_file(file)
		encrypt(file,5)
	elif choice == 6:
		file = input("Enter Image name : ")
		check_file(file)
		decrypt(file,6)
	elif choice == 7:
		file = input("Enter Text file name : ")
		check_file(file)
		decrypt(file,7)
	elif choice == 8:
		file = input("Enter Audio file name : ")
		check_file(file)
		decrypt(file,8)
	elif choice == 9:
		file = input("Enter Video file name : ")
		check_file(file)
		decrypt(file,9)
	elif choice == 10:
		file = input("Enter File name : ")
		check_file(file)
		decrypt(file,10)
	elif choice == 0:
		print("Terminating..")
		exit(1)
	else:
		print("Invalid choice..")
		exit(1)
if __name__ == '__main__':
	main()