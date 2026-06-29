from flask import Flask, render_template, request, jsonify
from database import db
from models import Feedback

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/api/feedbacks', methods=['GET'])
def get_feedbacks():
    feedbacks = Feedback.query.order_by(Feedback.created_at.desc()).all()
    return jsonify([f.to_dict() for f in feedbacks])

@app.route('/api/feedbacks', methods=['POST'])
def create_feedback():
    data = request.get_json()
    new_feedback = Feedback(
        title=data['title'],
        message=data['message']
    )
    db.session.add(new_feedback)
    db.session.commit()
    return jsonify(new_feedback.to_dict()), 201

@app.route('/api/feedbacks/<int:id>', methods=['PUT'])
def update_feedback(id):
    feedback = Feedback.query.get_or_404(id)
    data = request.get_json()
    feedback.status = data['status']
    db.session.commit()
    return jsonify(feedback.to_dict())

if __name__ == '__main__':
    app.run(debug=True)