import psycopg2

hostname = 'localhost'
username = 'postgres'
database = 'GardenHub'
password = '1234'
port_id = '5432'
try:
    conn = psycopg2.connect(host=hostname, user=username, password=password, dbname=database, port=port_id)

    """ query = "insert into yonetici(mail,sifre) values('admin@hotmail.com','admin')"
    preparedStatement = conn.prepareStatement(query)
    preparedStatement.executeQuery()

    query = "select * from yonetici"
    preparedStatement = conn.prepareStatement(query)
    resultSet = preparedStatement.executeQuery(query)

    while resultSet.next():
        print(resultSet.getString(1), resultSet.getString(2)) """
    
    cur = conn.cursor()
    #query = ''' insert into yonetici(mail,sifre) values('admin@hotmail.com','admin') '''
    #cur.execute(query)
    conn.commit()
    query = ''' select * from yonetici '''
    cur.execute(query)
    rows = cur.fetchall()
    print("a",rows[1][1])
    for row in rows:
        print(row)
    cur.close()
    conn.close()
except Exception as e:
    print("Error: ", e)
