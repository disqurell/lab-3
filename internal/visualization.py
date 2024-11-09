# cspell:ignore barplot boxplot set_xlabel histplot figsize set_ylabel axhline arange

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def plot_all(data):
    hours_data, service_times, readers_in_room, librarian_load = data

    # Создаем общую фигуру с несколькими подграфиками
    fig, axs = plt.subplots(2, 2, figsize=(14, 10))

    # Устанавливаем начальный час для графиков
    start_hour = 9
    hours_range = np.arange(start_hour, start_hour + len(hours_data))

    # 1. Количество обслуженных библиотекарем читателей в час (столбчатая диаграмма)
    sns.barplot(x=hours_range, y=hours_data, ax=axs[0, 0])
    axs[0, 0].set_xlabel("Час (ч)")
    axs[0, 0].set_ylabel("Обслуженные читатели")
    axs[0, 0].set_title("Количество обслуженных читателей в час")

    # 810.3850813798157 сек = 810.3850813798157 // 3600 ч
    # 810.3850813798157 сек = (810.3850813798157 // 60) - (810.3850813798157 // 3600 * 60)

    # 2. Среднее время обслуживания читателей у библиотекаря (перевод в часы)
    service_times_hours = [
        (
            f"{int(time // 3600)} ч. {int((time % 3600) // 60)} мин."
            if time >= 3600
            else f"{int((time % 3600) // 60)} мин."
        )
        for time in service_times
    ]

    print(service_times_hours)
    sns.boxplot(data=service_times_hours, ax=axs[0, 1])
    axs[0, 1].set_xlabel("Среднее время обслуживания (мин)")
    axs[0, 1].set_title("Среднее время обслуживания")

    # 3. Среднее количество читателей в читальном зале в час
    sns.barplot(x=hours_range, y=readers_in_room, ax=axs[1, 0])
    axs[1, 0].set_xlabel("Час (ч)")
    axs[1, 0].set_ylabel("Среднее количество людей")
    axs[1, 0].set_title("Среднее количество читателей в читальном зале в час")

    # 4. Загруженность библиотекаря (в процентах)
    hours_range = np.arange(start_hour - 1, start_hour + len(hours_data) + 1)

    axs[1, 1].plot(hours_range, librarian_load, label="Загрузка", marker="o")
    axs[1, 1].set_xlabel("Час (ч)")
    axs[1, 1].set_ylabel("Загруженность (%)")
    axs[1, 1].set_title("Загруженность библиотекаря со временем")
    axs[1, 1].legend()

    # Расстояние между графиками
    plt.tight_layout()
    plt.show()
