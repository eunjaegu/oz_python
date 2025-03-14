# 패키지 안에 있는 함수 임포트
from task_9_animals.mammals import Dog
from task_9_animals.birds import Eagle

# Dog 객체 생성
dog = Dog(name="Toto, Dallae", breed="Dachshund")
print(dog.get_info())

# Eagle 객체 생성
eagle = Eagle(name="Jojo", species="pigeon")
print(eagle.get_info())