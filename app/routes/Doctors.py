from flask import Blueprint, jsonify, request, make_response, g
from app.services.Doctors import get_all_doctors, add_doctor, delete_doctor, update_doctor, get_doctor
from app.utils.response_util import make_response_data

doctor_bp = Blueprint('doctor', __name__)

# 解析POST请求参数，对于GET则在request.args中获取
@doctor_bp.before_request
def parse_request_data():
    if request.is_json:
        g.data = request.get_json()
    else:
        g.data = request.form

@doctor_bp.route('/get_doctor', methods=['GET'])
def get_doctor_route():
    doctor_name = request.args.get('doctor_name')
    doctor = get_doctor(doctor_name)
    if doctor is None:
        responses = make_response_data(message='获取医生信息失败')
    else:
        responses = make_response_data(data=doctor, message='获取医生信息成功')
    return make_response(jsonify(responses))

# 查询所有医生信息
@doctor_bp.route('/get_all_doctors', methods=['GET'])
def get_all_doctors_route():
    doctors = get_all_doctors()
    if doctors is None:
        responses = make_response_data(message='获取所有医生信息失败')
    else:
        responses = make_response_data(data=doctors, message='获取所有医生信息成功')
    return make_response(jsonify(responses))

# 增加医生信息
@doctor_bp.route('/add_doctor', methods=['GET'])
def add_doctor_route():
    # 获取请求参数
    doctor_number = request.args.get('doctor_number')
    name = request.args.get('name')
    gender = request.args.get('gender')
    age = request.args.get('age')
    department = request.args.get('department')
    contact_phone = request.args.get('contact_phone')
    outpatient_time = request.args.get('outpatient_time')
    registration_fee = request.args.get('registration_fee')

    flag = add_doctor(doctor_number, name, gender, age, department, contact_phone, outpatient_time, registration_fee)
    if flag:
        response = make_response_data(message='添加医生信息成功')
    else:
        response = make_response_data(message='添加医生信息失败')
    return make_response(jsonify(response))

# 删除医生信息
@doctor_bp.route('/delete_doctor', methods=['GET'])
def delete_doctor_route():
    doctor_number = request.args.get('doctor_number')
    flag = delete_doctor(doctor_number)
    if flag:
        responses = make_response_data(message='删除医生信息成功')
    else:
        responses = make_response_data(message='删除医生信息失败')
    return make_response(jsonify(responses))

# 修改医生信息
@doctor_bp.route('/update_doctor', methods=['GET'])
def update_doctor_route():
    doctor_number = request.args.get('doctor_number')
    new_name = request.args.get('new_name')
    new_gender = request.args.get('new_gender')
    new_age = request.args.get('new_age')
    new_department = request.args.get('new_department')
    new_contact_phone = request.args.get('new_contact_phone')
    new_outpatient_time = request.args.get('new_outpatient_time')
    new_registration_fee = request.args.get('new_registration_fee')
    print(new_registration_fee)

    flag = update_doctor(doctor_number, new_name, new_gender, new_age, new_department, new_contact_phone, new_outpatient_time,new_registration_fee)
    if flag:
        responses = make_response_data(message='修改医生信息成功')
    else:
        responses = make_response_data(message='修改医生信息失败')
    return make_response(jsonify(responses))

# 测试代码
if __name__ == '__main__':
    all_doctors = get_all_doctors()
    print(all_doctors)