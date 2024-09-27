from flask import Flask, render_template
import requests

app = Flask(__name__)

# Route to fetch data from the API and display it on the webpage
@app.route('/')
def home():
    # Fetch data from the API
    response = requests.get("https://restcountries.com/v3.1/all")
    
    # Convert the response data to JSON format
    countries = response.json()

    # Pass the data to the HTML template
    return render_template('index.html', countries=countries)

if __name__ == '__main__':
    app.run(debug=True)