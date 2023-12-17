# Preflexion: AI-Based Book and Movie Recommendation System

## Table of Contents
1. [Introduction](#introduction)
2. [Overview](#overview)
3. [Setup Instructions](#setup-instructions)
4. [Project Structure](#project-structure)
5. [License](#license)

## Introduction <a name="introduction"></a>
Preflexion is an AI-powered web application designed to provide personalized book and movie recommendations. Utilizing OpenAI's GPT-4 for intelligent suggestions, it caters to user-specific preferences, offering a unique and engaging experience.

## Overview <a name="overview"></a>
The application utilizes OpenAI's GPT-4 model to interpret and respond to user queries with relevant book and movie recommendations. It's built using Flask, a lightweight web framework, ensuring a seamless and interactive user experience. Preflexion is not only a testament to the advancements in AI but also serves as an engaging tool for book and movie enthusiasts seeking personalized content.

## Setup Instructions <a name="setup-instructions"></a>
This project requires Python and pip for installing dependencies. It is recommended to use a virtual environment to keep the dependencies required by different projects in separate places.

### Prerequisites
 - **Python 3.9** or later. You can download it from [here](https://www.python.org/downloads/).
 - **pip**. It is already installed if you have Python 2 >=2.7.9 or Python 3 >=3.4 downloaded from python.org. If not, you can download it from [here](https://pip.pypa.io/en/stable/installation/).
 - **Docker** (optional for Docker setup)
 - **OpenAI API key**

### Installing
To get Preflexion up and running on your local machine, follow these steps:

1. **Clone the Repository**:
    ```shell
    git clone https://github.com/Shayawnn/Preflexion.git
    ```

2. **Change into the project directory**:
    ```shell
    cd Preflexion
    ```
   
3. **(Recommended) Set Up the Environment**:
   - If you're using python3, it comes with the built-in `venv` module.
   - Create a virtual environment:
   ```shell
    python3 -m venv venv
    ```
   - Activate the virtual environment:
     - Windows: `venv\Scripts\activate`
     - Unix/MacOS: `source venv/bin/activate`

4. **Install Dependencies**:
    ```shell
    pip install -r requirements.txt
    ```

5. **Environment Variables**:
   - Create a `.env` file in the root directory.
   - Add your OpenAI API key: `OPENAI_API_KEY=your_api_key_here`

6. **Run the Application**:
    ```shell
    python app.py
    ```

7. **Access the Web Application**:
- Open your browser and go to `http://localhost:5000/`

### Docker Deployment
If you prefer using Docker, a Dockerfile is provided. Build the Docker image and run it to start the application.

1. **Ensure Docker is installed**
2. **Build the Docker image**:
    ```bash
    docker build -t preflexion:latest .
    ```
3. **Run the container**:
    ```bash
   docker run -p 5000:5000 preflexion:latest
    ```
4. **Access the application** via a browser at `http://localhost:5000`.

## Project Structure <a name="project-structure"></a>

 - **app.py**: The main Flask application file.
 - **Dockerfile**: For building a Docker image of the application.
 - **requirements.txt**: List of Python dependencies.
 - **response/**: Directory for storing user queries and AI responses for debugging purposes.
 - **static/**: Contains CSS stylesheets and media files.
 - **templates/**: HTML templates for the web interface.
 - **.env:** Houses environment-specific variables, primarily the OpenAI API key.

## License <a name="license"></a>
This project is licensed under the terms of the [GNU General Public License v3.0](LICENSE).

