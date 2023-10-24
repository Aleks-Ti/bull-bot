from db.settings.sql_query_executor import query_request


def create_tables():
    query = """
        CREATE TABLE Users (
        id SERIAL PRIMARY KEY,
        telegram_id INTEGER UNIQUE NOT NULL,
        username VARCHAR(255) NOT NULL,
        first_name VARCHAR(255),
        last_name VARCHAR(255),
        date_registered DATE NOT NULL,
        last_channel_visit DATE
    )
    """
    query_request(query, None)

    query = """
        CREATE TABLE Reminders (
            id SERIAL PRIMARY KEY,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            task_description TEXT NOT NULL,
            is_completed BOOLEAN DEFAULT FALSE,
            remind_at TIMESTAMP NOT NULL
    )
    """
    query_request(query, None)

    query = """
        CREATE TABLE UsersReminders (
            users_id INT,
            reminder_id INT,
            PRIMARY KEY (users_id, reminder_id),
            FOREIGN KEY (users_id) REFERENCES Users(id)
                ON DELETE CASCADE,
            FOREIGN KEY (reminder_id) REFERENCES Reminders(id)
                ON DELETE CASCADE
        )
    """  # промежуточная
    query_request(query, None)

    query = """
        CREATE TABLE ReminderMessages (
        id SERIAL PRIMARY KEY,
        message_text TEXT NOT NULL
    )
    """
    query_request(query, None)

    query = """
        CREATE TABLE ReminderMessagesReminders (
            reminders_id INT,
            remindermessages_id INT,
            PRIMARY KEY (reminders_id, remindermessages_id),
            FOREIGN KEY (reminders_id) REFERENCES Reminders(id)
                ON DELETE CASCADE,
            FOREIGN KEY (remindermessages_id) REFERENCES ReminderMessages(id)
                ON DELETE CASCADE
        )
    """  # промежуточная
    query_request(query, None)

    query = """
        CREATE TABLE Stickers (
            id SERIAL PRIMARY KEY,
            sticker_angry VARCHAR(255) NOT NULL,
            evil_sticker VARCHAR(255) NOT NULL,
            good_sticker VARCHAR(255) NOT NULL,
            thoughtful_post_it VARCHAR(255) NOT NULL,
            bad_sticker VARCHAR(255) NOT NULL,
            frustrated_sticker VARCHAR(255) NOT NULL,
            fuck_sticker VARCHAR(255) NOT NULL,
            neglect_sticker VARCHAR(255) NOT NULL
    )
    """
    query_request(query, None)

    query = """
        CREATE TABLE RemindersStickers (
            reminders_id INT,
            stickers_id INT,
            PRIMARY KEY (reminders_id, stickers_id),
            FOREIGN KEY (stickers_id) REFERENCES Stickers(id)
                ON DELETE CASCADE,
            FOREIGN KEY (reminders_id) REFERENCES Reminders(id)
                ON DELETE CASCADE
        )
    """
    query_request(query, None)


if __name__ == '__main__':
    create_tables()
