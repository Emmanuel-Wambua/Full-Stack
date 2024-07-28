# Project Title: Anime API Backend

Welcome to the Anime API Backend repository! This project serves as the backend of a full stack application, providing APIs for three popular anime series: Attack on Titan, My Hero Academia, and Jujutsu Kaisen. These APIs are created using the Django Rest Framework (DRF).

## Table of Contents

- [Project Description](#project-description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Project Description

This repository contains the backend code for a full stack application, featuring APIs for three renowned anime series. The APIs are designed to deliver data related to characters, episodes, and other relevant information from Attack on Titan, My Hero Academia, and Jujutsu Kaisen. The backend is built with Django and Django Rest Framework, providing a robust and scalable solution for anime enthusiasts.

## Features

- **Django Rest Framework**: Utilizes DRF for building and consuming RESTful APIs.
- **Modular Structure**: Separate modules for each anime series to maintain clean and manageable code.
- **CRUD Operations**: Perform Create, Read, Update, and Delete operations on the anime data.
- **Authentication**: Secure API endpoints with JWT authentication.
- **Pagination**: Handle large sets of data with ease using pagination.

## Installation

To get a local copy up and running, follow these simple steps.

1. **Clone the repository**
   ```sh
   git clone https://github.com/your_username/anime-api-backend.git
   ```
2. **Navigate to the project directory**
   ```sh
   cd anime-api-backend
   ```
3. **Create a virtual environment**
   ```sh
   python -m venv venv
   ```
4. **Activate the virtual environment**
   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source venv/bin/activate
     ```
5. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
6. **Apply migrations**
   ```sh
   python manage.py migrate
   ```
7. **Run the development server**
   ```sh
   python manage.py runserver
   ```

## Usage

To use the APIs, start the development server and navigate to `http://127.0.0.1:8000` in your browser or use tools like Postman to interact with the endpoints.

## API Endpoints

### Attack on Titan

- **List all characters**
  ```
  GET /api/attack-on-titan/characters/
  ```
- **Retrieve a character by ID**
  ```
  GET /api/attack-on-titan/characters/{id}/
  ```
- **Create a new character**
  ```
  POST /api/attack-on-titan/characters/
  ```
- **Update a character**
  ```
  PUT /api/attack-on-titan/characters/{id}/
  ```
- **Delete a character**
  ```
  DELETE /api/attack-on-titan/characters/{id}/
  ```

### My Hero Academia

- **List all characters**
  ```
  GET /api/my-hero-academia/characters/
  ```
- **Retrieve a character by ID**
  ```
  GET /api/my-hero-academia/characters/{id}/
  ```
- **Create a new character**
  ```
  POST /api/my-hero-academia/characters/
  ```
- **Update a character**
  ```
  PUT /api/my-hero-academia/characters/{id}/
  ```
- **Delete a character**
  ```
  DELETE /api/my-hero-academia/characters/{id}/
  ```

### Jujutsu Kaisen

- **List all characters**
  ```
  GET /api/jujutsu-kaisen/characters/
  ```
- **Retrieve a character by ID**
  ```
  GET /api/jujutsu-kaisen/characters/{id}/
  ```
- **Create a new character**
  ```
  POST /api/jujutsu-kaisen/characters/
  ```
- **Update a character**
  ```
  PUT /api/jujutsu-kaisen/characters/{id}/
  ```
- **Delete a character**
  ```
  DELETE /api/jujutsu-kaisen/characters/{id}/
  ```

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/YourFeature`)
3. Commit your Changes (`git commit -m 'Add some YourFeature'`)
4. Push to the Branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

---

Thank you for visiting the Anime API Backend repository! If you have any questions, feel free to open an issue or reach out to the maintainers. Enjoy exploring the APIs!
