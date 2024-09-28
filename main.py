import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import words
from skills import *

# Инициализация векторизатора и модели
vectorizer = CountVectorizer()
vectors = vectorizer.fit_transform(list(words.data_set.keys()))

clf = LogisticRegression()
clf.fit(vectors, list(words.data_set.values()))


def recognize(data, vectorizer, clf):
    trg = words.TRIGGERS.intersection(data.lower().split())
    if not trg:
        return "Я не нашел подходящей команды."

    for trigger in trg:
        data = data.replace(trigger, '').strip()

    if not data:
        return "Я не нашел подходящей команды после удаления триггера."

    text_vector = vectorizer.transform([data]).toarray()[0]
    answer = clf.predict([text_vector])[0]
    func_name = answer.split()[0]
    response = answer.replace(func_name, '').strip()

    if func_name in globals() and callable(globals()[func_name]):
        globals()[func_name]()

    return response


def main():
    print("Введите запрос:")
    while True:
        data = input("Вы: ")
        if data.lower() in ["выход", "exit"]:
            print("До свидания!")
            break
        response = recognize(data, vectorizer, clf)
        print("Бот:", response)


if __name__ == '__main__':
    main()