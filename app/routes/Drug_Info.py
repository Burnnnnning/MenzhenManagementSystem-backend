from flask import Blueprint, jsonify, request, make_response, g
from app.services.Drug_Info import get_all_drug_infos, add_drug_info, delete_drug_info, update_drug_info, get_drug_info
from app.utils.response_util import make_response_data

drug_info_bp = Blueprint('drug', __name__)

@drug_info_bp.before_request
def parase_request_data():
    if request.is_json:
        g.data = request.get_json()
    else:
        g.data = request.form

# 获取所有药品信息
@drug_info_bp.route('/get_all_drug_infos', methods=['GET'])
def get_all_drug_infos_route():
    drug_infos = get_all_drug_infos()
    if drug_infos is None:
        response = make_response_data(message='获取药品信息失败')
    else:
        response = make_response_data(data=drug_infos, message='获取药品信息成功')
    return make_response(jsonify(response))

# 获取药品信息
@drug_info_bp.route('/get_drug_info', methods=['GET'])
def get_drug_info_route():
    drug_name = request.args.get('drug_name')
    drug_info = get_drug_info(drug_name)
    if drug_info is None:
        response = make_response_data(message='获取药品信息失败')
    else:
        response = make_response_data(data=drug_info, message='获取药品信息成功')
    return make_response(jsonify(response))

# 添加药品信息
@drug_info_bp.route('/add_drug_info', methods=['GET'])
def add_drug_info_route():
    drug_number = request.args.get('drug_number')
    drug_name = request.args.get('drug_name')
    drug_price = request.args.get('drug_price')
    drug_production_date = request.args.get('drug_production_date')

    print(drug_number, drug_name, drug_price, drug_production_date)
    flag = add_drug_info(drug_number, drug_name, drug_price, drug_production_date)
    if flag:
        response = make_response_data(message='药品信息添加成功')
    else:
        response = make_response_data(message='药品信息添加失败')
    return make_response(jsonify(response))

# 删除药品信息
@drug_info_bp.route('/delete_drug_info', methods=['GET'])
def delete_drug_info_route():
    drug_number = request.args.get('drug_number')

    flag = delete_drug_info(drug_number)
    if flag:
        response = make_response_data(message='药品信息删除成功')
    else:
        response = make_response_data(message='药品信息删除失败')
    return make_response(jsonify(response))

# 修改药品信息
@drug_info_bp.route('/update_drug_info', methods=['GET'])
def update_drug_info_route():
    drug_number = request.args.get('drug_number')
    new_drug_name = request.args.get('new_drug_name')
    new_drug_price = request.args.get('new_drug_price')
    new_drug_production_date = request.args.get('new_drug_production_date')

    flag = update_drug_info(drug_number, new_drug_name, new_drug_price, new_drug_production_date)
    if flag:
        response = make_response_data(message='药品信息修改成功')
    else:
        response = make_response_data(message='药品信息修改失败')
    return make_response(jsonify(response))

if __name__ == '__main__':
    all_drug_infos = get_all_drug_infos()
    print(all_drug_infos)


