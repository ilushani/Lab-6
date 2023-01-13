class Employee:
    objectsCount = 0
    def __init__(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary
        self.__worked = 0
        self.__teams = []
        Employee.objectsCount = Employee.objectsCount + 1
    #Рассчитываем премию сотрудника
    def calc_bonus(self, workdays):     #Считает премию
        return self.__salary * self.get_bonus() / workdays * self.__worked
    def calc_salary(self, workdays):    #Считает зарплату
        return self.__salary / workdays * self.__worked
    def fire(self): #Увольняет работника (удаляет из всх групп)
        while len(self.__teams)!=0:
            self.__teams[0].remove(self)
        print("Работник %s уволен" % (self.__name))
    def getname(self):  #Возвращает имя работника
        return self.__name
    def work(self,n): #Добавляет n рабочих смен
        self.__worked +=n
        print("Работник %s отработал смену" % self.__name)
    def invite(self,team):  #Добавляет группу в список групп
        self.__teams.append(team)
    def uninvite(self,team): #Удаляет группу из списка групп
        self.__teams.remove(team)
    def get_bonus(self):
        return 0.05

class SeniorEmployee(Employee):
    def __init__(self, name, age, salary, is_bearded):
        self.is_bearded = is_bearded
        super().__init__(name, age, salary)

    def get_bonus(self):
        return 0.1
    pass

class Manager(Employee):
    def __init__(self, name, age, salary, is_bald):
        self.is_bald = is_bald
        super().__init__(name, age, salary)
    def get_bonus(self):
        return 0.2

class Team:
    def __init__(self, name, *args):
        self.__members = []
        self.teamname = name
        for i in args:
            self.add(i)
    def add(self, other):   #Удаляет работника в группу
        for i in self.__members:
            if other == i:
                print('Работник %s уже в команде!' %(other.getname()))
                return
        self.__members.append(other)
        other.invite(self)
        print("Работник %s добавлен в команду %s" %(other.getname(),self.teamname))
    def remove(self, member):   #Удаляет работника из группы
        for i in self.__members:
            if member == i:
                self.__members.remove(i)
                i.uninvite(self)
                print('Работник %s удален из %s' %(i.getname(), self.teamname))
                return
        print('Работник не найден')
    def show_members(self): #Выводит всех работников данной группы
        print("В команде %s следующие работники:" %(self.teamname))
        for i in self.__members:
            print(i.getname())


#Набираем работников
se_001 = SeniorEmployee('Денис', 35, 40000, 0)
se_001 = SeniorEmployee('Денис', 35, 40000, True)
e_001 = Employee('Леонид', 26, 20000)
e_002 = Employee('Виктор', 24, 20000)
m_001 = Manager('Ипполит', 45, 100000, 0)
m_001 = Manager('Ипполит', 45, 100000, True)
e_003 = Employee('Прокофий', 21, 20000)
e_004 = Employee('Порфирий', 22, 20000)
se_002 = SeniorEmployee('Арсений', 35, 40000, 0)
se_002 = SeniorEmployee('Арсений', 35, 40000, False)
e_005 = Employee('Евгений', 25, 20000)
e_006 = Employee('Василий', 24, 20000)
#Собираем команду
team_001 = Team("Отдел кадров",se_001,e_006)
team_001.add(e_005)
team_001.add(e_004)
team_001.show_members()
#Собираем еще команду
team_002 = Team("Отдел продаж",se_002,e_003)
team_002.add(e_001)
team_002.add(e_004)
#Пробуем добавить того же человека еще раз
team_002.add(e_004)
team_002.show_members()
#Увольняем Порфирия и Дениса
e_004.fire()
se_001.fire()
#Смотрим кто остался
team_001.show_members()
team_002.show_members()
workdays = 30
#Теперь пробуем
e_001.work(30)
se_002.work(30)
m_001.work(30)
print("Премия работника %s составляет %.2f рублей" %(e_001.getname(),e_001.calc_bonus(workdays)))
print("Премия работника %s составляет %.2f рублей" %(se_002.getname(),se_002.calc_bonus(workdays)))
print("Премия работника %s составляет %.2f рублей" %(m_001.getname(),m_001.calc_bonus(workdays)))
