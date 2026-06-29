from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='ثبت شده')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'message': self.message,
            'status': self.status,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M')
        }

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
    feedbacks = Feedback.query.all()
    return jsonify([f.to_dict() for f in feedbacks])

@app.route('/api/feedbacks', methods=['POST'])
def create_feedback():
    data = request.get_json()
    new = Feedback(title=data['title'], message=data['message'])
    db.session.add(new)
    db.session.commit()
    return jsonify(new.to_dict()), 201

@app.route('/api/feedbacks/<int:id>', methods=['PUT'])
def update_feedback(id):
    f = Feedback.query.get_or_404(id)
    data = request.get_json()
    f.status = data['status']
    db.session.commit()
    return jsonify(f.to_dict())

if __name__ == '__main__':
    app.run(debug=True, port=5000)