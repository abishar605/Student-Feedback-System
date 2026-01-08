from flask import Flask, request, jsonify
from db import get_connection

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit_feedback():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO student_feedback
    (student_name, class, subject, rating, comments)
    VALUES (%s, %s, %s, %s, %s)
    """
    values = (
        data['student_name'],
        data['class'],
        data['subject'],
        data['rating'],
        data['comments']
    )

    cursor.execute(query, values)
    conn.commit()

    return jsonify({"message": "Feedback Submitted Successfully"})

if __name__ == '__main__':
    app.run(debug=True)
