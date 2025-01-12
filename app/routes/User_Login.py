from flask import Blueprint, jsonify, request, make_response, g
from app.services.User_Login import check_login, add_user_login, delete_user_login, update_password, \
    get_all_user_logins, get_user_login
from app.utils.response_util import make_response_data

user_login_bp = Blueprint('user_login', __name__)

# 用户登录信息属于私密信息，因此使用POST请求确保安全
@user_login_bp.before_request
def parse_request_data():
    if request.is_json:
        g.data = request.get_json()
    else:
        g.data = request.form

# 检验用户登录信息
@user_login_bp.route('', methods=['POST'])
def check_login_route():
    user_name = g.data.get('user_name')
    password = g.data.get('password')

    if user_name is None or password is None:
        response = make_response_data(message='用户名或密码不能为空', code=400)
    if check_login(user_name, password):
        response = make_response_data(message='登录成功', code=200)
    else:
        response = make_response_data(message='用户名或密码错误', code=400)
    return make_response(jsonify(response))

# 获取所有用户登录信息
@user_login_bp.route('/get_all_user_logins', methods=['GET'])
def get_all_user_logins_route():
    user_logins = get_all_user_logins()
    if user_logins is None:
        response = make_response_data(message='获取所有用户登录信息失败')
    else:
        response = make_response_data(data=user_logins, message='获取所有用户登录信息成功')
    return make_response(jsonify(response))

# 获取用户登录信息
@user_login_bp.route('/get_user_login', methods=['GET'])
def get_user_login_route():
    user_name = request.args.get('user_name')
    print(user_name)
    if user_name is None:
        response = make_response_data(message='用户名不能为空', code=400)
    else:
        user_login = get_user_login(user_name)
        if user_login is None:
            response = make_response_data(message='获取用户登录信息失败')
        else:
            response = make_response_data(data=user_login, message='获取用户登录信息成功')
    return make_response(jsonify(response))

# 添加用户
@user_login_bp.route('/add_user_login', methods=['POST'])
def add_user_login_route():
    user_name = g.data.get('user_name')
    password = g.data.get('password')
    if user_name is None or password is None:
        response = make_response_data(message='用户名或密码不能为空', code=400)
    else:
        if add_user_login(user_name, password):
            response = make_response_data(message='添加用户成功', code=200)
        else:
            response = make_response_data(message='添加用户失败', code=400)
    return make_response(jsonify(response))

# 删除用户
@user_login_bp.route('/delete_user_login', methods=['POST'])
def delete_user_login_route():
    user_name = g.data.get('user_name')
    password = g.data.get('password')
    if user_name is None or password is None:
        response = make_response_data(message='用户名或密码不能为空', code=400)
    else:
        if delete_user_login(user_name, password):
            response = make_response_data(message='删除用户成功', code=200)
        else:
            response = make_response_data(message='删除用户失败', code=400)
    return make_response(jsonify(response))

# 更新用户密码
@user_login_bp.route('/update_password', methods=['POST'])
def update_password_route():
    user_name = g.data.get('user_name')
    old_password = g.data.get('old_password')
    new_password = g.data.get('new_password')
    if user_name is None or old_password is None or new_password is None:
        response = make_response_data(message='用户名或密码不能为空', code=400)
    else:
        if update_password(user_name, old_password, new_password):
            response = make_response_data(message='更新用户密码成功', code=200)
        else:
            response = make_response_data(message='更新用户密码失败', code=400)
    return make_response(jsonify(response))