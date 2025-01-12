from app.models import Doctor, Treatment_Item, Drug_Info
from app.services.Patient_Drug_Info import get_patient_drug_info, delete_patient_drug_info
from app.services.Patient_Treatment_Item import get_patient_treatment_item, delete_patient_treatment_item
from app.utils.db_database import MyDatabase
from app.services.Patient_Doctor import get_patient_doctor, delete_patient_doctor


# 查询收费表
def get_charge(patient_number):
    session = MyDatabase.get_session()

    # 初始化费用
    registration_fee = 0
    treatment_fee = 0
    drug_fee = 0

    # 根据患者编号查询挂号费
    registration_fee_item = get_patient_doctor(patient_number)
    if registration_fee_item is not None:
        doctor_number = registration_fee_item[0]['Doctor_Number']
        if doctor_number is not None:
            registration_fee_result = session.query(Doctor.Registration_Fee).filter(
                Doctor.Doctor_Number == doctor_number).first()
            if registration_fee_result is not None:
                registration_fee = registration_fee_result[0]
        else:
            print(f"找不到医生编号{doctor_number}")
    print("挂号费：", registration_fee)

    # 根据患者编号查询诊疗项目费用
    patient_treatment_item = get_patient_treatment_item(patient_number)
    if patient_treatment_item is not None:
        treat_item = [item['Item_Number'] for item in patient_treatment_item]
        if treat_item:
            for item in treat_item:
                treatment_fee_result = session.query(Treatment_Item.Price).filter(
                    Treatment_Item.Item_Number == item).first()
                if treatment_fee_result is not None:
                    treatment_fee += treatment_fee_result[0]
        else:
            print("找不到诊疗项目编号")
    print("诊疗费：", treatment_fee)

    # 根据患者编号查询药品费用
    patient_drug_info = get_patient_drug_info(patient_number)  # 获取患者的药品信息

    if patient_drug_info is not None:
        for item in patient_drug_info:
            drug_number = item['Drug_Number']  # 药品编号
            usage = item['Usage']  # 药品数量

            # 查询药品单价
            drug_fee_result = session.query(Drug_Info.Drug_Price).filter(
                Drug_Info.Drug_Number == drug_number).first()
            if drug_fee_result is not None:
                drug_price = drug_fee_result[0]  # 药品单价
                drug_fee += drug_price * usage  # 计算单种药品费用并累加
            else:
                print(f"找不到药品编号 {drug_number} 的单价")
    else:
        print("找不到患者的药品信息")

    # 计算总费用
    registration_fee = float(registration_fee)
    treatment_fee = float(treatment_fee)
    drug_fee = float(drug_fee)

    total_fee = registration_fee + treatment_fee + drug_fee
    print("总费用：", total_fee)

    # 封装费用为字典
    fee_dict = {
        "registration_fee": registration_fee,  # 挂号费
        "treatment_fee": treatment_fee,  # 诊疗费
        "drug_fee": drug_fee,  # 药品费
        "total_fee": total_fee  # 总费用
    }
    print("费用字典：", fee_dict)
    session.close()
    return fee_dict  # 返回费用字典


# 根据用户编号删除挂号信息，诊疗信息，药品信息
def settle_charge(patient_number):
    session = MyDatabase.get_session()
    flag = True

    # 根据患者编号删除挂号信息
    try:
        registration_fee_item = get_patient_doctor(patient_number)
        if registration_fee_item is not None:
            for registration_fee_item in registration_fee_item:
                delete_patient_doctor(registration_fee_item['Patient_Doctor_Number'])
            print("删除挂号信息成功")
        else:
            print("找不到挂号信息")
    except Exception as e:
        session.rollback()
        flag = False
        print("删除挂号信息失败：", e)

    # 根据患者编号删除诊疗信息
    try:
        treatment_fee_item = get_patient_treatment_item(patient_number)
        if treatment_fee_item is not None:
            for item in treatment_fee_item:
                delete_patient_treatment_item(item['Patient_Treatment_Item_Number'])
            print("删除诊疗信息成功")
        else:
            print("找不到诊疗信息")
    except Exception as e:
        session.rollback()
        flag = False
        print("删除诊疗信息失败：", e)

    # 根据患者编号删除药品信息
    try:
        drug_fee_item = get_patient_drug_info(patient_number)
        if drug_fee_item is not None:
            for item in drug_fee_item:
                delete_patient_drug_info(item['Patient_Drug_Info_Number'])
            print("删除处方信息成功")
        else:
            print("找不到处方信息")
    except Exception as e:
        session.rollback()
        flag = False
        print("删除处方信息失败：", e)

    session.close()
    return flag


if __name__ == '__main__':
    print(settle_charge(1001))
