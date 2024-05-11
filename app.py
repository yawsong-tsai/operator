from flask import Flask, jsonify, redirect, url_for ,request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/add', methods=['POST'])
def add():
    p1 = request.form.get('p1')
    p2 = request.form.get('p2')
    if check_param(p1,p2):
        result=int(p1)+int(p2)
        status='200'
        msg='成功'
    else:
        result=None
        status='500'
        msg='缺少參數'
    return jsonify(p1=p1, p2=p2, result=str(result), status=status, message=msg)

@app.route('/sub', methods=['POST'])
def sub():
    p1 = request.form.get('p1')
    p2 = request.form.get('p2')
    if check_param(p1,p2):
        result=int(p1)-int(p2)
        status='200'
        msg='成功'
    else:
        result=None
        status='500'
        msg='缺少參數'
    return jsonify(p1=p1, p2=p2, result=str(result), status=status, message=msg)

@app.route('/mul', methods=['POST'])
def mul():
    p1 = request.form.get('p1')
    p2 = request.form.get('p2')
    if check_param(p1,p2):
        result=int(p1)*int(p2)
        status='200'
        msg='成功'
    else:
        result=None
        status='500'
        msg='缺少參數'
    return jsonify(p1=p1, p2=p2, result=str(result), status=status, message=msg)

@app.route('/div', methods=['POST'])
def div():
    p1 = request.form.get('p1')
    p2 = request.form.get('p2')
    if check_param(p1,p2):
        result=int(p1)/int(p2)
        status='200'
        msg='成功'
    else:
        result=None
        status='500'
        msg='缺少參數'
    return jsonify(p1=p1, p2=p2, result=str(result), status=status, message=msg)

@app.route('/mod', methods=['POST'])
def mod():
    p1 = request.form.get('p1')
    p2 = request.form.get('p2')
    if check_param(p1,p2):
        result=int(p1)%int(p2)
        status='200'
        msg='成功'
    else:
        result=None
        status='500'
        msg='缺少參數'
    return jsonify(p1=p1, p2=p2, result=str(result), status=status, message=msg)

#檢查是否缺少參數
def check_param(p1,p2):
    if p1!=None and p2!=None:
        res=True
    else:
        res=False
    return res

if __name__ == '__main__':
    app.run('0.0.0.0', '4500', debug=True)
