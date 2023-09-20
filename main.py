import http
import random
from gettext import translation

import telebot
from chardet import detect
from telebot import types
from googletrans import Translator
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
from settings import BOT_TOKEN
bot = telebot.TeleBot(BOT_TOKEN)

recognizer = sr.Recognizer()


translator = Translator()
src = "ru"
dest = "en"


@bot.message_handler(func=lambda message: "переведи" in message.text.lower())
def handle_message(message):
    translated_message = translator.translate(message.text, dest='en')
    bot.send_message(message.chat.id, translated_message.text)


@bot.message_handler(func=lambda message: "translate" in message.text.lower())
def handle_message(message):
    translated_message = translator.translate(message.text, dest='ru')
    bot.send_message(message.chat.id, translated_message.text)


@bot.message_handler(func=lambda message: 'привет' in message.text.lower())
def send_welcome(message):
    bot.reply_to(message, 'Приветствую! Меня зовут Алекса, чем я могу помочь?')
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAP6ZQXUijPR2SlR4l2diMIz3VCE8J0AAowxAALV_DBIEWj40AXSpkIwBA')


@bot.message_handler(func=lambda message: 'как дела?' in message.text.lower())
def handle_hello(message):
    bot.reply_to(message, "Хорошо, спасибо!")
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIBEGUF232iya_5weRW5d3IbvEDyOhYAAL2MQAC1fwwSPqdhrR-15LYMAQ')


@bot.message_handler(func=lambda message: 'ты лучшая' in message.text.lower())
def handle_hello(message):
    bot.reply_to(message, "Спасибо!")
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIDL2UG7gdVySkk3Iwi7TltSdnuTTX6AAJgNgAC06w4SJsi7DYzuc40MAQ')


@bot.message_handler(func=lambda message: 'что ты умеешь?' in message.text.lower())
def handle_hello(message):
    bot.reply_to(message, "Я уникальный ассистент, котороый поможет справиться с любыми сложностями английского языка."
                          "Я умею:"
                          "-  переводить тексты с русского на английский и наоборот;"
                          "-  объяснять правила английского языка;"
                          "-  веселить тебя."
                 )


@bot.message_handler(func=lambda message: 'кто тебя создал?' in message.text.lower())
def handle_hello(message):
    bot.reply_to(message, "Моего создателя зовут Дарья")


@bot.message_handler(func=lambda message: 'объясни мне правило' in message.text.lower())
def send_welcome(message):
    bot.reply_to(message, 'Хорошо, какое првило вам объяснять?')


@bot.message_handler(func=lambda message: 'present simple' in message.text.lower())
def send_welcome(message):
    bot.reply_to(message, 'Present Simple – простое настоящее время. Оно показывает действие, которое происходит регулярно, с определенной периодичностью. На первый взгляд может показаться, что это время один в один похоже на наше настоящее время. И действительно, в большинстве случаев функции Present Simple и русского настоящего времени совпадают. Но различия все же есть.')
    with open('D:/presentsimple.jpg', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)


@bot.message_handler(func=lambda message: 'present continuous' in message.text.lower())
def send_welcome(message):
    bot.reply_to(message, 'Present Continuous Tense (Present Progressive Tense) – настоящее длительное время. В речи оно встречается так же часто, как и Present Simple. Главное, что надо знать о Present Continuous, – это время показывает длительность действия в настоящем. Длительность может проявляться по-разному: действие может продолжаться недолго, а может занимать большой промежуток времени.')
    with open('D:/continuous.jpg', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)


@bot.message_handler(func=lambda message: 'past simple' in message.text.lower())
def send_welcome(message):
    bot.reply_to(message, 'Past Simple (простое прошедшее) – одно из самых распространенных времен в английском языке. С помощью Past Simple мы можем передать события, происходившие в прошлом. Прошу заметить, что в данном времени используются глаголы во второй форме. Существуют правильные и неправильные глаголы. К правильным добавляем окончание -ed, неправильные - запоминаем. (!) В отрицательных и вопросительных предложениях глагол остается в первой форме.')
    with open('D:/pastsimple.jpg', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)


@bot.message_handler(func=lambda message: 'давай поговорим о сериалах?' in message.text.lower())
def handle_hello(message):
    bot.reply_to(message, "Хорошо, какой твой любимый сериал?")


@bot.message_handler(func=lambda message: 'очень странные дела' in message.text.lower())
def start(message):
    quotation = ['"You shouldn’t like things because people tell you you’re supposed to."',
                 '"This is not yours to fix alone. You act like you’re all alone out there in the world, but you’re not. You’re not alone."',
                 '"Do you wanna be normal? Do you wanna be just like everyone else? Being a freak is the best. I’m a freak!"'
                 ]
    tell_quotation = random.choice(list(quotation))
    bot.reply_to(message, f"Вот цитата из твоего любимого сериала: {tell_quotation}")
    with open('D:/stranger.jpg', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)


@bot.message_handler(func=lambda message: 'ведьмак' in message.text.lower())
def start(message):
    quotation2 = ["'Fear Is An Illness. If You Leave It Untreated, It Can Consume You.'",
                 "'This World Doesn't Need A Hero. It Needs A Professional.'"
                 "You Can Do Anything. Doesn't Mean You Have To."
                 ]
    tell_quotation2 = random.choice(list(quotation2))
    bot.reply_to(message, f"Вот цитата из твоего любимого сериала: {tell_quotation2}")
    with open('D:/witcher.jpg', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)



@bot.message_handler(func=lambda message: 'игра престолов' in message.text.lower())
def start(message):
    quotation3 = ["Any man who must say 'I am the king' is no true king.",
                 "Never forget what you are. The rest of the world will not."
                 "When you play the game of thrones, you win or you die. There is no middle ground."
                 ]
    tell_quotation3 = random.choice(list(quotation3))
    bot.reply_to(message, f"Вот цитата из твоего любимого сериала: {tell_quotation3}")
    with open('D:/game_of_thrones.jpg', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)


@bot.message_handler(func=lambda message: 'расскажи мне какую-нибудь историю на английском' in message.text.lower())
def handle_hello(message):
    story = ['A curious child asked his mother: “Mommy, why are some of your hairs turning grey?" The mother tried to use this occasion to teach her child: “It is because of you, dear. Every bad action of yours will turn one of my hairs grey!" The child replied innocently: “Now I know why grandmother has only grey hairs on her head."',
             'A police officer found a perfect hiding place for watching for speeding motorists. One day, the officer was amazed when everyone was under the speed limit, so he investigated and found the problem. A 10 years old boy was standing on the side of the road with a huge hand painted sign which said “Radar Trap Ahead.” A little more investigative work led the officer to the boy’s accomplice: another boy about 100 yards beyond the radar trap with a sign reading “TIPS” and a bucket at his feet full of change.',
             'The class teacher asks students to name an animal that begins with an “E”. One boy says, “Elephant.” Then the teacher asks for an animal that begins with a “T”. The same boy says, “Two elephants.” The teacher sends the boy out of the class for bad behavior. After that she asks for an animal beginning with “M”. The boy shouts from the other side of the wall: “Maybe an elephant!”'
             ]
    tell_story = random.choice(list(story))
    bot.reply_to(message, f"Вот история на английском: {tell_story}")


@bot.message_handler(func=lambda message: 'пока' in message.text.lower())
def send_welcome(message):
    bot.reply_to(message, 'Всего доброго!')
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIBFGUF28DQzjQgJPOeoiMeU3NGqYuhAAL5MQAC1fwwSOLIGkCbKmMeMAQ')


@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):
    print(message.sticker.file_id)


@bot.message_handler(commands=['play'])
def start(message):
    bot.reply_to(message,
                 "Welcome to the English Word Game! I will give you a word and you have to guess the correct translation. Let's get started!")
    play_game(message)


def play_game(message):
    global translation

    word_dict = {
        'apple': 'яблоко',
        'cat': 'кошка',
        'dog': 'собака',
        'tree': 'дерево',
        'airplane': 'самолет',
        'to go': 'идти',
        'to speak': 'говорить',
        'air': 'воздух',
        'sea': 'море',
        'flower': 'цветок',
        'morning': 'утро',
        'fire': 'огонь',
        'bird': 'птица',
        'fish': 'рыба',
        'world': 'мир',
        'family': 'семья',
        'mother': 'мама',
        'father': 'папа',
        'love': 'любовь',
        'to begin': 'начинать',
        'education': 'образование',
        'to abate': 'сокращать',
        'to dangle': 'зависать',
        'to diminish': 'уменьшать',
        'discerning': 'распознавание',
        'oversight': 'надзор',
        'unveiling': 'разоблачение',
        'addiction': 'зависимость',
        'confidence': 'уверенность',
        'craving': 'тяга',
        'fervor': 'рвение',
        'to define': 'определить',
        'attractive': 'привлекательный',
        'boring': 'скучный',
        'to overwhelm': 'переполнять',
        'accolade': 'награда',
        'workforce': 'рабочая сила',
        'lifelong': 'пожизненный',
        'lucrative': 'выгодный',
        'savvy': 'проницательный',
        'elusive': 'неуловимый',
        'luxurious': 'роскошный',
        'feasible': 'ощутимый',
        'unavoidable': 'неизбежный',
        'disastrous': 'катастрофический',
        'existence': 'существование'
    }

    word = random.choice(list(word_dict.keys()))
    translation = word_dict[word]

    bot.send_message(message.chat.id, f"Translate the word: {word}")


@bot.message_handler(func=lambda message: True)
def check_translation(message):
    global translation

    user_translation = message.text.lower()
    if user_translation == translation:
        bot.reply_to(message, "Correct! You guessed the translation.")
    elif user_translation == "хватит":
        return bot.reply_to(message, "Хорошо, спасибо за игру!"), bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIDJWUG7J8nnlR6ss1VFT_P4OfN2acaAAI8NgAC06w4SNzY9-JQwoytMAQ')
    else:
        bot.reply_to(message, f"Wrong! The correct translation is: {translation}.")

    play_game(message)


@bot.message_handler(commands=['quiz'])
def quiz(message):
    global questions
    questions = {
        "Какой столицей является Москва?": "Москва",
        "Какого цвета яблоко?": "Зеленое",
        "Кто изображен на долларовой купюре США?": "Джордж Вашингтон"
    }
    question = list(questions.keys())[0]
    bot.reply_to(message, question)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    global questions
    current_question = list(questions.keys())[0]
    correct_answer = questions[current_question]
    if message.text.lower() == correct_answer.lower():
        bot.reply_to(message, "Верно!")
    else:
        bot.reply_to(message, "Неправильно!")
    del questions[current_question]
    if questions:
        next_question = list(questions.keys())[0]
        bot.reply_to(message, next_question)
    else:
        bot.reply_to(message, "Викторина завершена!")


@bot.message_handler(commands=['search'])
def search(message):
    query = message.text.split(' ', 1)[1]
    response = requests.get(f'https://www.google.com/search?q={query}')
    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.select('.r a')
    titles = [result.text for result in results]
    bot.reply_to(message, '\n'.join(titles))


bot.polling()
