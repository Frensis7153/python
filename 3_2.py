def user_data(name, surname, year_of_birth, current_city, email, contact_number):
    """Возвращает данные пользователя, которые принимает.
    """
    print(f'имя - {name}, фамилия - {surname}, год рождения - {year_of_birth}, город проживания - {current_city},'
          f' email - {email}, контактный телефон - {contact_number}')


user_data(year_of_birth='16.12.1999', current_city='Москва', contact_number='8-916-000-44-44', surname='Иванов',
          email='user@gmail.ru', name='Иван')
