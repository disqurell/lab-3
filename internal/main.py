import random
from operators import Reader, Librarian
from visualization import plot_all
import config


def simulate_library():
    librarian = Librarian()
    hours_data = []
    service_times = []
    readers_in_room = []
    librarian_load = []

    for hour in range(config.HOURS_TO_SIMULATE):
        print(f"Текущий час: {hour}")
        readers_this_hour = random.randint(config.MIN_READERS_PER_HOUR, config.MAX_READERS_PER_HOUR)
        readers_in_room.append(readers_this_hour)
        served_this_hour = 0
        total_service_time = 0
        free_time = 0
        current_hour_time = 0

        for _ in range(readers_this_hour):
            priority = random.randint(*config.PRIORITY_RANGE)
            service_time = random.uniform(*config.SERVICE_TIME_RANGE)
            reader = Reader(name=f"Reader_{_}", priority=priority, service_time=service_time)
            librarian.add_reader(reader)

        # Моделирование часа работы библиотеки
        while current_hour_time < 3600:  # 1 час = 3600 секунд
            if not librarian.queue.empty():
                librarian.serve_reader()
                served_this_hour += 1
                total_service_time += librarian.current_time
                current_hour_time += librarian.current_time  # Учитываем время обслуживания
            else:
                # Если очередь пуста, библиотекарь ожидает
                idle_time = 10  # Например, проверяет раз в 10 секунд, свободен ли он
                free_time += idle_time
                current_hour_time += idle_time

        # Записываем данные для анализа
        hours_data.append(served_this_hour)
        avg_service_time = total_service_time / served_this_hour if served_this_hour else 0
        service_times.append(avg_service_time)
        librarian_load.append((3600 - free_time) / 36)  # Процент загруженности за час

    # Добавляем 0% загрузки в начале и конце, чтобы график начинался и заканчивался на 0%
    librarian_load.insert(0, 0)
    librarian_load.append(0)

    # Визуализация всех графиков на одной странице
    plot_all((hours_data, service_times, readers_in_room, librarian_load))


if __name__ == "__main__":
    simulate_library()
