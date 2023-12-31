# Event-Registration-System

The Event Registration System is a Django-based web application that allows users to create and register for events. It includes features such as user registration, event creation, user authentication, and API endpoints for interaction with the system.

## Features

### 1. User Registration and Authentication

- Users can create accounts to log in.
- Authentication ensures that only logged-in users can register for events.

### 2. Event Management

- Users can create events with details like title, description, date, time, and location.
- Events have a limited number of available slots, and registration is restricted based on available slots.

### 3. Admin Panel

- Utilizes Django's admin panel for managing events and user registrations.

### 4. Search Functionality

- Implements a basic search functionality that allows users to search for events based on keywords.

### 5. User Dashboard

- Provides a user dashboard where users can see the events they've registered for and manage their registrations.

### 6. API Endpoints (Using Django Rest Framework)

### 7. User-Friendly Templates

- Uses Bootstrap and crispy forms for a visually appealing and user-friendly interface.

## Installation

1. Clone the repository:

```bash
   git clone https://github.com/Muk74dir/Event-Registration-System.git

   cd event-registration-system
```


2. Install dependencies:
```bash
    pip install -r requirements.txt
 ```

3. Create a superuser for accessing the admin panel:
```bash
    python manage.py createsuperuser
    Run the development server:
    python manage.py runserver
```

4. Run the development server:
```bash
    python manage.py runserver
```

# Event Registration System API Documentation

## Overview

The Event Registration System (ERS) API allows users to interact with events, registrations, and user details.

## Base URL
The base URL for all API endpoints is `https://127.0.0.1:8000/api/`.

## Endpoints
### 1. List of All Events
#### http://127.0.0.1:8000/api/events/ [GET]

### 2. Details of a Specific Event
#### http://127.0.0.1:8000/api/events/{event_id}/ [GET]

### 3. User Registration for an Event
#### http://127.0.0.1:8000/api/events/{event_id}/register/ [POST]

### 4. User's Registered Events
#### http://127.0.0.1:8000/api/user/events/ [GET]


