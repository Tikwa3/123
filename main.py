meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное"
            }
world = input("Введите непонятное слово(большими буквами)")
if world in meme_dict.keys():
    print(meme_dict[world])
else:
    print("Такого слова пока что нет")
        
