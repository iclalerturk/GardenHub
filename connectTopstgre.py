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
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM kullanicilar WHERE mail = %s AND sifre = %s", ("iclalerturk@gardenhub.com", "12345678"))
    user_data = cursor.fetchone()
    conn.close()
    if user_data:
            isim=user_data[0],
            soyisim=user_data[1],
            kullanici_id=user_data[2],
            mail=user_data[3],
            sifre=user_data[4],
            bdate=user_data[5],
            butce=user_data[6],
            user_type=user_data[7],
    print(isim,soyisim)

    # cur = conn.cursor()
    # query = ''' insert into yonetici(mail,sifre) values('admin@hotmail.com','admin') '''
    # cur.execute(query)
    # conn.commit()
    # query = ''' select * from yonetici '''
    # cur.execute(query)
    # rows = cur.fetchall()

    # for row in rows:
    #     print(row)
    # cur.close()
    # conn.close()
except Exception as e:
    print("Error: ", e)
