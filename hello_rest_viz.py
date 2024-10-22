from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    # Sample data - replace this with your actual data
    labels = ['January', 'February', 'March', 'April', 'May']
    values = [10, 25, 30, 15, 20]
    
    return render_template('index.html', labels=json.dumps(labels), values=json.dumps(values))