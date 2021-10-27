from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from forms import CreateProductForm, RegisterForm, LoginForm
import os

app = Flask(__name__)
login_manager = LoginManager()
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)
login_manager.init_app(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL",  "sqlite:///shop.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##CONFIGURE TABLE
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    price = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

class Buy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    title = db.Column(db.String(250), nullable=False)
    price = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))

db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()

        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('home'))
    return render_template("login.html", form=form)

@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():

        if User.query.filter_by(email=form.email.data).first():
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))

        hash_and_salted_password = generate_password_hash(
            form.password.data,
            method='pbkdf2:sha256',
            salt_length=8
        )
        new_user = User(
            email=form.email.data,
            name=form.name.data,
            password=hash_and_salted_password,
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for("home"))

    return render_template("register.html", form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/')
def home():
    product = Product.query.all()
    return render_template("index.html", all_products=product, logged_in=current_user.is_authenticated)

@app.route("/product/<int:product_id>")
def show_product(product_id):
    product = Product.query.get(product_id)
    return render_template("product.html", product=product)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/new-product", methods=["GET", "POST"])
def add_new_product():
    form = CreateProductForm()
    if form.validate_on_submit():
        new_product = Product(
            title=form.title.data,
            body=form.body.data,
            img_url=form.img_url.data,
            price=form.price.data,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("make-product.html", form=form)


@app.route("/edit-product/<int:product_id>", methods=["GET", "POST"])
def edit_product(product_id):
    product = Product.query.get(product_id)
    edit_form = CreateProductForm(
        title=product.title,
        img_url=product.img_url,
        price=product.price,
        body=product.body
    )
    if edit_form.validate_on_submit():
        product.title = edit_form.title.data
        product.img_url = edit_form.img_url.data
        product.price = edit_form.price.data
        product.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_product", product_id=product.id))
    return render_template("make-product.html", form=edit_form, is_edit=True)


@app.route("/delete/<int:product_id>")
def delete_product(product_id):
    product_to_delete = Product.query.get(product_id)
    db.session.delete(product_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/buy/<int:product_id>")
def buy_product(product_id):
    product_to_buy = Product.query.get(product_id)
    if product_to_buy:
        new_buy = Buy(
            title=product_to_buy.title,
            user_id=current_user.id,
            img_url=product_to_buy.img_url,
            price=product_to_buy.price,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_buy)
        db.session.commit()

        return redirect(url_for("home"))

@app.route("/purchases")
def purchases():
    all_purchases = Buy.query.filter_by(user_id=current_user.id)
    return render_template("purchases.html", purchases=all_purchases)

if __name__ == "__main__":
    app.run(port=5000)