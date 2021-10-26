from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import SubmitField, FileField
from wtforms.validators import DataRequired
from flask import Flask, render_template
from werkzeug.utils import secure_filename
import os
import colorgram

def getPalette(filename):
    colors = colorgram.extract(filename, 6)
    all_colors = []
    for color in colors:
        hex_color = '#%02x%02x%02x' % (color.rgb.r, color.rgb.g, color.rgb.b)
        all_colors.append(hex_color)
    return all_colors


app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY",  '8BYkEfBA6O6donzWlSihBXox7C0sKR6b')
Bootstrap(app)

class ImgForm(FlaskForm):
    file = FileField('Image', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=["GET", "POST"])
def home():
    form = ImgForm()
    if form.validate_on_submit():

        filename = secure_filename(form.file.data.filename)
        path = 'uploads/' + filename
        form.file.data.save(path)
        colors = getPalette(path)

        return render_template('color.html', colors=colors)
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
