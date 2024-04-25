# Django Google Maps Click Location App

This Django application allows users to click on a Google Map and display the clicked location's data in a table. This guide will help you set up the application on your local environment.

## Prerequisites

Before running this app, make sure you have the following installed on your PC:

- Python 3.x
- Django

Also you need Google Maps API Key.

## Getting Started

### 1. Clone the Repository

Clone this repository to your local environment:

```bash
git clone https://github.com/Imesh-Isuranga/MapViewDjango.git
```

### 2. Set Up a Virtual Environment (Optional)
Creating a virtual environment is recommended to keep dependencies isolated:
Run below script in CMD.

```
pip install virtualenv
virtualenv env
env\Scripts\activate

```
If u dont have install django install it using below pip command.

```
pip install django
```

### 3. Install Dependencies

```
pip install googlemaps
```

### 4. Set Up the Google Maps API Key
To use Google Maps in your application, you need an API key. Follow these steps to obtain an API key:

- Go to the Google Cloud Console.
- Create a new project.
- Enable the Google Maps JavaScript API.
- Create an API key.
- Restrict the key for security (optional but recommended).

Once you have the API key, insert it into home.html at the following line:

```
<script async
    src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCeHNMTy_QJmoL5IU9YdL0D8-QsrCbf3JY&callback=initMap">
</script>
```
Replace {Your_GOOGLE_API_KEY} with your actual Google Maps API key.

### 5. Run the Django Server
Run the Django development server to start your application:
```
python manage.py runserver
```

Visit http://127.0.0.1:8000/ in your web browser to see the app in action.

### 6. Accessing the App
The app allows you to click on the Google Map and displays the clicked location data in a table. Make sure you have a stable internet connection while using the app.
