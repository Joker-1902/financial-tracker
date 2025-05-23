# Financial tracker
Financial Tracker is my personal pet project designed for easily adding and controlling incomes and expenses.

## 1.Functionality
* User login and registration
* Adding income and expense transactions
* Viewing a list of all transactions
* Filtering transactions

## 2. Installation and launch
1. **Clone the repository**
    ```bash
    git clone [https://github.com/your_username/name_of_repository.git](https://github.com/your_username/name_of_repository.git)
    cd name_of_repository
    ```
2. **Create and activate virtual environment**
    ```bash
    python -m venv .venv
    # For Windows:
    .venv\Scripts\activate
    # For macOS/Linux:
    source .venv/bin/activate
    ```    
3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Create the '.env' file**
    
    In the root of the project, create a `.env` file and fill it with the necessary environment variables. Example contents:
    ```
    SECRET_KEY='Your_secret_key'
    DEBUG=True

    DB_NAME='Your_local_db'
    DB_USER='Your_db_user'
    DB_PASSWORD='Your_db_password'
    DB_HOST='localhost'
    DB_PORT='5432'
    ```
    *Important: Never commit the`.env` to the Git!*
5. **Run db migrations**    
    ```bash
    python manage.py migrate
    ```
6. **Create Superuser(optional)**
    ```bash
    python manage.py createsuperuser
    ```
7. **Start the development server**      
    ```bash
    python manage.py runserver
    ```
    Now the app will be available on `http://127.0.0.1:8000/`.

## 3. How to use
    '''Once the server is running, you can interact with the application using the provided buttons or by navigating directly to these endpoints:'''
* Home page: '/'
* Login '/login/' 
* Registration '/registration/'
* Add transaction '/add/'
* View all transactions '/show_list/'
* Add new_category'/add_category/'

## 4. Used technologies
This project was developed using the following technologies::
* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [PostgreSQL](https://www.postgresql.org/)
* [HTML5](https://developer.mozilla.org/ru/docs/Web/HTML)

## 5. License
This project has [MIT License](LICENSE) for more informations, please see [LICENSE](LICENSE.md) file
## 6.Contribution to development
We welcome the contribution to the project! If you;d like to contribute, please follow these steps:
1. Fork the repository
2. Create a new branch (`git checkout -b feature/name_of_feature`).
3. Make changes and commit them (`git commit -m 'Add the new feature'`).
4. Push changes to your fork (`git push origin feature/name_of_feature`).
5. Open a Pull Request


