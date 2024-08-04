from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'User'}
    posts = [
        {
        'text': '''Каждый раз, начиная создавать тот или иной пост, 
                стоит помнить, что социальные сети — это не заседание 
                докторов академических наук, которые будут решать давать ли 
                автору награду за самый умный пост или нет (хотя такие личности 
                тоже присутствуют).''',
        'date': '2020-01-01',
        'title': 'Как создать пост'
        },
        {
        'text': ''' Первым делом автор поста должен 
        заинтересовать свою аудиторию.
        Помимо качественного снимка 
        (о нем мы расскажем позже),
        первым делом аудитория обращает внимание на тематику поста. ''',
        'date': '2023-09-01',
        'title': 'Как создать пост шаг 2'
        },

        {
            'text': ''' После того, как автор обратил на себя внимание, 
            следующим шагом необходимо вызвать еще более глубокий интерес к посту, 
            чем был при прочтении заголовка. 
            Для этого можно использовать интересный факт, 
            новость или даже личную историю из жизни, 
            которые относятся к теме поста. ''',
            'date': '2024-03-01',
            'title': 'Как создать пост шаг 3'
        }
    ]  

    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(
            'Вход был запрошен пользователем {}, remember_me={}'.format(
                form.username.data, form.remember_me.data
            )
        )
        return redirect('/index')
    return render_template('login.html', title='Войти', form=form)