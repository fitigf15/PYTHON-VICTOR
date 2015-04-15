def futval():
	anysinversio = input("Aquest programa calcula el valor futur duna determinada inversio als anys que escriviu a continuació: ")
	principal = input("Entra la inversio inicial: ")
	apr = input("Entra linteres anual: ")
	for i in range(anysinversio):
            principal = principal * (1 + apr)
	print " La quantitat al cap de ", anysinversio, "anys es: ", principal, "."
futval()
