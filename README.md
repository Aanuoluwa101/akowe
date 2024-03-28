# Akowe API Documentation

This is the API documentation for akowe. This documents covers only the endpoints needed for the planned user testing of the application. So, no signup or signin etc

## Base URL

The base URL for all API routes is `https://akowe.onrender.com/api/v1`.

## Routes

### 1. Get rankings

- **Route:** `/rankings`
- **Method:** GET
- **Description:** Get officiator ranks.
- **Response Code:** 200 OK
- **Response Body:**
```json
[
  {
    "name": "Brother",
    "short": "Bro.",
    "weight": 1
  },
  {
    "name": "Elder Brother",
    "short": "Eld. Bro.",
    "weight": 2
  }
]
```


### 2. Generate Roster

- **Route:** `/rosters`
- **Method:** POST
- **Description:** Generate a roster.
- **Request Body:**
 ```json
 {
    "temp_user": "John",
    "email": "aanu@gmail.com",
    "month": "April", 
    "year": "2024",
    "bible_lesson_file": "bible_lessons_d.json",
    "officiators": [
            {
              "id": 5,
              "name": "Akande Tosin",
              "rank": {"name": "Sup Evang", "weight": 9, "short": "Sup. Evang"},
              "can_conduct_on_weekdays": true,
              "can_conduct_on_sundays": true,
              "can_read_on_weekdays": true,
              "can_read_on_sundays": true,
              "can_preach_on_weekdays": true,
              "can_preach_on_sundays": true,
              "enforcements": [
                           { 
                             "date": "03-04-2024", 
                             "service_type": "weekday", 
                             "officiation": "first_lesson_reader"
                           }
                      ]
            },
            {
              "id": 6,
              "name": "Wonderful",
              "rank": {"name": "Sup Evang", "weight": 9, "short": "Sup. Evang"},
              "can_conduct_on_weekdays": false,
              "can_conduct_on_sundays": true,
              "can_read_on_weekdays": true,
              "can_read_on_sundays": true,
              "can_preach_on_weekdays": true,
              "can_preach_on_sundays": true,
              "enforcements": []
            }
       ]
}
 ```
- **Notes on Request Body**
 - Enforcements can be more than one
 - temp_user will be entered on the UI as username and email as email
 - The month and year should be April and 2024 respectively but this should be shown to the user.
 - bible lesson file should be hardcoded as "bible_lessons_d.json"
- **Response Code:** 201 CREATED
- **Response Body:**
```json
{
  "username": "John",
  "email": "aanu@gmail.com",
  "month": "April",
  "year": "2024",
  "roster": [
    {
      "date": "03-04-2024",
      "day": "Wednesday",
      "conductor": "Sup. Evang Akande Tosin",
      "first_lesson": {
        "lesson": "Romans 6:1-14",
        "reader": "Sup. Evang Akande Tosin"
      },
      "second_lesson": null,
      "preacher": "Sup. Evang Wonderful"
    },
    {
      "date": "04-04-2024",
      "day": "Thursday",
      "conductor": "Sup. Evang Akande Tosin",
      "first_lesson": {
        "lesson": "Amos 8:1-10",
        "reader": "Sup. Evang Akande Tosin"
      },
      "second_lesson": null,
      "preacher": "Sup. Evang Wonderful"
    },
    {
      "date": "05-04-2024",
      "day": "Friday",
      "conductor": "Sup. Evang Akande Tosin",
      "first_lesson": {
        "lesson": "Amos 8:10-14",
        "reader": "Sup. Evang Wonderful"
      },
      "second_lesson": null,
      "preacher": "Sup. Evang Akande Tosin"
    },
    {
      "date": "07-04-2024",
      "day": "Sunday",
      "conductor": "Sup. Evang Akande Tosin",
      "first_lesson": {
        "lesson": "Micah 1:1-16",
        "reader": "Sup. Evang Akande Tosin"
      },
      "second_lesson": {
        "lesson": "Acts 17:1-14",
        "reader": "Sup. Evang Wonderful"
      },
      "preacher": "Sup. Evang Wonderful"
    },
    {
      "date": "10-04-2024",
      "day": "Wednesday",
      "conductor": "Sup. Evang Akande Tosin",
      "first_lesson": {
        "lesson": "Philippians 3:15-21",
        "reader": "Sup. Evang Akande Tosin"
      },
      "second_lesson": null,
      "preacher": "Sup. Evang Wonderful"
    },
    {
      "date": "12-04-2024",
      "day": "Friday",
      "conductor": "Sup. Evang Akande Tosin",
      "first_lesson": {
        "lesson": "1 Thessalonians 2:13-16",
        "reader": "Sup. Evang Wonderful"
      },
      "second_lesson": null,
      "preacher": "Sup. Evang Akande Tosin"
    },
    {
      "date": "14-04-2024",
      "day": "Sunday",
      "conductor": "Sup. Evang Wonderful",
      "first_lesson": {
        "lesson": "Joshua 11:1-15",
        "reader": "Sup. Evang Akande Tosin"
      },
      "second_lesson": {
        "lesson": "2 Corinthians 2:1-17",
        "reader": "Sup. Evang Wonderful"
      },
      "preacher": "Sup. Evang Akande Tosin"
    },
    {
      "date": "17-04-2024",
      "day": "Wednesday",
      "conductor": "Sup. Evang Akande Tosin",
      "first_lesson": {
        "lesson": "1 Chronicles 17:15-27",
        "reader": "Sup. Evang Akande Tosin"
      },
      "second_lesson": null,
      "preacher": "Sup. Evang Wonderful"
    },
    {
      "date": "19-04-2024",
      "day": "Friday",
      "conductor": "Sup. Evang Akande Tosin",
      "first_lesson": {
        "lesson": "1 Thessalonians 1:4-10",
        "reader": "Sup. Evang Wonderful"
      },
      "second_lesson": null,
      "preacher": "Sup. Evang Akande Tosin"
    },
    {
      "date": "21-04-2024",
      "day": "Sunday",
      "conductor": "Sup. Evang Akande Tosin",
      "first_lesson": {
        "lesson": "Isaiah 50:1-11",
        "reader": "Sup. Evang Akande Tosin"
      },
      "second_lesson": {
        "lesson": "Colossians 1:12-23",
        "reader": "Sup. Evang Wonderful"
      },
      "preacher": "Sup. Evang Wonderful"
    },
    {
      "date": "24-04-2024",
      "day": "Wednesday",
      "conductor": "Sup. Evang Akande Tosin",
      "first_lesson": {
        "lesson": "1 Chronicles 16:7-22",
        "reader": "Sup. Evang Akande Tosin"
      },
      "second_lesson": null,
      "preacher": "Sup. Evang Wonderful"
    },
    {
      "date": "26-04-2024",
      "day": "Friday",
      "conductor": "Sup. Evang Akande Tosin",
      "first_lesson": {
        "lesson": "1 Chronicles 16:23-33",
        "reader": "Sup. Evang Wonderful"
      },
      "second_lesson": null,
      "preacher": "Sup. Evang Akande Tosin"
    },
    {
      "date": "28-04-2024",
      "day": "Sunday",
      "conductor": "Sup. Evang Wonderful",
      "first_lesson": {
        "lesson": "Leviticus 3:1-17",
        "reader": "Sup. Evang Wonderful"
      },
      "second_lesson": {
        "lesson": "1 Corinthians 16:1-14",
        "reader": "Sup. Evang Akande Tosin"
      },
      "preacher": "Sup. Evang Akande Tosin"
    }
  ]
}
```
- **Notes on Reponse Body**
 -- Consider each object in the roster array as a service

### 3. Create a Comment
- **Route:** `/test/comments`
- **Method:** POST
- **Description:** Create a comment. Some input box on the UI where users are encouraged to comment on the app and suggest how it can be improved.
- **Request Body:**
 ```json
 {
  "username": "mercy",
  "email": "mercy@gmai.com",
  "comment": "very nice app"
}
 ```
- **Response Code:** 201 CREATED
- **Response Body:** The created comment
