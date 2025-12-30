from flask import Blueprint, render_template, redirect, url_for, flash
from app.forms import RegisterForm

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
    
        flash('Formulário enviado com sucesso!', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html', form=form)

