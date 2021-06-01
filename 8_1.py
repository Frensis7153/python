import traceback


class Date:
    row = ''

    @classmethod
    def separator_of_date(cls):
        return list(map(int, cls.row.split('-')))

    @staticmethod
    def validator_of_date():
        list_of_date = Date.separator_of_date()

        try:
            if not 0 < list_of_date[1] < 13:
                raise Exception('ошибка месяца')
            elif list_of_date[1] % 2 == 1 and 31 < list_of_date[0] or list_of_date[0] < 0:
                raise Exception('ошибка дня')
            elif list_of_date[1] % 2 == 0 and 30 < list_of_date[0] or list_of_date[0] < 0:
                raise Exception('ошибка дня')
            elif list_of_date[1] == 2 and 0 < list_of_date[0] < 29:
                raise Exception('ошибка февраля')
            else:
                return 'Дата в порядке'
        except Exception:
            print(traceback.format_exc())


Date.row = '169778896-5-7877'
print(Date.separator_of_date())
print(Date.validator_of_date())
