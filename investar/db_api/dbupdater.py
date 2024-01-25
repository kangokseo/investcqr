import pymysql

'''
connection = pymysql.connect(host='localhost', port=3306, 
            db='INVESTAR', user='root', password='eugene99', autocommit=True)

cursor = connection.cursor()
cursor.execute ("select version();")
result = cursor.fetchone()

print ("kaseo mariadb version : {}".format(result))

connection.close()        
'''