from .Patients import patient_bp
from .Doctors import doctor_bp
from .Treatment_Items import treatment_item_bp
from .Patient_Doctor import patient_doctor_bp
from .Patient_Treatment_Item import patient_treatment_item_bp
from .User_Login import user_login_bp

__all__ = ['patient_bp', 'doctor_bp', 'treatment_item_bp',
           'patient_doctor_bp', 'patient_treatment_item_bp', user_login_bp]  # 指定允许导入的模块
