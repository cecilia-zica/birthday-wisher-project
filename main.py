import datetime as dt
import random
import pandas as pd
import smtplib

MYEMAIL = "seu_email@gmail.com"
PASSWORD = "sua_senha_de_app"

today = dt.datetime.now()
today_tuple = (today.month, today.day)

try:
    dataframe = pd.read_csv('birthdays.csv')
except FileNotFoundError:
    print("O arquivo 'birthdays.csv' não foi encontrado.")
    exit()

# Cria o dicionário de aniversários
birthdays_dict = {
    (row['month'], row['day']): row.to_dict()
    for (index, row) in dataframe.iterrows()
}

# Verifica se a data de hoje está no dicionário
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]['name']
    # Seleciona uma carta aleatoriamente
    letter_path = f"letter_templates/letter_{random.randint(1,3)}.txt"

    try:
        with open(letter_path) as letter_file:
            letter = letter_file.read()
            # Carta personalizada
            letter = letter.replace("[NAME]", birthday_person)

    except FileNotFoundError:
        print(f"O arquivo de carta '{letter_path}' não foi encontrado.")
        exit()

    # Envia o e-mail
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=MYEMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MYEMAIL,
            to_addrs=birthday_person['email'],
            msg=f"Subject:Happy Birthday!\n\n{letter}"
        )