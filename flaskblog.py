from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'BMX420'

posts = [
    {
        'author': 'Artur',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'September 16, 2020'
    },
    {
        'author': 'Sandel',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'September 17, 2020'
    }

]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Registration', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('Login Successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Unsuccessful Login', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':     #Used to start the server directly through python in debug mode
    app.run(debug=True)
