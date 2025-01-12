from flask import Flask
from .config import Config
from flask_cors import CORS
from .models import db
from .routes import patient_bp, doctor_bp, treatment_item_bp, patient_doctor_bp, patient_treatment_item_bp, \
    user_login_bp
from .routes.Charge import charge_bp
from .routes.Drug_Info import drug_info_bp
from .routes.Patient_Drug_Info import patient_drug_info_bp
from .utils.my_custom_json_encoder import SQLAJSONEncoder

def create_app():
    app = Flask(__name__)  # 创建 Flask 应用实例
    app.config.from_object(Config)  # 加载配置

    db.init_app(app)  # 初始化数据库

    # 注册蓝图
    app.register_blueprint(patient_bp, url_prefix='/patient')
    app.register_blueprint(doctor_bp, url_prefix='/doctor')
    app.register_blueprint(treatment_item_bp, url_prefix='/treatment')
    app.register_blueprint(patient_doctor_bp, url_prefix='/patient_doctor')
    app.register_blueprint(patient_treatment_item_bp, url_prefix='/patient_treatment_item')
    app.register_blueprint(patient_drug_info_bp, url_prefix='/patient_drug_info')
    app.register_blueprint(user_login_bp, url_prefix='/user_login')
    app.register_blueprint(drug_info_bp, url_prefix='/drug')
    app.register_blueprint(charge_bp, url_prefix='/charge')

    CORS(app)  # 允许跨域请求

    app.json_encoder = SQLAJSONEncoder  # 设置自定义 JSON 编码器

    return app


