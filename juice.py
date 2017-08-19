from flask import Flask, jsonify, request, render_template, url_for, redirect, flash, make_response
app = Flask(__name__)

@app.route('/juice')
@app.route('/juice/<name>')
def hello(name=None):
  return render_template('juice.html', name_template=name)


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        flash("Successfully logged in")
        # return redirect(url_for('welcome', username= request.form.get('username')))
        response = make_response(redirect(url_for('welcome')))
        response.set_cookie('username', request.form.get('username'))
        return response
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    response = make_response(redirect(url_for('login')))
    response.set_cookie('username', '', expires = 0)
    return response

@app.route('/')
def welcome():
    username = request.cookies.get('username')
    if username:
        return render_template('welcome.html', username = username)
    else:
        return redirect(url_for('login'))

# @app.route('/products', methods=['POST'])
# def create_products():
#     request_data = request.get_json()
#     new_report = {
#     'max_value': request_data['metric']
#     }


if __name__ == '__main__':
    app.secret_key = 'SuperSecretKey'
    app.run(debug=True)