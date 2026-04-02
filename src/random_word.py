import logging
from database import check_for_language, retrieve_random_word


def get_random_word(language, number):
    if not check_for_language(language):
        raise ValueError(f"Language '{language}' not found in the database.")

    rows = retrieve_random_word(language, number)

    if rows is None:
        logging.info("No data retrieved from the database.")
        return

    if isinstance(rows, tuple) and (len(rows) == 0 or not isinstance(rows[0], (list, tuple))):
        rows = [rows]

    col_w = 40
    print(
        f"{'article'.ljust(col_w)} {'word'.ljust(col_w)} "
        f"{'meaning'.ljust(col_w)} {'pronunciation'.ljust(col_w)}"
    )
    print("-" * (col_w * 4 + 3))

    for row in rows:
        article = (row[0] or "").ljust(col_w)[:col_w]
        word = (row[1] or "").ljust(col_w)[:col_w]
        meaning = (row[2] or "").ljust(col_w)[:col_w]
        pronunciation = (row[3] or "").ljust(col_w)[:col_w]

        print(f"{article} {word} {meaning} {pronunciation}")
