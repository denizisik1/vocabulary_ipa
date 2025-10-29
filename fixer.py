import sqlite3

connection = sqlite3.connect('pronunciations.db')
cursor = connection.cursor()

""" Connect to the database and to the "german" table
    if the word column has die, der, das, das/die, das/der, der/das, der/die, die/das, die/der
    move them to the column article and remove them from the word column.
"""
cursor.execute("SELECT id, article, word FROM german WHERE word LIKE 'die %' OR word LIKE 'der %' OR word LIKE 'das %' OR word LIKE 'das/die %' OR word LIKE 'das/der %' OR word LIKE 'der/das %' OR word LIKE 'der/die %' OR word LIKE 'die/das %' OR word LIKE 'die/der %'")
rows = cursor.fetchall()
for row in rows:
    id = row[0]
    article = row[1]
    word = row[2]

    parts = word.split(" ", 1)
    new_article = parts[0]
    new_word = parts[1] if len(parts) > 1 else ""

    cursor.execute("UPDATE german SET article = ?, word = ? WHERE id = ?", (new_article, new_word, id))
    print(f"Updated id {id}: article='{new_article}', word='{new_word}'")
    
connection.commit()
connection.close()
