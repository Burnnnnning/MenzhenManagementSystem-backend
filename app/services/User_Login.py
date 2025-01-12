from app.models import User_Login
from app.utils.db_database import MyDatabase

# 检验登录信息
def check_login(Username, password):
    session = MyDatabase.get_session()
    user_login = session.query(User_Login).filter(User_Login.Username == Username).first()
    if user_login is None:
        return False
    if user_login.Password != password:
        return False
    return True

# 获取所有用户
def get_all_user_logins():
    session = MyDatabase.get_session()
    try:
        user_logins = session.query(
            User_Login.User_Number,
            User_Login.Username,
            User_Login.Password
        ).all()
        user_logins_dict = [dict(user_login._mapping) for user_login in user_logins]
        return user_logins_dict
    except Exception as e:
        print(f"获取用户信息失败：{e}")
        return None
    finally:
        session.close()

# 获取用户信息
def get_user_login(Username):
    session = MyDatabase.get_session()
    user_login = session.query(
        User_Login.User_Number,
        User_Login.Username,
        User_Login.Password
    ).filter(User_Login.Username == Username).all()
    user_login_dict = [dict(user_login._mapping) for user_login in user_login]
    session.close()
    return user_login_dict


# 增加用户
def add_user_login(Username, password):
    session = MyDatabase.get_session()
    flag = True
    try:
        Username_find = session.query(User_Login).filter(User_Login.Username == Username).first()
        if Username_find is not None:
            flag = False
            print(f"用户名{Username}已存在，请重新输入用户名")
        else:
            new_user_login = User_Login(Username=Username, Password=password)
            session.add(new_user_login)
            session.commit()
            print("用户添加成功")
    except Exception as e:
        session.rollback()
        flag = False
        print(f"用户信息添加失败：{e}")
    finally:
        session.close()
    return flag

# 删除用户
def delete_user_login(Username, password):
    session = MyDatabase.get_session()
    flag = True
    try:
        user_login = session.query(User_Login).filter(User_Login.Username == Username).first()
        if user_login is None:
            flag = False
            print(f"用户{Username}不存在，删除用户失败")
        else:
            if user_login.Password != password:
                flag = False
                print(f"用户{Username}密码错误，删除用户失败")
            else:
                session.delete(user_login)
                session.commit()
                print(f"用户{Username}删除成功")
    except Exception as e:
        # 回滚事物
        session.rollback()
        flag = False
        print(f"用户信息删除失败：{e}")
    finally:
        session.close()
    return flag

# 修改密码
def update_password(Username, old_password, new_password):
    session = MyDatabase.get_session()
    flag = True
    try:
        user_login = session.query(User_Login).filter(User_Login.Username == Username).first()
        if user_login is None:
            flag = False
            print(f"用户{Username}不存在，修改密码失败")
        else:
            if user_login.Password != old_password:
                flag = False
                print(f"用户{Username}密码错误，修改密码失败")
            else:
                user_login.Password = new_password
                session.commit()
                print(f"用户{Username}密码修改成功")
    except Exception as e:
        # 回滚事物
        session.rollback()
        flag = False
        print(f"用户密码修改失败：{e}")
    finally:
        session.close()
    return flag
