from getpass import getpass

masterkey = "Davescpm092023"
pw = getpass ("ENTER THE TERMUX KEY:")
while pw != masterkey :
	pw = getpass ("ENTER THE TERMUX KEY:")

print(" Login Success")