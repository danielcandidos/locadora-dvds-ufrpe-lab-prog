import MySQLdb
db = MySQLdb.connect("localhost","root","mugen","projeto")
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print"Database version: %s"% data

db.close()

print "Selecione a op��o que ser� efetuada.:\n "
print "Digite.:\n "
print "1 - Para cadastrar funcin�rios\n"
print "2 - Para atualizar cadastro de funcion�rios\n"
x = 1

while x == 1:
    print 'Digite zero para encerrar as operacoes.:\n'
    pergunta = input ("Qual op��o ser� selecionada.:\n ")
    
    if pergunta == 0:break

    elif pergunta == 1:
        print 'Digite os dados para os clientes.:\n'
        Fun_ID = raw_input ("Digite o codigo do funcion�rio.: ")
        Fun_nome = raw_input("Informe o nome do funcion�rio a ser cadastrado*: ")
        Fun_sexo = raw_input("Informe o sexo do funcionario*(M/F): " )
        Fun_cpf = raw_input("Infome o CPF(Apenas os n�meros)*: ")
        Fun_rg = raw_input("Informe o RG: ")
        Fun_endereco = raw_input("Informe o endereco*: ")
        Fun_numero = raw_input("Informe o n�mero da resid�ncia: ")
        Fun_complemento = raw_input("Informe o complemento (se houver): ")
        Fun_bairro = raw_input("Informe o Bairro: ")
        Fun_cep = raw_input("Informe o CEP(somente n�meros)*: ")
        Fun_cidade = raw_input("Informe a Cidade*: ")
        Fun_estado = raw_input("informe o Estado*: ")
        Fun_tel = raw_input("Informe o Tel: ")
        Fun_cel = raw_input ("Informe o Cel: ")
        Fun_n_carteira = raw_input("Informe o n�mero da carteira de trabalho do funcion�rio: ")
        Fun_admissao = raw_input('Informe a Data de Admiss�o (formato DD/MM/AAAA): ')
        Fun_login_usuario = raw_input("Digite o nome de Login de usu�rio deste sistema: ")
        Fun_senha_usuario = raw_input("Digite a senha de acesso ao sistema, deste usu�rio: ")
        Fun_observacoes = raw_input ("Digite as observa�oes sobre o funcionario.: ")
        Fun_funcao = raw_input ("Digite a funcao do funcionario.: ")
        sql = "INSERT INTO funcionarios values ('"+Fun_ID+"','"+Fun_nome+"','"+Fun_sexo+"','"+Fun_cpf+"','"+Fun_rg+"','"+Fun_endereco+"','"+Fun_numero+"','"+Fun_complemento+"','"+Fun_bairro+"','"+Fun_cep+"','"+Fun_cidade+"','"+Fun_estado+"','"+Fun_tel+"','"+Fun_cel+"','"+Fun_n_carteira+"','"+Fun_admissao+"','"+Fun_login_usuario+"','"+Fun_senha_usuario+"','"+Fun_observacoes+"','"+Fun_funcao+"')"
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
        db.close()

                
    
