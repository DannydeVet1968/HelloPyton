
class Person:
    def __init__(self, name, age, gender, height, mass, occupation, favourite_food):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.mass = mass
        self.occupation = occupation
        self.favourite_food = favourite_food

    def walk(self):
        return f"{self.name} is going on a long drunk relaxing walk."

    def eat(self, food):
        if food == self.favourite_food:
            return f"{self.name} is enjoying {food} and can eat it all day long! I could eat a cow without bothering to kill it!"
        else:
            return f"{self.name} is eating {food} because hunger is the best sauce."

    def sleep(self):
        return f"{self.name} is sleeping…Zzz… and dreaming about a bunch of naked girls in my bedroom!"

    def work(self):
        return f"{self.name} is going to work as a {self.occupation}."

    def introduce(self):
        bmi = self.mass / (self.height ** 2)
        if bmi < 20:
            bmi_category = "underweight"
        elif 20 <= bmi < 25:
            bmi_category = "ok"
        elif 25 <= bmi < 30:
            bmi_category = "overweight"
        elif 30 <= bmi < 40:
            bmi_category = "obese"
        else:
            bmi_category = "morbidly obese"
        return (f"Howdy folks, my name is {self.name}. I’m a {self.age}-year-old {self.gender} " f"and I’m {bmi_category}. My favourite food is {self.favourite_food}, " f"and I work as a {self.occupation}.")