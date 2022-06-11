import telebot
import random
from telebot import types
import pandas as pd
# import constants as const

bot = telebot.TeleBot('5364339560:AAFW5USMhFbowpQsTnLv0euiQOjHH-Qw5PM')

x = 1
y = 1
repeat_flag = True

number_list = [2, 3, 4, 5, 6, 7, 8, 9]
is_train = [True, True, True, True, False, False, False, False]
symbol_list = ["2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣"]
callback_add_list = ["second_add", "third_add", "fourth_add", "fifth_add",
                     "sixth_add", "seventh_add", "eighth_add", "ninth_add"]
callback_remove_list = ["second_remove", "third_remove", "fourth_remove",
                        "fifth_remove", "sixth_remove", "seventh_remove", "eighth_remove",
                        "ninth_remove"]

# config_dict = {'id':1,'number': number_list, 'status': is_train}
# config_df = pd.DataFrame(config_dict)
filename_config = "user_config.csv"
filename_result = "user_result.csv"

try:
    config_df = pd.read_csv(filename_config, index_col=False)
    result_df = pd.read_csv(filename_result, index_col=False)
except:
    config_df = pd.DataFrame()
    result_df = pd.DataFrame()

right_message = f"""
✅ Right
"""


def wrong_message(x, y):
    text = f"""
❌❌❌❌❌
{x} * {y} = {x * y}
---------------
"""
    return text


@bot.message_handler(commands=['start'])
def start(message):
    if len(config_df.query('id == @message.from_user.id')) == 0:
        add_data_to_config(int(message.from_user.id))

    if len(result_df.query('id == @message.from_user.id')) == 0:
        add_result_new_user(int(message.from_user.id))
    bot.send_message(message.chat.id, "<b>Привет</b>", parse_mode='html')
    config(message)


@bot.message_handler(commands=['test'])
def start_test(message):
    suitable_number_list = config_df.query('id == @message.from_user.id & status == True').number.to_list()
    if len(suitable_number_list) == 0:
        suitable_number_list = config_df.query('id == @message.from_user.id').number.to_list()

    number_list = []
    for i in range(len(suitable_number_list)):
        number_list.append(symbol_list[suitable_number_list[i] - 2])

    list_of_nymber_text = ' '.join(number_list)

    mess = f"""
Тренируем примеры на:
{list_of_nymber_text}

<b>Поехали, желаю удачи ...</b>
    """
    bot.send_message(message.chat.id, mess, parse_mode='html')
    new_example(message)


@bot.message_handler(commands=['config'])
def config(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    zerro_button = types.KeyboardButton(text='Тренироваться')
    first_button = types.KeyboardButton(text='Добавить число')
    second_button = types.KeyboardButton(text='Убрать число')
    third_button = types.KeyboardButton(text='Статистика')

    markup.add(zerro_button, third_button, first_button, second_button)
    bot.send_message(message.chat.id, "Приступим...", reply_markup=markup)


@bot.message_handler(commands=['reset'])
def reset(message):
    global result_df
    result_df.loc[(result_df.id == message.from_user.id), 'number_right'] = 0
    result_df.loc[(result_df.id == message.from_user.id), 'number_right_last'] = 0
    result_df.loc[(result_df.id == message.from_user.id), 'number_wrong'] = 0
    result_df.to_csv(filename_result, index=False)
    bot.send_message(message.chat.id, "Статистика обнулена")

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, f"{create_table()}")

@bot.message_handler(commands=['add'])
def add_number(message):
    markup = types.InlineKeyboardMarkup([create_button_add(message.from_user.id)])
    add_all_button = types.InlineKeyboardButton(text="Добавить все",
                                                callback_data="add_all_number",
                                                resize_keyboard=True)
    markup.add(add_all_button)
    bot.send_message(message.chat.id, "На какую цифру добавим примеры?", reply_markup=markup)


def remove_number(message):
    markup = types.InlineKeyboardMarkup([create_button_remove(message.from_user.id)])
    remove_all_button = types.InlineKeyboardButton(text="Убрать все",
                                                   callback_data="remove_all_number",
                                                   resize_keyboard=True)
    markup.add(remove_all_button)
    bot.send_message(message.chat.id, "На какую цифру уберем примеры?", reply_markup=markup)


@bot.callback_query_handler(func=lambda c: True)
def answer(c):
    cid = c.message.chat.id
    keyboard = types.InlineKeyboardMarkup()

    if c.data in callback_add_list:
        try:
            index = callback_add_list.index(c.data)
        except:
            index = 0
        bot.send_message(cid, f'Были добавлены примеры на {symbol_list[index]}', reply_markup=keyboard)
        config_df.loc[((config_df.id == c.message.chat.id) & (config_df.number == (index + 2))), 'status'] = True
        config_df.to_csv(filename_config, index=False)

    elif c.data in callback_remove_list:
        try:
            index = callback_remove_list.index(c.data)
        except:
            index = 0
        bot.send_message(cid, f'Были убраны примеры на{symbol_list[index]}', reply_markup=keyboard)
        config_df.loc[((config_df.id == c.message.chat.id) & (config_df.number == (index + 2))), 'status'] = False
        config_df.to_csv(filename_config, index=False)

    elif c.data == "add_all_number":
        bot.send_message(cid, f'Тренируем примеры на все числа', reply_markup=keyboard)
        config_df.loc[config_df.id == c.message.chat.id, 'status'] = True
        config_df.to_csv(filename_config, index=False)

    elif c.data == "remove_all_number":
        bot.send_message(cid, f'Все числа убраны из тестов', reply_markup=keyboard)
        config_df.loc[config_df.id == c.message.chat.id, 'status'] = False
        config_df.to_csv(filename_config, index=False)


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    global x, y, config_df
    if message.text == "Тренироваться":
        start_test(message)
    elif message.text == "Добавить число":
        try:
            add_number(message)
        except:
            if len(config_df.query('id == @message.from_user.id')) == 0:
                add_data_to_config(int(message.from_user.id))
    elif message.text == "Убрать число":
        try:
            remove_number(message)
        except:
            if len(config_df.query('id == @message.from_user.id')) == 0:
                add_data_to_config(int(message.from_user.id))

    elif message.text.lower() == "помощь":
        help(message)

    elif message.text == "Статистика":
        user_statistic = calculate_statistic(message.from_user.id)
        if len(user_statistic) > 0:
            text = (
                '\n'.join(user_statistic.apply(lambda row:
                                               f"{symbol_list[number_list.index(row.x)]} ✅ - {row.rate}% (🏁 {row.progress}%)"
                                               , axis=1)
                          .to_list())
            )
            mess = f"""
        {text}
            """
        else:
            mess = "Нехватает данных, для формирования статистики"
        bot.send_message(message.chat.id, mess)

    elif message.text == str(x * y):
        try:
            result_df.loc[((result_df.id == message.from_user.id)
                           & (result_df.x == x)
                           & (result_df.y == y)), 'number_right'] += 1
            result_df.loc[((result_df.id == message.from_user.id)
                           & (result_df.x == x)
                           & (result_df.y == y)), 'number_right_last'] += 1
            result_df.to_csv(filename_result, index=False)
        except:
            if len(result_df.query('id == @message.from_user.id')) == 0:
                add_result_new_user(int(message.from_user.id))

        bot.send_message(message.chat.id, right_message, parse_mode='html')
        if message.date % 10 in [0, 9]:
            calculate_end(message)
        new_example(message)
    else:
        try:
            result_df.loc[((result_df.id == message.from_user.id)
                           & (result_df.x == x)
                           & (result_df.y == y)), 'number_wrong'] += 1
            result_df.loc[((result_df.id == message.from_user.id)
                           & (result_df.x == x)
                           & (result_df.y == y)), 'number_right_last'] = 0
            result_df.to_csv(filename_result, index=False)
        except:
            if len(result_df.query('id == @message.from_user.id')) == 0:
                add_result_new_user(int(message.from_user.id))

        bot.send_message(message.chat.id, wrong_message(x, y), parse_mode='html')
        new_example(message)


def new_example(message):
    global x, y
    if len(config_df.query('id == @message.from_user.id')) == 0:
        add_data_to_config(int(message.from_user.id))

    suitable_number_list = (
        config_df.query('id == @message.from_user.id & status == True').
            number.to_list()
    )
    if len(suitable_number_list) != 0:
        x, y = create_x_y(int(message.from_user.id))
    else:
        x = random.randint(2, 9)
        y = random.randint(2, 9)

    bot.send_message(message.chat.id, f"{x} * {y} = ?", parse_mode='html')


def add_data_to_config(id):
    global config_df
    user_config_dict = {'id': id, 'number': number_list, 'status': is_train}
    user_config_df = pd.DataFrame(user_config_dict)
    config_df = pd.concat([config_df, user_config_df])
    config_df.drop_duplicates(subset=['id', 'number'], keep='first', inplace=True)
    config_df.to_csv(filename_config, index=False)


def create_button_add(user_id):
    suitable_number_list = config_df.query('id == @user_id & status == False')['number'].to_list()
    result_list = []
    for i in range(len(suitable_number_list)):
        result_list.append(types.
                           InlineKeyboardButton(text=symbol_list[suitable_number_list[i] - 2],
                                                callback_data=callback_add_list[suitable_number_list[i] - 2],
                                                resize_keyboard=False))
    return result_list


def create_button_remove(user_id):
    suitable_number_list = config_df.query('id == @user_id & status == True')['number'].to_list()
    result_list = []
    for i in range(len(suitable_number_list)):
        result_list.append(types.
                           InlineKeyboardButton(text=symbol_list[suitable_number_list[i] - 2],
                                                callback_data=callback_remove_list[suitable_number_list[i] - 2],
                                                resize_keyboard=False))
    return result_list


def add_result_new_user(user_id):
    global result_df
    x_dict = {'id': user_id, 'x': number_list}
    x_df = pd.DataFrame(x_dict)
    y_dict = {'id': user_id, 'y': number_list, 'number_right': 0, 'number_wrong': 0, 'number_right_last': 0}
    y_df = pd.DataFrame(y_dict)
    result_new_user = x_df.merge(y_df, on="id")
    result_df = pd.concat([result_df, result_new_user])
    result_df.drop_duplicates(subset=['id', 'x', 'y'], keep='first', inplace=True)
    result_df.to_csv(filename_result, index=False)


def calculate_statistic(user_id):
    user_results = result_df.loc[result_df.id == user_id]
    # user_results['rate'] = (
    #     user_results.
    #         apply(lambda row: int(row.number_right * 100 / (row.number_right + row.number_wrong))
    #     if (((row.number_right + row.number_wrong) != 0) & (row.number_right_last < 3))
    #     else 100 if row.number_right_last >= 3
    #     else 0, axis=1)
    # )
    user_results.loc[:, 'rate'] = (
        user_results.
            apply(lambda row: int(row.number_right * 100 / (row.number_right + row.number_wrong))
        if (((row.number_right + row.number_wrong) != 0) & (row.number_right_last < 3))
        else 100 if ((row.number_right_last >= 3) | (row.number_right + row.number_wrong == 0))
        else 0, axis=1)
    ).astype("int")

    user_results.loc[:, 'progress'] = (
        user_results.
            apply(lambda row: int(row.number_right_last / 3 * 100) if row.number_right_last < 3
        else 100 if row.number_right_last >= 3
        else 0, axis=1)
    ).astype("int")

    user_statistic1 = (
        user_results.query('number_right + number_wrong != 0').
            groupby('x', as_index=False).
            agg({'rate': 'mean'})
    )

    user_statistic2 = (
        user_results.  # query('number_right + number_wrong != 0').
            groupby('x', as_index=False).
            agg({'progress': 'mean'})
    )
    user_statistic = user_statistic1.merge(user_statistic2, on="x")

    user_statistic.loc[:, 'rate'] = round(user_statistic.loc[:, 'rate'], 0).astype("int")
    user_statistic.loc[:, 'progress'] = round(user_statistic.loc[:, 'progress'], 0).astype("int")
    return user_statistic


def create_x_y(user_id):
    global repeat_flag
    is_ok = True
    current_data = (
        result_df.
            merge(config_df.
                  loc[(config_df.loc[:, 'id'] == user_id) & (config_df.loc[:, 'status'] == True)],
                  left_on=['id', 'x'],
                  right_on=['id', 'number'])
    )

    if repeat_flag:
        current_data_type = current_data.loc[(current_data.loc[:, 'number_right_last'] < 4)
                                             & (current_data.loc[:, 'number_wrong'] == 0)]
        if len(current_data_type) == 0:
            is_ok = False
        else:
            attempt = current_data_type.sample()
            repeat_flag = False if repeat_flag else True
            return int(attempt.x.values), int(attempt.y.values)

    if (not repeat_flag) | (not is_ok):
        current_data_type = current_data.loc[(current_data.loc[:, 'number_right_last'] < 4)
                                             & (current_data.loc[:, 'number_wrong'] > 0)]
        repeat_flag = False if repeat_flag else True
        if len(current_data_type) == 0:
            attempt = current_data.sample()
            return int(attempt.x.values), int(attempt.y.values)
        else:
            attempt = current_data_type.sample()
            return int(attempt.x.values), int(attempt.y.values)


def calculate_end(message):
    current_data = (
        result_df.
            merge(config_df.
                  loc[(config_df.loc[:, 'id'] == message.from_user.id)
                      & (config_df.loc[:, 'status'] == True)],
                  left_on=['id', 'x'],
                  right_on=['id', 'number'])
    )
    if len(current_data.loc[current_data.loc[:, 'number_right_last'] <= 3]) == 0:
        mess = """
🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵

Предлагаю закончить тренировку
Твоя оценка 5+

🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇🥇     
        """
        bot.send_message(message.chat.id, mess)

def create_table():
    list_ = []
    for i in range(2, 10):
        list_.append(f"       ")
        list_.append(f"Таблица умножения на {i}")
        list_.append(f"______________________")
        for j in range(2, 10):
            list_.append(f"{i} * {j} = {j*i}")
    text = (
        '\n'.join(list_)
    )
    return text


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    bot.polling(none_stop=True)



