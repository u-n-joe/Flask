from flask import Flask, render_template, url_for, request, redirect
from forms import MainForm, LoginForm, JoinForm, ManagerForm, AddItemForm, EditItemForm, RemoveItemForm, MForm

# dao 함수 선언
from werkzeug.utils import secure_filename
# from fruit_detection.dao import getAll
import secrets

app = Flask(__name__)
app.config["SECRET_KEY"] = secrets.token_hex(16)

@app.route('/')
def home():
    return render_template('main.html', form=MainForm(), forma=MForm())


@app.route('/payment', methods=['POST'])
def payment():
    data = {}
    if request.method == 'POST':
        data = request.form
    return render_template('payment.html', data=data)


@app.route('/login')
def login():
    return render_template('login.html', form=LoginForm())


@app.route('/join')
def join():
    return render_template('join.html', form=JoinForm())

# @app.route('/manager')
# def manager():
#     return render_template('manager.html', form=ManagerForm, list=getAll())


@app.route('/upload')
def upload():
    return render_template('item_upload.html')

@app.route('/item_add', methods=['POST'])
def item_add():
    return render_template('item_add.html', form=AddItemForm)

@app.route('/item_edit')
def item_edit():
    return render_template('item_edit.html', form=EditItemForm)

@app.route('/item_remove')
def item_remove():
    return render_template('item_remove.html', form=RemoveItemForm)

@app.route('/pay_card')
def pay_card():
    return render_template('pay_card.html')

@app.route('/pay_cash')
def pay_cash():
    return render_template('pay_cash.html')


@app.route('/itemUpload', methods=['POST'])
def upload_file():
    f = request.files['file']
    # 저장할 경로 + 파일명
    f.save(secure_filename(f.filename))
    return 'uploads 디렉토리 -> 파일 업로드 성공!'


@app.route('/main')
def main():
    return redirect("http://127.0.0.1:5000/")


# server shutdown
def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'


if __name__ == '__main__':
    app.run(debug=True)
