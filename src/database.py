import sqlite3


def get_connection():
    return sqlite3.connect("pronunciations.db")


def check_for_language(language):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name=?",
        (language,),
    )
    result = cursor.fetchone()
    connection.close()
    return result is not None


def retrieve_random_word(language, number=1):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT article, word, meaning, pronunciation "  # nosec
        f"FROM {language} "
        "ORDER BY RANDOM() "
        f"LIMIT {number}"
    )
    result = cursor.fetchall()
    connection.close()
    return result if result else None


def analyze_data(language):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT COUNT(*) "  # nosec
        f"FROM {language} "
        "WHERE pronunciation IS NULL OR pronunciation = ''"
    )
    result = cursor.fetchone()
    connection.close()
    return result[0] if result else 0


def list_available_languages():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    connection.close()
    return [table[0] for table in tables if table[0].isalpha()]


def store_pronunciation(language, word, pronunciation):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        f"UPDATE {language} SET pronunciation = ? WHERE word = ?",  # nosec
        (pronunciation, word)
    )
    connection.commit()
    connection.close()
