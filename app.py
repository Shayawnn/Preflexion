import os
from openai import OpenAI
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from flask_cors import CORS

# load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def get_gpt4_response(prompt):
    # Send the combined prompt to the GPT API
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an advanced AI specializing in recommending books and movies based on specific user requests."},
            {"role": "user", "content": prompt},
        ]
    )

    # Extract the assistant's reply
    result = response.choices[0].message.content

    # Specify the directory where you want to save the files
    directory = './response/'

    # Write data to files
    write_data_to_file(directory + 'prompt.txt', prompt)
    write_data_to_file(directory + 'response.txt', result)

    return result

# For Debugging purpose
def write_data_to_file(filename, data):
    with open(filename, 'w') as f:
        f.write(data)

@app.route('/search_movies', methods=['POST'])
def search_movies():
    data = request.get_json()
    user_query = data['query']
    prompt = f"Suggest a compelling movie that aligns with the following interests: {user_query}. Please include genre, IMDB rating, notable themes, and a brief summary."
    response = get_gpt4_response(prompt)
    return jsonify({'response': response})

@app.route('/search_books', methods=['POST'])
def search_books():
    data = request.get_json()
    user_query = data['query']
    prompt = f"Recommend an engaging book matching these criteria: {user_query}. Include the genre, key themes, and a succinct overview."
    response = get_gpt4_response(prompt)
    return jsonify({'response': response})

@app.route('/')
def home():
    return render_template('index.html')

# Additional routes for movies and books
@app.route('/movies')
def movies():
    # Logic for movie suggestions
    return render_template('movies.html')

@app.route('/books')
def books():
    # Logic for book suggestions
    return render_template('books.html')


if __name__ == '__main__':
    app.run(debug=True)
