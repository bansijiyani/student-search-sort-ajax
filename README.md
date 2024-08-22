# Student Search and Sort Application

This Django application allows users to search and sort student data from a CSV file (`student_dataset.csv`). Users can search by name, nationality, or city, and sort the results by name, nationality, city, or age.

## Features

- Search students by name, nationality, or city.
- Sort search results by name, nationality, city, or age.
- Display search results in a tabular format.

## Prerequisites

- Python 3.x
- Django 3.x or later
- pandas library

## Setup

1. **Clone the repository:**

    ```sh
    git clone https://github.com/bansijiyani/student-search-sort-ajax.git
    cd student-search-sort
    ```

2. **Create a virtual environment and activate it:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Run migrations:**

    ```sh
    python manage.py migrate
    ```

5. **Load the student data from the CSV file:**

    ```sh
    python manage.py loaddata student_dataset.csv
    ```

6. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

7. **Open your browser and navigate to:**

    ```
    http://127.0.0.1:8000/
    ```

## Usage

1. **Search Students:**

    - Select the search criteria (Name, Nationality, City) from the dropdown.
    - Enter the search query in the input box.
    - Click the "Search" button to display the results.

2. **Sort Results:**

    - Select the sort criteria (Name, Nationality, City, Age) from the dropdown.
    - The results will be sorted based on the selected criteria.

