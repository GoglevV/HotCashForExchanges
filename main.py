import pyodbc
import config




if __name__ == '__main__':
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+config.server+';DATABASE='+config.database+';UID='+config.username+';PWD='+ config.password)
    cursor = cnxn.cursor()
    cursor.execute('SELECT TOP 5 [code], [Остаток] as Count, [Цена] as Price FROM sales.w_остаток_как_на_сайте')
    row = cursor.fetchone()
    while row:
        print(row[0], row[1], row[2])
        row = cursor.fetchone()


