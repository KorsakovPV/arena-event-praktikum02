import random


class Thing:
    def __init__(self, name_Thing, defense_Thing, attack_Thing, health_Thing):
        self.name_Thing = name_Thing
        self.defense_Thing = defense_Thing
        self.attack_Thing = attack_Thing
        self.health_Thing = health_Thing


class Person:
    def __init__(self, name_Person, health_Person, attack_Person, defense_Person):
        self.name_Person = name_Person
        self.health_Person = health_Person
        self.attack_Person = attack_Person
        self.defense_Person = defense_Person
        self.finalProtection = 0

    def setThings(self, setThings):
        self.setThings = setThings

    def defense(self, attack_person):
        if self.finalProtection == 0:
            self.finalProtection += self.defense_Person
            for i in self.setThings:
                self.finalProtection += i.defense_Thing

        HitPoints = attack_person.attack_Person - attack_person.attack_Person * self.finalProtection

        self.health_Person -= HitPoints
        print(attack_person.name_Person, 'наносит удар по', self.name_Person, 'на', HitPoints)


class Paladin(Person):
    def __init__(self, name_Person, health_Person, attack_Person, defense_Person):
        self.name_Person = name_Person
        self.health_Person = health_Person * 2
        self.attack_Person = attack_Person
        self.defense_Person = defense_Person * 2
        self.finalProtection = 0


class Warrior(Person):
    def __init__(self, name_Person, health_Person, attack_Person, defense_Person):
        self.name_Person = name_Person
        self.health_Person = health_Person
        self.attack_Person = attack_Person * 2
        self.defense_Person = defense_Person
        self.finalProtection = 0


person_max = 10
things_max = person_max * 4
things = []
defensething = []

for i in range(things_max):
    defensething.append(random.uniform(0, 0.1))

defensething.sort()

for i in range(things_max):
    things.append(Thing('Things' + str(i), defensething[i], random.uniform(0, 0.1), random.uniform(0, 0.1)))

random.shuffle(things)

paladin = random.randint(1, person_max - 1)
warrior = person_max - paladin

nameperson = ['Роланд',
              'Ричард',
              'Галахад',
              'Томас',
              'Малькольм',
              'Джон',
              'Ааррон',
              'Абрахам',
              'Азэлстан',
              'Алгар',
              'Аластеир',
              'Арне',
              'Артур',
              'Байярд',
              'Бардолф',
              'Барнабас',
              'Бедивир',
              'Беорегард',
              'Бернард',
              'Валентайн',
              'Вард',
              'Вестлей',
              'Вилберн',
              'Вольф',
              'Габриэль',
              'Гарольд',
              'Глендауэр',
              'Голладжер',
              'Даймонд',
              'Дариан',
              'Двэйн',
              'Деметриус',
              'Джеральд',
              'Зандер',
              'Ирвинг',
              'Каллен',
              'Кендрик',
              'Киллиан',
              'Кристофер',
              'Лемюэль',
              'Леонард',
              'Лисандр',
              'Людовик',
              'Мариус',
              'Марлен',
              'Миллард',
              'Мэйсон',
              'Николас',
              'Норберт',
              'Олдред',
              'Оллгар',
              'Освальд',
              'Персиваль',
              'Реджинальд',
              'Роуланд',
              'Теобальд'
              ]

random.shuffle(nameperson)

persons = []

for i in range(person_max):
    if i < paladin:
        persons.append(Paladin(nameperson[i], 10, 10, 0.1))
    else:
        persons.append(Warrior(nameperson[i], 10, 10, 0.1))

count = 0
for person in persons:
    things_person = []
    x = random.randint(1, 4)
    for i in range(x):
        things_person.append(things[count])
        count += 1
    person.setThings(things_person)

while len(persons) > 1:
    random.shuffle(persons)
    for i in range(0, len(persons) - 1, 2):
        persons[i].defense(persons[i + 1])
    for i in persons:
        if i.health_Person < 0:
            persons.remove(i)

print('Победил', persons[0].name_Person)
