
endereco_do_arqlogin = "C:\\Users\KF1\\Desktop\\Proj Locadora\\Implementacoes\\login.txt"
endereco_do_arq_cad_func = "C:\\Users\\KF1\\Desktop\\Proj Locadora\\Implementacoes\\cadastro_funcionarios.txt"
separador1 = "�"
separador2 = "�"

arqlogin=open(endereco_do_arqlogin,"r")



usuarios = arqlogin.readlines()
tentativas = 0
passa = 0
if passa == 0:
    while (passa == 0) and (tentativas < 3):
        verificar_usuario = raw_input("Digite o seu nome de usu�rio: ")
        verificar_senha = raw_input("Digite sua senha: ")
        tentativas += 1

        for u in usuarios:
            divisor1 = u.find(separador1)
            divisor2 = u.find(separador2)
            usuario = u[0 : divisor1]
            senha = u[divisor1 + 1 : divisor2]
            #print usuario, senha
            if (verificar_usuario == usuario) and (verificar_senha == senha):
                passa = 1        
                tipo = u[divisor2 + 1 : -1]
                usuario_logado = usuario
                usuario = ""
                senha = ""
                break

        if passa == 0:
            print "Usu�rio e/ou senha inv�lido(s).\n"

    if (passa == 1):
        if (tipo == 'g') or (tipo == 'a'):
            print "\n>>> Login efetuado com sucesso!"
        else:
            print "\n>>> Login n�o foi efetuado. Reinicie o sistema."

    if (tentativas >= 3) and (passa == 0):
        print "S�o permitidas apenas 3 (tr�s) tentativas. O programa deve ser encerrado!"

    arqlogin.close()

dic_func = {}

if passa == 1:

    arq_cad_func = open(endereco_do_arq_cad_func,'r')
    dic_func = arq_cad_func.read()
    arq_cad_func.close()

    if tipo == 'g':
        print ">>> Voc� est� logado como 'Gerente'.\n"

        atividade = input("O que deseja executar agora:\n\n1 - Cadastrar Funcion�rio\n2 - Atualizar Cadastro de Funcion�rio\n3 - Remover Cadastro de Funcion�rio\n4 - Cadastrar Cliente\n5 - Atualizar Cadastro de Cliente\n6 - Remover Cadastro de Cliente\n7 - Pesquisar Acervo\n8 - etc e tal\n9 - Sair\n> ")

        if atividade == 1:
            nome = raw_input("Informe o nome do funcion�rio a ser cadastrado*: ")
            cpf = raw_input("Infome o cpf(Apenas os n�meros)*: ")
            endereco = raw_input("Informe o endereco*: ")
            cep = input("Informe o CEP(somente n�meros)*: ")
            cidade = raw_input("Informe a Cidade*: ")
            estado = raw_input("informe o Estado*: ")
            tel = input("Informe o Tel: ")
            cel = input ("Informe o Cel: ")
            n_carteira = raw_input("Informe o n�mero da carteira de trabalho: ")
            login_usuario = raw_input("Digite o nome de Login de usu�rio deste sistema: ")
            senha_usuario = raw_input("Digite a senha de acesso ao sistema, deste usu�rio: ")

            tipo_func = raw_input("Informe a fun��o (Digite 'g' para 'Gerente' ou 'a' para 'Atendente'): ")
            while (tipo_func != 'g') and (tipo_func != 'a'):
                tipo_func = raw_input("\nInforma��o digitada incorretamente.\nInforme a fun��o (Digite 'g' para 'Gerente' ou 'a' para 'Atendente'): ")
                tipo_func = tipo_func.lower()

            dic_func[cpf] = nome, endereco, cep, cidade, estado, tel, cel, n_carteira
            lista_dic_f = ['Nome:','Endere�o:','CEP:','Cidade:','Estado:','Telefone:','Celular:','Carteira Profissional:']

            print "\nCPF:", cpf
            for a in range(0,len(lista_dic_f)):
                print lista_dic_f[a],dic_func[cpf][a]

            print dic_func

            arq_cad_func = open(endereco_do_arq_cad_func,'a')
            #arq_cad_func.write(xxxxxxxxxxxxxxxxxx)
            arq_cad_func.close()


        elif atividade == 2:
            pesquisar_func = raw_input("Pesquise o nome do funcion�rio que deseja atualizar o cadastro: ")
            arq_cad_func = open(endereco_do_arq_cad_func,'r')

            arq_cad_func.close()


    elif tipo == 'a':
        print ">>> Voc� est� logado como 'Atendente'.\n"

        atividade = input("O que deseja executar agora:\n\n1 - Cadastrar Cliente\n2 - Atualizar Cadastro de Cliente\n3 - Pesquisar Acervo\n4 - etc e tal\n> ")

        if atividade == 1:
            nome = raw_input("Informe o nome do funcion�rio a ser cadastrado*: ")
            cpf = input("Infome o cpf(Apenas os n�meros)*: ")
            endereco = raw_input("Informe o endereco*: ")
            cep = input("Informe o CEP(somente n�meros)*: ")
            cidade = raw_input("Informe a Cidade*: ")
            estado = raw_input("informe o Estado*: ")
            tel = input("Informe o Tel: ")
            cel = input ("Informe o Cel: ")
            
