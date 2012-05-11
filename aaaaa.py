import MySQLdb
db = MySQLdb.connect("localhost","root","mugen","projeto")
cursor = db.cursor()
sql = """create table funcionarios(
                                    Fun_ID int not null auto_increment primary key,
                                    Fun_nome varchar(60) not null,
                                    Fun_sexo char(1) not null,
                                    Fun_cpf varchar(11) not null,
                                    Fun_rg varchar(20) not null,
                                    Fun_endereco varchar(50) not null,
                                    Fun_numero varchar(5),
                                    Fun_complemento varchar(50),
                                    Fun_bairro varchar(30),
                                    Fun_cep varchar(10) not null,
                                    Fun_cidade varchar(30) not null,
                                    Fun_estado char(2) not null,
                                    Fun_tel varchar(15),
                                    Fun_cel varchar (15),
                                    Fun_n_carteira varchar(25) not null,
                                    Fun_admissão varchar (15) not null,
                                    Fun_login_usuario varchar(10) not null,
                                    Fun_senha_usuario varchar(10) not null,
                                    Fun_observacoes varchar(80),
                                    Fun_funcao varchar (25) not null)"""

cursor.execute(sql)

db.close()
