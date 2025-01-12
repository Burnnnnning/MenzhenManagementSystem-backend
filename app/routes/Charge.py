from flask import Blueprint, jsonify, request, make_response, g
from app.services.Charge import get_charge, settle_charge
from app.utils.response_util import make_response_data

charge_bp = Blueprint('charge', __name__)

# 解析POST请求参数，对于GET则在request.args中获取
@charge_bp.before_request
def parse_request_data():
    if request.is_json:
        g.data = request.get_json()
    else:
        g.data = request.form

# 根据病人编号获取收费信息
@charge_bp.route('/get_charge', methods=['GET'])
def get_charge_route():
    patient_number = request.args.get('patient_number')
    print("patient_number:", patient_number)
    charge = get_charge(patient_number)
    print("收费信息：", charge)
    if charge is not None:
        response = make_response_data(data=charge, message='获取收费信息成功')
    else:
        response = make_response_data(code=404, message='获取收费信息失败')
    return make_response(jsonify(response))

# 根据病人编号结算收费信息
@charge_bp.route('/settle_charge', methods=['GET'])
def settle_charge_route():
    patient_number = request.args.get('patient_number')
    print("patient_number:", patient_number)
    flag = settle_charge(patient_number)
    if flag:
        response = make_response_data(message='结算收费信息成功')
    else:
        response = make_response_data(code=404, message='结算收费信息失败')
    return make_response(jsonify(response))