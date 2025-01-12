from app.models import Drug_Info
from app.utils.db_database import MyDatabase

# 查询所有药品信息
def get_all_drug_infos():
    # 查询药品信息
    session = MyDatabase.get_session()
    try:
        drugs = session.query(
            Drug_Info.Drug_Number,
            Drug_Info.Drug_Name,
            Drug_Info.Drug_Price,
            Drug_Info.Drug_Production_Date
        ).all()
        # 将查询结果转换为字典 ._mapping是行对象的一个属性
        drugs_dict = [dict(drug._mapping) for drug in drugs]
        return drugs_dict
    except Exception as e:
        print(f"查询药品信息失败：{e}")
        return None
    finally:
        session.close()

# 查询药品信息
def get_drug_info(drug_name):
    session = MyDatabase.get_session()
    drug = session.query(
        Drug_Info.Drug_Number,
        Drug_Info.Drug_Name,
        Drug_Info.Drug_Price,
        Drug_Info.Drug_Production_Date
    ).filter(Drug_Info.Drug_Name == drug_name).all()
    drug_dict = [dict(drug._mapping) for drug in drug]
    return drug_dict

# 增加药品信息
def add_drug_info(drug_number, drug_name=None, drug_price=None, drug_production_date=None):
    session = MyDatabase.get_session()
    flag = True
    try:
        # 创建一个Drug_Info对象
        drug = Drug_Info(
            Drug_Number=drug_number,
            Drug_Name=drug_name,
            Drug_Price=drug_price,
            Drug_Production_Date=drug_production_date
        )
        # 添加到数据库会话
        session.add(drug)
        session.commit()
        print("药品信息添加成功")
    except Exception as e:
        session.rollback()
        flag = False
        print(f"药品信息添加失败：{e}")
    finally:
        session.close()
    return flag

# 删除药品信息
def delete_drug_info(drug_number):
    session = MyDatabase.get_session()
    flag = True
    try:
        drug_info_to_delete = session.query(Drug_Info).filter(Drug_Info.Drug_Number == drug_number).first()

        if drug_info_to_delete:
            session.delete(drug_info_to_delete)
            session.commit()
            print(f"药品信息{drug_number}删除成功")
        else:
            session.rollback()
            flag = False
            print(f"药品信息{drug_number}不存在")
    except Exception as e:
        session.rollback()
        flag = False
        print(f"删除药品信息失败：{e}")
    finally:
        session.close()
    return flag


# 修改药品信息
def update_drug_info(drug_number, new_drug_name=None, new_drug_price=None, new_drug_production_date=None):
    session = MyDatabase.get_session()
    flag = True
    try:
        drug_info_to_update = session.query(Drug_Info).filter(Drug_Info.Drug_Number == drug_number).first()

        if drug_info_to_update:
            if new_drug_name is not None:
                drug_info_to_update.Drug_Name = new_drug_name
            if new_drug_price is not None:
                drug_info_to_update.Drug_Price = new_drug_price
            if new_drug_production_date is not None:
                drug_info_to_update.Drug_Production_Date = new_drug_production_date

            session.commit()
            print(f"药品信息{drug_number}修改成功")
        else:
            session.rollback()
            flag = False
            print(f"药品信息{drug_number}不存在")
    except Exception as e:
        session.rollback()
        flag = False
        print(f"修改药品信息失败：{e}")
    finally:
        session.close()
    return flag

if __name__ == '__main__':
    all_drug_infos = get_all_drug_infos()
    print(all_drug_infos)