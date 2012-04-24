
endereco_do_arqlogin = "C:\\Users\KF1\\Desktop\\Proj Locadora\\Implementacoes\\login.txt"
endereco_do_arq_cad_func = "C:\\Users\\KF1\\Desktop\\Proj Locadora\\Implementacoes\\cadastro_funcionarios.txt"
separador1 = "«"
separador2 = "»"

arqlogin=open(endereco_do_arqlogin,"r")



usuarios = arqlogin.readlines()
tentativas = 0
passa = 0
if passa == 0:
    while (passa == 0) and (tentativas < 3):
        verificar_usuario = raw_input("Digite o seu nome de usuário: ")
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
            print "Usuário e/ou senha inválido(s).\n"

    if (passa == 1):
        if (tipo == 'g') or (tipo == 'a'):
            print "\n>>> Login efetuado com sucesso!"
        else:
            print "\n>>> Login não foi efetuado. Reinicie o sistema."

    if (tentativas >= 3) and (passa == 0):
        print "São permitidas apenas 3 (três) tentativas. O programa deve ser encerrado!"

    arqlogin.close()

dic_func = {}

if passa == 1:

    arq_cad_func = open(endereco_do_arq_cad_func,'r')
    dic_func = arq_cad_func.read()
    arq_cad_func.close()

    if tipo == 'g':
        print ">>> Você está logado como 'Gerente'.\n"

        atividade = input("O que deseja executar agora:\n\n1 - Cadastrar Funcionário\n2 - Atualizar Cadastro de Funcionário\n3 - Remover Cadastro de Funcionário\n4 - Cadastrar Cliente\n5 - Atualizar Cadastro de Cliente\n6 - Remover Cadastro de Cliente\n7 - Pesquisar Acervo\n8 - etc e tal\n9 - Sair\n> ")

        if atividade == 1:
            nome = raw_input("Informe o nome do funcionário a ser cadastrado*: ")
            cpf = raw_input("Infome o cpf(Apenas os números)*: ")
            endereco = raw_input("Informe o endereco*: ")
            cep = input("Informe o CEP(somente números)*: ")
            cidade = raw_input("Informe a Cidade*: ")
            estado = raw_input("informe o Estado*: ")
            tel = input("Informe o Tel: ")
            cel = input ("Informe o Cel: ")
            n_carteira = raw_input("Informe o número da carteira de trabalho: ")
            login_usuario = raw_input("Digite o nome de Login de usuário deste sistema: ")
            senha_usuario = raw_input("Digite a senha de acesso ao sistema, deste usuário: ")

            tipo_func = raw_input("Informe a função (Digite 'g' para 'Gerente' ou 'a' para 'Atendente'): ")
            while (tipo_func != 'g') and (tipo_func != 'a'):
                tipo_func = raw_input("\nInformação digitada incorretamente.\nInforme a função (Digite 'g' para 'Gerente' ou 'a' para 'Atendente'): ")
                tipo_func = tipo_func.lower()

            dic_func[cpf] = nome, endereco, cep, cidade, estado, tel, cel, n_carteira
            lista_dic_f = ['Nome:','Endereço:','CEP:','Cidade:','Estado:','Telefone:','Celular:','Carteira Profissional:']

            print "\nCPF:", cpf
            for a in range(0,len(lista_dic_f)):
                print lista_dic_f[a],dic_func[cpf][a]

            print dic_func

            arq_cad_func = open(endereco_do_arq_cad_func,'a')
            #arq_cad_func.write(xxxxxxxxxxxxxxxxxx)
            arq_cad_func.close()


        elif atividade == 2:
            pesquisar_func = raw_input("Pesquise o nome do funcionário que deseja atualizar o cadastro: ")
            arq_cad_func = open(endereco_do_arq_cad_func,'r')

            arq_cad_func.close()


    elif tipo == 'a':
        print ">>> Você está logado como 'Atendente'.\n"

        atividade = input("O que deseja executar agora:\n\n1 - Cadastrar Cliente\n2 - Atualizar Cadastro de Cliente\n3 - Pesquisar Acervo\n4 - etc e tal\n> ")

        if atividade == 1:
            nome = raw_input("Informe o nome do funcionário a ser cadastrado*: ")
            cpf = input("Infome o cpf(Apenas os números)*: ")
            endereco = raw_input("Informe o endereco*: ")
            cep = input("Informe o CEP(somente números)*: ")
            cidade = raw_input("Informe a Cidade*: ")
            estado = raw_input("informe o Estado*: ")
            tel = input("Informe o Tel: ")
            cel = input ("Informe o Cel: ")
            
