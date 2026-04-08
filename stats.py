import pandas as pd
import matplotlib.pyplot as plt
import os
from logs import logger
class Stats: # ого какое адекватное название
    def __init__(self, file_path):
        if not os.path.exists(file_path): # проверка на ∃-е файла
            raise FileNotFoundError(f"Файл {file_path} не найден")
        # открываем и читаем файлик
        self.df = pd.read_csv(file_path)
    @logger
    def plot(self): # 4 буквы и хватит
        # смотрим, съел ли кто колонки
        if 'country' not in self.df.columns or 'playerid' not in self.df.columns:
            print("В файле отсутствуют необходимые колонки")
            return
        # берем данные
        counts = self.df.groupby('country')['playerid'].count()
        # позорники в один столбик, потому что их много и из-за них график убожественный
        b_min = 1000 # базовый минимум, чтобы не быть позорником
        np_countries = counts[counts >= b_min] # типа не позорники
        others_count = counts[counts < b_min].sum()
        # отделение позорников от норм стран
        if others_count > 0:
            others_series = pd.Series({'Другие': others_count})
            counts = pd.concat([np_countries, others_series])
        else:
            counts = np_countries
        # (не)грустно убираем нули 
        minus0 = counts / 100_000 # буквально минус нули
        # сортировка чтобы было
        minus0 = minus0.sort_values(ascending=False)

        # рождение не пикми графика (найти название цвета было сложно)
        plt.figure(figsize=(12, 8))
        # делаем его чуть меньшим уродом, чем могли бы (лучше ему не стало)
        ax = minus0.plot(kind='bar', color='violet', edgecolor='purple', alpha=0.9)
        # великий и могучий русский на графике был необходим
        plt.title('Количество игроков по странам', fontsize=15, pad=20)
        plt.xlabel('Страна', fontsize=12)
        plt.ylabel('Игроков (в сотнях тысяч)', fontsize=12)
        
        plt.xticks(rotation=90, ha='center') 
        plt.grid(axis='y', linestyle='--', alpha=0.6)
        # текстовые метки над столбцами
        for i, val in enumerate(minus0):
            plt.text(i, val + 0.01, f'{val:.2f}', ha='center', fontsize=10) # карты сказали надо 10 писать

        plt.tight_layout()
        plt.show()
