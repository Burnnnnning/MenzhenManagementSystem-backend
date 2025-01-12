from app.models import Patient_Treatment_Item
from app.utils.db_database import MyDatabase

# 查询所有患者诊疗项目信息
def get_all_patient_treatment_items():
    session = MyDatabase.get_session()
    try:
        patient_treatment_items = session.query(
            Patient_Treatment_Item.Patient_Treatment_Item_Number,
            Patient_Treatment_Item.Patient_Number,
            Patient_Treatment_Item.Item_Number,
            Patient_Treatment_Item.Treatment_Time
        ).all()
        # 将查询结果转换为字典 ._mapping是行对象的一个属性
        patient_treatment_items_dict = [dict(patient_treatment_item._mapping) for patient_treatment_item in patient_treatment_items]
        return patient_treatment_items_dict
    except Exception as e:
        print(f"查询患者诊疗项目信息失败：{e}")
        return None
    finally:
        session.close()


# 按照患者编号查询患者诊疗项目信息
def get_patient_treatment_item(patient_number):
    session = MyDatabase.get_session()
    try:
        patient_treatment_items = session.query(
            Patient_Treatment_Item.Patient_Treatment_Item_Number,
            Patient_Treatment_Item.Patient_Number,
            Patient_Treatment_Item.Item_Number,
            Patient_Treatment_Item.Treatment_Time
        ).filter(Patient_Treatment_Item.Patient_Number == patient_number).all()
        if patient_treatment_items:
            patient_treatment_item_dict = [dict(patient_treatment_item._mapping) for patient_treatment_item in patient_treatment_items]
            return patient_treatment_item_dict
        else:
            return None
    except Exception as e:
        print(f"按照患者编号查询患者诊疗项目信息失败：{e}")
        return None
    finally:
        session.close()

# 按照患者编号查询患者诊疗项目信息
def get_patient_treatment(patient_number):
    session = MyDatabase.get_session()
    try:
        patient_treatment_items = session.query(
            Patient_Treatment_Item.Patient_Treatment_Item_Number,
            Patient_Treatment_Item.Patient_Number,
            Patient_Treatment_Item.Item_Number,
            Patient_Treatment_Item.Treatment_Time
        ).filter(Patient_Treatment_Item.Patient_Number == patient_number).all()
        if patient_treatment_items:
            patient_treatment_item_dict = [dict(patient_treatment_item._mapping) for patient_treatment_item in patient_treatment_items]
            return patient_treatment_item_dict
        else:
            return None
    except Exception as e:
        print(f"按照患者编号查询患者诊疗项目信息失败：{e}")
        return None
    finally:
        session.close()

# 增加患者诊疗项目信息
def add_patient_treatment_item(patient_number=None, item_number=None, treatment_time=None):
    session = MyDatabase.get_session()
    flag = True
    try:
        # 创建新对象
        new_patient_treatment_item = Patient_Treatment_Item(
            Patient_Number=patient_number,
            Item_Number=item_number,
            Treatment_Time=treatment_time
        )
        session.add(new_patient_treatment_item)
        session.commit()
        print("患者诊疗项目信息添加成功")
    except Exception as e:
        session.rollback()
        flag = False
        print(f"患者诊疗项目信息添加失败：{e}")
    finally:
        session.close()
    return flag


# 删除患者诊疗项目信息
def delete_patient_treatment_item(patient_treatment_item_number):
    session = MyDatabase.get_session()
    flag = True
    try:
        patient_treatment_item_to_delete = session.query(Patient_Treatment_Item).filter(Patient_Treatment_Item.Patient_Treatment_Item_Number == patient_treatment_item_number).first()

        if patient_treatment_item_to_delete:
            session.delete(patient_treatment_item_to_delete)
            session.commit()
            print(f"患者诊疗项目编号 {patient_treatment_item_number} 的信息删除成功")
        else:
            session.rollback()
            flag = False
            print(f"患者诊疗项目编号 {patient_treatment_item_number} 的信息不存在")
    except Exception as e:
        session.rollback()
        flag = False
        print(f"患者诊疗项目信息删除失败：{e}")
    finally:
        session.close()
    return flag


# 修改患者诊疗项目信息
def update_patient_treatment_item(patient_treatment_item_number, new_patient_number=None, new_item_number=None, new_treatment_time=None):
    session = MyDatabase.get_session()
    flag = True
    try:
        patient_treatment_item_to_update = session.query(Patient_Treatment_Item).filter(Patient_Treatment_Item.Patient_Treatment_Item_Number == patient_treatment_item_number).first()

        if patient_treatment_item_to_update:
            # 更新字段值
            if new_patient_number is not None:
                patient_treatment_item_to_update.Patient_Number = new_patient_number
            if new_item_number is not None:
                patient_treatment_item_to_update.Item_Number = new_item_number
            if new_treatment_time is not None:
                patient_treatment_item_to_update.Treatment_Time = new_treatment_time

            # 提交事物
            session.commit()
            print(f"患者诊疗项目编号 {patient_treatment_item_number} 的信息已更新")
        else:
            session.rollback()
            flag = False
            print(f"患者诊疗项目编号 {patient_treatment_item_number} 的信息不存在")
    except Exception as e:
        session.rollback()
        flag = False
        print(f"患者诊疗项目信息更新失败：{e}")
    finally:
        session.close()
    return flag

# 测试代码
if __name__ == '__main__':
    all_patient_treatment_items = get_all_patient_treatment_items()
    print(all_patient_treatment_items)
