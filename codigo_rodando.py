
##Obs: Código feito por: Felix Neto, Gutemberg, Robson Müller, Daniel Candido.

import MySQLdb
db = MySQLdb.connect('localhost','root','mugen','projeto')
cursor = db.cursor()


##
##endereco_do_arqlogin = "C:\\Users\\ADM\\Documents\\login.txt"
##endereco_do_arq_cad_func = "C:\\Users\\ADM\\Documents\\cadastro_funcionarios.txt"
##separador1 = "«"
##separador2 = "»"
##
##arqlogin=open(endereco_do_arqlogin,"r")
##
##usuarios = arqlogin.readlines()
##
##tentativas = 0
##passa = 0
##
### Efetuando login no Sistema
##if passa == 0:
##    while (passa == 0) and (tentativas < 3):
##        verificar_usuario = raw_input("Digite o seu nome de usuário: ")
##        verificar_senha = raw_input("Digite sua senha: ")
##        tentativas += 1
##        # Pesquisando por usuarios e suas respectivas senhas (no arquivo)
##        for u in usuarios:
##            divisor1 = u.find(separador1)
##            divisor2 = u.find(separador2)
##            usuario = u[0 : divisor1]
##            senha = u[divisor1 + 1 : divisor2]
##            #print usuario, senha
##
##            # Verificação de senha do usuario
##            if (verificar_usuario == usuario) and (verificar_senha == senha):
##                passa = 1        
##                tipo = u[divisor2 + 1 : -1]
##                usuario_logado = usuario
##                usuario = ""
##                senha = ""
##                break
##
##        if passa == 0:
##            print "Usuário e/ou senha inválido(s).\n"
##
##    if (passa == 1):
##        if (tipo == 'g') or (tipo == 'a'):
##            print "\n>>> Login efetuado com sucesso!"
##        else:
##            print "\n>>> Login não foi efetuado. Reinicie o sistema."
##
##    # Encerramento do sistema após 3 tentativas de login mal sucedidas
##    if (tentativas >= 3) and (passa == 0):
##        print "São permitidas apenas 3 (três) tentativas. O sistema deve ser encerrado!"
##
##arqlogin.close()
##
##dic_func = {}

passa = 1
tipo = 'g'

if passa == 1:
##
##    arq_cad_func = open(endereco_do_arq_cad_func,'r')
##    linhas_cf = arq_cad_func.readlines()
##    arq_cad_func.close()
##
##    for t in linhas_cf:
##        dois_pontos = t.find(":")
###        print dois_pontos

    # Tipo de funcionário (Logado): Gerente
    if tipo == 'g':
        print ">>> Você está logado como 'Gerente'."

        fica = 1
        # Condição de encerramento do Sistema
        while fica == 1:

            atividade = input("\n> O que deseja executar agora?\n\n1 - Cadastrar Funcionário\n2 - Atualizar Cadastro de Funcionário\n3 - Remover Cadastro de Funcionário\n4 - Cadastrar Cliente\n5 - Atualizar Cadastro de Cliente\n6 - Remover Cadastro de Cliente\n7 - Cadastrar Filme no Acervo\n8 - Atualizar Cadastro de Filme no Acervo\n9 - Excluir Filme do Acervo\n10 - Pesquisar Acervo\n11 - Reservar Filme\n12 - Efetuar Locação\n13 - Efetuar Devolução\n14 - etc e tal\n15 - Sair\n> ")
##            usuario_modificador = usuario_logado
            # Cadastrar Funcionário
            if atividade == 1:
                Fun_ID = raw_input ("Digite o codigo do funcionário.: ")
                Fun_nome = raw_input("Informe o nome do funcionário a ser cadastrado*: ")
                Fun_sexo = raw_input("Informe o sexo do funcionario*(M/F): " )
                Fun_cpf = raw_input("Infome o CPF(Apenas os números)*: ")
                Fun_rg = raw_input("Informe o RG: ")
                Fun_endereco = raw_input("Informe o endereco*: ")
                Fun_numero = raw_input("Informe o número da residência: ")
                Fun_complemento = raw_input("Informe o complemento (se houver): ")
                Fun_bairro = raw_input("Informe o Bairro: ")
                Fun_cep = raw_input("Informe o CEP(somente números)*: ")
                Fun_cidade = raw_input("Informe a Cidade*: ")
                Fun_estado = raw_input("informe o Estado*: ")
                Fun_tel = raw_input("Informe o Tel: ")
                Fun_cel = raw_input ("Informe o Cel: ")
                Fun_n_carteira = raw_input("Informe o número da carteira de trabalho do funcionário: ")
                Fun_admissao = raw_input('Informe a Data de Admissão (formato DD/MM/AAAA): ')
                Fun_login_usuario = raw_input("Digite o nome de Login de usuário deste sistema: ")
                Fun_senha_usuario = raw_input("Digite a senha de acesso ao sistema, deste usuário: ")
                Fun_observacoes = raw_input ("Digite as observaçoes sobre o funcionario.: ")
                Fun_funcao = raw_input ("Digite a funcao do funcionario.: ")

                sql = "INSERT INTO funcionarios values ('"+Fun_ID+"','"+Fun_nome+"','"+Fun_sexo+"','"+Fun_cpf+"','"+Fun_rg+"','"+Fun_endereco+"','"+Fun_numero+"','"+Fun_complemento+"','"+Fun_bairro+"','"+Fun_cep+"','"+Fun_cidade+"','"+Fun_estado+"','"+Fun_tel+"','"+Fun_cel+"','"+Fun_n_carteira+"','"+Fun_admissao+"','"+Fun_login_usuario+"','"+Fun_senha_usuario+"','"+Fun_observacoes+"','"+Fun_funcao+"')"
                try:
                    cursor.execute(sql)
                    db.commit()
            
                except:
                    db.rollback()
                db.close()


            if atividade == 2:
                Busca = raw_input ("Digite o CPF do funcionario que deseja atualizar os dados.: ")
                campo = raw_input ("Digte o campo que quer atualizar.:")
                if campo == Fun_ID:
                    novoFun_ID = input ("Digite o novo código do funcionário.: ")
                    sql = """update funcionarios set Fun_ID = '"+novoFun_ID+"' where Fun_cpf = '"+Busca+"'"""

                    cursor.execute(sql)
                    db.close()

                    
            
                

##                tipo_func = raw_input("Informe a função (Digite 'g' para 'Gerente' ou 'a' para 'Atendente'): ")
##                while (tipo_func != 'g') and (tipo_func != 'a'):
##                    tipo_func = raw_input("\nInformação digitada incorretamente.\nInforme a função (Digite 'g' para 'Gerente' ou 'a' para 'Atendente'): ")
##                    tipo_func = tipo_func.lower()
##
##                dic_func[cpf] = nome, rg, endereco, numero, complemento, bairro, cep, cidade, estado, tel, cel, n_carteira, admissao
##                lista_dic_f = ['Nome:','RG:','Endereço:', 'Número: ', 'Complemento: ', 'Bairro: ','CEP:','Cidade:','Estado:','Telefone:','Celular:','Carteira Profissional:','Data de Admissao: ']
##
##                print "\nCPF:", cpf
##                for a in range(0,len(lista_dic_f)):
##                    print lista_dic_f[a],dic_func[cpf][a]

    #            print dic_func

##                arqlogin=open(endereco_do_arqlogin,"a")
##                arqlogin.write(login_usuario+separador1+senha_usuario+separador2+tipo_func+'\n')
##                arqlogin.close()
##
##                arq_cad_func = open(endereco_do_arq_cad_func,'r')
##                linhas = arq_cad_func.readlines()
##    ##            print linhas
##                arq_cad_func.close()
##
##
##    ## for para escrita no arquivo.
##                arq_cad_func = open(endereco_do_arq_cad_func,'a')
##
##                for chave1,valor1 in dic_func.iteritems():
##                    chave1 = str(chave1)
##                    valor1 = str(valor1)
##                    arq_cad_func.write(chave1+":"+valor1+'\n')
##                arq_cad_func.close()
##
####             Atualizar cadastro de Funcionário
##            elif atividade == 2:
##                pesquisar_func = raw_input("Pesquise o nome do funcionário que deseja atualizar o cadastro: ")
##               
##
##                arq_cad_func = open(endereco_do_arq_cad_func,'r')
##
##                linhas = arq_cad_func.readlines()
####                print linhas
##                arq_cad_func.close()
##                if linhas == []:
##                    print "Não ha funcionário cadastrado"
##                   
##                else:
##                    google = []
##                    for lin in linhas:
##                        lin = lin.rstrip('\n')
##                        google.append(lin.split(':'))
#### GOOGLE = A LISTA DE LINHAS SEM O \N E SEPARADA PELOS DOIS PONTOS
##                    arq_cad_func.close()
##                    lista_dados = []
##                    for vari_avel in google:
##                        iniciar_dados = vari_avel[1]
##                        iniciar_separacao = iniciar_dados.strip("(").strip(")").split(", ")
##                       
##                        del iniciar_separacao[-1]
##                    lista_strip = []
##                    for strip in iniciar_separacao:
##                        strip = strip.strip("'")
##                        lista_strip.append(strip)
##                    print "strip",lista_strip
##                       
####                        iniciar_separacao = iniciar_separacao.split(',')
##                       
##                       
##                       
####                        lista_dados.append(iniciar_separacao)
####
##                    print "eu",iniciar_separacao
####                    for juju in iniciar_separacao:
####                        print '>',juju
##
##            # Sair do sistema
##            elif atividade == 15:
##                logout = ''
##                while (logout != 's') and (logout != 'n'):
##                    logout = raw_input('Tem certeza que deseja sair? (s/n) \n> ')
##                    logout = logout.lower()
##                    if logout == 's':
##                        fica = 0
##
##            # Opções não implementadas
##            elif (atividade > 1) and (atividade < 15) and (type(atividade) == int):
##                print "Opção ainda não implementada."
##
##            # Quando escolhida uma opção diferente das previstas
##            else:
##                print "Opção Inválida."
##               
##    # Tipo de Funcionário (Logado): Atendente
##    elif tipo == 'a':
##        print ">>> Você está logado como 'Atendente'.\n"
##
##        fica = 1
##        #Condição de encerramento do Sistema
##        while fica == 1:
##
##            atividade = input("\n> O que deseja executar agora?\n\n1 - Cadastrar Cliente\n2 - Atualizar Cadastro de Cliente\n3 - Cadastrar Filme no Acervo\n4 - Atualizar Cadastro de Filme no Acervo\n5 - Pesquisar Acervo\n6 - Reservar Filme\n7 - Efetuar Locação\n8 - Efetuar Devolução\n9 - etc e tal\n10 - Sair\n> ")
##
##            # Cadastrar Cliente
##            if atividade == 1:
##                usuario_modificador = usuario_logado
##                nome = raw_input("Informe o nome do Cliente a ser cadastrado*: ")
##                cpf = input("Infome o cpf(Apenas os números)*: ")
##                endereco = raw_input("Informe o endereco*: ")
##                cep = input("Informe o CEP(somente números): ")
##                cidade = raw_input("Informe a Cidade*: ")
##                estado = raw_input("informe o Estado*: ")
##                tel = input("Informe o Telefone Fixo: ")
##                cel = input ("Informe o Telefone Celular: ")
##                print '\nCliente Cadastrado com Sucesso!'
##                print '(Ainda não foi implementada a ADIÇÃO a arquivo do cadastro de clientes.)'
##
##            elif atividade == 10:
##                logout = ''
##                while (logout != 's') and (logout != 'n'):
##                    logout = raw_input('Tem certeza que deseja sair? (s/n) \n> ')
##                    logout = logout.lower()
##                    if logout == 's':
##                        fica = 0
##
##            elif (atividade > 1) and (atividade < 10) and (type(atividade) == int):
##                print "Opção ainda não implementada."
##
##            else:
##                print "Opção Inválida."
##
##
###print google
##               
###print linhas
