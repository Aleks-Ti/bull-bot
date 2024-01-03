from crud.reminders import reminder_create


class MainKeyboard:
    """
    Кнопки для главного меню.

    Attributes:
    - create_reminds = 'Создать напоминание'
    - view_reminds = 'Посмотреть напоминания'
    - view_reminds_id = 'Найти напоминание по ID'
    - off_remind_today = 'Выключить напоминания'
    - cancel = 'Отмена'
    """

    create_reminders: str = 'Создать напоминание'
    view_reminders: str = 'Посмотреть напоминания'
    view_reminder_id: str = 'Найти напоминание по ID'
    off_reminders_today: str = 'Выключить напоминания'
    cancel: str = 'Отмена'

    # @classmethod
    # def get_keys(cls):
    #     return [
    #         attr
    #         for attr in dir(cls)
    #         if not callable(getattr(cls, attr)) and not attr.startswith('__')
    #     ]

    # @classmethod
    # def get_values(cls):
    #     return [
    #         getattr(cls, attr)
    #         for attr in dir(cls)
    #         if not callable(getattr(cls, attr)) and not attr.startswith('__')
    #     ]


class ReminderKeyboard:
    """
    Инлайн кнопки для меню напоминаний.

    Attributes:
    - cycle_reminder = 'Циклическое напоминание'
    - single_reminder = 'Одноразовое напоминание'
    - cancel = 'Отмена'
    """

    cycle_reminder: str = 'Циклическое напоминание'
    single_reminder: str = 'Одноразовое напоминание'
    cancel: str = 'Отмена'

