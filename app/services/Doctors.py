from app.models import Doctor
from app.utils.db_database import MyDatabase

# 查询所有医生信息
def get_all_doctors():
    # 查询医生信息
    session = MyDatabase.get_session()
    try:
        doctors = session.query(
            Doctor.Doctor_Number,
            Doctor.Name,
            Doctor.Gender,
            Doctor.Age,
            Doctor.Department,
            Doctor.Contact_Phone,
            Doctor.Outpatient_Time,
            Doctor.Registration_Fee
        ).all()
        # 将查询结果转换为字典 ._mapping是行对象的一个属性
        doctors_dict = [dict(doctor._mapping) for doctor in doctors]
        return doctors_dict
    except Exception as e:
        print(f"查询医生信息失败：{e}")
        return None
    finally:
        session.close()

# 按照医生姓名查询医生信息
def get_doctor(name):
    session = MyDatabase.get_session()
    doctor = session.query(
        Doctor.Doctor_Number,
        Doctor.Name,
        Doctor.Gender,
        Doctor.Age,
        Doctor.Department,
        Doctor.Contact_Phone,
        Doctor.Outpatient_Time,
        Doctor.Registration_Fee
    ).filter(Doctor.Name == name).all()
    # 将查询结果转换为字典 ._mapping是行对象的一个属性
    doctor_dict = [dict(doctor._mapping) for doctor in doctor]
    session.close()
    return doctor_dict

# 增加医生信息
# 未考虑如果数据库中医生编号已存在的情况
def add_doctor(doctor_number, name=None, gender=None, age=None, department=None, contact_phone=None, outpatient_time=None, registration_fee=None):
    # 获取对话
    session = MyDatabase.get_session()
    flag = True
    try:
        # 创建新对象
        new_doctor = Doctor(
            Doctor_Number=doctor_number,
            Name=name,
            Gender=gender,
            Age=age,
            Department=department,
            Contact_Phone=contact_phone,
            Outpatient_Time=outpatient_time,
            Registration_Fee=registration_fee
        )
        # 添加到对话
        session.add(new_doctor)
        # 提交事务
        session.commit()
        print("医生信息添加成功")
    except Exception as e:
        # 回滚事物
        session.rollback()
        flag = False
        print(f"医生信息添加失败：{e}")
    finally:
        # 关闭对话
        session.close()
    return flag


# 删除医生信息
def delete_doctor(doctor_number):
    # 获取对话
    session = MyDatabase.get_session()
    flag = True
    try:
        # 删除对象
        # 遇到的错误是：sqlalchemy.orm.exc.UnmappedInstanceError: Class 'NoneType' is not mapped
        # doctor_to_delete = session.query(Doctor).filter(Doctor.Doctor_Number == doctor_number).all()
        doctor_to_delete = session.query(Doctor).filter(Doctor.Doctor_Number == doctor_number).first()

        if doctor_to_delete:
            session.delete(doctor_to_delete)
            # 提交事务
            session.commit()
            print(f"医生编号 {doctor_number} 的信息删除成功")
        else:
            session.rollback()
            flag = False
            print(f"医生编号 {doctor_number} 的信息不存在")
    except Exception as e:
        # 回滚事物
        session.rollback()
        flag = False
        print(f"医生信息删除失败：{e}")
    finally:
        # 关闭对话
        session.close()
    return flag


# 修改医生信息
def update_doctor(doctor_number, new_name=None, new_gender=None, new_age=None, new_department=None, new_contact_phone=None, new_outpatient_time=None, new_registration_fee=None):
    # 获取会话
    session = MyDatabase.get_session()
    flag = True
    try:
        # 查询要修改的医生
        doctor_to_update = session.query(Doctor).filter(Doctor.Doctor_Number == doctor_number).first()

        if doctor_to_update:
            # 更新字段值
            if new_name is not None:
                doctor_to_update.Name = new_name
            if new_gender is not None:
                doctor_to_update.Gender = new_gender
            if new_age is not None:
                doctor_to_update.Age = new_age
            if new_department is not None:
                doctor_to_update.Department = new_department
            if new_contact_phone is not None:
                doctor_to_update.Contact_Phone = new_contact_phone
            if new_outpatient_time is not None:
                doctor_to_update.Outpatient_Time = new_outpatient_time
            if new_registration_fee is not None:
                doctor_to_update.Registration_Fee = new_registration_fee

            # 提交事务
            session.commit()
            print(f"医生编号 {doctor_number} 的信息已更新")
        else:
            session.rollback()
            flag = False
            print(f"未找到医生编号 {doctor_number} 的信息")
    except Exception as e:
        # 回滚事务
        session.rollback()
        flag = False
        print(f"更新医生信息失败：{e}")
    finally:
        # 关闭会话
        session.close()
    return flag


# 测试代码
if __name__ == '__main__':
    # all_doctors = get_all_doctors()
    # print(all_doctors)
    # doctor = get_doctor_by_doctor_number(1001)
    # print(doctor)
    # 测试增加医生信息
    # add_doctor(1001, "张三", "男", 30, "内科", "12345678901", "09:00-12:00")
    # all_doctors = get_all_doctors()
    # print(all_doctors)
    # 测试删除医生信息
    # delete_doctor(1001)
    # 测试修改医生信息
    update_doctor(1001, "李四", "男", 30, "内科", "12345678901", "09:00-12:00")