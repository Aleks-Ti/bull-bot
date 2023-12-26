from datetime import datetime

from db.settings.sql_query_executor import query_request


def create_user(message):
    current_date = datetime.now()
    date_registered = current_date.strftime('%Y-%m-%d')
    last_channel_visit_str = current_date.strftime('%Y-%m-%d %H:%M:%S')
    user = message.from_user
    query = """
        INSERT INTO Users (telegram_id,
                            username,
                            first_name,
                            last_name,
                            date_registered,
                            last_channel_visit)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    query_condition = (
        user.id,
        user.username,
        user.first_name,
        user.last_name,
        date_registered,
        last_channel_visit_str,
        )
    query_request(query, query_condition)
