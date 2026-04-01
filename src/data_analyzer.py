from database import check_for_language, analyze_data


def analyze_data_for_language(language):
    if not check_for_language(language):
        raise ValueError(f"Language '{language}' not found in the database.")
    count = analyze_data(language)
    print("Number of rows without pronunciation %s: %d", language, count)
    return count
