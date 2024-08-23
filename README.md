## Description

This project consists of a frontend React application and a backend Django application.

This project is a submission for kangacooks assesment of creating a website in react with a django backend with two apis. I decided to create a simple generative art project recreating joy division's iconic album cover. Usually something like this would be drawn using Javascript but as a challenge to myself and to meet the requirements I decided to create the generative algorithm on the backend and utilize the api to create the drawing and save/display past generations. Because this functionality is not usually done in Python I was only able to create a rough imitation without adding an array of dependencies to perfect the drawing. It was a fun and interesting challenge nonetheless. Have fun messing around with it! This will also serve as a base for other generative projects I decide to create!
#Frontend

npm install
npm start

will be available on localhost:3000

#Backend

python -m venv env (depending on version my have to run 'python3 -m venv env')
source env/bin/activate  # On Windows, use `env\Scripts\activate`

pip install -r requirements.txt
python manage.py migrate (depending on version my have to run 'python3 manage.py migrate')
python manage.py runserver (depending on version my have to run 'python3 manage.py runserver')

The backend will be available at http://localhost:8000

The frontend and backend should now be running concurrently, and you can interact with them locally.
