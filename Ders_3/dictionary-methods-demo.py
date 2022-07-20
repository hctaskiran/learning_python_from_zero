'''
    player 1:
        id: 1
        name: cristiano ronaldo
        yearOfBirth: 1985
        nationality: Portug=al
        current_team: Portugal
        history: Juventus, Real Madrid, Portugal

    player 2
        id: 2
        name: lionel messi
        yearOfBirth: 1987
        nationality: Argentina
        current_team: Barcelona
        history: Barcelona, Argentina, Portugal
'''
#  Yukarıda verilen bilgileri liste içine ekle




players = {
    '1': 
        {
            'name': 'Cristiano Ronaldo', 'yearOfBirth': '1985', 'nationality': 'Portugal', 'current_team': 'Portugal', 'history': ['Juventus', ' Real Madrid', ' Portugal']
        }, 
    '2': 
        {
            'name': 'Lionel Messi', 'yearOfBirth': '1987', 'nationality': 'Argentina', 'current_team': 'Barcelona', 'history': ['Barcelona', ' Argentina', ' Portugal']}
        }

# id = input("Oyuncu Id: ")
# name = input("Oyuncu adı: ")
# nationality = input("Milliyeti: ")
# yearOfBirth = input("Doğum yılı: ")
# current_team = input("Takım: ")
# history = input("Geçmiş: ")

# players.update({
#     id: {
#         "name": name,
#         "yearOfBirth": yearOfBirth,
#         "nationality": nationality,
#         "current_team": current_team,
#         "history": history.split(",")
#     }
# })


# id = input("Oyuncu Id: ")
# name = input("Oyuncu adı: ")
# nationality = input("Milliyeti: ")
# yearOfBirth = input("Doğum yılı: ")
# current_team = input("Takım: ")
# history = input("Geçmiş: ")

# players.update({
#     id: {
#         "name": name,
#         "yearOfBirth": yearOfBirth,
#         "nationality": nationality,
#         "current_team": current_team,
#         "history": history.split(",")
#     }
# })

#  id'e göre arama yap

id = input("aramak istediğiniz oyuncu id: ")
player = players.get(id)
print(f'name: {player.get("name")}')

#  id'e göre bilgi kayıt sil
id = input("silmek istediğiniz id: ")
players.pop(id)


# print(players)