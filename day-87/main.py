from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY",  '8BYkEfBA6O6donzWlSihBXox7C0sKR6b')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL",  'sqlite:///cafes.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

Bootstrap(app)
db = SQLAlchemy(app)

class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    open = db.Column(db.String(250), nullable=True)
    close = db.Column(db.String(250), nullable=True)
    coffee_rating = db.Column(db.Integer, nullable=True)
    wifi_rating = db.Column(db.Integer, nullable=True)
    power_rating = db.Column(db.Integer, nullable=True)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField("Cafe Location", validators=[DataRequired()])
    map_url = StringField("Cafe Location on Google Maps (URL)", validators=[DataRequired(), URL()])
    img_url = StringField("Cafe image (URL)", validators=[DataRequired(), URL()])
    open = StringField("Opening Time e.g. 8AM", validators=[DataRequired()])
    close = StringField("Closing Time e.g. 5:30PM", validators=[DataRequired()])
    coffee_rating = SelectField("Coffee Rating", choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"], validators=[DataRequired()])
    wifi_rating = SelectField("Wifi Strength Rating", choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"], validators=[DataRequired()])
    power_rating = SelectField("Power Socket Availability", choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"], validators=[DataRequired()])
    submit = SubmitField('Submit')

db.create_all()

def cafe_form_to_db(form):
    return Cafe(
        name=form.cafe.data,
        map_url=form.map_url.data,
        img_url=form.img_url.data,
        location=form.location.data,
        open=form.open.data,
        close=form.close.data,
        coffee_rating=form.coffee_rating.data,
        wifi_rating=form.wifi_rating.data,
        power_rating=form.power_rating.data,
    )


def cafe_db_to_dict(cafe):
    return {
        'id': cafe.id,
        'name': cafe.name,
        'map_url': cafe.map_url,
        'img_url': cafe.img_url,
        'location': cafe.location,
        'open': cafe.open,
        'close': cafe.close,
        'coffee_rating': cafe.coffee_rating,
        'wifi_rating': cafe.wifi_rating,
        'power_rating': cafe.power_rating,
    }

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_cafe = cafe_form_to_db(form)
        db.session.add(new_cafe)
        db.session.commit()

        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)

@app.route('/cafes')
def cafes():
    cafes_list = []
    cafes = db.session.query(Cafe).all()
    for cafe in cafes:
        each_cafe = cafe_db_to_dict(cafe)
        cafes_list.append(each_cafe)
    return render_template('cafes.html', all_cafes=cafes_list)


@app.route("/delete/<int:cofe_id>")
def delete(cofe_id):
    cofe_to_delete = Cafe.query.get(cofe_id)
    db.session.delete(cofe_to_delete)
    db.session.commit()
    return redirect(url_for('cafes'))

if __name__ == '__main__':
    app.run(debug=True)
