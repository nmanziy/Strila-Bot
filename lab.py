import library
import math
import random
import datetime
library.print_greeting()
user_input = library.get_user_input()

while True:
    if user_input == "допомога":
        library.print_help_1()
        user_input = library.get_user_input()

    elif user_input == "назад":
        library.print_greeting()
        user_input = library.get_user_input()
    elif user_input == "вихід":
        library.print_farewell()
        break
    elif user_input == "1":
        library.print_response(f"""Ви обрали тему "Фізика". Я можу допомогти: \n1 - Вивести гравітаційну сталу; \n2 - Вивести сталу Планка; \n3 - Вивести кулонівську сталу.""")
        physics_question = library.get_user_input()

        while True :
            if physics_question == "1":
                library.print_add_response(f"""Гравітаційна стала дорівнює G = 6.67430e-11 Н*(м/кг)².""")
                physics_question = library.get_user_input()
            elif physics_question == "2":
                library.print_add_response(f"""Стала Планка дорівнює h = 6.626e-34 Дж*с.""")
                physics_question = library.get_user_input()
            elif physics_question == "3":
                k = 9e9
                library.print_add_response(f"""Кулонівська стала дорівнює {k:.2e} Н·м²/Кл².""")
                physics_question = library.get_user_input()

            elif physics_question == "назад":
                library.print_greeting()
                user_input = library.get_user_input()
                break
            elif physics_question == "вихід":
                library.print_farewell()
                break
            elif physics_question == "допомога":
                library.print_help_2()
                user_input = library.get_user_input()
                break

    elif user_input == "2":
        library.print_response(f"""Ви обрали тему "Математика". Ви можете задати мені питання з наступних тем: \n1 - Найбільший спільний дільник двох чисел;\
         \n2 - Найменше спільне кратне двох чисел; \n3 - Векторний добуток векторів; \n4 - Обчислення площі трикутника за допомогою векторного добутку;\
          \n5 - Площа прямокутника; \n6 - Площа трапеції; \n7 - Вивести sin(x) та cos(x).""")
        math_question = library.get_user_input()
        while True:
                if math_question == "1":
                    a = int(input("Ви обрали тему Найбільший спільний дільник двох чисел. \nВведіть перше число: "))
                    b = int(input("Введіть друге число: "))
                    gcd_result = library.gcd(a, b)
                    library.print_add_response(f"Найбільший спільний дільник для чисел {a} та {b} = {gcd_result}")
                    math_question = library.get_user_input()

                elif math_question == "2":
                    a = int(input("Ви обрали тему Найменше спільне кратне двох чисел. \nВведіть перше число: "))
                    b = int(input("Введіть друге число: "))
                    lcm_result = library.lcm(a, b)
                    library.print_add_response(f"Найменше спільне кратне для чисел {a} та {b} = {lcm_result}")
                    math_question =library.get_user_input()

                elif math_question == "3":
                    Ax = int(input("Ви обрали тему Векторний добуток векторів. \nВведіть координату х1 першого вектора: "))
                    Ay = int(input("Введіть координату y1 першого вектора: "))
                    Az = int(input("Введіть координату z1 першого вектора: "))
                    Bx = int(input("Введіть координату х2 другого вектора: "))
                    By = int(input("Введіть координату y2 другого вектора: "))
                    Bz = int(input("Введіть координату z2 другого вектора: "))
                    x, y, z = library.vector_product(Ax, Ay, Az, Bx, By, Bz)
                    library.print_add_response("Векторний добуток векторів A і B: ({}, {}, {})".format(x, y, z))
                    math_question = library.get_user_input()

                elif math_question == "4":
                    Ax = int(input("Ви обрали тему Обчислення площі трикутника за допомогою векторного добутку. \nВведіть координату х1 вектора, що відповідає першій стороні трикутника: "))
                    Ay = int(input("Введіть координату y1 вектора, що відповідає першій стороні трикутника: "))
                    Az = int(input("Введіть координату z1 вектора, що відповідає першій стороні трикутника: "))
                    Bx = int(input("Введіть координату х2 вектора, що відповідає другій стороні трикутника: "))
                    By = int(input("Введіть координату y2 вектора, що відповідає другій стороні трикутника: "))
                    Bz = int(input("Введіть координату z2 вектора, що відповідає другій стороні трикутника: "))
                    x, y, z = library.vector_area(Ax, Ay, Az, Bx, By, Bz)
                    area_s = 0.5 * math.sqrt(x ** 2 + y ** 2 + z ** 2)
                    library.print_add_response("Площа даного трикутника: {:.2f}".format(round(area_s, 2)))
                    math_question = library.get_user_input()

                elif math_question == "5":
                    a = int(input("Ви обрали тему Площа прямокутника. \nВведіть довжину першої сторони прямокутника: "))
                    b = int(input("Введіть довжину другої сторони прямокутника: "))
                    s = a * b
                    library.print_add_response(f"Площа даного прямокутника: {s}")
                    math_question = library.get_user_input()

                elif math_question == "6":
                    a = int(input("Ви обрали тему Площа трапеції. \nВведіть довжину першої основи трапеції: "))
                    b = int(input("Введіть довжину другої основи трапеції: "))
                    h = int(input("Введіть довжину висоти трапеції: "))
                    S = 0.5 * (a + b) * h,
                    library.print_add_response(f"Площа даної трапеції: {S}")
                    math_question = library.get_user_input()

                elif math_question == "7":
                    x = int(input("Ви обрали тему Виведення sin(x) та cos(x). \nВведіть х для якого треба знайти значення sin(x) та cos(x): "))
                    sin_x = math.sin(x)
                    cos_x = math.cos(x)
                    library.print_add_response(f"Для даного Х: sin(x)={sin_x}, cos(x)={cos_x}")
                    math_question = library.get_user_input()

                elif math_question == "назад":
                    library.print_greeting()
                    user_input = library.get_user_input()
                    break
                elif math_question == "вихід":
                    library.print_farewell()
                    break
                elif math_question == "допомога":
                    library.print_help_2()
                    user_input = library.get_user_input()
                    break

    elif user_input == "3":
        library.print_response(f"""Ви обрали тему "Географія". Ви можете задати мені наступні питання: \n1 - Яке найбільше озеро в світі за площею?;\
         \n2 - Де знаходиться Сахара - найбільша пустеля в світі?; \n3 - Яка держава має найбільшу кількість озер в світі?; \
         \n4 - Назвіть дві держави, які мають найбільшу кількість водосховищ в світі; \n5 - Знайти азимут від точки А (x1, y1) до точки В (x2, y2), якщо відомі їх координати.""")
        geography_question = library.get_user_input()

        while True:
            if geography_question == "1":
                library.print_add_response(f"Найбільшим озером в світі за площею є Каспійське море. Хоча його називають морем, насправді воно є солоним озером. \
                \nКаспійське море займає площу близько 143 000 квадратних кілометрів і розташоване між Азією та Європою.")
                geography_question = library.get_user_input()

            elif geography_question == "2":
                library.print_add_response(f"Сахара є найбільшою пустелею в світі і знаходиться в Північній Африці. \
                \nВона охоплює території більш ніж 10 країн, зокрема Алжир, Чад, Єгипет, Лівія, Малі, Марокко, Мавританія, Нігер, Західна Сахара та Судан. ")
                geography_question = library.get_user_input()

            elif geography_question == "3":
                library.print_add_response(f"Канада має найбільшу кількість озер в світі. За даними Канадського центру з водних ресурсів, у Канаді є більше 2 мільйонів озер. ")
                geography_question = library.get_user_input()

            elif geography_question == "4":
                library.print_add_response(f"Дві держави, які мають найбільшу кількість водосховищ в світі - це російська федерація та Канада.\
                \nросійська федерація має найбільшу кількість водосховищ у світі, загальний об'єм яких становить більше 10 000 кубічних кілометрів.\
                 \nКанада є другою за кількістю водосховищами державою у світі, загальний об'єм яких становить більше 3 000 кубічних кілометрів.")
                geography_question = library.get_user_input()

            elif geography_question == "5":
                x1 = int(input("Ви обрали тему Знаходження азимута. \nВведіть координату х точки А: "))
                y1 = int(input("Введіть координату y точки А: "))
                x2 = int(input("Введіть координату x точки B: "))
                y2 = int(input("Введіть координату y точки B: "))
                azimuth_deg = library.azimuth(x1,x2,y1,y2)
                library.print_add_response("Азимут від точки А до точки В: {} градусів.".format(round(azimuth_deg, 1)))
                geography_question = library.get_user_input()

            elif geography_question == "назад":
                library.print_greeting()
                user_input = library.get_user_input()
                break
            elif geography_question == "вихід":
                library.print_farewell()
                break
            elif geography_question == "допомога":
                library.print_help_2()
                user_input = library.get_user_input()
                break

    elif user_input == "4":
        library.print_response(f"""Ви обрали тему "Філологія". Я можу допомогти з такими запитаннями: \n1 - Які часи є в англійській мові?;\
        \n2 - Як утворюються питальні речення в англійській мові?; \n3 - Які відмінки є в українській мові?; \
        \n4 - Які роди іменників існують в українській мові?; \n5 - Як утворити форму множини іменників в українській мові?""")
        philology_question = library.get_user_input()

        while True:
            if philology_question == "1":
                library.print_add_response(f'Якщо говорити про часи як про фізичний феномен, то їх всього три – теперішнє, минуле і майбутнє.\
                \nПри класичному ж підході до граматики англійської мови, ці три, в свою чергу поділяються на наступні 12: \n• Present Simple; \n• Present Continuous; \n• Present Perfect; \
                \n• Present Perfect Continuous; \n• Past Simple; \n• Past Continuous; \n• Past Perfect; \n• Past Perfect Continuous; \n• Future Simple; \n• Future Continuous;\
                \n• Future Perfect; \n• Future Perfect Continuous.')
                philology_question = library.get_user_input()

            elif philology_question == "2":
                library.print_add_response(f"""В англійській мові розрізняють чотири типи питальних речень: загальні, спеціальні, роз\'єднувальні й альтернативні.\
                \n• У загальних запитаннях допоміжне або модальне дієслово, що входить до присудка, ставиться на початку речення перед підметом.\
                \n   Якщо у складі присудка немає допоміжного або модального дієслова, то перед підметом ставиться допоміжне дієслово do (does) або did, \
                \n   а після нього — основне дієслово у формі інфінітива без частки to. Решта членів речення стоять у такому ж порядку, як і в розповідному реченні. - Do you have a dictionary?\
                \n• Порядок слів у спеціальних запитаннях такий самий, як і в загальних, але перед допоміжним або модальним дієсловом стоїть питальне слово. - Where do you live?\
                \n• Роз\'єднувальне запитання складається з двох частин. Перша частина — це розповідне речення у ствердній або заперечній формі, друга — коротке загальне запитання, \
                \n   що складається з підмета, вираженого особовим займенником, який відповідає підмету першої частини, і допоміжного або модального дієслова. - You don\'t speak French, do you?\
                \n• Альтернативне запитання складається з двох загальних запитань, з\'єднаних сполучником or. Хоча альтернативні запитання починаються з допоміжного чи \
                    модального дієслова, як і загальні, за змістом вони є спеціальними, тому вимагають повної відповіді. - Is he a teacher or a doctor?""")
                philology_question = library.get_user_input()

            elif philology_question == "3":
                library.print_add_response(f'В українській мові є 7 відмінків: \n• Називний (відповідає на питання хто? що?); \n• Родовий (кого? чого?);\
                \n• Давальний (кому? чому?); \n• Знахідний (кого? що?); \n• Орудний (ким? чим?); \n• Місцевий (на/у кому? на/у чому?); \n• Кличний (звертання).')
                philology_question = library.get_user_input()

            elif philology_question == "4":
                library.print_add_response(f'Українська мова має три роди іменників: чоловічий, жіночий та середній. \
                \n• До ЧОЛОВІЧОГО роду належать іменники, що в називному відмінку однини мають нульову флексію або закінчення -о; \
                \n  в родовому — закінчення -а(у), -я(ю); в орудному — закінчення -ом, -ем, -єм.\
                \n• До ЖІНОЧОГО роду — іменники, що в називному відмінку однини мають закінчення -а , -я; \
                \n  в родовому — закінчення -и, -і, -ї; в орудному — закінчення -ою, -ею, -єю.\
                \n• До СЕРЕДНЬОГО роду — іменники, що в називному відмінку однини мають закінчення -о, -е; \
                \n  в непрямих відмінках — закінчення, спільні із закінченнями іменників чоловічого роду.')
                philology_question = library.get_user_input()

            elif philology_question == "5":
                library.print_add_response(f'Українська мова має дві форми множини іменників:\
                \n1. Регулярна форма множини: Додається суфікс -и до основи іменника. \
                \n   Наприклад: книга - книги, стіл - столи.\
                \n2. Нерегулярна форма множини: Ця форма відрізняється від основної форми іменника.\
                \n   Вона може мати іншу основу, закінчення, або взагалі бути унікальною та її треба запам\'ятати для кожного іменника окремо.\
                \n   Наприклад: людина - люди, музей - музеї.\
                \n3. Деякі іменники мають тільки форму множини, але не мають однини. \
                \n   Наприклад, ножиці, окуляри.')
                philology_question = library.get_user_input()

            elif philology_question == "назад":
                library.print_greeting()
                user_input = library.get_user_input()
                break
            elif philology_question == "вихід":
                library.print_farewell()
                break
            elif philology_question == "допомога":
                library.print_help_2()
                user_input = library.get_user_input()
                break

    elif user_input == "5":
        library.print_response(f"""Ви обрали тему "Астрономія". Я можу відповісти на дуже цікаві запитання: \n1 - Які планети Сонячної системи мають найбільші та найменші орбіти?\
        \n2 - Як впливає зоряне світло на здоров'я людини?""")
        astronomy_question = library.get_user_input()
        while True:
            if astronomy_question == "1":
                library.print_add_response(f'Найбільшу орбіту має планета Нептун, її середня відстань від Сонця становить близько 4,5 млрд км. \
                \nНайменшу орбіту має планета Меркурій, її середня відстань до Сонця становить приблизно 58 млн км.')
                astronomy_question = library.get_user_input()

            elif astronomy_question == "2":
                library.print_add_response(f'Зоряне світло може впливати на здоров\'я людини в різні способи. \
                \nНаприклад, недостатня кількість природного світла, особливо в зимовий період, може призводити \
                \nдо сезонного афективного розладу (SAD), депресії та інших порушень настрою та поведінки.\
                \nЗ іншого боку, надмірна експозиція штучному світлу, особливо вночі, може порушувати\
                \nбіологічний ритм людини та призводити до різних захворювань, таких як безсоння, \
                \nголовні болі, депресія, зниження імунної системи та інших проблем зі здоров\'ям.')
                astronomy_question = library.get_user_input()

            elif astronomy_question == "назад":
                library.print_greeting()
                user_input = library.get_user_input()
                break
            elif astronomy_question == "вихід":
                library.print_farewell()
                break
            elif astronomy_question == "допомога":
                library.print_help_2()
                user_input = library.get_user_input()
                break

    elif user_input == "6":
        library.print_response(f"""Ви обрали тему "Загальні запитання". Ви можете задати мені наступні питання: \n1 - Котра година?\
         \n2 - Скільки днів до Нового Року? \n3 - Як тебе звати? \n4 - Заспівай колядку;\
          \n5 - Скажи надихаючу цитату.""")
        general_question = library.get_user_input()
        while True:
            if general_question == "1":
                time = library.get_current_time()
                library.print_response(f"Ваш поточний час {time}" )
                general_question = library.get_user_input()

            elif general_question == "2":
                new_year = library.days_till_new_year()
                library.print_add_response(f" {new_year} Встигніть виконати все заплановане!")
                general_question = library.get_user_input()

            elif general_question == "3":
                library.print_add_response(f"Привіт! Я - Бот Стріла! З радістю відповім на Ваші запитання!♥")
                general_question = library.get_user_input()

            elif general_question == "4":
                song = random.choice(library.carol_songs)
                library.print_add_response(f"Ось одна із моїх улюблених колядок: \n{song}")
                general_question = library.get_user_input()

            elif general_question == "5":
                quote = random.choice(library.motivation_quote)
                library.print_add_response(f"Ловіть порцію натхнення: \n{quote}")
                general_question = library.get_user_input()

            elif general_question == "назад":
                library.print_greeting()
                user_input = library.get_user_input()
                break
            elif general_question == "вихід":
                library.print_farewell()
                break
            elif general_question == "допомога":
                library.print_help_2()
                user_input = library.get_user_input()
                break

