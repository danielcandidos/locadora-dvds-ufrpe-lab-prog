

endereco_do_arq = "C:\\Users\\KF1\\Documents\\Proj_Locadora\\login.txt"
separador1 = "«"
separador2 = "»"

arq=open(endereco_do_arq,"r+")

usuarios = arq.readlines()
print usuarios

pesquisar_usuario = raw_input("Digite o nome do usuário que deseja pesquisar: ")

for u in usuarios:
    print u
    encontrado = u.find(pesquisar_usuario)
    print encontrado
