from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY",  '8BYkEfBA6O6donzWlSihBXox7C0sKR6b')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL",  'sqlite:///todo.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

Bootstrap(app)
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(250), unique=True, nullable=False)


class TodoForm(FlaskForm):
    task = StringField('Task description', validators=[DataRequired()])
    submit = SubmitField('Submit')

db.create_all()

def todo_form_to_db(form):
    return Todo(
        task=form.task.data,
    )


def todo_db_to_dict(todo):
    return {
        'id': todo.id,
        'task': todo.task,
    }

@app.route("/")
def home():
    todo_list = []
    todos = db.session.query(Todo).all()
    for todo in todos:
        each_cafe = todo_db_to_dict(todo)
        todo_list.append(each_cafe)
    return render_template('index.html', all_todo=todo_list)

@app.route('/add', methods=["GET", "POST"])
def add_todo():
    form = TodoForm()
    if form.validate_on_submit():
        new_todo = todo_form_to_db(form)
        db.session.add(new_todo)
        db.session.commit()

        return redirect(url_for('home'))
    return render_template('add.html', form=form)

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo_to_delete = Todo.query.get(todo_id)
    db.session.delete(todo_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
