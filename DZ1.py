class Person:
    def __init__(self, name, midlename, lastname, numbers):
        self.name = name
        self.midlename = midlename
        self.lastname = lastname
        self.numbers = numbers

    def get_phone(self):
        return self.numbers.get("private")

    def get_name(self):
        return f' {self.lastname} {self.name} {self.midlename}'

    def get_work_phone(self):
        return self.numbers.get("work")

    def get_sms_text(self):
        return f'Уважаемый {self.name} {self.midlename} примите участие в нашем ' \
               f'беспроигрышном конкурсе для физических лиц'


class Company:

    def __init__(self, company_name, c_type, company_numbers, *args):
        self.company_name = company_name
        self.c_type = c_type
        self.company_numbers = company_numbers
        self.persons = args

    def get_phone(self):
        contact = self.company_numbers.get("contact")
        if not contact:
            for person in self.persons:
                phone = person.get_work_phone()
                if phone:
                    #print(phone)
                    return phone
        else:
            return contact

    def get_name(self):
        return self.company_name

    def get_sms_text(self):
        return f'Для компании {self.company_name} примите участие в нашем ' \
               f'беспроигрышном конкурсе для {self.c_type}'
        

def send_sms (*args):
    
    for contact in args:
        if contact.get_phone():
            
            print(f"Отправлен смс на номер {contact.get_phone()} с текстом {contact.get_sms_text()} ")
        else:
            print(f'Не удалось отправить сообщение абоненту {contact.get_name()}')


# person1 = Person("Ivan", "Ivanonich", "Ivanov", {"private": "+787878787", "work": "+12148578"})
# person2 = Person("Petrov", "Petrovicn", "Petrov", {"private": "+458787877"})
# person3 = Person("Michail", "Amtonovich", "Sidorov", {"work": "+999778444"})
# person4 = Person("Jon", "Unknown", "Doe", {})
# company1 = Company("Bell", "OOO", {"contact": "+21445555"}, person3, person4)
# company2 = Company("Cell", "AO", {"non_contact": "222"}, person2, person3)
# company3 = Company('Dell', 'Ltd', {'none_contact' : '333'}, person2, person4)
# send_sms(person1, person2, person3, person4, company1, company2, company3)



person1 = Person("Степан", "Петрович", "Джобсов", {"private": "555"})
person2 = Person("Боря", "Иванович", "Гейтсов", {"private": "777", "work" : "888"})
person3 = Person("Семен", "Робертович", "Возняцкий", {"work": "789"})
person4 = Person("Леонид", "Арсенович", "Торвальдсон", {})
company1 = Company("Яблочный комбинат", "OOO", {"contact": "111"}, person1, person3)
company2 = Company("Пластокно", "AO", {"non_contact": "222"}, person2)
company3 = Company('Пингвинья ферма', 'Ltd', {'none_contact' : '333'}, person4)
send_sms(person1, person2, person3, person4, company1, company2, company3)