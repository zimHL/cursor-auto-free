from sqlalchemy import create_engine
from urllib.parse import quote_plus  # 新增编码模块

password = "Woshini@88"
encoded_password = quote_plus(password)  # 自动处理特殊字符


def save_account(u_id, u_email, u_password, access_token):
    engine = create_engine(
        f'mysql+pymysql://root:{encoded_password}@127.0.0.1:3306/zim_home',
        pool_recycle=3600,
        connect_args={'connect_timeout': 5}
    )

    # 使用参数化查询
    sql = "INSERT INTO cursor_account (user_id, email, password, access_token) VALUES (%s, %s, %s, %s)"

    # 获取原始连接
    conn = engine.raw_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (u_id, u_email, u_password, access_token))
        conn.commit()
    finally:
        conn.close()

