## react_django

An app created using React for front-end and Django for back-end.Based on an online YouTube tutorial by TechWithTim.

House Party App where one can create/join rooms and the host can play songs(linked to Spotify account using Spotify API) and the users in room can listen.Options to play/pause and skip songs are also available.


## House_Party_alt_app

The code for the django-react fullstack app can be set up as follows

## Setup Instructions

### Install Required Python Modules

```bash
pip install -r requirements.txt
```
### Start Web Server

To start the web server you need to run the following sequence of commands.

Clone the repo and cd into the repo folder.

Next run the django web server.
```bash
python manage.py runserver
```

### [Install Node.js](https://nodejs.org/en/)

### Install Node Modules

First cd into the ```frontend``` folder.
```bash
cd frontend
```
Next install all dependicies.
```bash
npm i
```

### Compile the Front-End

Run the production compile script
```bash
npm run build
```
or for development:
```bash
npm run dev
```


### Spotify API

Go to [Spotify Developer](https://developer.spotify.com/) and create/login into your account.Create a <b>house party</b> application.

Get the credentials and save them as <b>CLIENT_ID,CLIENT_SECRET and REDIRECT_URI</b> in a .env file in the spotify app folder.

Add ```localhost:8000/spotify/redirect``` to redirect URIS.

