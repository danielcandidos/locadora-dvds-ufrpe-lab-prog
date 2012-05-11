import MySQLdb
db = MySQLdb.connect ('localhost','root','mugen','projeto')
cursor = db.cursor()
ID = raw_input ("Digite o ID da cidade.: ")
Nome = raw_input ("Digite o nome da cidade.: ")
Estado = raw_input ("Digite o nome do estado.:")

sql = "insert into cidades values("+ID+", '"+Nome+"', '"+Estado+"')"                      

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()

