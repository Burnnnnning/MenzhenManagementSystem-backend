from app.models import Treatment_Item
from app.utils.db_database import MyDatabase

# 查询所有诊疗项目信息
def get_all_treatment_items():
    # 查询诊疗项目信息
    session = MyDatabase.get_session()
    try:
        treatment_items = session.query(
            Treatment_Item.Item_Number,
            Treatment_Item.Item_Name,
            Treatment_Item.Price
        ).all()
        # 将查询结果转换为字典 ._mapping是行对象的一个属性
        treatment_items_dict = [dict(treatment_item._mapping) for treatment_item in treatment_items]
        return treatment_items_dict
    except Exception as e:
        print(f"查询诊疗项目信息失败：{e}")
        return None
    finally:
        session.close()

# 按照诊疗项目名称查询诊疗项目信息
def get_treatment_item_by_item_number(item_name):
    session = MyDatabase.get_session()
    treatment_item = session.query(
        Treatment_Item.Item_Number,
        Treatment_Item.Item_Name,
        Treatment_Item.Price
    ).filter(Treatment_Item.Item_Name == item_name).all()
    # 将查询结果转换为字典 ._mapping是行对象的一个属性
    treatment_item_dict = [dict(treatment_item._mapping) for treatment_item in treatment_item]
    return treatment_item_dict


# 增加诊疗项目信息
def add_treatment_item(item_number, item_name=None, price=None):
    session = MyDatabase.get_session()
    flag = True
    try:
        # 创建新对象
        treatment_item = Treatment_Item(
            Item_Number=item_number,
            Item_Name=item_name,
            Price=price
        )
        # 添加到对话
        session.add(treatment_item)
        # 提交事务
        session.commit()
        print("诊疗项目信息添加成功")
    except Exception as e:
        # 回滚事物
        session.rollback()
        flag = False
        print(f"诊疗项目信息添加失败：{e}")
    finally:
        # 关闭对话
        session.close()
    return flag

# 删除诊疗项目信息
def delete_treatment_item(item_number):
    session = MyDatabase.get_session()
    flag = True
    try:
        # 删除对象
        treatment_item_to_delete = session.query(Treatment_Item).filter(Treatment_Item.Item_Number == item_number).first()
        if treatment_item_to_delete:
            session.delete(treatment_item_to_delete)
            # 提交事务
            session.commit()
            print(f"诊疗项目编号 {item_number} 的信息删除成功")
        else:
            session.rollback()
            flag = False
            print(f"诊疗项目编号 {item_number} 的信息不存在")
    except Exception as e:
        # 回滚事物
        session.rollback()
        flag = False
        print(f"诊疗项目信息删除失败：{e}")
    finally:
        # 关闭对话
        session.close()
    return flag

# 修改诊疗项目信息
def update_treatment_item(item_number, new_item_name=None, new_price=None):
    session = MyDatabase.get_session()
    flag = True
    try:
        # 更新对象
        treatment_item_to_update = session.query(Treatment_Item).filter(Treatment_Item.Item_Number == item_number).first()
        if treatment_item_to_update:
            # 更新字段值
            if new_item_name is not None:
                treatment_item_to_update.Item_Name = new_item_name
            if new_price is not None:
                treatment_item_to_update.Price = new_price
            # 提交事务
            session.commit()
            print(f"诊疗项目编号 {item_number} 的信息更新成功")
        else:
            session.rollback()
            flag = False
            print(f"诊疗项目编号 {item_number} 的信息不存在")
    except Exception as e:
        # 回滚事务
        session.rollback()
        flag = False
        print(f"诊疗项目信息更新失败：{e}")
    finally:
        session.close()
    return flag


# 测试代码
if __name__ == '__main__':
    all_treatment_items = get_all_treatment_items()
    print(all_treatment_items)