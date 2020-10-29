from sqlProject import dbSql

b1 = dbSql('test')
b1.createTable({'firstColumn': 'TEXT', 'secondColumn': 'REAL'})
