from db.settings.connector import db_pool


def query_request(query, query_condition):
    try:
        conn = db_pool.getconn()
        cursor = conn.cursor()
        cursor.execute(query, query_condition)
    except Exception as err:
        raise Exception(f'error: outstanding {err}') from err
    finally:
        conn.commit()
        conn.close()
        cursor.close()
        db_pool.putconn(conn)
