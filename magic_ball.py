from random import *

answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]


def magic_ball():
    print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
    name = input('Как тебя зовут?\n')
    print(f'Привет {name}')
    while True:
        ans = input('Ты пришел ко мне с вопросом, ибо будущее твое туманно. Задай же вопрос и получишь ответ.\n')
        print(choice(answers))
        a = input('Хочет ли он задать еще один вопрос?\n')
        if a.lower() != 'да':
            print('Возвращайся если возникнут вопросы!')
            break


magic_ball()