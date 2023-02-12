import sqlite3

connection = sqlite3.connect('app.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE groceries 
               (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)''')
groceries = ['Apples',
             'Bananas',
             'Strawberries',
             'Avocados',
             'Bell Peppers',
             'Carrots',
             'Broccoli',
             'Garlic',
             'Lemons/Limes',
             'Onion',
             'Parsley',
             'Cilantro',
             'Basil',
             'Potatoes',
             'Spinach',
             'Tomatoes'
             ]

for i in groceries:
    cursor.execute("insert into groceries (name) values (?)", [i])

connection.commit()
connection.close()
