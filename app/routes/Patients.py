from flask import Blueprint, jsonify, request, make_response, g
from app.services.Patients import get_all_patients, add_patient, delete_patient, update_patient, get_patient
from app.utils.response_util import make_response_data

patient_bp = Blueprint('patient', __name__)


@patient_bp.before_request
def parse_request_data():
    if request.is_json:
        g.data = request.get_json()
    else:
        g.data = request.form

# 查询所有患者信息
@patient_bp.route('get_all_patients', methods=['GET'])
def get_all_patients_route():
    patients = get_all_patients()
    if patients is None:
        response = make_response_data(message='获取所有病人信息失败')
    else:
        response = make_response_data(data=patients, message='获取所有病人信息成功')
    return make_response(jsonify(response))

# 查询患者信息
@patient_bp.route('/search_patient', methods=['GET'])
def get_patient_route():
    name = request.args.get('name')
    patient = get_patient(name)
    if patient is None:
        response = make_response_data(message='获取病人信息失败')
    else:
        response = make_response_data(data=patient, message='获取病人信息成功')
    return make_response(jsonify(response))

# 增加患者信息
@patient_bp.route('/add_patient', methods=['GET'])
def add_patient_route():
    patient_number = request.args.get('patient_number')
    id_card_number = request.args.get('id_card_number')
    name = request.args.get('name')
    age = request.args.get('age')
    gender = request.args.get('gender')
    symptom = request.args.get('symptom')
    contact_info = request.args.get('contact_info')
    medical_insurance = request.args.get('medical_insurance')

    flag = add_patient(patient_number, id_card_number, name, age, gender, symptom, contact_info, medical_insurance)
    if flag:
        response = make_response_data(message='增加病人信息成功')
    else:
        response = make_response_data(message='增加病人信息失败')
    return make_response(jsonify(response))

# 删除患者信息
@patient_bp.route('/delete_patient', methods=['GET'])
def delete_patient_route():
    patient_number = request.args.get('patient_number')
    flag = delete_patient(patient_number)
    if flag:
        response = make_response_data(message='删除病人信息成功')
    else:
        response = make_response_data(message='删除病人信息失败')
    return make_response(jsonify(response))

# 修改患者信息
@patient_bp.route('/update_patient', methods=['GET'])
def update_patient_route():
    patient_number = request.args.get('patient_number')
    new_id_card_number = request.args.get('new_id_card_number')
    new_name = request.args.get('new_name')
    new_age = request.args.get('new_age')
    new_gender = request.args.get('new_gender')
    new_symptom = request.args.get('new_symptom')
    new_contact_info = request.args.get('new_contact_info')
    new_medical_insurance = request.args.get('new_medical_insurance')

    flag = update_patient(patient_number, new_id_card_number, new_name, new_age, new_gender, new_symptom, new_contact_info, new_medical_insurance)
    if flag:
        response = make_response_data(message='修改病人信息成功')
    else:
        response = make_response_data(message='修改病人信息失败')
    return make_response(jsonify(response))

# 测试代码
if __name__ == '__main__':
    all_patients = get_all_patients()
    print(all_patients)