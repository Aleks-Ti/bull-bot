class MainKeyboard:
    """
    Кнопки для главного меню.
    Attributes:
    - create_reminds = "Создать напоминание"
    - view_reminds = "Посмотреть напоминания"
    - view_reminds_id = "Найти напоминание по ID"
    - off_remind_today = "Выключить напоминания"
    """

    create_reminds: str = 'Создать напоминание'
    view_reminds: str = 'Посмотреть напоминания'
    view_reminds_id: str = 'Найти напоминание по ID'
    off_remind_today: str = 'Выключить напоминания'

    @classmethod
    def get_keys(cls):
        return [
            attr
            for attr in dir(cls)
            if not callable(getattr(cls, attr)) and not attr.startswith('__')
        ]

    @classmethod
    def get_values(cls):
        return [
            getattr(cls, attr)
            for attr in dir(cls)
            if not callable(getattr(cls, attr)) and not attr.startswith('__')
        ]
