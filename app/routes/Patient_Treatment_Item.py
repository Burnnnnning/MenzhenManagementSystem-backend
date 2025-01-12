from flask import Blueprint, jsonify, request, make_response, g
from app.services.Patient_Treatment_Item import get_all_patient_treatment_items, add_patient_treatment_item, \
    delete_patient_treatment_item, update_patient_treatment_item, get_patient_treatment_item
from app.utils.response_util import make_response_data


patient_treatment_item_bp = Blueprint('patient_treatment_item', __name__)

@patient_treatment_item_bp.before_request
def parse_request_data():
    if request.is_json:
        g.data = request.get_json()
    else:
        g.data = request.form

# 查询所有治疗信息
@patient_treatment_item_bp.route('/get_all_patient_treatment_items', methods=['GET'])
def get_all_patient_treatment_items_route():
    patient_treatment_items = get_all_patient_treatment_items()
    if patient_treatment_items is None:
        responses = make_response_data(message='获取所有治疗信息失败')
    else:
        responses = make_response_data(data=patient_treatment_items, message='获取所有治疗信息成功')
    return make_response(jsonify(responses))

# 查询治疗信息
@patient_treatment_item_bp.route('/get_patient_treatment_item', methods=['GET'])
def get_patient_treatment_item_route():
    patient_number = request.args.get('patient_number')
    patient_treatment_item = get_patient_treatment_item(patient_number)
    if patient_treatment_item is None:
        responses = make_response_data(message='获取治疗信息失败')
    else:
        responses = make_response_data(data=patient_treatment_item, message='获取治疗信息成功')
    return make_response(jsonify(responses))

# 增加治疗信息
@patient_treatment_item_bp.route('/add_patient_treatment_item', methods=['GET'])
def add_patient_treatment_item_route():
    patient_number = request.args.get('patient_number')
    item_number = request.args.get('item_number')
    treatment_time = request.args.get('treatment_time')

    flag = add_patient_treatment_item(patient_number, item_number, treatment_time)
    if flag:
        responses = make_response_data(message='添加治疗信息成功')
    else:
        responses = make_response_data(message='添加治疗信息失败')
    return make_response(jsonify(responses))

# 删除治疗信息
@patient_treatment_item_bp.route('/delete_patient_treatment_item', methods=['GET'])
def delete_patient_treatment_item_route():
    patient_treatment_item_number = request.args.get('patient_treatment_item_number')
    flag = delete_patient_treatment_item(patient_treatment_item_number)
    if flag:
        responses = make_response_data(message='删除治疗信息成功')
    else:
        responses = make_response_data(message='删除治疗信息失败')
    return make_response(jsonify(responses))

# 修改治疗信息
@patient_treatment_item_bp.route('/update_patient_treatment_item', methods=['GET'])
def update_patient_treatment_item_route():
    patient_treatment_item_number = request.args.get('patient_treatment_item_number')
    new_patient_number = request.args.get('new_patient_number')
    new_item_number = request.args.get('new_item_number')
    new_treatment_time = request.args.get('new_treatment_time')

    flag = update_patient_treatment_item(patient_treatment_item_number, new_patient_number, new_item_number, new_treatment_time)
    if flag:
        responses = make_response_data(message='修改治疗信息成功')
    else:
        responses = make_response_data(message='修改治疗信息失败')
    return make_response(jsonify(responses))

# 测试代码
if __name__ == '__main__':
    all_patient_treatment_items = get_all_patient_treatment_items()
    print(all_patient_treatment_items)