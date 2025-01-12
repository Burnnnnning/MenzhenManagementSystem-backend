from flask import Blueprint, jsonify, request, make_response, g
from app.services.Treatment_Items import get_all_treatment_items, add_treatment_item, delete_treatment_item, \
    update_treatment_item, get_treatment_item_by_item_number
from app.utils.response_util import make_response_data

treatment_item_bp = Blueprint('treatment', __name__)


@treatment_item_bp.before_request
def parse_request_data():
    if request.is_json:
        g.data = request.get_json()
    else:
        g.data = request.form

# 查询所有诊疗项目信息
@treatment_item_bp.route('/get_all_treatment_items', methods=['GET'])
def get_all_treatment_items_route():
    treatment_items = get_all_treatment_items()
    if treatment_items is None:
        responses = make_response_data(message='获取所有诊疗项目信息失败')
    else:
        responses = make_response_data(data=treatment_items, message='获取所有诊疗项目信息成功')
    return make_response(jsonify(responses))

# 查找诊疗项目
@treatment_item_bp.route('/search_treatment_item', methods=['GET'])
def get_treatment_item_route():
    item_name = request.args.get('item_name')
    treatment_item = get_treatment_item_by_item_number(item_name)
    if treatment_item is None:
        responses = make_response_data(message='获取诊疗项目信息失败')
    else:
        responses = make_response_data(data=treatment_item, message='获取诊疗项目信息成功')
    return make_response(jsonify(responses))

# 增加诊疗项目信息
@treatment_item_bp.route('/add_treatment_item', methods=['GET'])
def add_treatment_item_route():
    item_number = request.args.get('item_number')
    item_name = request.args.get('item_name')
    price = request.args.get('price')

    flag = add_treatment_item(item_number, item_name, price)
    if flag:
        responses = make_response_data(message='增加诊疗项目信息成功')
    else:
        responses = make_response_data(message='增加诊疗项目信息失败')
    return make_response(jsonify(responses))

# 删除诊疗项目信息
@treatment_item_bp.route('/delete_treatment_item', methods=['GET'])
def delete_treatment_item_route():
    item_number = request.args.get('item_number')
    flag = delete_treatment_item(item_number)
    if flag:
        responses = make_response_data(message='删除诊疗项目信息成功')
    else:
        responses = make_response_data(message='删除诊疗项目信息失败')
    return make_response(jsonify(responses))

# 修改诊疗项目信息
@treatment_item_bp.route('/update_treatment_item', methods=['GET'])
def update_treatment_item_route():
    item_number = request.args.get('item_number')
    new_item_name = request.args.get('new_item_name')
    new_price = request.args.get('new_price')
    flag = update_treatment_item(item_number, new_item_name, new_price)
    if flag:
        responses = make_response_data(message='修改诊疗项目信息成功')
    else:
        responses = make_response_data(message='修改诊疗项目信息失败')
    return make_response(jsonify(responses))

# 测试代码
if __name__ == '__main__':
    all_treatment_items = get_all_treatment_items()
    print(all_treatment_items)