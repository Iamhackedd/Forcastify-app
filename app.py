from flask import Flask, render_template, request
import weather  # Replace with your actual module name

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form['city']
        weather_data = your_weather_module.get_weather(city)  # Call your weather function
    return render_template('index.html', weather=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
