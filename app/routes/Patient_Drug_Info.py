from flask import Blueprint, jsonify, request, make_response, g
from app.services.Patient_Drug_Info import get_all_patient_drug_info, add_patient_drug_info, delete_patient_drug_info, \
    update_patient_drug_info, get_patient_drug_info
from app.utils.response_util import make_response_data


patient_drug_info_bp = Blueprint('patient_drug_info', __name__)

@patient_drug_info_bp.before_request
def parse_request_data():
    if request.is_json:
        g.data = request.get_json()
    else:
        g.data = request.form

# 获取所有患者药品信息
@patient_drug_info_bp.route('/get_all_patient_drug_infos', methods=['GET'])
def get_all_patient_drug_info_route():
    patient_drug_info_list = get_all_patient_drug_info()
    if patient_drug_info_list is None:
        response = make_response_data(message='获取所有患者药品信息失败')
    else:
        response = make_response_data(data=patient_drug_info_list, message='获取所有患者药品信息成功')
    return make_response(jsonify(response))

# 获取患者药品信息
@patient_drug_info_bp.route('/get_patient_drug_info', methods=['GET'])
def get_patient_drug_info_route():
    patient_number = request.args.get('patient_number')
    patient_drug_info_list = get_patient_drug_info(patient_number)
    if patient_drug_info_list is None:
        response = make_response_data(message='获取患者药品信息失败')
    else:
        response = make_response_data(data=patient_drug_info_list, message='获取患者药品信息成功')
    return make_response(jsonify(response))

# 添加患者药品信息
@patient_drug_info_bp.route('/add_patient_drug_info', methods=['GET'])
def add_patient_drug_info_route():
    patient_number = request.args.get('patient_number')
    drug_number = request.args.get('drug_number')
    usage = request.args.get('usage')
    issue_date = request.args.get('issue_date')

    flag = add_patient_drug_info(patient_number, drug_number, usage, issue_date)
    if flag:
        response = make_response_data(message='添加患者药品信息成功')
    else:
        response = make_response_data(message='添加患者药品信息失败')
    return make_response(jsonify(response))

# 删除患者药品信息
@patient_drug_info_bp.route('/delete_patient_drug_info', methods=['GET'])
def delete_patient_drug_info_route():
    patient_drug_info_number = request.args.get('patient_drug_info_number')
    flag = delete_patient_drug_info(patient_drug_info_number)
    if flag:
        response = make_response_data(message='删除患者药品信息成功')
    else:
        response = make_response_data(message='删除患者药品信息失败')
    return make_response(jsonify(response))

# 修改患者药品信息
@patient_drug_info_bp.route('/update_patient_drug_info', methods=['GET'])
def update_patient_drug_info_route():
    patient_drug_info_number = request.args.get('patient_drug_info_number')
    new_patient_number = request.args.get('new_patient_number')
    new_drug_number = request.args.get('new_drug_number')
    new_usage = request.args.get('new_usage')
    new_issue_date = request.args.get('new_issue_date')

    flag = update_patient_drug_info(patient_drug_info_number, new_patient_number, new_drug_number, new_usage, new_issue_date)
    if flag:
        response = make_response_data(message='修改患者药品信息成功')
    else:
        response = make_response_data(message='修改患者药品信息失败')
    return make_response(jsonify(response))

if __name__ == '__main__':
    print(get_all_patient_drug_info())