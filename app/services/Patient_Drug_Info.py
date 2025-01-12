from app.models import Patient_Drug_Info
from app.utils.db_database import MyDatabase

# 查询所有病人的处方信息
def get_all_patient_drug_info():
    session = MyDatabase.get_session()
    try:
        patient_drug_info = session.query(
            Patient_Drug_Info.Patient_Drug_Info_Number,
            Patient_Drug_Info.Patient_Number,
            Patient_Drug_Info.Drug_Number,
            Patient_Drug_Info.Usage,
            Patient_Drug_Info.Issue_Date
        ).all()
        patient_drug_info_dict = [dict(patient_drug_info_item._mapping) for patient_drug_info_item in patient_drug_info]
        return patient_drug_info_dict
    except Exception as e:
        print(f"查询病人处方信息失败：{e}")
        return None
    finally:
        session.close()

# 按照患者编号查询处方信息
def get_patient_drug_info(patient_number):
    session = MyDatabase.get_session()
    try:
        patient_drug_infos = session.query(
            Patient_Drug_Info.Patient_Drug_Info_Number,
            Patient_Drug_Info.Patient_Number,
            Patient_Drug_Info.Drug_Number,
            Patient_Drug_Info.Usage,
            Patient_Drug_Info.Issue_Date
        ).filter(Patient_Drug_Info.Patient_Number == patient_number).all()
        if patient_drug_infos:
            patient_drug_info_dict = [dict(patient_drug_info_item._mapping) for patient_drug_info_item in patient_drug_infos]
            return patient_drug_info_dict
        else:
            return None
    except Exception as e:
        print(f"按照病人编号查询病人处方信息失败：{e}")
        return None
    finally:
        session.close()

# 查询病人处方信息
def get_all_patient_drug_info():
    session = MyDatabase.get_session()
    patient_drug_info = session.query(
        Patient_Drug_Info.Patient_Drug_Info_Number,
        Patient_Drug_Info.Patient_Number,
        Patient_Drug_Info.Drug_Number,
        Patient_Drug_Info.Usage,
        Patient_Drug_Info.Issue_Date
    ).all()
    patient_drug_info_dict = [dict(patient_drug_info_item._mapping) for patient_drug_info_item in patient_drug_info]
    return patient_drug_info_dict

# 增加病人处方信息
def add_patient_drug_info(patient_number, drug_number, usage, issue_date):
    session = MyDatabase.get_session()
    flag = True
    try:
        # 创建一个Patient_Drug_Info对象
        patient_drug_info = Patient_Drug_Info(
            Patient_Number=patient_number,
            Drug_Number=drug_number,
            Usage=usage,
            Issue_Date=issue_date
        )
        # 添加到数据库会话
        session.add(patient_drug_info)
        session.commit()
        print("病人处方信息添加成功")
    except Exception as e:
        session.rollback()
        flag = False
        print(f"病人处方信息添加失败：{e}")
    finally:
        session.close()
    return flag

# 删除病人处方信息
def delete_patient_drug_info(patient_drug_info_number):
    session = MyDatabase.get_session()
    flag = True
    try:
        # 根据ID删除病人处方信息
        patient_drug_info_to_delete = session.query(Patient_Drug_Info).filter(
            Patient_Drug_Info.Patient_Drug_Info_Number == patient_drug_info_number).first()
        if patient_drug_info_to_delete:
            session.delete(patient_drug_info_to_delete)
            session.commit()
            print(f"病人处方信息{patient_drug_info_number}删除成功")
        else:
            session.rollback()
            flag = False
            print(f"病人处方信息{patient_drug_info_number}不存在")
    except Exception as e:
        session.rollback()
        flag = False
        print(f"病人处方信息{patient_drug_info_number}删除失败：{e}")
    finally:
        session.close()
    return flag

# 修改病人处方信息
def update_patient_drug_info(patient_drug_info_number, new_patient_number=None, new_drug_number=None, new_usage=None, new_issue_date=None):
    session = MyDatabase.get_session()
    flag = True
    try:
        patient_drug_info_to_update = session.query(Patient_Drug_Info).filter(
            Patient_Drug_Info.Patient_Drug_Info_Number == patient_drug_info_number).first()
        if patient_drug_info_to_update:
            if new_patient_number is not None:
                patient_drug_info_to_update.Patient_Number = new_patient_number
            if new_drug_number is not None:
                patient_drug_info_to_update.Drug_Number = new_drug_number
            if new_usage is not None:
                patient_drug_info_to_update.Usage = new_usage
            if new_issue_date is not None:
                patient_drug_info_to_update.Issue_Date = new_issue_date

            session.commit()
            print(f"病人处方信息{patient_drug_info_number}修改成功")
        else:
            session.rollback()
            flag = False
            print(f"病人处方信息{patient_drug_info_number}不存在")
    except Exception as e:
        session.rollback()
        flag = False
        print(f"病人处方信息{patient_drug_info_number}修改失败：{e}")
    finally:
        session.close()
    return flag

if __name__ == '__main__':
    # 查询所有病人处方信息
    patient_drug_info = get_all_patient_drug_info()
    print(patient_drug_info)