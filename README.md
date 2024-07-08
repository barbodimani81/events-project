1. Install the required dependencies.

   ```bash
   pip install -r requirements.txt
   ```

2. Apply migrations to set up the database.

   ```bash
   python manage.py makemigrations
   
   python manage.py migrate
   ```

3. Create a superuser to access the Django admin panel.

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to create a superuser account.

4. Run the development server.

   ```bash
   python manage.py runserver
   ```

   The application will be accessible at [http://localhost:8000/](http://localhost:8000/).


# steps:
1. create a user
2. login with user
3. create category: /content/categories/
4. create session: /content/categories/
5. create event: content/event/create/   # sample date or time: 2024-07-05 or 13:31:02
6. admin panel