from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # 创建数据库实例

# 医生表
class Doctor(db.Model):
    __tablename__ = 'Doctor'
    Doctor_Number = db.Column(db.Integer, primary_key=True, autoincrement=False)  # 禁用自增
    Name = db.Column(db.String(255), nullable=False)
    Gender = db.Column(db.String(10), nullable=False)
    Age = db.Column(db.Integer, nullable=False)
    Department = db.Column(db.String(255), nullable=False)
    Registration_Fee = db.Column(db.Numeric(10, 2), nullable=False)  # 挂号费，浮点数
    Contact_Phone = db.Column(db.String(255), nullable=False)
    Outpatient_Time = db.Column(db.String(255), nullable=False)

# 患者表
class Patient(db.Model):
    __tablename__ = 'Patient'
    Patient_Number = db.Column(db.Integer, primary_key=True, autoincrement=False)
    ID_Card_Number = db.Column(db.String(255), nullable=False)
    Name = db.Column(db.String(255), nullable=False)
    Age = db.Column(db.Integer, nullable=False)
    Gender = db.Column(db.String(10), nullable=False)
    Symptom = db.Column(db.String(255), nullable=False)
    Contact_Info = db.Column(db.String(255), nullable=False)
    Medical_Insurance = db.Column(db.String(255), nullable=False)

# 诊疗项目表
class Treatment_Item(db.Model):
    __tablename__ = 'Treatment_Item'
    Item_Number = db.Column(db.Integer, primary_key=True, autoincrement=False)
    Item_Name = db.Column(db.String(255), nullable=False)
    Price = db.Column(db.Float, nullable=False)

# 患者与医生的关系
class Patient_Doctor(db.Model):
    __tablename__ = 'Patient_Doctor'
    Patient_Doctor_Number = db.Column(db.Integer, primary_key=True)
    Patient_Number = db.Column(db.Integer, primary_key=False)
    Doctor_Number = db.Column(db.Integer, primary_key=False)
    Medical_Time = db.Column(db.String(255), nullable=False)


# 患者与诊疗项目的关系
class Patient_Treatment_Item(db.Model):
    __tablename__ = 'Patient_Treatment_Item'
    Patient_Treatment_Item_Number = db.Column(db.Integer, primary_key=True)
    Patient_Number = db.Column(db.Integer, primary_key=False)
    Item_Number = db.Column(db.Integer, primary_key=False)
    Treatment_Time = db.Column(db.String(255), nullable=False)


# 用户登录表
class User_Login(db.Model):
    __tablename__ = 'User_Login'
    User_Number = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(255), nullable=False)
    Password = db.Column(db.String(255), nullable=False)

# 药品信息表
class Drug_Info(db.Model):
    __tablename__ = 'Drug_Info'
    Drug_Number = db.Column(db.String(255), primary_key=True)  # 药品编号，主键
    Drug_Name = db.Column(db.String(255), nullable=False)     # 药品名称，字符串类型
    Drug_Price = db.Column(db.DECIMAL(10, 2), nullable=False) # 药品价格，浮点数类型
    Drug_Production_Date = db.Column(db.String(255), nullable=False) # 药品生产日期，日期类型

# 处方表
class Patient_Drug_Info(db.Model):
    __tablename__ = 'Patient_Drug_Info'
    Patient_Drug_Info_Number = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 处方表编号，主键，自动递增
    Patient_Number = db.Column(db.Integer, nullable=False)  # 患者编号，外键
    Drug_Number = db.Column(db.String(255), nullable=False)  # 药品编号，外键
    Usage = db.Column(db.Integer, nullable=False)  # 使用量，整数类型
    Issue_Date = db.Column(db.String(255), nullable=False)  # 开具日期