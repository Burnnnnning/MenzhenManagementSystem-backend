from app.models import Patient
from app.utils.db_database import MyDatabase

# 查询所有患者信息
def get_all_patients():
    # 查询患者信息
    session = MyDatabase.get_session()
    try:
        patients = session.query(
            Patient.Patient_Number,
            Patient.ID_Card_Number,
            Patient.Name,
            Patient.Age,
            Patient.Gender,
            Patient.Symptom,
            Patient.Contact_Info,
            Patient.Medical_Insurance
        ).all()
        # 将查询结果转换为字典 ._mapping是行对象的一个属性
        patients_dict = [dict(patient._mapping) for patient in patients]
        return patients_dict
    except Exception as e:
        print(e)
        return None
    finally:
        session.close()



# 按照患者姓名查询患者信息
def get_patient(name):
    session = MyDatabase.get_session()
    patient = session.query(
        Patient.Patient_Number,
        Patient.ID_Card_Number,
        Patient.Name,
        Patient.Age,
        Patient.Gender,
        Patient.Symptom,
        Patient.Contact_Info,
        Patient.Medical_Insurance
    ).filter(Patient.Name == name).all()
    # 将查询结果转换为字典 ._mapping是行对象的一个属性
    patient_dict = [dict(patient._mapping) for patient in patient]
    return patient_dict

# 增加患者信息
def add_patient(patient_number, id_card_number=None, name=None, age=None, gender=None, symptom=None, contact_info=None, medical_insurance=None):
    session = MyDatabase.get_session()
    flag = True
    try:
        # 创建新对象
        patient = Patient(
            Patient_Number=patient_number,
            ID_Card_Number=id_card_number,
            Name=name,
            Age=age,
            Gender=gender,
            Symptom=symptom,
            Contact_Info=contact_info,
            Medical_Insurance=medical_insurance
        )
        # 添加到对话
        session.add(patient)
        # 提交事务
        session.commit()
        print("患者信息添加成功")
    except Exception as e:
        # 回滚事物
        session.rollback()
        flag = False
        print(f"患者信息添加失败：{e}")
    finally:
        # 关闭对话
        session.close()
    return flag

# 删除患者信息
def delete_patient(patient_number):
    session = MyDatabase.get_session()
    flag = True
    try:
        # 删除对象
        patient_to_delete = session.query(Patient).filter(Patient.Patient_Number == patient_number).first()
        if patient_to_delete:
            session.delete(patient_to_delete)
            # 提交事务
            session.commit()
            print(f"患者编号 {patient_number} 的信息删除成功")
        else:
            session.rollback()
            flag = False
            print(f"患者编号 {patient_number} 的信息不存在")
    except Exception as e:
        # 回滚事物
        session.rollback()
        flag = False
        print(f"患者信息删除失败：{e}")
    finally:
        # 关闭对话
        session.close()
    return flag


# 修改患者信息
def update_patient(patient_number, new_id_card_number=None, new_name=None, new_age=None, new_gender=None, new_symptom=None, new_contact_info=None, new_medical_insurance=None):
    session = MyDatabase.get_session()
    flag = True
    try:
        # 获取对象
        patient_to_update = session.query(Patient).filter(Patient.Patient_Number == patient_number).first()
        if patient_to_update:
            if new_id_card_number is not None:
                patient_to_update.ID_Card_Number = new_id_card_number
            if new_name is not None:
                patient_to_update.Name = new_name
            if new_age is not None:
                patient_to_update.Age = new_age
            if new_gender is not None:
                patient_to_update.Gender = new_gender
            if new_symptom is not None:
                patient_to_update.Symptom = new_symptom
            if new_contact_info is not None:
                patient_to_update.Contact_Info = new_contact_info
            if new_medical_insurance is not None:
                patient_to_update.Medical_Insurance = new_medical_insurance

            # 提交事务
            session.commit()
            print(f"患者编号 {patient_number} 的信息已更新")
        else:
            session.rollback()
            flag = False
            print(f"未找到患者编号 {patient_number} 的信息")
    except Exception as e:
        # 回滚事务
        session.rollback()
        flag = False
        print(f"更新患者信息失败：{e}")
    finally:
        # 关闭会话
        session.close()
    return flag



# 测试代码
if __name__ == '__main__':
    all_patients = get_all_patients()
    print(all_patients)