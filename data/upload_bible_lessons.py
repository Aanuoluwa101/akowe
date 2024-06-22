import pandas as pd
import json


def upload_bible_lessons(year, month, lesson_csv_file, type):
    df = pd.read_csv(lesson_csv_file)

    json_data = {}
    for index, row in df.iterrows():
        date = pd.to_datetime(row['Date'], format='%d/%m/%Y').strftime('%d-%m-%Y')
        first_lesson = row['First Lesson'] if not pd.isnull(row['First Lesson']) else None
        second_lesson = row['Second Lesson'] if not pd.isnull(row['Second Lesson']) else None

        json_data[date] = {
            'first_lesson': first_lesson,
            'second_lesson': second_lesson
        }

    if type == "t":
        lesson_file = f"./years/{year}/{month}/bible_lessons_t.json"
    elif type == "d":
        lesson_file = f"./years/{year}/{month}/bible_lessons_d.json"

    with open(lesson_file, 'w') as json_file:
        json.dump(json_data, json_file, indent=2)


if __name__ == "__main__":
    upload_bible_lessons("2024", "July", "./July_2024_Bible_Lessons - Sheet1.csv", "d")