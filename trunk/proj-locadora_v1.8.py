
#upado por Jose Clodoalves(Carpina), Robson Müller, Daniel Candido, Felix Neto, Gutenberg Duarte
import MySQLdb
import calendar
import datetime

db = MySQLdb.connect('localhost','root','mugen','projeto')
cursor = db.cursor()
s = 1
b = 0
i = 0
l = 0
d = 0
e = 0
w = 0
o = 0
sql = ""
cargo = ""


#
# Baseado no exposto no site: http://kykocamp.blogspot.com.br/2007/09/manipulando-datas-em-python.html
#



listanum = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
invalida = 1

diasemana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

data = ''
novadata = ''
dia = ''
mes = ''
ano = ''
novodia = 0
novomes = 0
novoano = 0
entrou = []









#########################################################################################################################################################





print "Faça o login no sistema.:"
while cargo == "":
    login = raw_input ("Digite o login.: ")
    login = login.lower()
    senha = raw_input ("Digite a senha.: ")
    if ((login == "") or (senha == "")):
        continue
    else:
        sql = "select * from cadastro_funcionarios where login like '"+login+"'"

        cursor.execute(sql)

        results = cursor.fetchall()
        for row in results:
            l = row[0]
         

        sql = "select * from cadastro_funcionarios where senha like '"+senha+"'"
        cursor.execute(sql)

        results = cursor.fetchall()
        for row in results:
            d = row[1]
           


        if login == str(l) and senha == str(d):
            cargo = 'a'
            print'Você está logado como atendente'
            break
        ##elif login != str(l) and senha == str(d):
        ##    cargo = 'erro'
        ##    print 'erro'


        else:   
            sql = "select * from cadastro_gerente where login like '"+login+"'"
            cursor.execute(sql)

            results = cursor.fetchall()
            for row in results:
                w = row[0]
##                print str(w)

            sql = "select * from cadastro_gerente  where senha like '"+senha+"'"
            cursor.execute(sql)

            results = cursor.fetchall()
            for row in results:
                e = row[1]
##                print str(e)



            if login == str(w) and senha == str(e):
                cargo = 'g'
                print 'Você está logado como gerente'
                break
            else:
                continue


fica = 1

        
while fica==1:
    if cargo == 'a':
        atividade = input("\n> O que deseja executar agora?\n\n1 - Cadastrar Funcionário\n2 - Cadastrar Cliente\n3 - Cadastrar Filme no Acervo\n4 - Pesquisar Acervo\n5 - Reservar Filme\n6 - Efetuar Locação\n7 - Efetuar Devolução\n8 - Sair\n> ")
        if atividade == 1:
            sql = "select * from funcionarios" 
            cursor.execute(sql)
            print 'Os funcionários inseridos no sistema são.: '
            results = cursor.fetchall()
            for row in results:
                e = row[1]
##                print e
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                e = row[0]
                d = int(e) + 1
          
            print "Os campos marcados com asterisco não podem ser vazios"     
            Fun_ID = str(d)
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
            if Fun_funcao == 'a':
                sql = "insert into cadastro_funcionarios values ('"+Fun_login_usuario+"','"+Fun_senha_usuario+"')"
                try:
                    cursor.execute(sql)
                    db.commit()
                except:
                    db.rollback()
                    
            elif Fun_funcao =='g':
                 sql = "insert into cadastro_gerente values ('"+Fun_login_usuario+"','"+Fun_senha_usuario+"')"
                 try:
                     cursor.execute(sql)
                     db.commit()
                 except:
                     db.rollback()
                
           

            sql = "INSERT INTO funcionarios values ('"+Fun_ID+"','"+Fun_nome+"','"+Fun_sexo+"','"+Fun_cpf+"','"+Fun_rg+"','"+Fun_endereco+"','"+Fun_numero+"','"+Fun_complemento+"','"+Fun_bairro+"','"+Fun_cep+"','"+Fun_cidade+"','"+Fun_estado+"','"+Fun_tel+"','"+Fun_cel+"','"+Fun_n_carteira+"','"+Fun_admissao+"','"+Fun_login_usuario+"','"+Fun_senha_usuario+"','"+Fun_observacoes+"','"+Fun_funcao+"')"
            try:
                cursor.execute(sql)
                db.commit()

            except:
                db.rollback()
        elif atividade == 2:
            print "Os campos marcados com asterisco não podem ser vazios"
            sql = "select * from clientes"
            cursor.execute(sql)
            print 'Os clientes inseridos no sistema são.: '
            results = cursor.fetchall()
            for row in results:
                e = row[1]
                print e
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                w = 0
                e = row[0]
                d = int(e) + 1 + w
                print e
                print d

            Cli_ID = str(d)
            Cli_nome = raw_input ("Digite o nome do cliente*.: ")
            Cli_sexo = raw_input ("Digite o sexo do cliente*.: ")
            Cli_endereco = raw_input ("Digite o endereco do cliente*.: ")
            Cli_numero = raw_input ("Digite o numero da residencia do cliente*.: ")
            Cli_complemento = raw_input ("Digite as informações adicionais sobre o endereço do cliente.: ")
            Cli_bairro = raw_input ("Digite o bairro do cliente*.: ")
            Cli_cep = raw_input ("Digite o CEP do cliente*.: ")
            Cli_cidade = raw_input ("Digite a cidade do cliente*.: ")
            Cli_estado = raw_input ("Digite o estado do cliente*.: ")
            Cli_telefone = raw_input ("Digite o número do telefone do cliente.: ")
            Cli_celular = raw_input ("Digite o número do celular do cliente*.: ")
            Cli_observacoes = raw_input ("Digite as informações adicionais sobre o cliente.: ")
            Cli_CPF = raw_input ("Digite o CPF do cliente.: ")
            Cli_saldo = str(0.0)

            sql = "insert into clientes values ('"+Cli_ID+"','"+Cli_nome+"', '"+Cli_sexo+"', '"+Cli_endereco+"', '"+Cli_numero+"', '"+Cli_complemento+"','"+Cli_bairro+"', '"+Cli_cep+"','"+Cli_cidade+"', '"+Cli_estado+"', '"+Cli_telefone+"', '"+Cli_celular+"','"+Cli_observacoes+"','"+Cli_CPF+"','"+Cli_saldo+"')"

            try:
                cursor.execute(sql)
                db.commit ()

            except:
                db.rollback()
            
            
                
        elif atividade == 3:
            sql = "select * from filme" 
            print 'Os filmes inseridos no sistema são.: '
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                e = row[1]
                print e
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                w = row[0]
                d = int(w) + 1
            Fil_ID = str(d)
            Fil_nome = raw_input ("Digite o nome do filme.: ")
            Fil_genero = raw_input ("Digite o gênero do filme.: ")
            Fil_class_et = raw_input ("Digite a classe etária do filme.: ")
            Fil_observacoes = raw_input ("Digite informações adicionais sobre o filme.: ")
           
            sql = "insert  filme values ('"+Fil_ID+"','"+Fil_nome+"','"+Fil_genero+"','"+Fil_class_et+"','"+Fil_observacoes+"')"
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()
        elif atividade == 4:
            print 'Pesquisa de cadastro de filme'
            sql = "select * from filme" 
            cursor.execute(sql)
            print 'Os filmes cadastrados no sistema são.: '
            results = cursor.fetchall()
            for row in results:
                w = row[1]
                print w
            print 'Pesquisa de disponibilidade de filme para locacao.: '
##          Pesquisa da variável busca na coluna Loc_filme da tabela locacao
            busca = raw_input ("Digite o nome do filme.: ")

            sql = "select * from locacao where Loc_filme like '"+busca+"'"
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                e = row[2]
                print str(e)
##          Pesquisa da variável busca na coluna Fil_nome da tabela filme
            sql = "select * from filme where Fil_nome like '"+busca+"'"
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                d = row[1]
                print str(d)

            if busca == str(e) and busca == str(d):
                print 'O filme já está locado'
            elif busca != str(e) and busca == str(d):
                print 'O fime está disponível para locacao'
            elif busca != str(e) and busca != str(d):
                print 'O filme não existe no acervo'
                
            
        elif atividade == 5:
            sql = "select * from filme" 
            cursor.execute(sql)
            print 'Os filmes cadastrados no sistema são.: '
            results = cursor.fetchall()
            for row in results:
                w = row[1]
                print w
                
            busca = raw_input ("Digite o filme que deseja reservar.: ")
            sql = "select * from locacao where Loc_filme like '"+busca+"'"
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                e = row[2]
               
            sql = "select * from filme where Fil_nome like '"+busca+"'"
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                d = row[1]
          
            if str(d) != busca:
                print 'O filme não está cadastrado no sistema'
            elif str(d) == busca:
                if busca == str(e) and busca == str(d):
                    print 'O filme já está locado'
                elif busca != str(e) and busca == str(d):
                    print 'O filme está disponível para locacao'
                    sql = "select * from clientes" 
                    cursor.execute(sql)
                    print 'Os clientes inseridos no sistema são.: '
                    results = cursor.fetchall()
                    for row in results:
                        l = row[1]
                        print l
                    busca1 = raw_input ("Digite o nome do cliente que deseja reservar o filme.: ")
                    sql = "select * from clientes where Cli_nome like '"+busca1+"'"
                    cursor.execute(sql)
                    results = cursor.fetchall()
                    for row in results:
                        i = row[0]
                        l = row[1]
                    if str(l) != busca1:
                        print 'Este usuário não está cadastrado no sistema'
                    elif str(l) == busca1:
                        Res_ID = i
                        Res_nome = l
                        Res_filme = busca
                        Res_data = raw_input ("Digite uma data para a reserva do filme.: ")
                        sql ="insert into reserva values ('"+Res_ID+"','"+Res_nome+"','"+Res_filme+"','"+Res_data+"')"
                        try:
                            cursor.execute(sql)
                            db.commit()
                        except:
                            db.rollback()
                
                elif busca != str(e) and busca != str(d):
                    print 'O filme não existe no acervo'
            
        elif atividade == 6:
            sql = "select * from clientes"
            cursor.execute(sql)
            print 'Os clientes inseridos no sistema são.: '
            results = cursor.fetchall()
            for row in results:
                e = row[1]
                print e
            sql = "select * from filme" 
            cursor.execute(sql)
            print 'Os filmes cadastrados no sistema são.: '
            results = cursor.fetchall()
            for row in results:
                w = row[1]
                print w
                    
            x = raw_input ("Digite um nome do cliente para a pesquisa de seu registro no banco de dados.: ")
            sql = "select * from clientes where Cli_nome like '"'%'+x+'%'"'"
            cursor.execute(sql)

            results = cursor.fetchall()
            for row in results:
                e = row[0]
                l = row[1]
                print'Código do cliente.:', e
                print'Nome do cliente.:',l
            if x !=l:
                print 'O cliente não está cadastrado no sistema'
            elif x == l:
                Loc_ID_cliente = e
                Loc_cliente = l
                Loc_filme = raw_input ("Digite o nome do filme.: ")
                Loc_data = raw_input ("Digite a data de locacao de filme.: ")
                Loc_devolucao = raw_input ("Digite a data de devolucao do filme.: ")

                sql = "insert into locacao values ('"+Loc_ID_cliente+"', '"+Loc_cliente+"','"+Loc_filme+"','"+Loc_data+"','"+Loc_devolucao+"')"

                try:
                    cursor.execute(sql)
                    db.commit()
                except:
                    db.rollback()
        elif atividade == 7:
            print 'Os filmes que estão locados sao.: '
            sql = "select * from locacao"
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                e = row[2]
                print e
            busca = raw_input ('Digite o filme que será devolvido.: ')
            sql = "delete from locacao where Loc_filme = '"+busca+"'"
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()
            
        elif atividade == 8:
            exit()
            
  
    elif cargo == 'g':
        atividade = input("\n> O que deseja executar agora?\n\n1 - Cadastrar Funcionário\n2 - Atualizar Cadastro de Funcionário\n3 - Remover Cadastro de Funcionário\n4 - Cadastrar Cliente\n5 - Atualizar Cadastro de Cliente\n6 - Remover Cadastro de Cliente\n7 - Cadastrar Filme no Acervo\n8 - Atualizar Cadastro de Filme no Acervo\n9 - Excluir Filme do Acervo\n10 - Pesquisar Acervo\n11 - Efetuar Locação\n12 - Efetuar Devolução\n13 - Sair\n> ")
        sql = "select * from funcionarios"
        o = ""
        
        if atividade == 1:
            sql = "select * from funcionarios" 
            cursor.execute(sql)
            print 'Os funcionários inseridos no sistema são.: '
            results = cursor.fetchall()
            for row in results:
                e = row[1]
                print e
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                p = row[0]
                d = int(p) + 1
        
            print "Os campos marcados com asterisco não podem ser vazios"
            Fun_ID = str(d)
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
            if Fun_funcao == 'a':
                sql = "insert into cadastro_funcionarios values ('"+Fun_login_usuario+"','"+Fun_senha_usuario+"')"
                try:
                    cursor.execute(sql)
                    db.commit()
                except:
                    db.rollback()
                    
            elif Fun_funcao =='g':
                sql = "insert into cadastro_gerente values ('"+Fun_login_usuario+"','"+Fun_senha_usuario+"')"

                try:
                    cursor.execute(sql)
                    db.commit()
                except:
                    db.rollback()
           

            sql = "INSERT INTO funcionarios values ('"+Fun_ID+"','"+Fun_nome+"','"+Fun_sexo+"','"+Fun_cpf+"','"+Fun_rg+"','"+Fun_endereco+"','"+Fun_numero+"','"+Fun_complemento+"','"+Fun_bairro+"','"+Fun_cep+"','"+Fun_cidade+"','"+Fun_estado+"','"+Fun_tel+"','"+Fun_cel+"','"+Fun_n_carteira+"','"+Fun_admissao+"','"+Fun_login_usuario+"','"+Fun_senha_usuario+"','"+Fun_observacoes+"','"+Fun_funcao+"')"
            try:
                cursor.execute(sql)
                db.commit()

            except:
                db.rollback()
            
        elif atividade == 2:
            sql = "select * from funcionarios" 
            cursor.execute(sql)
            print 'Os funcionários inseridos no sistema são.: '
            results = cursor.fetchall()
            for row in results:
                e = row[1]
                d = row[3]
                print 'Nome =>',str (e),'CPF =>', str(d)
            busca = raw_input ("Digite o cpf do funcionário que deseja alterar os dados.: ")
            sql = "select * from funcionarios where Fun_cpf like '"+busca+"'"
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                d = row[3]
            
            if busca != str(d):
                 print 'O funcionário não está cadastrado no sistema'
            elif busca == str(d):
                 print 'O funcionário está cadastrado no sistema.:'
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
                 print '11-Para atualizar a cidade do funcionário.: '
                 print '12-Para atualizar o estado do funcionário.: '
                 print '13-Para atualizar o número de telefone do funcionário.: '
                 print '14-Para atualizar o celular de telefone do funcionário.: '
                 print '15-Para atualizar o número de carteira de trabalho do funcionário.: '
                 print '16-Para atualizar a data de admissão do funcionário.: '
                 print '17-Para atualizar o login do funcionário.: '
                 print '18-Para atualizar a senha do funcionário.: '
                 print '19-Para atulizar as observações sobre o funcionário.: '
                 print '20-Para atualizar a função do funcionário\n.: '
                 campo = input ("Digite o campo deseja quer atualizar.:")
                 if campo == 1:
                     Fun_ID = raw_input ("Redefina o código do funcionário.: ")
                     sql = "update funcionarios set Fun_ID = '"+Fun_ID+"' where Fun_cpf = '"+busca+"'"
                     try:
                         cursor.execute(sql)
                         db.commit()
                     except:
                        db.rollback()
                 elif campo == 2:
                    Fun_nome = raw_input ("Redefina o nome do funcionário.: ")
                    sql = "update funcionarios set Fun_nome = '"+Fun_nome+"' where Fun_cpf = '"+busca+"'"
                    try:
                        cursor.execute(sql)
                        db.commit()
                        
                    except:
                        db.rollback()
                              
                                
                 elif campo == 3:
                      Fun_sexo = raw_input ("Redefina o sexo do funcionário.: ")
                      sql = "update funcionarios set Fun_sexo = '"+Fun_sexo+"' where Fun_cpf = '"+busca+"'"
                      try:
                          cursor.execute(sql)
                          db.commit()
                      except:
                          db.rollback()
                               

                 elif campo == 4:
                     Fun_cpf = raw_input ("Redefina o CPF do funcionário.: ")
                     sql = "update funcionarios set Fun_cpf = '"+Fun_cpf+"' where Fun_cpf = '"+busca+"'"
                     try:
                         cursor.execute(sql)
                         db.commit()
                     except:
                         db.rollback()
                          

                 elif campo == 5:
                      Fun_rg = raw_input ("Redefina o RG do funcionário.: ")
                      sql = "update funcionarios set Fun_rg = '"+Fun_rg+"' where Fun_cpf = '"+busca+"'"
                      try:
                          cursor.execute(sql)
                          db.commit()
                      except:
                          db.rollback()

                 elif campo == 6:
                      Fun_endereco = raw_input ("Redefina o endereço do funcionário.: ")
                      sql = "update funcionarios set Fun_endereco = '"+Fun_endereco+"' where Fun_cpf = '"+busca+"'"
                      try:
                          cursor.execute(sql)
                          db.commit()
                      except:
                          db.rollback()

                 elif campo == 7:
                      Fun_numero = raw_input ("Redefina o numero da residência do funcionário.: ")
                      sql = "update funcionarios set Fun_numero = '"+Fun_numero+"' where Fun_cpf = '"+busca+"'"
                      try:
                          cursor.execute(sql)
                          db.commit()
                        
                      except:
                          db.rollback()
                          
                 elif campo == 8:
                      Fun_complemento= raw_input ("Redefina o complemento sobre a residência do funcionário.: ")
                      sql = "update funcionarios set Fun_complemento = '"+Fun_complemento+"' where Fun_cpf = '"+busca+"'"
                      try:
                          cursor.execute(sql)
                          db.commit()
                      except:
                          db.rollback()
                               

                 elif campo == 9:
                     Fun_bairro = raw_input ("Redefina o bairro do funcionário.: ")
                     sql = "update funcionarios set Fun_bairro = '"+Fun_bairro+"' where Fun_cpf = '"+busca+"'"
                     try:
                         cursor.execute(sql)
                         db.commit()
                     except:
                         db.rollback()
                                

                 elif campo == 10:
                      Fun_cep = raw_input ("Redefina CEP do funcionário.: ")
                      sql = "update funcionarios set Fun_cep = '"+Fun_cep+"' where Fun_cpf = '"+busca+"'"
                      try:
                          cursor.execute(sql)
                          db.commit()
                      except:
                          db.rollback()

                 elif campo == 11:
                     Fun_cidade = raw_input ("Redefina a cidade do funcionário.: ")
                     sql = "update funcionarios set Fun_cidade = '"+Fun_cidade+"' where Fun_cpf = '"+busca+"'"
                     try:
                         cursor.execute(sql)
                         db.commit()
                     except:
                         db.rollback()

                 elif campo == 12:
                     Fun_estado = raw_input ("Redefina o estado: ")
                     sql = "update funcionarios set Fun_estado = '"+Fun_estado+"' where Fun_cpf = '"+busca+"'"
                     try:
                         cursor.execute(sql)
                         db.commit()
                     except:
                         db.rollback()

                 elif campo == 13:
                     Fun_tel= raw_input ("Redefina o telefone do funcionário.: ")
                     sql = "update funcionarios set Fun_tel = '"+Fun_tel+"' where Fun_cpf = '"+busca+"'"
                     try:
                         cursor.execute(sql)
                         db.commit()
                     except:
                         db.rollback()

                 elif campo == 14:
                     Fun_cel = raw_input ("Redefina o celular do funcionário.: ")
                     sql = "update funcionarios set Fun_cel = '"+Fun_cel+"' where Fun_cpf = '"+busca+"'"
                     try:
                         cursor.execute(sql)
                         db.commit()
                     except:
                         db.rollback()
                               

                 elif campo == 15:
                     Fun_n_carteira= raw_input ("Redefina o o número de carteira de trabalho do funcionário.: ")
                     sql = "update funcionarios set Fun_n_carteira = '"+Fun_n_carteira+"' where Fun_cpf = '"+busca+"'"
                     try:
                         cursor.execute(sql)
                         db.commit()
                     except:
                         db.rollback()
                                

                 elif campo == 16:
                     Fun_admissao= raw_input ("Redefina a data de admissão do funcionário.: ")
                     sql = "update funcionarios set Fun_admissao = '"+Fun_admissao+"' where Fun_cpf = '"+busca+"'"
                     try:
                         cursor.execute(sql)
                         db.commit()
                     except:
                         db.rollback()
                                
                                
                 elif campo == 17:
                     Fun_login_usuario= raw_input ("Redefina o login do funcionário.: ")
                     sql = "update funcionarios set Fun_login_usuario = '"+Fun_login_usuario+"' where Fun_cpf = '"+busca+"'"
                     try:
                         cursor.execute(sql)
                         db.commit()
                     except:
                         db.rollback()

                 elif campo == 18:
                     Fun_senha_login = raw_input ("Redefina a senha do funcionário.: ")
                     sql = "update funcionarios set Fun_senha_login = '"+Fun_senha_login+"' where Fun_cpf = '"+busca+"'"
                     try:
                         cursor.execute(sql)
                         db.commit()
                     except:
                         db.rollback()
                                

                 elif campo == 19:
                     Fun_observacoes = raw_input ("Redefina as observações sobre funcionário.: ")
                     sql = "update funcionarios set Fun_observacoes = '"+Fun_observacoes+"' where Fun_cpf = '"+busca+"'"
                     try:
                         cursor.execute(sql)
                         db.commit()
                     except:
                         db.rollback()
                                

                 elif campo == 20:
                     Fun_funcao= raw_input ("Redefina a função do funcionário.: ")
                     sql = "update funcionarios set Fun_funcao = '"+Fun_funcao+"' where Fun_cpf = '"+busca+"'"
                     try:
                         cursor.execute(sql)
                         db.commit()

                     except:
                         db.rollback()
                                


        elif atividade == 3:
            sql = "select * from funcionarios" 
            cursor.execute(sql)
            print 'Os funcionários inseridos no sistema são.: '
            results = cursor.fetchall()
            for row in results:
                e = row[1]
                print e
            busca = raw_input ("Digite o CPF do funcionário que deseja excluir.: ")
            sql = "delete from funcionarios where Fun_cpf = '"+busca+"'"
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()
                

        elif atividade == 4:
            print "Os campos marcados com asterisco não podem ser vazios"
            sql = "select * from clientes"
            cursor.execute(sql)
            print 'Os clientes inseridos no sistema são.: '
            results = cursor.fetchall()
            for row in results:
                e = row[1]
                print(e)
        
            sql = "select * from clientes"    
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                l = row[0]
                o = int(l)
                b = o + 1

            Cli_ID = str(b)
            Cli_nome = raw_input ("Digite o nome do cliente*.: ")
            Cli_sexo = raw_input ("Digite o sexo do cliente*.: ")
            Cli_endereco = raw_input ("Digite o endereco do cliente*.: ")
            Cli_numero = raw_input ("Digite o numero da residencia do cliente*.: ")
            Cli_complemento = raw_input ("Digite as informações adicionais sobre o endereço do cliente.: ")
            Cli_bairro = raw_input ("Digite o bairro do cliente*.: ")
            Cli_cep = raw_input ("Digite o CEP do cliente*.: ")
            Cli_cidade = raw_input ("Digite a cidade do cliente*.: ")
            Cli_estado = raw_input ("Digite o estado do cliente*.: ")
            Cli_telefone = raw_input ("Digite o número do telefone do cliente.: ")
            Cli_celular = raw_input ("Digite o número do celular do cliente*.: ")
            Cli_observacoes = raw_input ("Digite as informações adicionais sobre o cliente.: ")
            Cli_CPF = raw_input ("Digite o CPF do cliente.: ")
            Cli_saldo = str(0.0)


            sql = "insert into clientes values ('"+Cli_ID+"','"+Cli_nome+"', '"+Cli_sexo+"', '"+Cli_endereco+"', '"+Cli_numero+"', '"+Cli_complemento+"','"+Cli_bairro+"', '"+Cli_cep+"','"+Cli_cidade+"', '"+Cli_estado+"', '"+Cli_telefone+"', '"+Cli_celular+"','"+Cli_observacoes+"','"+Cli_CPF+"', '"+Cli_saldo+"')"

            try:
                cursor.execute(sql)
                db.commit ()

            except:
                db.rollback()
                
        elif atividade == 5:
            sql = "select * from clientes" 
            cursor.execute(sql)
            print 'Os clientes inseridos no sistema são.: '
            results = cursor.fetchall()
            for row in results:
                e = row[1]
                d = row[13]
            print 'Nome =>',str (e), 'CPF =>', str(d)
            busca = raw_input ("Digite o CPF do cliente que deseja alterar os dados.: ")
            sql = "select * from clientes where Cli_cpf like '"+busca+"'"
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                d = row[13]
         
            if str(d) != busca:
                print 'Esse cliente não existe no sistema.: '
            elif str(d) == busca:
                print 'O funcionário está cadastrado no sistema.:'
                print 'Opcões de atualização.: '
                print ' 1-Para atualizar o código do cliente.: '
                print ' 2-Para atualizar o nome do cliente.: '
                print ' 3-Para atualizar o sexo do cliente.: '
                print ' 4-Para atualizar o endereço do cliente.: '
                print ' 5-Para atualizar o número da residência do cliente.: '
                print ' 6-Para atualizar as informações adicionais sobre o endereco do cliente.: '
                print ' 7-Para atualizar o bairro do cliente.: '
                print ' 8-Para atualizar o CEP do cliente.: '
                print ' 9-Para atualizar a cidade do cliente.: '
                print '10-Para atualizar o .estado do cliente: '
                print '11-Para atualizar o número de telefone do cliente.: '
                print '12-Para atualizar o número de celular do cliente.: '
                print '13-Para atualizar as informacoes adicionais sobre o cliente.: '
                print '14-Para atualizar o CPF do cliente.:\n '
                
                campo = input ("Digite o campo deseja quer atualizar.:")
                if campo == 1:
                    Cli_ID = raw_input ("Redefina um código para o cliente*.: ")
                    sql = "update clientes set Cli_ID = '"+Cli_ID+"' where Cli_cpf = '"+busca+"'"
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()
                elif campo == 2:               
                    Cli_nome = raw_input ("Redefina o nome do cliente*.: ")
                    sql = "update clientes set Cli_nome = '"+Cli_nome+"' where Cli_cpf = '"+busca+"'"
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()
                elif campo == 3:               
                    Cli_sexo = raw_input ("Redefina o sexo do cliente*.: ")
                    sql = "update clientes set Cli_sexo = '"+Cli_sexo+"' where Cli_cpf = '"+busca+"'" 
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()
                elif campo ==4:
                    Cli_endereco = raw_input ("Redefina o endereço do cliente*.: ")
                    sql = "update clientes set Cli_endereco = '"+Cli_endereco+"' where Cli_cpf = '"+busca+"'"
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()
                elif campo == 5:
                    Cli_numero = raw_input ("Redfina o número da residência do cliente*.: ")
                    sql = "update clientes set Cli_numero = '"+Cli_numero+"' where Cli_cpf = '"+busca+"'"
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()
                elif campo ==6:
                    Cli_complemento = raw_input ("Redefina as informações adicionais sobre o endereço do cliente.: ")
                    sql = "update clientes  set Cli_complemento = '"+Cli_complemento+"' where Cli_cpf = '"+busca+"'" 
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()
                elif campo==7:
                    Cli_bairro = raw_input ("Redefina o bairro do cliente*.: ")
                    sql = "update clientes  set Cli_bairro = '"+Cli_bairro+"' where Cli_cpf = '"+busca+"'"
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()
                elif campo == 8:
                    Cli_cep = raw_input ("Redefina o CEP do cliente*.: ")
                    sql = "update clientes set Cli_campo = '"+Cli_campo+"' where Cli_cpf = '"+busca+"'"
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()
                elif campo == 9:
                    Cli_cidade = raw_input ("Redefina a cidade do cliente*.: ")
                    sql = "update clientes  set Cli_cidade = '"+Cli_cidade+"' where Cli_cpf = '"+busca+"'"
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()
                
                elif campo ==10:
                    Cli_estado = raw_input ("Redefina o estado do cliente*.: ")
                    sql = "update clientes  set Cli_estado = '"+Cli_estado+"' where Cli_cpf = '"+busca+"'"
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()
                elif campo == 11:
                    Cli_telefone = raw_input ("Redefina o número do telefone do cliente.: ")
                    sql = "update clientes  set Cli_telefone = '"+Cli_telefone+"' where Cli_cpf = '"+busca+"'"
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()
                elif campo ==12:
                    Cli_celular = raw_input ("Redefina o número do celular do cliente*.: ")
                    sql = "update clientes  set Cli_campo = '"+Cli_campo+"' where Cli_cpf = '"+busca+"'"
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()
                elif campo == 13:
                    Cli_observacoes = raw_input ("Redefina as informações adicionais sobre o cliente.: ")
                    sql = "update clientes set Cli_observacoes = '"+Cli_observacoes+"' where Cli_cpf = '"+busca+"'"
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()
                elif campo == 14:
                    Cli_cpf = raw_input ("Redefina o cpf do cliente.: ")
                    sql = "update clientes set Cli_CPF = '"+Cli_cpf+"' where Cli_cpf = '"+busca+"'"
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()

        elif atividade == 6:
            sql = "select * from clientes" 
            cursor.execute(sql)
            print 'Os clientes inseridos no sistema são.: '
            results = cursor.fetchall()
            for row in results:
                e = row[1]
                d = row[13]
                print 'Nome =>',str (e),'CPF =>', str(d)

            busca = raw_input ("Digite o CPF do cliente que deseja excluir.: ")
            sql = "delete from clientes where Cli_cpf = '"+busca+"'"
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()
      
        elif atividade == 7:
            sql = "select * from filme" 
            print 'Os filmes inseridos no sistema são.: '
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                e = row[1]
                print e
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                w = row[0]
                d = int(w) + 1
            Fil_ID = str (d)
            Fil_nome = raw_input ("Digite o nome do filme.: ")
            Fil_genero = raw_input ("Digite o gênero do filme.: ")
            Fil_class_et = raw_input ("Digite a classe etária do filme.: ")
            Fil_observacoes = raw_input ("Digite informações adicionais sobre o filme.: ")
            Fil_quant = raw_input ("Digite a quantidade de unidades.: ")
            Fil_loc_quant = "0"
           
            sql = "insert into filme values ('"+Fil_ID+"','"+Fil_nome+"','"+Fil_genero+"','"+Fil_class_et+"','"+Fil_observacoes+"', '"+Fil_quant+"','"+Fil_loc_quant+"')"
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()
        elif atividade == 8:
             sql = "select * from filme" 
             cursor.execute(sql)
             print 'Os filmes cadastrados no sistema são.: '
             results = cursor.fetchall()
             for row in results:
                 w = row[1]
                 print w
             busca = raw_input ("Digite o nome do filmes que deseja alterar os dados.: ")
             sql = "select * from filme where Fil_nome = '"+busca+"'"
             cursor.execute(sql)
             results = cursor.fetchall()
             for row in results:
                 e = row[1]
                 print e
             if busca != e:
                 print "Esse filme não está cadastrado no sistema"
             elif busca == e:
                 print 'Opcões de atualização.: '
                 print ' 1-Para atualizar o código do filme.: '
                 print ' 2-Para atualizar o nome do filme.: '
                 print ' 3-Para atualizar o gênero do filme.: '
                 print ' 4-Para atualizar a classificação etária do filme.: '
                 print ' 5-Para atualizar as observações sobre o filme.:\n '
                 campo = input ("Digite o campo que deseja atualizar.: ")
                 if campo == 1:
                     Fil_ID = raw_input ("Redefina o código do filme.: ")
                     sql = "update filme set Fil_ID = '"+Fil_ID+"' where Fil_nome = '"+busca+"'"
                     try:
                         cursor.execute(sql)
                         db.commit()
                     except:
                         db.rollback()
                 elif campo == 2:
                     Fil_nome = raw_input ("Redefina o nome do filme.: ")
                     sql = "update filme set Fil_nome = '"+Fil_nome+"' where Fil_nome = '"+busca+"'"
                     try:
                         cursor.execute(sql)
                         db.commit()
                     except:
                         db.rollback()
                 elif campo == 3:
                     Fil_genero = raw_input ("Redefina o gênero do filme.: ")
                     sql = "update filme set Fil_genero = '"+Fil_genero+"' where Fil_nome = '"+busca+"'"
                     try:
                         cursor.execute(sql)
                         db.commit()
                     except:
                         db.rollback()
                 elif campo == 4:
                     Fil_class_et = raw_input ("Redefina a classificação etária do filme.: ")
                     sql = "update filme set Fil_class_et = '"+Fil_class_et+"' where Fil_nome = '"+busca+"'"
                     try:
                         cursor.execute(sql)
                         db.commit()
                     except:
                         db.rollback()
                 elif campo == 5:
                     Fil_observacoes = raw_input ("Redefina as observacoes sobre o filme.: ")
                     sql = "update filme set Fil_observacoes = '"+Fil_observacoes+"' where Fil_nome = '"+busca+"'"
                     try:
                         cursor.execute(sql)
                         db.commit()
                     except:
                         db.rollback()
        elif atividade == 9:
            sql = "select * from filme"
            cursor.execute(sql)
            print 'Os filmes cadastrados no sistema são.: '
            results = cursor.fetchall()
            for row in results:
                w = row[1]
                print w
            busca = raw_input ("Digite o nome do filme que deseja excluir.: ")
            if w != busca:
                print "Esse filme não está cadastrado no sistema.: "
            elif w == busca:
                sql = "delete from filme where Fil_nome = '"+busca+"'"
                try:
                    cursor.execute(sql)
                    db.commit()
                except:
                    db.rollback()
                
            
        elif atividade == 10:
##          Pesquisa de cadastro de filme
            sql = "select * from filme" 
            cursor.execute(sql)
            print 'Os filmes cadastrados no sistema são.: '
            results = cursor.fetchall()
            for row in results:
                w = row[1]
                print w
            print 'Pesquisa de disponibilidade de filme para locacao.: '
##          Pesquisa da variável busca na coluna Loc_filme da tabela locacao
            busca = raw_input ("Digite o nome do filme.: ")

            sql = "select * from locacao where Loc_filme like '"+busca+"'"
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                e = row[2]
                print str(e)
##          Pesquisa da variável busca na coluna Fil_nome da tabela filme
            sql = "select * from filme where Fil_nome like '"+busca+"'"
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                d = row[1]
                print str(d)

            if busca == str(e) and busca == str(d):
                print 'O filme já está locado'
            elif busca != str(e) and busca == str(d):
                print 'O fime está disponível para locacao'
            elif busca != str(e) and busca != str(d):
                print 'O filme não existe no acervo'
                

                
            
            
        elif atividade == 11:
                sql = "select * from clientes" 
                cursor.execute(sql)
                print 'Os clientes inseridos no sistema são.: '
                results = cursor.fetchall()
                for row in results:
                    e = row[1]
                    d = row[13]
                    print 'Nome =>',str (e),'CPF =>', str(d)
                sql = "select * from filme" 
                cursor.execute(sql)
                print 'Os filmes cadastrados no sistema são.: '
                results = cursor.fetchall()
                for row in results:
                    w = row[1]
                    print w
                    
                x = raw_input ("Digite o CPF do cliente para a pesquisa de seu registro no banco de dados.: ")
                sql = "select * from clientes where Cli_cpf like '"'%'+x+'%'"'"
                cursor.execute(sql)

                results = cursor.fetchall()
                for row in results:
                   
                    b = row[1]
                    i = row[13]
                    print 'Nome =>',str (b),'CPF =>', str(i)
                    
                if x !=i:
                    print 'O cliente não está cadastrado no sistema'
                elif x == i:
                    while (invalida == 1):
                        # Capturando hora do sistema Windows
                        agora = datetime.date.today()
                        mes = agora.month-1
                        #diadoano = agora.strftime('%j')
                        diadasemana_hoje = datetime.date.weekday(agora)
                        hoje = agora.strftime('%d/%m/%Y')

                        print ''
                        prosseguir = ''
                        categ_filme = ''
                        while (prosseguir != 's' ):
                            prosseguir = ''
                            while ((categ_filme != 'c') and (categ_filme != 'l') and (categ_filme != 's')):
                                categ_filme = raw_input("> Qual a categoria do filme c - catálogo / l - lançamento.: ")
                                categ_filme = categ_filme.lower()

                                if ((categ_filme != 'c') and (categ_filme != 'l') and (categ_filme != 's')):
                                    print 'Categoria inserida é inválida. Digite novamente.\n'

                                if (categ_filme == 'c'):
                                    categoria_filme = 'Catálogo'
                                elif (categ_filme == 'l'):
                                    categoria_filme = 'Lançamento'
                      

                            while ((prosseguir != 's') and (prosseguir != 'n')):
                                prosseguir = raw_input("> Confirma categoria escolhida [%s] (s/n)? " %(categoria_filme))
                                prosseguir = prosseguir.lower()
                                if (prosseguir == 'n'):
                                    categ_filme = ''
                                    continue
                            print ''

                        if (categ_filme == 'c'):
                            somar_dias = 3

                        elif (categ_filme == 'l'):
                            somar_dias = 2

                        elif (categ_filme == 's'):
                            somar_dias = 1

                        data_dev = (agora + datetime.timedelta(days=somar_dias))
                        diadasemana_dev = datetime.date.weekday(data_dev)
                        if (diadasemana_dev == 6):
                            data_dev = (agora + datetime.timedelta(days=somar_dias+1))
                            diadasemana_dev = datetime.date.weekday(data_dev)

                        devolucao = data_dev.strftime('%d/%m/%Y')
                        print "Data de devolução: " + devolucao + '(' + diasemana[diadasemana_dev] + ')'

                        confirma = ''
                        while ((confirma != 's') and (confirma != 'n')):
                            confirma = raw_input("\n> Confirma data de devolução informada (s/n): ")
                            confirma = confirma.lower()

                        if (confirma == 'n'):
                            invalida = 1
                        else:
                            invalida = 0

                        print ""

                        # Inserção de data prevista de Devolução do filme (pelo atendente/gerente)
                        alteracao = False
                        while (invalida == 1):
                            alteracao = True
                            print "Obs.: Locação máxima de 30(trinta) dias."
                            data = raw_input('> Insira uma data de Devolução (no formato DD/MM/AAAA): ')

                            if ((len(data) == 10) and (data[2] == '/') and (data[5] == '/')):
                                novadata = data[0:2] + data[3:5] + data[6:10]
                                entrou = []

                                for c in novadata:
                                    for n in listanum:
                                        if (c == n):
                                            entrou.append(c)

                                if (len(novadata) == len(entrou)):
                                    invalida = 0
                                    dia = novadata[0:2]
                                    mes = novadata[2:4]
                                    ano = novadata[4:8]

                                    if (dia[0] == '0'):
                                        novodia = dia[1]
                                    else:
                                        novodia = dia

                                    if (mes[0] == '0'):
                                        novomes = mes[1]
                                    else:
                                        novomes = mes

                                    if (ano[0:2] != '20'):
                                        invalida = 1
                                    else:
                                        novoano = ano

                                    novodia = int(novodia)
                                    novomes = int(novomes)
                                    novoano = int(novoano)

                                    if ((novodia == 0) or (novomes == 0)):
                                        invalida = 1

                                    if ((novomes < 1) or (novomes > 12) or (type(novomes) != int)):
                                        invalida = 1

                                    if ((novomes == 1) or (novomes == 3) or (novomes == 5) or (novomes == 7) or (novomes == 8) or (novomes == 10) or (novomes == 12)):
                                        if ((novodia < 1) or (novodia > 31)):
                                            invalida = 1

                                    if ((novomes == 4) or (novomes == 6) or (novomes == 9) or (novomes == 11)):
                                        if ((novodia < 1) or (novodia > 30)):
                                            invalida = 1

                                    if (novomes == 2):
                                        if (calendar.isleap(novoano) == True):
                                            if ((novodia < 1) or (novodia > 29)):
                                                invalida = 1
                                        else:
                                            if ((novodia < 1) or (novodia > 28)):
                                                invalida = 1

                            if (invalida == 1):
                                print 'Data inserida é inválida!\n'

                            else:
                                #print 'Data Inserida: %d/%d/%d' %(novodia,novomes,novoano)
                                data_dev = datetime.date(novoano, novomes, novodia)
                                diadasemana_dev = datetime.date.weekday(data_dev)
                                devolucao = data_dev.strftime('%d/%m/%Y')

                                if (diadasemana_dev == 6):
                                    print "\nDia da semana escolhido é um Domingo!"
                                    continua = ''
                                    while ((continua != 's') and (continua != 'n')):
                                        continua = raw_input('> Confirmar data escolhida (s/n): ')
                                        continua = continua.lower()
                                    if (continua == 'n'):
                                        invalida = 1
                                        print ""
                                        continue

                                print '\nHoje: ' + hoje + '(' +  diasemana[diadasemana_hoje] + ')'
                                print '\nData da Devolução inserida: ' + devolucao + '(' + diasemana[diadasemana_dev] + ')'

                                quant_dias = data_dev - agora
                                quant_dias = str(quant_dias)
                                loc = quant_dias.find(' day')

                                if (loc == -1):
                                    quant_dias = '0'
                                else:
                                    quant_dias = quant_dias[0:loc]

                                quant_dias = int(quant_dias)

                                if (quant_dias < 0):
                                    print '\n>> Data de devolução é anterior à data de locação.\n'
                                    invalida = 1
                                elif (quant_dias == 0):
                                    print '\n>> Locação devolvida no mesmo dia'
                                    invalida = 0
                                    ## Fazer cálculo de cobrança de locação, para devolução de filme no mesmo dia.
                                elif (quant_dias > 30):
                                    print "\n>> A locação deve ter no máximo 30(trinta) dias.\n"
                                    invalida = 1
                        ##        else:
                        ##            print '\nQuantidade de Dias (Locação):',quant_dias

                        if (alteracao == False):
                            print 'Hoje: ' + hoje + '(' +  diasemana[diadasemana_hoje] + ')'
                            print '\nDevolução: ' + devolucao + '(' + diasemana[diadasemana_dev] + ')'

                            quant_dias = data_dev - agora
                            quant_dias = str(quant_dias)
                            loc = quant_dias.find(' day')

                            if (loc == -1):
                                quant_dias = '0'
                            else:
                                quant_dias = quant_dias[0:loc]

                            quant_dias = int(quant_dias)

                        quant_domingos = 0
                        for mais_d in range(1,quant_dias):
                            mais_dias = (agora + datetime.timedelta(days=mais_d))
                            diadasemana_mais_dias = datetime.date.weekday(mais_dias)
                            if (diadasemana_mais_dias == 6): 
                                quant_domingos += 1

                        print 'Quantidade de Domingos passados:', quant_domingos

                        quant_dias = quant_dias - quant_domingos
                        print '\nQuantidade de Dias (Locação):',quant_dias


##                           data = raw_input('Insira uma data de Devolução (no formato DD/MM/AAAA): ')
##                        if (len(data) == 10) and (data[2] == '/') and (data[5] == '/'):
##                            novadata = data[0:2] + data[3:5] + data[6:10]
##                            entrou = []
##
##                            for c in novadata:
##                                for n in listanum:
##                                    if c == n:
##                                        entrou.append(c)
##
##                            if len(novadata) == len(entrou):
##                                invalida = 0
##                                dia = novadata[0:2]
##                                mes = novadata[2:4]
##                                ano = novadata[4:8]
##
##                                if dia[0] == '0':
##                                    novodia = dia[1]
##                                else:
##                                    novodia = dia
##
##                                if mes[0] == '0':
##                                    novomes = mes[1]
##                                else:
##                                    novomes = mes
##
##                                if (ano[0:2] != '20'):
##                                    invalida = 1
##                                else:
##                                    novoano = ano
##
##                                novodia = int(novodia)
##                                novomes = int(novomes)
##                                novoano = int(novoano)
##
##                                if (novodia == 0) or (novomes == 0):
##                                    invalida = 1
##
##                                if (novomes < 1) or (novomes > 12) or (type(novomes) != int):
##                                    invalida = 1
##
##                                if (novomes == 1) or (novomes == 3) or (novomes == 5) or (novomes == 7) or (novomes == 8) or (novomes == 10) or (novomes == 12):
##                                    if (novodia < 1) or (novodia > 31):
##                                        invalida = 1
##
##                                if (novomes == 4) or (novomes == 6) or (novomes == 9) or (novomes == 11):
##                                    if (novodia < 1) or (novodia > 30):
##                                        invalida = 1
##
##                                if (novomes == 2):
##                                    if calendar.isleap(novoano) == True:
##                                        if (novodia < 1) or (novodia > 29):
##                                            invalida = 1
##
##                                    else:
##                                        if (novodia < 1) or (novodia > 28):
##                                            invalida = 1
##
##                        if (invalida == 1):
##                            print 'Data inserida é inválida!\n'
##
##                        else:
##                            print 'Data Inserida: %d/%d/%d' %(novodia,novomes,novoano)
##
##                            # Capturando hora do sistema Windows
##
##                            agora = datetime.date.today()
##                            mes = agora.month-1
##                            diadoano = agora.strftime('%j')
##                            diadasemana = datetime.date.weekday(agora)
##
##                            hoje = agora.strftime('%d/%m/%Y')
##
##                            data_dev = datetime.date(novoano, novomes, novodia)
##
##                            print ""
##                            print 'Hoje é:', hoje
##                            print 'Dia da semana (hoje): ', diasemana[diadasemana]
##
##                            diadasemana_dev = datetime.date.weekday(data_dev)
##                            devolucao = data_dev.strftime('%d/%m/%Y')
##
##                            print ""
##                            print 'Data da Devolução:', devolucao
##                            print 'Dia da semana (Devolução): ', diasemana[diadasemana_dev]
##
##                            quant_dias = data_dev - agora
##                            quant_dias = str(quant_dias)
##
##                            loc = quant_dias.find(' days')
##                            quant_dias = quant_dias[0:loc]
##                            quant_dias = int(quant_dias)
##                            if quant_dias <= 0:
##                                print '\n>> A locação deve ter um mínimo de 1(um) dia.\n'
##                                invalida = 1
##                            elif quant_dias > 30:
##                                print "\n>> Locação máxima de 30(trinta) dias.\n"
##                                invalida = 1
##                            else:
##                                print ""
##                                print 'Quantidade de Dias (Locação):',quant_dias
##


                    Loc_cliente = b
                    Loc_filme = raw_input ("Digite o nome do filme.: ")
                    Loc_data = hoje
                    Loc_devolucao = devolucao
                    calculo = (quant_dias/2) * 2
                    Loc_preco = str(calculo)
                    Loc_CPF = str(x)
                   
                                                
                    sql = "insert into locacao values ('"+Loc_cliente+"','"+Loc_filme+"','"+Loc_data+"','"+Loc_devolucao+"', '"+Loc_preco+"','"+Loc_CPF+"')"

                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()

                    sql = "select * from filme where Fil_nome = '"+Loc_filme+"'"
                    cursor.execute (sql)
                    results = cursor.fetchall()
                    for row in results:
                        # aqui é a quantidade de filme locado
                        z = row [1]
                        l = row [6]
                        o = int (l)
                        e = o + 1
                        e = str(e)
                        #aqui é a quantidade de filme disponível no estoque subtraída da quantidade de filme locada
                        d = row [5]
                        w = int (d)
                        s = w - 1
                        s = str(s)
                    print 'Nome do filme',z,'Quantidade de filme disponível',s,'Quantidade de filme locado',e
                    
                    if s == str (-1):
                        print 'Não existe mais o filme',z,'para a locação'
                       
                        
                            
                    elif s > str(-1):
                        sql = "update filme set Fil_quant = '"+s+"' where Fil_nome = '"+Loc_filme+"'"
                        try:
                            cursor.execute(sql)
                            db.commit()
                        except:
                            db.rollback()
                        sql1 = "update filme set Fil_loc_quant = '"+e+"' where Fil_nome = '"+Loc_filme+"'"
                        try:
                            cursor.execute(sql1)
                            db.commit()
                        except:
                            db.rollback()


        elif atividade == 12:
            print 'Os filmes que estão locados sao.: '
            sql = "select * from locacao"
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                e = row[1]
                i = row [0]
                w = row [5]
                print '*Filme locado =>',e, '*Nome => ',i, '*CPF => ', w
            busca = raw_input ('Digite o CPF do cliente.: ')
            sql = "select * from locacao where Loc_CPF = '"+busca+"'"
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                s = row[1]
                print 'Os filmes locados por ',i, 'sao', s 
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()

            sql = "select * from filme where Fil_nome = '"+s+"'"
            cursor.execute (sql)
            results = cursor.fetchall()
            for row in results:
                # aqui é a quantidade de filme locado
                z = row [1]
                l = row [6]
                o = int (l)
                e = o -1
                e = str(e)
                #aqui é a quantidade de filme disponível no estoque somada da quantidade de filme locada
                d = row [5]
                w = int (d)
                s = w + 1
                s = str(s)
                   
                sql = "update filme set Fil_quant = '"+s+"' where Fil_nome = '"+busca+"'"
                try:
                    cursor.execute(sql)
                    db.commit()
                except:
                    db.rollback()

                sql1 = "update filme set Fil_loc_quant = '"+e+"' where Fil_nome = '"+busca+"'"
                try:
                    cursor.execute(sql1)
                    db.commit()
                except:
                    db.rollback()

                
                sql2 = "delete from locacao where Loc_CPF = '"+busca+"'"
                try:
                    cursor.execute(sql2)
                    db.commit()
                except:
                    db.rollback()
            
   

                                

        elif atividade == 13:
            #exit()
            print 'programa encerrado!'
            break
            




db.close()


                


            

                

                

