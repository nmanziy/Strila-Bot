import math
import datetime
topic_history = []
topics_dictionary = {
    '1.Фізика': {},
    '2.Математика': {},
    '3.Географія': {},
    '4.Філологія': {},
    '5.Астрономія': {},
    '6.Загальні': {},
}
def print_greeting():
    global topics_dictionary
    greeting = "\033[35m" + f"""Вітаю, мене звати Стріла➶. Ви можете задати мені питання з наступних тем (Введіть номер запитання): 
{', '.join(topics_dictionary.keys())}."""
    print_response(greeting)

def print_farewell():
    farewell = "\033[35m" + f"""Завжди рада допомогти! До зустрічі."""
    print_response(farewell)

def print_idk():
    idk = "\033[35m" +  f"""На жаль, я не знаю цієї теми. Спробуйте іншу."""
    print_response(idk)

def print_response(text):
    print( "\033[35m" + '[Bот]: ' + text )

def print_add_response(text):
    print("\033[35m" + f'[Bot]: {text} \n\033[30mВи можете задати наступне питання з цієї теми, або ввести "назад", щоб вибрати іншу тему. Також ви можете ввести "вихід", щоб завершити роботу.')

def get_user_input():
    return input("\033[36m" + '[User]: ')

def get_current_topic():
    global topic_history
    if len(topic_history) == 0:
        return None
    return topic_history[-1]

def print_help_1():
    print("\033[35m[Bot]: Оберіть тему, з якої бажаєте задати питання")

def print_help_2():
    print("\033[35m[Bot]: Введіть \"назад\", щоб повернутися до вибору теми. Введіть \"вихід\" для завершення роботи." )

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)

def lcm(a, b):
    lcm = (a * b) // gcd(a, b)
    return lcm

def vector_product(Ax, Ay, Az, Bx, By, Bz):
    AxBy = Ax * By
    AyBx = Ay * Bx
    AyBz = Ay * Bz
    AzBy = Az * By
    AzBx = Az * Bx
    AxBz = Ax * Bz

    x = AyBz - AzBy
    y = AzBx - AxBz
    z = AxBy - AyBx
    return x, y, z

def vector_area(Ax, Ay, Az, Bx, By, Bz):
    AxBy = Ax * By
    AyBx = Ay * Bx
    AyBz = Ay * Bz
    AzBy = Az * By
    AzBx = Az * Bx
    AxBz = Ax * Bz
    x = AyBz - AzBy
    y = AzBx - AxBz
    z = AxBy - AyBx
    return x, y, z

def azimuth(x1,x2,y1,y2):
    delta_x = x2 - x1
    delta_y = y2 - y1
    azimuth_rad = math.atan2(delta_y, delta_x)
    azimuth_deg = math.degrees(azimuth_rad)
    return azimuth_deg

def get_current_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    return current_time

def days_till_new_year():
    now = datetime.datetime.now()
    new_year = datetime.datetime(now.year + 1, 1, 1)
    delta = new_year - now
    days_left = delta.days
    message = f"До Нового року залишилось {days_left}"
    message = message.replace("days", "").split(",")[0] + " днів!"
    return message

carol_songs=["По всьому світу сталась новина:\
            \nДіва Марія Сина зродила,\
            \nСіном притрусила,\
            \nВ яслах положила\
            \nГосподнього Сина.\
            \nДіва Марія Бога просила:\
            \n\"В що ж би я Сина свого повила?\"\
            \nТи, небесний Царю,\
            \nЗішли свої дари\
            \nЦього дому господарю." ,
            "Нова радість стала, яка не бувала,\
            \nНад вертепом звізда ясна на весь світ засіяла.\
            \nДе Христос родився, з Діви воплотився,\
            \nЯк чоловік пеленами убого оповився.\
            \nПастушки з ягнятком перед тим дитятком\
            \nНа колінця припадають, Царя-Бога вихваляють.\
            \n– Ой ти, Царю, Царю, небесний Владарю,\
            \nДаруй літа щасливії цього дому господарю.\
            \nДаруй господарю, даруй господині,\
            \nДаруй літа щасливії нашій славній Україні." ,
            "Бог ся рождає, хто ж Го може знати!\
            \nІсус Му ім’я, Марія Му Мати!\
            \nПриспів:\
            \n**Тут Ангели чудяться,\
            \nРожденного бояться,\
            \nА віл стоїть, трясеться,\
            \nОсел смутно пасеться.\
            \nПастиріє клячуть,\
            \nВ плоти Бога бачуть,\
            \nТут же, тут же,\
            \nТут же, тут же, тут!**" ,
            "Небо і Земля (2) нині торжествують.\
            \nАнгели й люди (2) весело празнують.\
            \nПриспів:\
            \n**Христос родився, Бог воплотився,\
            \nАнгели співають, царіє вітають,\
            \nПоклін віддають, пастиріє грають,\
            \n\"Чудо, чудо!\" - повідають. (2)**\
            \nВо Вифлеємі (2) весела новина:\
            \nПречиста Діва (2) породила Сина.",
            "Тиха ніч, свята ніч!\
            \nЯсність б’є від зірниць.\
            \nДитинонька Пресвята,\
            \nТака ясна, мов зоря,\
            \nСпочиває в тихім сні.\
            \nСвята ніч настає,\
            \nЯсний блиск з неба б'є,\
            \nВ людськім тілі Божий Син\
            \nПрийшо нині в Вифлеєм\
            \nЩоб спасти цілий світ."]

motivation_quote=["☻♥Щастя - це не відсутність проблем у житті, а вміння з ними справлятися.♥☻",
                  "☻♥Найбільший ворог успіху – це страх. Тож, не бійся ризикувати і діяти.♥☻" ,
                  "☻♥Будьте зміною, яку хочете бачити у світі.♥☻",
                  "☻♥Вір у себе та в свої здібності. Якщо ти цього не зробиш, то хто ж зможе?♥☻",
                  "☻♥Звичайна людина вірить у можливість. Незвичайна людина робить її реальністю.♥☻",
                  "☻♥Потрібен тільки перший крок, і весь шлях розкриється перед тобою.♥☻"]



