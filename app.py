from flask import Flask,render_template,redirect,url_for,request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)   ###creates an application to name the application by the name of the file.
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://arun:hahaha123@localhost:5432/todoapp'


db = SQLAlchemy(app)
migrate = Migrate(app,db)

class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(),nullable=False)
    completed = db.Column(db.Boolean, nullable=False,default=False)
    
    def __repr__(self):
        return f'<Todo {self.id} {self.description}>'

#with app.app_context():
#    db.create_all()

@app.route('/todos/create', methods=['POST'])
def create_todo():
  description = request.form.get('description', '')
  todo = Todo(description=description)
  db.session.add(todo)
  db.session.commit()
  return redirect(url_for('index'))

@app.route('/')
def index():
    return render_template('index.html',data=Todo.query.all())


