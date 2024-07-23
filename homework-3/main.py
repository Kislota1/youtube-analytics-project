from src.channel import Channel

if __name__ == '__main__':
    # Создаем два экземпляра класса
    moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    highload = Channel('UCwHL6WHUarjGfUM_586me8w')

    # Используем различные магические методы
    print(moscowpython)  # 'MoscowPython (https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A)'
    print(moscowpython + highload)  # 100100 есть
    print(moscowpython - highload)  # -48300 есть
    print(highload - moscowpython)  # 48300
    print(moscowpython > highload)  # False есть
    print(moscowpython >= highload)  # False есть
    print(moscowpython < highload)  # True есть
    print(moscowpython <= highload)  # True есть
    print(moscowpython == highload)  # False есть
    
