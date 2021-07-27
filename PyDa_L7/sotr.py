class Employee:
    def __init__(self, name, seniority):
        self.name = name
        self.seniority = seniority

        self.grade = 1

    def grade_up(self):
        """Повышает уровень сотрудника"""
        self.grade += 1

    def publish_grade(self):
        """Публикация результатов аккредитации сотрудников"""
        print(self.name, self.grade)

    def check_if_it_is_time_for_upgrade(self):
        pass


class Developer(Employee):
    def __init__(self, name, seniority):
        super().__init__(name, seniority)

    def check_if_it_is_time_for_upgrade(self):
        # для каждой аккредитации увеличиваем счетчик на 1
        # пока считаем, что все разработчики проходят аккредитацию
        self.seniority += 1

        # условие повышения сотрудника из презентации
        if self.seniority % 5 == 0:
            self.grade_up()

        # публикация результатов
        return self.publish_grade()


class Designer(Employee):
    '''
    Напишите класс Designer, который учитывает количество международных премий
    для дизайнеров (из презентации: “Повышение на 1 грейд за каждые 7 баллов.
    Получение международной премии – это +2 балла”). Считайте, что при выходе
    на работу сотрудник уже имеет две премии и их количество не меняется со
    стажем (конечно если хотите это можно вручную менять).

    Класс Designer пишется по аналогии с классом Developer из материалов занятия.
    '''
    def __init__(self, name, seniority, reward=2):
        super().__init__(name, seniority)
        self.reward = reward

    def check_if_it_is_time_for_upgrade(self):
        # добавляем параметр международной премии, если такая есть
        # прибавляем к self.seniority 2
        # для каждой аккредитации увеличиваем счетчик на 1
        # пока считаем, что все разработчики проходят аккредитацию
        self.seniority += 1


        # условие повышения сотрудника из презентации
        if self.seniority % 7 == 0:
            if self.reward:
                self.seniority += self.reward


            self.grade_up()

        # публикация результатов
        return self.publish_grade()

alex = Designer('Александр', 0, 3)
for i in range(20):
    alex.check_if_it_is_time_for_upgrade()