
import MySQLdb
db = MySQLdb.connect('localhost','root','mugen','projeto')
cursor = db.cursor()
s = 1
i = ""
l = ""
d = ""
e = ""
w = ""
sql = ""
cargo = ""
print "Fa�a o login no sistema.:"

login = raw_input ("Digite o login.: ")
senha = raw_input ("Digite a senha.: ")

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
    print'Voc� est� logado como atendente'
elif login != str(l) and senha == str(d):
    cargo = 'erro'
    print 'erro'



sql = "select * from cadastro_gerente where login like '"+login+"'"
cursor.execute(sql)

results = cursor.fetchall()
for row in results:
    w = row[0]
    print str(w)

sql = "select * from cadastro_gerente  where senha like '"+senha+"'"
cursor.execute(sql)

results = cursor.fetchall()
for row in results:
    e = row[1]
    print str(e)



if login == str(w) and senha == str(e):
    cargo = 'g'
    print 'Voc� est� logado como gerente'
elif login != str(l) and senha != str(d):
    cargo = 'erro'
    print 'erro'




fica=1


while fica==1:
    if cargo == 'a':
        atividade = input("\n> O que deseja executar agora?\n\n1 - Cadastrar Funcion�rio\n2 - Cadastrar Cliente\n3 - Cadastrar Filme no Acervo\n4 - Pesquisar Acervo\n5 - Reservar Filme\n6 - Efetuar Loca��o\n7 - Efetuar Devolu��o\n8 - Sair\n> ")
        if atividade == 1:
            print "Os campos marcados com asterisco n�o podem ser vazios"
            Fun_ID = raw_input ("Digite o codigo do funcion�rio*.: ")
            Fun_nome = raw_input("Informe o nome do funcion�rio a ser cadastrado*: ")
            Fun_sexo = raw_input("Informe o sexo do funcionario*(M/F): " )
            Fun_cpf = raw_input("Infome o CPF(Apenas os n�meros)*.: ")
            Fun_rg = raw_input("Informe o RG*.: ")
            Fun_endereco = raw_input("Informe o endereco*.: ")
            Fun_numero = raw_input("Informe o n�mero da resid�ncia.*: ")
            Fun_complemento = raw_input("Informe o complemento.: ")
            Fun_bairro = raw_input("Informe o Bairro*.: ")
            Fun_cep = raw_input("Informe o CEP(somente n�meros)*.: ")
            Fun_cidade = raw_input("Informe a Cidade*.: ")
            Fun_estado = raw_input("informe o Estado*.: ")
            Fun_tel = raw_input("Informe o Tel*.: ")
            Fun_cel = raw_input ("Informe o Cel*.: ")
            Fun_n_carteira = raw_input("Informe o n�mero da carteira de trabalho do funcion�rio*.: ")
            Fun_admissao = raw_input('Informe a Data de Admiss�o (formato DD/MM/AAAA)*.: ')
            Fun_login_usuario = raw_input("Digite o nome de Login de usu�rio deste sistema*.: ")
            Fun_senha_usuario = raw_input("Digite a senha de acesso ao sistema, deste usu�rio*.: ")
            Fun_observacoes = raw_input ("Digite as observa��es sobre o funcionario.: ")
            Fun_funcao = raw_input ("Digite a fun��o do funcion�rio*.: ")
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
            print "Os campos marcados com asterisco n�o podem ser vazios"

            Cli_ID = raw_input ("Digite o c�digo do cliente*.: ")
            Cli_nome = raw_input ("Digite o nome do cliente*.: ")
            Cli_sexo = raw_input ("Digite o sexo do cliente*.: ")
            Cli_endereco = raw_input ("Digite o endereco do cliente*.: ")
            Cli_numero = raw_input ("Digite o numero da residencia do cliente*.: ")
            Cli_complemento = raw_input ("Digite as informa��es adicionais sobre o endere�o do cliente.: ")
            Cli_bairro = raw_input ("Digite o bairro do cliente*.: ")
            Cli_cep = raw_input ("Digite o CEP do cliente*.: ")
            Cli_cidade = raw_input ("Digite a cidade do cliente*.: ")
            Cli_estado = raw_input ("Digite o estado do cliente*.: ")
            Cli_telefone = raw_input ("Digite o n�mero do telefone do cliente.: ")
            Cli_celular = raw_input ("Digite o n�mero do celular do cliente*.: ")
            Cli_observacoes = raw_input ("Digite as informa��es adicionais sobre o cliente.: ")
            Cli_CPF = raw_input ("Digite o CPF do cliente.: ")


            sql = "insert into clientes values ('"+Cli_ID+"','"+Cli_nome+"', '"+Cli_sexo+"', '"+Cli_endereco+"', '"+Cli_numero+"', '"+Cli_complemento+"','"+Cli_bairro+"', '"+Cli_cep+"','"+Cli_cidade+"', '"+Cli_estado+"', '"+Cli_telefone+"', '"+Cli_celular+"','"+Cli_observacoes+"','"+Cli_CPF+"')"

            try:
                cursor.execute(sql)
                db.commit ()

            except:
                db.rollback()
            
            
                
        elif atividade == 3:
            sql = "select * from filme" 
            cursor.execute(sql)
            print 'Os filmes inseridos no sistema s�o.: '
            results = cursor.fetchall()
            for row in results:
                e = row[1]
                print e
            Fil_ID = raw_input("Digite um c�digo para o filme.: ")
            Fil_nome = raw_input ("Digite o nome do filme.: ")
            Fil_genero = raw_input ("Digite o g�nero do filme.: ")
            Fil_class_et = raw_input ("Digite a classe et�ria do filme.: ")
            Fil_observacoes = raw_input ("Digite informa��es adicionais sobre o filme.: ")
           
            sql = "insert into filme values ('"+Fil_ID+"','"+Fil_nome+"','"+Fil_genero+"','"+Fil_class_et+"','"+Fil_observacoes+"')"
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()
        elif atividade == 4:
            print 'Pesquisa de cadastro de filme'
            sql = "select * from filme" 
            cursor.execute(sql)
            print 'Os filmes cadastrados no sistema s�o.: '
            results = cursor.fetchall()
            for row in results:
                w = row[1]
                print w
            print 'Pesquisa de disponibilidade de filme para locacao.: '
##          Pesquisa da vari�vel busca na coluna Loc_filme da tabela locacao
            busca = raw_input ("Digite o nome do filme.: ")

            sql = "select * from locacao where Loc_filme like '"+busca+"'"
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                e = row[2]
                print str(e)
##          Pesquisa da vari�vel busca na coluna Fil_nome da tabela filme
            sql = "select * from filme where Fil_nome like '"+busca+"'"
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                d = row[1]
                print str(d)

            if busca == str(e) and busca == str(d):
                print 'O filme j� est� locado'
            elif busca != str(e) and busca == str(d):
                print 'O fime est� dispon�vel para locacao'
            elif busca != str(e) and busca != str(d):
                print 'O filme n�o existe no acervo'
                
            
        elif atividade == 5:
            sql = "select * from filme" 
            cursor.execute(sql)
            print 'Os filmes cadastrados no sistema s�o.: '
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
                print 'O filme n�o est� cadastrado no sistema'
            elif str(d) == busca:
                if busca == str(e) and busca == str(d):
                    print 'O filme j� est� locado'
                elif busca != str(e) and busca == str(d):
                    print 'O filme est� dispon�vel para locacao'
                    sql = "select * from clientes" 
                    cursor.execute(sql)
                    print 'Os clientes inseridos no sistema s�o.: '
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
                        print 'Este usu�rio n�o est� cadastrado no sistema'
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
                    print 'O filme n�o existe no acervo'
            
        elif atividade == 6:
            sql = "select * from clientes"
            cursor.execute(sql)
            print 'Os clientes inseridos no sistema s�o.: '
            results = cursor.fetchall()
            for row in results:
                e = row[1]
                print e
            sql = "select * from filme" 
            cursor.execute(sql)
            print 'Os filmes cadastrados no sistema s�o.: '
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
                print'C�digo do cliente.:', e
                print'Nome do cliente.:',l
            if x !=l:
                print 'O cliente n�o est� cadastrado no sistema'
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
            print 'Os filmes que est�o locados sao.: '
            sql = "select * from locacao"
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                e = row[2]
                print e
            busca = raw_input ('Digite o filme que ser� devolvido.: ')
            sql = "delete from locacao where Loc_filme = '"+busca+"'"
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()
            
        elif atividade == 8:
            break
            



    elif cargo == 'g':
        atividade = input("\n> O que deseja executar agora?\n\n1 - Cadastrar Funcion�rio\n2 - Atualizar Cadastro de Funcion�rio\n3 - Remover Cadastro de Funcion�rio\n4 - Cadastrar Cliente\n5 - Atualizar Cadastro de Cliente\n6 - Remover Cadastro de Cliente\n7 - Cadastrar Filme no Acervo\n8 - Atualizar Cadastro de Filme no Acervo\n9 - Excluir Filme do Acervo\n10 - Pesquisar Acervo\n11 - Reservar Filme\n12 - Efetuar Loca��o\n13 - Efetuar Devolu��o\n14 - Sair\n> ")
        sql = "select * from funcionarios"
        o = ""
        
        if atividade == 1:
            sql = "select * from funcionarios" 
            cursor.execute(sql)
            print 'Os funcion�rios inseridos no sistema s�o.: '
            results = cursor.fetchall()
            for row in results:
                e = row[1]
                print e
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                e = row[0]
                d = int(e) + 1
            print 'Existem',e,'cadastros no sistema' 
            print "Os campos marcados com asterisco n�o podem ser vazios"
            Fun_ID = str(d)
            Fun_nome = raw_input("Informe o nome do funcion�rio a ser cadastrado*: ")
            Fun_sexo = raw_input("Informe o sexo do funcionario*(M/F): " )
            Fun_cpf = raw_input("Infome o CPF(Apenas os n�meros)*.: ")
            Fun_rg = raw_input("Informe o RG*.: ")
            Fun_endereco = raw_input("Informe o endereco*.: ")
            Fun_numero = raw_input("Informe o n�mero da resid�ncia.*: ")
            Fun_complemento = raw_input("Informe o complemento.: ")
            Fun_bairro = raw_input("Informe o Bairro*.: ")
            Fun_cep = raw_input("Informe o CEP(somente n�meros)*.: ")
            Fun_cidade = raw_input("Informe a Cidade*.: ")
            Fun_estado = raw_input("informe o Estado*.: ")
            Fun_tel = raw_input("Informe o Tel*.: ")
            Fun_cel = raw_input ("Informe o Cel*.: ")
            Fun_n_carteira = raw_input("Informe o n�mero da carteira de trabalho do funcion�rio*.: ")
            Fun_admissao = raw_input('Informe a Data de Admiss�o (formato DD/MM/AAAA)*.: ')
            Fun_login_usuario = raw_input("Digite o nome de Login de usu�rio deste sistema*.: ")
            Fun_senha_usuario = raw_input("Digite a senha de acesso ao sistema, deste usu�rio*.: ")
            Fun_observacoes = raw_input ("Digite as observa��es sobre o funcionario.: ")
            Fun_funcao = raw_input ("Digite a fun��o do funcion�rio*.: ")
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
            print 'Os funcion�rios inseridos no sistema s�o.: '
            results = cursor.fetchall()
            for row in results:
                e = row[1]
                print e
            busca = raw_input ("Digite o nome do funcion�rio que deseja alterar os dados.: ")
            sql = "select * from funcionarios where Fun_nome like '"+busca+"'"
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                e = row[1]
                print str(e)
            if busca != str(e):
                 print 'O funcion�rio n�o est� cadastrado no sistema'
            elif busca == str(e):
                 print 'O funcion�rio est� cadastrado no sistema.:'
                 print 'Opc�es de atualiza��o.: '
                 print ' 1-Para atualizar o c�digo do funcion�rio.: '
                 print ' 2-Para atualizar o nome do funcion�rio.: '
                 print ' 3-Para atualizar o sexo do funcion�rio.: '
                 print ' 4-Para atualizar o CPF do funcion�rio.: '
                 print ' 5-Para atualizar o RG do funcion�rio.: '
                 print ' 6-Para atualizar o endere�o do funcion�rio.: '
                 print ' 7-Para atualizar o n�mero da resid�ncia do funcion�rio.: '
                 print ' 8-Para atualizar complementos das informa��es sobre a resid�ncia.: '
                 print ' 9-Para atualizar o bairro do fucion�rio.: '
                 print '10-Para atualizar o CEP do funcion�rio.: '
                 print '11-Para atualizar a cidade do funcion�rio.: '
                 print '12-Para atualizar o estado do funcion�rio.: '
                 print '13-Para atualizar o n�mero de telefone do funcion�rio.: '
                 print '14-Para atualizar o celular de telefone do funcion�rio.: '
                 print '15-Para atualizar o n�mero de carteira de trabalho do funcion�rio.: '
                 print '16-Para atualizar a data de admiss�o do funcion�rio.: '
                 print '17-Para atualizar o login do funcion�rio.: '
                 print '18-Para atualizar a senha do funcion�rio.: '
                 print '19-Para atulizar as observa��es sobre o funcion�rio.: '
                 print '20-Para atualizar a fun��o do funcion�rio\n.: '
                 campo = input ("Digite o campo deseja quer atualizar.:")
                 if campo == 1:
                     Fun_ID = raw_input ("Redefina o c�digo do funcion�rio.: ")
                     sql = "update funcionarios set Fun_ID = '"+Fun_ID+"' where Fun_nome = '"+busca+"'"
                     try:
                         cursor.execute(sql)
                         db.commit()
                     except:
                        db.rollback()
                 elif campo == 2:
                    Fun_nome = raw_input ("Redefina o nome do funcion�rio.: ")
                    sql = "update funcionarios set Fun_nome = '"+Fun_nome+"' where Fun_nome = '"+busca+"'"
                    try:
                        cursor.execute(sql)
                        db.commit()
                        
                    except:
                        db.rollback()
                              
                                
                 elif campo == 3:
                      Fun_sexo = raw_input ("Redefina o sexo do funcion�rio.: ")
                      sql = "update funcionarios set Fun_sexo = '"+Fun_sexo+"' where Fun_nome = '"+busca+"'"
                      try:
                          cursor.execute(sql)
                          db.commit()
                      except:
                          db.rollback()
                               

                 elif campo == 4:
                     Fun_cpf = raw_input ("Redefina o CPF do funcion�rio.: ")
                     sql = "update funcionarios set Fun_cpf = '"+Fun_cpf+"' where Fun_nome = '"+busca+"'"
                     try:
                         cursor.execute(sql)
                         db.commit()
                     except:
                         db.rollback()
                          

                 elif campo == 5:
                      Fun_rg = raw_input ("Redefina o RG do funcion�rio.: ")
                      sql = "update funcionarios set Fun_rg = '"+Fun_rg+"' where Fun_nome = '"+busca+"'"
                      try:
                          cursor.execute(sql)
                          db.commit()
                      except:
                          db.rollback()

                 elif campo == 6:
                      Fun_endereco = raw_input ("Redefina o endere�o do funcion�rio.: ")
                      sql = "update funcionarios set Fun_endereco = '"+Fun_endereco+"' where Fun_nome = '"+busca+"'"
                      try:
                          cursor.execute(sql)
                          db.commit()
                      except:
                          db.rollback()

                 elif campo == 7:
                      Fun_numero = raw_input ("Redefina o numero da resid�ncia do funcion�rio.: ")
                      sql = "update funcionarios set Fun_numero = '"+Fun_numero+"' where Fun_nome = '"+busca+"'"
                      try:
                          cursor.execute(sql)
                          db.commit()
                        
                      except:
                          db.rollback()
                          
                 elif campo == 8:
                      Fun_complemento= raw_input ("Redefina o complemento sobre a resid�ncia do funcion�rio.: ")
                      sql = "update funcionarios set Fun_complemento = '"+Fun_complemento+"' where Fun_nome = '"+busca+"'"
                      try:
                          cursor.execute(sql)
                          db.commit()
                      except:
                          db.rollback()
                               

                 elif campo == 9:
                     Fun_bairro = raw_input ("Redefina o bairro do funcion�rio.: ")
                     sql = "update funcionarios set Fun_bairro = '"+Fun_bairro+"' where Fun_nome = '"+busca+"'"
                     try:
                         cursor.execute(sql)
                         db.commit()
                     except:
                         db.rollback()
                                

                 elif campo == 10:
                      Fun_cep = raw_input ("Redefina CEP do funcion�rio.: ")
                      sql = "update funcionarios set Fun_cep = '"+Fun_cep+"' where Fun_nome = '"+busca+"'"
                      try:
                          cursor.execute(sql)
                          db.commit()
                      except:
                          db.rollback()

                 elif campo == 11:
                     Fun_cidade = raw_input ("Redefina a cidade do funcion�rio.: ")
                     sql = "update funcionarios set Fun_cidade = '"+Fun_cidade+"' where Fun_nome = '"+busca+"'"
                     try:
                         cursor.execute(sql)
                         db.commit()
                     except:
                         db.rollback()

                 elif campo == 12:
                     Fun_estado = raw_input ("Redefina o estado: ")
                     sql = "update funcionarios set Fun_estado = '"+Fun_estado+"' where Fun_nome = '"+busca+"'"
                     try:
                         cursor.execute(sql)
                         db.commit()
                     except:
                         db.rollback()

                 elif campo == 13:
                     Fun_tel= raw_input ("Redefina o telefone do funcion�rio.: ")
                     sql = "update funcionarios set Fun_tel = '"+Fun_tel+"' where Fun_nome = '"+busca+"'"
                     try:
                         cursor.execute(sql)
                         db.commit()
                     except:
                         db.rollback()

                 elif campo == 14:
                     Fun_cel = raw_input ("Redefina o celular do funcion�rio.: ")
                     sql = "update funcionarios set Fun_cel = '"+Fun_cel+"' where Fun_nome = '"+busca+"'"
                     try:
                         cursor.execute(sql)
                         db.commit()
                     except:
                         db.rollback()
                               

                 elif campo == 15:
                     Fun_n_carteira= raw_input ("Redefina o o n�mero de carteira de trabalho do funcion�rio.: ")
                     sql = "update funcionarios set Fun_n_carteira = '"+Fun_n_carteira+"' where Fun_nome = '"+busca+"'"
                     try:
                         cursor.execute(sql)
                         db.commit()
                     except:
                         db.rollback()
                                

                 elif campo == 16:
                     Fun_admissao= raw_input ("Redefina a data de admiss�o do funcion�rio.: ")
                     sql = "update funcionarios set Fun_admissao = '"+Fun_admissao+"' where Fun_nome = '"+busca+"'"
                     try:
                         cursor.execute(sql)
                         db.commit()
                     except:
                         db.rollback()
                                
                                
                 elif campo == 17:
                     Fun_login_usuario= raw_input ("Redefina o login do funcion�rio.: ")
                     sql = "update funcionarios set Fun_login_usuario = '"+Fun_login_usuario+"' where Fun_nome = '"+busca+"'"
                     try:
                         cursor.execute(sql)
                         db.commit()
                     except:
                         db.rollback()

                 elif campo == 18:
                     Fun_senha_login = raw_input ("Redefina a senha do funcion�rio.: ")
                     sql = "update funcionarios set Fun_senha_login = '"+Fun_senha_login+"' where Fun_nome = '"+busca+"'"
                     try:
                         cursor.execute(sql)
                         db.commit()
                     except:
                         db.rollback()
                                

                 elif campo == 19:
                     Fun_observacoes = raw_input ("Redefina as observa��es sobre funcion�rio.: ")
                     sql = "update funcionarios set Fun_observacoes = '"+Fun_observacoes+"' where Fun_nome = '"+busca+"'"
                     try:
                         cursor.execute(sql)
                         db.commit()
                     except:
                         db.rollback()
                                

                 elif campo == 20:
                     Fun_funcao= raw_input ("Redefina a fun��o do funcion�rio.: ")
                     sql = "update funcionarios set Fun_funcao = '"+Fun_funcao+"' where Fun_nome = '"+busca+"'"
                     try:
                         cursor.execute(sql)
                         db.commit()

                     except:
                         db.rollback()
                                


        elif atividade == 3:
            sql = "select * from funcionarios" 
            cursor.execute(sql)
            print 'Os funcion�rios inseridos no sistema s�o.: '
            results = cursor.fetchall()
            for row in results:
                e = row[1]
                print e
            busca = raw_input ("Digite o nome do funcion�rio que deseja excluir.: ")
            sql = "delete from funcionarios where Fun_nome = '"+busca+"'"
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()
                


        elif atividade == 4:
            print "Os campos marcados com asterisco n�o podem ser vazios"

            Cli_ID = raw_input ("Digite o c�digo do cliente*.: ")
            Cli_nome = raw_input ("Digite o nome do cliente*.: ")
            Cli_sexo = raw_input ("Digite o sexo do cliente*.: ")
            Cli_endereco = raw_input ("Digite o endereco do cliente*.: ")
            Cli_numero = raw_input ("Digite o numero da residencia do cliente*.: ")
            Cli_complemento = raw_input ("Digite as informa��es adicionais sobre o endere�o do cliente.: ")
            Cli_bairro = raw_input ("Digite o bairro do cliente*.: ")
            Cli_cep = raw_input ("Digite o CEP do cliente*.: ")
            Cli_cidade = raw_input ("Digite a cidade do cliente*.: ")
            Cli_estado = raw_input ("Digite o estado do cliente*.: ")
            Cli_telefone = raw_input ("Digite o n�mero do telefone do cliente.: ")
            Cli_celular = raw_input ("Digite o n�mero do celular do cliente*.: ")
            Cli_observacoes = raw_input ("Digite as informa��es adicionais sobre o cliente.: ")
            Cli_CPF = raw_input ("Digite o CPF do cliente.: ")


            sql = "insert into clientes values ('"+Cli_ID+"','"+Cli_nome+"', '"+Cli_sexo+"', '"+Cli_endereco+"', '"+Cli_numero+"', '"+Cli_complemento+"','"+Cli_bairro+"', '"+Cli_cep+"','"+Cli_cidade+"', '"+Cli_estado+"', '"+Cli_telefone+"', '"+Cli_celular+"','"+Cli_observacoes+"','"+Cli_CPF+"')"

            try:
                cursor.execute(sql)
                db.commit ()

            except:
                db.rollback()
                
        elif atividade == 5:
            sql = "select * from clientes" 
            cursor.execute(sql)
            print 'Os usu�rios inseridos no sistema s�o.: '
            results = cursor.fetchall()
            for row in results:
                e = row[1]
                print e
            busca = raw_input ("Digite o nome do cliente que deseja alterar os dados.: ")
            sql = "select * from clientes where Cli_nome like '"+busca+"'"
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                e = row[1]
            
            if str(e) != busca:
                print 'Esse cliente n�o existe no sistema.: '
            elif str(e) == busca:
                print 'O funcion�rio est� cadastrado no sistema.:'
                print 'Opc�es de atualiza��o.: '
                print ' 1-Para atualizar o c�digo do cliente.: '
                print ' 2-Para atualizar o nome do cliente.: '
                print ' 3-Para atualizar o sexo do cliente.: '
                print ' 4-Para atualizar o endere�o do cliente.: '
                print ' 5-Para atualizar o n�mero da resid�ncia do cliente.: '
                print ' 6-Para atualizar as informa��es adicionais sobre o endereco do cliente.: '
                print ' 7-Para atualizar o bairro do cliente.: '
                print ' 8-Para atualizar o CEP do cliente.: '
                print ' 9-Para atualizar a cidade do cliente.: '
                print '10-Para atualizar o .estado do cliente: '
                print '11-Para atualizar o n�mero de telefone do cliente.: '
                print '12-Para atualizar o n�mero de celular do cliente.: '
                print '13-Para atualizar as informacoes adicionais sobre o cliente.: '
                print '14-Para atualizar o CPF do cliente.:\n '
                
                campo = input ("Digite o campo deseja quer atualizar.:")
                if campo == 1:
                    Cli_ID = raw_input ("Redefina um c�digo para o cliente*.: ")
                    sql = "update clientes set Cli_ID = '"+Cli_ID+"' where Cli_nome = '"+busca+"'"
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()
                elif campo == 2:               
                    Cli_nome = raw_input ("Redefina o nome do cliente*.: ")
                    sql = "update clientes set Cli_nome = '"+Cli_nome+"' where Cli_nome = '"+busca+"'"
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()
                elif campo == 3:               
                    Cli_sexo = raw_input ("Redefina o sexo do cliente*.: ")
                    sql = "update clientes set Cli_sexo = '"+Cli_sexo+"' where Cli_nome = '"+busca+"'" 
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()
                elif campo ==4:
                    Cli_endereco = raw_input ("Redefina o endere�o do cliente*.: ")
                    sql = "update clientes set Cli_endereco = '"+Cli_endereco+"' where Cli_nome = '"+busca+"'"
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()
                elif campo == 5:
                    Cli_numero = raw_input ("Redfina o n�mero da resid�ncia do cliente*.: ")
                    sql = "update clientes set Cli_numero = '"+Cli_numero+"' where Cli_nome = '"+busca+"'"
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()
                elif campo ==6:
                    Cli_complemento = raw_input ("Redefina as informa��es adicionais sobre o endere�o do cliente.: ")
                    sql = "update clientes  set Cli_complemento = '"+Cli_complemento+"' where Cli_nome = '"+busca+"'" 
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()
                elif campo==7:
                    Cli_bairro = raw_input ("Redefina o bairro do cliente*.: ")
                    sql = "update clientes  set Cli_bairro = '"+Cli_bairro+"' where Cli_nome = '"+busca+"'"
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()
                elif campo == 8:
                    Cli_cep = raw_input ("Redefina o CEP do cliente*.: ")
                    sql = "update clientes set Cli_campo = '"+Cli_campo+"' where Cli_nome = '"+busca+"'"
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()
                elif campo == 9:
                    Cli_cidade = raw_input ("Redefina a cidade do cliente*.: ")
                    sql = "update clientes  set Cli_cidade = '"+Cli_cidade+"' where Cli_nome = '"+busca+"'"
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()
                
                elif campo ==10:
                    Cli_estado = raw_input ("Redefina o estado do cliente*.: ")
                    sql = "update clientes  set Cli_estado = '"+Cli_estado+"' where Cli_nome = '"+busca+"'"
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()
                elif campo == 11:
                    Cli_telefone = raw_input ("Redefina o n�mero do telefone do cliente.: ")
                    sql = "update clientes  set Cli_telefone = '"+Cli_telefone+"' where Cli_nome = '"+busca+"'"
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()
                elif campo ==12:
                    Cli_celular = raw_input ("Redefina o n�mero do celular do cliente*.: ")
                    sql = "update clientes  set Cli_campo = '"+Cli_campo+"' where Cli_nome = '"+busca+"'"
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()
                elif campo == 13:
                    Cli_observacoes = raw_input ("Redefina as informa��es adicionais sobre o cliente.: ")
                    sql = "update clientes set Cli_observacoes = '"+Cli_observacoes+"' where Cli_nome = '"+busca+"'"
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()
                elif campo == 14:
                    Cli_cpf = raw_input ("Redefina o cpf do cliente.: ")
                    sql = "update clientes set Cli_CPF = '"+Cli_cpf+"' where Cli_nome = '"+busca+"'"
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()

        elif atividade == 6:
            sql = "select * from clientes" 
            cursor.execute(sql)
            print 'Os clientes inseridos no sistema s�o.: '
            results = cursor.fetchall()
            for row in results:
                e = row[1]
                print e
            busca = raw_input ("Digite o nome do cliente que deseja excluir.: ")
            sql = "delete from clientes where Cli_nome = '"+busca+"'"
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()
      
        elif atividade == 7:
            sql = "select * from filme" 
            cursor.execute(sql)
            print 'Os filmes inseridos no sistema s�o.: '
            results = cursor.fetchall()
            for row in results:
                e = row[1]
                print e
            Fil_ID = raw_input("Digite um c�digo para o filme.: ")
            Fil_nome = raw_input ("Digite o nome do filme.: ")
            Fil_genero = raw_input ("Digite o g�nero do filme.: ")
            Fil_class_et = raw_input ("Digite a classe et�ria do filme.: ")
            Fil_observacoes = raw_input ("Digite informa��es adicionais sobre o filme.: ")
           
            sql = "insert into filme values ('"+Fil_ID+"','"+Fil_nome+"','"+Fil_genero+"','"+Fil_class_et+"','"+Fil_observacoes+"')"
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()
        elif atividade == 8:
             sql = "select * from filme" 
             cursor.execute(sql)
             print 'Os filmes cadastrados no sistema s�o.: '
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
                 print "Esse filme n�o est� cadastrado no sistema"
             elif busca == e:
                 print 'Opc�es de atualiza��o.: '
                 print ' 1-Para atualizar o c�digo do filme.: '
                 print ' 2-Para atualizar o nome do filme.: '
                 print ' 3-Para atualizar o g�nero do filme.: '
                 print ' 4-Para atualizar a classifica��o et�ria do filme.: '
                 print ' 5-Para atualizar as observa��es sobre o filme.:\n '
                 campo = input ("Digite o campo que deseja atualizar.: ")
                 if campo == 1:
                     Fil_ID = raw_input ("Redefina o c�digo do filme.: ")
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
                     Fil_genero = raw_input ("Redefina o g�nero do filme.: ")
                     sql = "update filme set Fil_genero = '"+Fil_genero+"' where Fil_nome = '"+busca+"'"
                     try:
                         cursor.execute(sql)
                         db.commit()
                     except:
                         db.rollback()
                 elif campo == 4:
                     Fil_class_et = raw_input ("Redefina a classifica��o et�ria do filme.: ")
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
            print 'Os filmes cadastrados no sistema s�o.: '
            results = cursor.fetchall()
            for row in results:
                w = row[1]
                print w
            busca = raw_input ("Digite o nome do filme que deseja excluir.: ")
            if w != busca:
                print "Esse filme n�o est� cadastrado no sistema.: "
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
            print 'Os filmes cadastrados no sistema s�o.: '
            results = cursor.fetchall()
            for row in results:
                w = row[1]
                print w
            print 'Pesquisa de disponibilidade de filme para locacao.: '
##          Pesquisa da vari�vel busca na coluna Loc_filme da tabela locacao
            busca = raw_input ("Digite o nome do filme.: ")

            sql = "select * from locacao where Loc_filme like '"+busca+"'"
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                e = row[2]
                print str(e)
##          Pesquisa da vari�vel busca na coluna Fil_nome da tabela filme
            sql = "select * from filme where Fil_nome like '"+busca+"'"
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                d = row[1]
                print str(d)

            if busca == str(e) and busca == str(d):
                print 'O filme j� est� locado'
            elif busca != str(e) and busca == str(d):
                print 'O fime est� dispon�vel para locacao'
            elif busca != str(e) and busca != str(d):
                print 'O filme n�o existe no acervo'
                
        elif atividade == 11:
            sql = "select * from filme" 
            cursor.execute(sql)
            print 'Os filmes cadastrados no sistema s�o.: '
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
                print 'O filme n�o est� cadastrado no sistema'
            elif str(d) == busca:
                if busca == str(e) and busca == str(d):
                    print 'O filme j� est� locado'
                elif busca != str(e) and busca == str(d):
                    print 'O filme est� dispon�vel para locacao'
                    sql = "select * from clientes" 
                    cursor.execute(sql)
                    print 'Os clientes inseridos no sistema s�o.: '
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
                        print 'Este usu�rio n�o est� cadastrado no sistema'
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
                    print 'O filme n�o existe no acervo'
            
            
        elif atividade == 12:
                sql = "select * from clientes" 
                cursor.execute(sql)
                print 'Os clientes inseridos no sistema s�o.: '
                results = cursor.fetchall()
                for row in results:
                    e = row[1]
                    print e
                sql = "select * from filme" 
                cursor.execute(sql)
                print 'Os filmes cadastrados no sistema s�o.: '
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
                    print'C�digo do cliente.:', e
                    print'Nome do cliente.:',l
                if x !=l:
                    print 'O cliente n�o est� cadastrado no sistema'
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
                 
        elif atividade == 13:
            print 'Sistema de cadastro de filme.:\n '
            print 'Os filmes que est�o locados sao.: '
            sql = "select * from locacao"
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                e = row[2]
                print e
            busca = raw_input ('Digite o filme que ser� devolvido.: ')
            sql = "delete from locacao where Loc_filme = '"+busca+"'"
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()
            

        elif atividade == 14:
            break




db.close()


                


            

                

                

