#coding: utf-8
# Developer: Derxs
# Version: 1.0
import random, os

try:
	def main():
		def clear():
			os.system("clear")
		
		try:
			print('''\033[01;31m
╔═╗╔═╗╔═╗╔═╗┬ ┬
║  ╠═╝╠╣ ╠═╝└┬┘
╚═╝╩  ╚  ╩   ┴  by Derxs v1.0

\033[01;34m1)\033[00;00m Verificar CPF
\033[01;34m2)\033[00;00m Gerar CPF
\033[01;31m3)\033[00;00m Sair
\033[00;00m''')
			opc = input("\033[01;35mCPFPy>\033[00;00m ")

			if(int(opc) == 1):
				ge = input("\033[01;34m[+]\033[00;00m Digite um CPF: ")
				
				cpf = ge.replace('.', '')
				cpf = cpf.replace('-', '')

				if(len(cpf) == 11):
					n1 = int(cpf[0]) * 10
					n2 = int(cpf[1]) * 9
					n3 = int(cpf[2]) * 8
					n4 = int(cpf[3]) * 7
					n5 = int(cpf[4]) * 6
					n6 = int(cpf[5]) * 5
					n7 = int(cpf[6]) * 4
					n8 = int(cpf[7]) * 3
					n9 = int(cpf[8]) * 2
					n10 = int(cpf[9]) * 1
					n11 = int(cpf[10])
					result1 = (11 - ((n1+n2+n3+n4+n5+n6+n7+n8+n9) % 11))
					
					if(result1 == n10):
						n21 = int(cpf[0]) * 11
						n22 = int(cpf[1]) * 10
						n23 = int(cpf[2]) * 9
						n24 = int(cpf[3]) * 8
						n25 = int(cpf[4]) * 7
						n26 = int(cpf[5]) * 6
						n27 = int(cpf[6]) * 5
						n28 = int(cpf[7]) * 4
						n29 = int(cpf[8]) * 3
						n210 = result1 * 2
						n211 = int(cpf[10])
						result1 = (11 - ((n21+n22+n23+n24+n25+n26+n27+n28+n29+n210) % 11))
					
						if(result1 == n11):
							if(n1 == n2 == n3 == n4 == n5 == n6 == n7 == n8 == n9 == n10 == n11):
								print("\033[01;31m[!]\033[00;00m CPF:",cpf,"\033[01;31m[Inválido!]\033[00;00m")
								input("\033[01;32m[*]\033[00;00m Pressione \033[01;33m[ENTER]\033[00;00m para continuar...")
								clear()
							else:	
								print("\033[01;32m[*]\033[00;00m CPF:",cpf,"\033[01;32m[Válido!]\033[00;00m")
								input("\033[01;32m[*]\033[00;00m Pressione \033[01;33m[ENTER]\033[00;00m para continuar...")
								clear()
						else:
							print("\033[01;31m[!]\033[00;00m CPF:",cpf,"\033[01;31m[Inválido!]\033[00;00m")
							input("\033[01;32m[*]\033[00;00m Pressione \033[01;33m[ENTER]\033[00;00m para continuar...")
							clear()
					else:
						print("\033[01;31m[!]\033[00;00m CPF:",cpf,"\033[01;31m[Inválido!]\033[00;00m")
						input("\033[01;32m[*]\033[00;00m Pressione \033[01;33m[ENTER]\033[00;00m para continuar...")
						clear()
				else:
					print("\033[01;31m[!]\033[00;00m Digite um CPF com onze digitos!")
					input("\033[01;32m[*]\033[00;00m Pressione \033[01;33m[ENTER]\033[00;00m para continuar...")
					clear()
			elif(int(opc) == 2):
				n1 = random.randint(0,9)
				n2 = random.randint(0,9)
				n3 = random.randint(0,9)
				n4 = random.randint(0,9)
				n5 = random.randint(0,9)
				n6 = random.randint(0,9)
				n7 = random.randint(0,9)
				n8 = random.randint(0,9)
				n9 = random.randint(0,9)

				result1 = (11 - ((n1*10 + n2*9 + n3*8 + n4*7 + n5*6 + n6*5 + n7*4 + n8*3 + n9*2) % 11))
				
				if(result1 > 9):
					result1 = 0
					n10 = result1
				else:
					n10 = result1
					n21 = n1 * 11
					n22 = n2 * 10
					n23 = n3 * 9
					n24 = n4 * 8
					n25 = n5 * 7
					n26 = n6 * 6
					n27 = n7 * 5
					n28 = n8 * 4
					n29 = n9 * 3
					n210 = n10 * 2
					result2 = (11 - ((n21+n22+n23+n24+n25+n26+n27+n28+n29+n210) % 11))
				
					if(result2 > 9):
						result2 = 0
						n11 = result2
					else:
						n11 = result2
					
					print("\033[01;32m[*]\033[00;00m CPF Gerado: \033[01;32m%i%i%i.%i%i%i.%i%i%i-%i%i\033[00;00m" % (n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11))
					input("\033[01;32m[*]\033[00;00m Pressione \033[01;33m[ENTER]\033[00;00m para continuar...")
					clear()
			elif(int(opc) == 3):
				exit(0)
			else:
				print("\033[01;31m[!]\033[00;00m Opção inválida!")
				input("\033[01;32m[*]\033[00;00m Pressione \033[01;33m[ENTER]\033[00;00m para continuar...")
				clear()

		except ValueError:
			print("\033[01;31m[!]\033[00;00m Digite apenas o número da opção!")
			input("\033[01;32m[*]\033[00;00m Pressione \033[01;33m[ENTER]\033[00;00m para continuar...")
			clear()
	
	while(True):
		main()

except KeyboardInterrupt:
	print("\n\033[01;31m[!]\033[00;00m Você decidiu sair!")
