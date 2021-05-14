from sys import argv


def salary(output_in_hours: float, rate_per_hours: float, prize: float) -> Exception or float:
    """Возвращает результат расчета заработной платы.

    Формула расчета: (выработка в часах * ставка в час) + премия
    """
    try:
        return output_in_hours * rate_per_hours + prize
    except Exception as e:
        return e


try:
    name_script, output_n_hours, rate_p_hours, the_prize = argv
    print(salary(float(output_n_hours), float(rate_p_hours), float(the_prize)))
except Exception as q:
    print(q)
