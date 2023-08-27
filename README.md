# StudyPalConnect

StudyPalConnect is a web application that helps people find study partners for various subjects and topics.

## Features

- **Create Study Rooms**: Users can create study rooms for specific topics, such as Tech, History, Math ...

- **Join Study Rooms**: Users can join existing study rooms to collaborate with others who share their interests.

- **Real-time Chat**: Study room members can engage in real-time discussions and share study materials.

- **User Profiles**: Users can create and customize their profiles, providing information about their areas of expertise and study preferences.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/HMZElidrissi/StudyPalConnect.git
   cd StudyPalConnect
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create and apply database migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Create a superuser for admin access:

   ```bash
   python manage.py createsuperuser
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

6. Access the application at `http://127.0.0.1:8000`.

### Usage

- Visit the website and sign up or log in.
- Browse existing study rooms or create your own.
- If the topic you're interested in doesn't exist, you can create it when creating a new study room.
- Join study rooms and start discussions with fellow students.
- Customize your profile to showcase your expertise and interests.

## App Previews

### Homepage
![Homepage](/screenshots/homepage.png)

### Study Room
![Study Room](/screenshots/study_room.png)

### Profile
![Profile](/screenshots/profile.png)

