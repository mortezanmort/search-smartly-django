# SearchSmartly Project

## Overview
SearchSmartly is a Django project designed to import and manage Point of Interest (POI) data from various file formats using Celery for background task processing. It supports CSV, JSON, and XML file imports.

## Getting Started

### Prerequisites
- Python (>=3.10)
- Django
- Redis
- Celery
- SQLite

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/SearchSmartly.git
    cd SearchSmartly
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Start Redis server:
    ```bash
    redis-server
    ```

5. Run Celery:
    ```bash
    celery -A SearchSmartly worker -l info
    ```

6. Migrate and run the Django development server:
    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

7. Open your browser and go to http://127.0.0.1:8000/admin to access the Django admin.

## Importing POI Data

To import POI data, use the `import_poi_data` management command. For example:

```bash
python manage.py import_poi_data Data/pois.csv
python manage.py import_poi_data Data/pois.json
python manage.py import_poi_data Data/pois.xml
```
Or you can add all parameters with one command, for example: 
```bash


python manage.py import_poi_data Data/pois.csv Data/pois.json Data/pois.xml
```

## Assumptions

### Unique Identifier:

- Since the structure of files does not have any external ID attribute (in CSV, XML, JSON), a uuid4 unique key is created for each record.
- The approach of making each record unique by adding an external ID attribute was chosen to support the requirement of being able to search by external ID.
- The reason being one of the requirements stated 'be able to search record by external ID' 
- Upon Examining the data from files, External ID was not present. 
- My assumption was to make a new attribute 'External ID' for each record while inserting into the database and make it unique accross all files. 
- External ID, therefore, is a uuid.

### Duplicate Record Handling:

- The decision was made to create each record as unique with the addition of an external ID attribute.
- The alternative approach of checking each record while reading from files to see if it already exists with the same ID (internal POI_id) was considered but not implemented.


## Accessing Django Admin

#### 1. Create Superuser:

- To access the Django admin, create a superuser by running the following command:
```bash
python manage.py createsuperuser
```
- Follow the prompts to set up a username, email, and password for the superuser.


#### 2. Django Admin Access:

- Start the Django development server if not already running:
```bash
python manage.py runserver
```
- Open your browser and go to http://127.0.0.1:8000/admin.
- Log in using the superuser credentials created.


## Using Celery for Scalability
- Celery is used as a task queue to handle background processing of POI data imports.
- The ```celery -A SearchSmartly worker -l info``` command starts the Celery worker.
- This allows the project to scale efficiently when dealing with a large number of records, making the import process asynchronous and parallelizable.


## Further Improvements

### Testing:
- Implement test cases using a testing framework like pytest to ensure the correctness and reliability of the application.
