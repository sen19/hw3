questions = ['My name __ Vova', ' I __ a coder', 'I live __ Moscow']
answers = ['is', 'am', 'in']

correct_count = 0

incorrect_count = 0

print('Привет! Предлагаю проверить свои знания английского! Наберите "ready", чтобы начать')

user_input = input()

if user_input != "ready":
    print('Кажется,вы не хотите играть. Очень жаль')
else:
    for i in range(len(questions)):

        question_text = questions[i]
        answer_text = answers[i]

        print(questions[i])

        user_input = input()

        if user_input == answer_text:
            print('Ответ верный')
            correct_count += 1
        else:
            print(f'Неправильно. Правильный ответ: {answer_text}')
            incorrect_count += 1

    questions_total = len(questions)
    correct_percent = round(correct_count / questions_total * 100)

    print(f'Вот и все! Вы ответили на {correct_count} вопросов из {questions_total} верно,'
          f'это {correct_percent} процентов')
    
