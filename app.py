from flask import Flask, render_template, request, jsonify
from queries import QueryProcessor

app = Flask(__name__)
processor = QueryProcessor()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def handle_query():
    user_input = request.form.get('query', '')
    response = processor.process_query(user_input)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
