from flask import Blueprint, jsonify, request, make_response, g
from app.services.Patient_Doctor import get_all_patient_doctors, add_patient_doctor, delete_patient_doctor, \
    update_patient_doctor, get_patient_doctor
from app.utils.response_util import make_response_data


patient_doctor_bp = Blueprint('patient_doctor', __name__)

@patient_doctor_bp.before_request
def parse_request_data():
    if request.is_json:
        g.data = request.get_json()
    else:
        g.data = request.form

# 查询所有看病信息
@patient_doctor_bp.route('/get_all_patient_doctors', methods=['GET'])
def get_all_patient_doctors_route():
    patient_doctors = get_all_patient_doctors()
    if patient_doctors is None:
        response = make_response_data(message='获取所有看病信息失败')
    else:
        response = make_response_data(data=patient_doctors, message='获取所有看病信息成功')
    return response

# 获取看病信息
@patient_doctor_bp.route('/get_patient_doctor', methods=['GET'])
def get_patient_doctor_route():
    patient_number = request.args.get('patient_number')
    patient_doctor = get_patient_doctor(patient_number)
    if patient_doctor is None:
        response = make_response_data(message='获取看病信息失败')
    else:
        response = make_response_data(data=patient_doctor, message='获取看病信息成功')
    return make_response(jsonify(response))

# 增加挂号信息
@patient_doctor_bp.route('/add_patient_doctor', methods=['GET'])
def add_patient_doctor_route():
    patient_number = request.args.get('patient_number')
    doctor_number = request.args.get('doctor_number')
    medical_time = request.args.get('medical_time')

    flag = add_patient_doctor(patient_number, doctor_number, medical_time)
    if flag:
        response = make_response_data(message='添加看病信息成功')
    else:
        response = make_response_data(message='添加看病信息失败')
    return make_response(jsonify(response))



# 删除看病信息
@patient_doctor_bp.route('/delete_patient_doctor', methods=['GET'])
def delete_patient_doctor_route():
    patient_doctor_number = request.args.get('patient_doctor_number')
    flag = delete_patient_doctor(patient_doctor_number)
    if flag:
        response = make_response_data(message='删除看病信息成功')
    else:
        response = make_response_data(message='删除看病信息失败')
    return make_response(jsonify(response))


# 修改看病信息
@patient_doctor_bp.route('/update_patient_doctor', methods=['GET'])
def update_patient_doctor_route():
    patient_doctor_number = request.args.get('patient_doctor_number')
    new_patient_number = request.args.get('new_patient_number')
    new_doctor_number = request.args.get('new_doctor_number')
    new_medical_time = request.args.get('new_medical_time')

    flag = update_patient_doctor(patient_doctor_number, new_patient_number, new_doctor_number, new_medical_time)
    if flag:
        response = make_response_data(message='修改看病信息成功')
    else:
        response = make_response_data(message='修改看病信息失败')
    return make_response(jsonify(response))

# 测试代码
if __name__ == '__main__':
    all_patient_doctors = get_all_patient_doctors()
    print(all_patient_doctors)
