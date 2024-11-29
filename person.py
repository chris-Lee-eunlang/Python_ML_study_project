class Person:
    def __init__(self, name, gender, age):
        self.name  = name
        self.age = age
        self.gender = gender
        while True:
            if gender in ['female', 'male']:
                self.gender = gender
                break
            else:
                gender = input("잘못된 성별을 입력하셨습니다. 'male' 또는 'female'을 입력하세요. \n 성별: ")
                continue
    def display(self):
        return print(f"이름: {self.name}, 성별: {self.gender} \n 나이: {self.age}")
    
    def greet(self):
        if int(self.age) >= 19:
            print(f"안녕하세요, {self.name}! 성인이시군요")
        else:
            print(f"안녕하세요, {self.name}! 어린이시군요") 
Person = Person('페이커', 'female', '14')
Person.display()
Person.greet()