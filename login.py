import pymysql as pms
conn = pms.connect(host="localhost", 
                   port=3306,
                   user="root",
                   password="Satvika",
                   db="ab")
print(conn)
cursor=conn.cursor()

def getcredentials():
    username =[]
    pwd=[]
    cursor.execute("SELECT * FROM login ")
    result =cursor.fetchall()
    #print(result)
    for i in result:
        username.append(i[0])
        pwd.append(i[1])
    #print(username)
    return username , pwd
#print(getcredentials())
