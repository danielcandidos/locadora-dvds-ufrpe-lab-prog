

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
                print "Os campos marcados com asterisco não podem ser vazios"
                Fun_ID = raw_input ("Digite o codigo do funcionário*.: ")
                Fun_nome = raw_input("Informe o nome do funcionário a ser cadastrado*: ")
                Fun_sexo = raw_input("Informe o sexo do funcionario*(M/F): " )
                Fun_cpf = raw_input("Infome o CPF(Apenas os números)*.: ")
                Fun_rg = raw_input("Informe o RG*.: ")
                Fun_endereco = raw_input("Informe o endereco*.: ")
                Fun_numero = raw_input("Informe o número da residência.*: ")
                Fun_complemento = raw_input("Informe o complemento.: ")
                Fun_bairro = raw_input("Informe o Bairro*.: ")
                Fun_cep = raw_input("Informe o CEP(somente números)*.: ")
                Fun_cidade = raw_input("Informe a Cidade*.: ")
                Fun_estado = raw_input("informe o Estado*.: ")
                Fun_tel = raw_input("Informe o Tel*.: ")
                Fun_cel = raw_input ("Informe o Cel*.: ")
                Fun_n_carteira = raw_input("Informe o número da carteira de trabalho do funcionário*.: ")
                Fun_admissao = raw_input('Informe a Data de Admissão (formato DD/MM/AAAA)*.: ')
                Fun_login_usuario = raw_input("Digite o nome de Login de usuário deste sistema*.: ")
                Fun_senha_usuario = raw_input("Digite a senha de acesso ao sistema, deste usuário*.: ")
                Fun_observacoes = raw_input ("Digite as observações sobre o funcionario.: ")
                Fun_funcao = raw_input ("Digite a função do funcionário*.: ")

                sql = "INSERT INTO funcionarios values ('"+Fun_ID+"','"+Fun_nome+"','"+Fun_sexo+"','"+Fun_cpf+"','"+Fun_rg+"','"+Fun_endereco+"','"+Fun_numero+"','"+Fun_complemento+"','"+Fun_bairro+"','"+Fun_cep+"','"+Fun_cidade+"','"+Fun_estado+"','"+Fun_tel+"','"+Fun_cel+"','"+Fun_n_carteira+"','"+Fun_admissao+"','"+Fun_login_usuario+"','"+Fun_senha_usuario+"','"+Fun_observacoes+"','"+Fun_funcao+"')"
                try:
                    cursor.execute(sql)
                    db.commit()
            
                except:
                    db.rollback()
            


            if atividade == 2:
                busca = raw_input ("Digite o CPF do funcionario que deseja atualizar os dados.: ")
                print 'Opcões de atualização.: '
                print ' 1-Para atualizar o código do funcionário.: '
                print ' 2-Para atualizar o nome do funcionário.: '
                print ' 3-Para atualizar o sexo do funcionário.: '
                print ' 4-Para atualizar o CPF do funcionário.: '
                print ' 5-Para atualizar o RG do funcionário.: '
                print ' 6-Para atualizar o endereço do funcionário.: '
                print ' 7-Para atualizar o número da residência do funcionário.: '
                print ' 8-Para atualizar complementos das informações sobre a residência.: '
                print ' 9-Para atualizar o bairro do fucionário.: '
                print '10-Para atualizar o CEP do funcionário.: '
                print '11-Para atualizar a cidade do funcioáro.: '
                print '12-Para atualizar o estado do funcionário.: '
                print '13-Para atualizar o número de telefone do funcionário.: '
                print '14-Para atualizar o celular de telefone do funcionário.: '
                print '15-Para atualizar o número de carteira de trabalho do funcionário.: '
                print '16-Para atualizar a data de admissão do funcionário.: '
                print '17-Para atualizar o login do funcionário.: '
                print '18-Para atualizar a senha do funcionário.: '
                print '19-Para atulizar as observações sobre o funcionário.: '
                print '20-Para atualizar a função do funcionário\n.: '

##   lembrete: utilizar dicionários para saber se um cpf está presente no banco de dados ou não.
                campo = input ("Digite o campo deseja quer atualizar.:")

                if campo == 1:
                    novoFun_ID = raw_input ("Redefina o código do funcionário.: ")
                    sql = "update funcionarios set Fun_ID = '"+novoFun_ID+"' where Fun_cpf = '"+busca+"'"
                    try:
                        cursor.execute(sql)
                        db.commit()
            
                    except:
                        db.rollback()
              

                elif campo == 2:
                    novoFun_nome = raw_input ("Redefina o nome do funcionário.: ")
                    sql = "update funcionarios set Fun_nome = '"+novoFun_nome+"' where Fun_cpf = '"+busca+"'"
                    try:
                        cursor.execute(sql)
                        db.commit()
            
                    except:
                        db.rollback()
                  
                    
                elif campo == 3:
                     novoFun_sexo = raw_input ("Redefina o sexo do funcionário.: ")
                     sql = "update funcionarios set Fun_sexo = '"+novoFun_sexo+"' where Fun_cpf = '"+busca+"'"
                     try:
                         cursor.execute(sql)
                         db.commit()
                     except:
                         db.rollback()
                   

                elif campo == 4:
                    novoFun_cpf = raw_input ("Redefina o CPF do funcionário.: ")
                    sql = "update funcionarios set Fun_cpf = '"+novoFun_cpf+"' where Fun_cpf = '"+busca+"'"
                    try:
                        cursor.execute(sql)
                        db.commit()
            
                    except:
                        db.rollback()
              

                elif campo == 5:
                    novoFun_rg = raw_input ("Redefina o RG do funcionário.: ")
                    sql = "update funcionarios set Fun_rg = '"+novoFun_rg+"' where Fun_cpf = '"+busca+"'"
                    try:
                        cursor.execute(sql)
                        db.commit()
            
                    except:
                        db.rollback()
                 

                elif campo == 6:
                    novoFun_endereco = raw_input ("Redefina o endereço do funcionário.: ")
                    sql = "update funcionarios set Fun_endereco = '"+novoFun_endereco+"' where Fun_cpf = '"+busca+"'"
                    try:
                        cursor.execute(sql)
                        db.commit()
            
                    except:
                        db.rollback()
                

                
                elif campo == 7:
                    novoFun_numero = raw_input ("Redefina o numero da residência do funcionário.: ")
                    sql = "update funcionarios set Fun_numero = '"+novoFun_numero+"' where Fun_cpf = '"+busca+"'"
                    try:
                        cursor.execute(sql)
                        db.commit()
            
                    except:
                        db.rollback()
          

                
                elif campo == 8:
                    novoFun_complemento= raw_input ("Redefina o complemento sobre a residência do funcionário.: ")
                    sql = "update funcionarios set Fun_complemento = '"+novoFun_complemento+"' where Fun_cpf = '"+busca+"'"
                    try:
                        cursor.execute(sql)
                        db.commit()
            
                    except:
                        db.rollback()
                   

                elif campo == 9:
                    novoFun_bairro = raw_input ("Redefina o bairro do funcionário.: ")
                    sql = "update funcionarios set Fun_bairro = '"+novoFun_bairro+"' where Fun_cpf = '"+busca+"'"
                    try:
                        cursor.execute(sql)
                        db.commit()
            
                    except:
                        db.rollback()
                    

                elif campo == 10:
                    novoFun_cep = raw_input ("Redefina CEP do funcionário.: ")
                    sql = "update funcionarios set Fun_cep = '"+novoFun_cep+"' where Fun_cpf = '"+busca+"'"
                    try:
                        cursor.execute(sql)
                        db.commit()
            
                    except:
                        db.rollback()
                    

                elif campo == 11:
                    novoFun_cidade = raw_input ("Redefina a cidade do funcionário.: ")
                    sql = "update funcionarios set Fun_cidade = '"+novoFun_cidade+"' where Fun_cpf = '"+busca+"'"
                    try:
                        cursor.execute(sql)
                        db.commit()
            
                    except:
                        db.rollback()
                   

                elif campo == 12:
                    novoFun_estado = raw_input ("Redefina o estado: ")
                    sql = "update funcionarios set Fun_estado = '"+novoFun_estado+"' where Fun_cpf = '"+busca+"'"
                    try:
                        cursor.execute(sql)
                        db.commit()
            
                    except:
                        db.rollback()
                    

                elif campo == 13:
                    novoFun_tel= raw_input ("Redefina o telefone do funcionário.: ")
                    sql = "update funcionarios set Fun_tel = '"+novoFun_tel+"' where Fun_cpf = '"+busca+"'"
                    try:
                        cursor.execute(sql)
                        db.commit()
            
                    except:
                        db.rollback()
                   

                elif campo == 14:
                    novoFun_cel = raw_input ("Redefina o celular do funcionário.: ")
                    sql = "update funcionarios set Fun_cel = '"+novoFun_cel+"' where Fun_cpf = '"+busca+"'"
                    try:
                        cursor.execute(sql)
                        db.commit()
            
                    except:
                        db.rollback()
                   

                elif campo == 15:
                    novoFun_n_carteira= raw_input ("Redefina o o número de carteira de trabalho do funcionário.: ")
                    sql = "update funcionarios set Fun_n_carteira = '"+novoFun_n_carteira+"' where Fun_cpf = '"+busca+"'"
                    try:
                        cursor.execute(sql)
                        db.commit()
            
                    except:
                        db.rollback()
                    

                elif campo == 16:
                    novoFun_admissao= raw_input ("Redefina a data de admissão do funcionário.: ")
                    sql = "update funcionarios set Fun_admissao = '"+novoFun_admissao+"' where Fun_cpf = '"+busca+"'"
                    try:
                        cursor.execute(sql)
                        db.commit()
            
                    except:
                        db.rollback()
                    
                    
                elif campo == 17:
                    novoFun_login_usuario= raw_input ("Redefina o login do funcionário.: ")
                    sql = "update funcionarios set Fun_login_usuario = '"+novoFun_login_usuario+"' where Fun_cpf = '"+busca+"'"
                    try:
                        cursor.execute(sql)
                        db.commit()
            
                    except:
                        db.rollback()
                    

                elif campo == 18:
                    novoFun_senha_login = raw_input ("Redefina a senha do funcionário.: ")
                    sql = "update funcionarios set Fun_senha_login = '"+novoFun_senha_login+"' where Fun_cpf = '"+busca+"'"
                    try:
                        cursor.execute(sql)
                        db.commit()
            
                    except:
                        db.rollback()
                    

                elif campo == 19:
                    novoFun_observacoes = raw_input ("Redefina as observações sobre funcionário.: ")
                    sql = "update funcionarios set Fun_observacoes = '"+novoFun_observacoes+"' where Fun_cpf = '"+busca+"'"
                    try:
                        cursor.execute(sql)
                        db.commit()
            
                    except:
                        db.rollback()
                    

                elif campo == 20:
                    novoFun_funcao= raw_input ("Redefina a função do funcionário.: ")
                    sql = "update funcionarios set Fun_funcao = '"+novoFun_funcao+"' where Fun_cpf = '"+busca+"'"
                    try:
                        cursor.execute(sql)
                        db.commit()
            
                    except:
                        db.rollback()
                    

                


            if atividade == 3:
                busca = raw_input ("Digite o CPF do funcionario que deseja deletar os dados.: ")

                sql = "delete from funcionarios where Fun_cpf = '"+busca+"'\n"
                print 'Os dados do funcionário foram deletados'

                try:
                    cursor.execute(sql)
                    db.commit()
                except:
                    db.rollback()


            if atividade == 15: break

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
