# cspell:ignore barplot boxplot set_xlabel histplot figsize set_ylabel axhline arange
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def plot_all(data):
    hours_data, service_times, readers_in_room, librarian_load = data

    # Создаем общую фигуру с несколькими подграфиками
    fig, axs = plt.subplots(2, 2, figsize=(14, 10))

    # 1. Количество обслуженных библиотекарем читателей в час (столбчатая диаграмма)
    sns.barplot(x=np.arange(len(hours_data)), y=hours_data, ax=axs[0, 0])
    axs[0, 0].set_xlabel("Час (ч)")
    axs[0, 0].set_ylabel("Обслуженные читатели")
    axs[0, 0].set_title("Количество обслуженных читателей в час")

    # 2. Среднее время обслуживания читателей у библиотекаря (boxplot)
    sns.boxplot(data=service_times, ax=axs[0, 1])
    axs[0, 1].set_xlabel("Время обслуживания (с)")
    axs[0, 1].set_title("Среднее время обслуживания")

    # 3. Среднее количество читателей в читальном зале в час (гистограмма на каждый час)
    sns.barplot(x=np.arange(len(readers_in_room)), y=readers_in_room, ax=axs[1, 0])
    axs[1, 0].set_xlabel("Час (ч)")
    axs[1, 0].set_ylabel("Среднее количество людей")
    axs[1, 0].set_title("Среднее количество читателей в читальном зале в час")

    # 4. Загруженность библиотекаря (в долях)
    axs[1, 1].plot(librarian_load, label="Загрузка", marker="o")
    axs[1, 1].axhline(y=0, color="grey", linestyle="--")  # Линия на уровне 0
    axs[1, 1].set_xlabel("Час (ч)")
    axs[1, 1].set_ylabel("Загруженность (%)")
    axs[1, 1].set_title("Загруженность библиотекаря со временем")
    axs[1, 1].legend()

    # Расстояние между графиками
    plt.tight_layout()
    plt.show()
