from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    # Pass the current time to the template
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('index.html', current_time=current_time)

if __name__ == '__main__':
    app.run(host='192.168.1.24', port=5000, debug=True)
