from app.models import Patient_Doctor
from app.utils.db_database import MyDatabase

# 查询所有看病信息
def get_all_patient_doctors():
    # 查询看病信息
    session = MyDatabase.get_session()
    try:
        patient_doctors = session.query(
            Patient_Doctor.Patient_Doctor_Number,
            Patient_Doctor.Patient_Number,
            Patient_Doctor.Doctor_Number,
            Patient_Doctor.Medical_Time
        ).all()
        # 将查询结果转换为字典 ._mapping是行对象的一个属性
        patient_doctors_dict = [dict(patient_doctor._mapping) for patient_doctor in patient_doctors]
        return patient_doctors_dict
    except Exception as e:
        print(f"查询看病信息失败：{e}")
        return None
    finally:
        session.close()



# 按照患者编号查询看病信息
def get_patient_doctor(patient_number):
    session = MyDatabase.get_session()
    try:
        patient_doctors = session.query(
            Patient_Doctor.Patient_Doctor_Number,
            Patient_Doctor.Patient_Number,
            Patient_Doctor.Doctor_Number,
            Patient_Doctor.Medical_Time
        ).filter(Patient_Doctor.Patient_Number == patient_number).all()
        if patient_doctors:
            patient_doctor_dict = [dict(patient_doctor._mapping) for patient_doctor in patient_doctors]
            return patient_doctor_dict
        else:
            return None
    except Exception as e:
        print(f"按照患者编号查询看病信息失败：{e}")
        return None
    finally:
        session.close()


# 增加挂号信息
def add_patient_doctor(patient_number=None, doctor_number=None, medical_time=None):
    session = MyDatabase.get_session()
    flag = True
    try:
        patient_doctor = Patient_Doctor(
            Patient_Number=patient_number,
            Doctor_Number=doctor_number,
            Medical_Time=medical_time
        )
        session.add(patient_doctor)
        session.commit()
        print(f"看病信息添加成功")
    except Exception as e:
        session.rollback()
        flag = False
        print(f"看病信息添加失败：{e}")
    finally:
        session.close()
    return flag


# 删除看病信息
def delete_patient_doctor(patient_doctor_number):
    session = MyDatabase.get_session()
    flag = True
    try:
        patient_doctor_to_delete = session.query(Patient_Doctor).filter(Patient_Doctor.Patient_Doctor_Number == patient_doctor_number).first()
        if patient_doctor_to_delete:
            session.delete(patient_doctor_to_delete)
            session.commit()
            print(f"看病信息编号{patient_doctor_number}删除成功")
        else:
            session.rollback()
            flag = False
            print(f"看病信息编号{patient_doctor_number}不存在")
    except Exception as e:
        session.rollback()
        flag = False
        print(f"看病信息删除失败：{e}")
    finally:
        session.close()
    return flag

# 修改看病信息
def update_patient_doctor(patient_doctor_number, new_patient_number=None, new_doctor_number=None, new_medical_time=None):
    session = MyDatabase.get_session()
    flag = True
    try:
        patient_doctor_to_update = session.query(Patient_Doctor).filter(Patient_Doctor.Patient_Doctor_Number == patient_doctor_number).first()
        if patient_doctor_to_update:
            if new_patient_number is not None:
                patient_doctor_to_update.Patient_Number = new_patient_number
            if new_doctor_number is not None:
                patient_doctor_to_update.Doctor_Number =new_doctor_number
            if new_medical_time is not None:
                patient_doctor_to_update.Medical_Time = new_medical_time

            # 提交事务
            session.commit()
            print(f"看病信息编号 {patient_doctor_number} 的信息已更新")
        else:
            session.rollback()
            flag = False
            print(f"看病信息编号 {patient_doctor_number} 不存在")
    except Exception as e:
        session.rollback()
        flag = False
        print(f"更新看病信息失败：{e}")
    finally:
        session.close()
    return flag


# 测试代码
if __name__ == '__main__':
    all_patient_doctors = get_all_patient_doctors()
    print(all_patient_doctors)