class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)  # ✅ округляем сразу
        self.count_of_ratings = count_of_ratings

    def _needed_diff(self, car: Car) -> int:
        """Возвращает, насколько нужно очистить машину (0, если уже чистая)."""
        return max(self.clean_power - car.clean_mark, 0)

    def calculate_washing_price(self, car: Car) -> float:
        """Вычисляет стоимость мойки для одной машины."""
        diff = self._needed_diff(car)
        if diff == 0:
            return 0.0
        # ✅ исправленный стиль — без переноса строки с оператором
        price = car.comfort_class * diff * self.average_rating / self.distance_from_city_center
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        """Моет одну машину, если нужно."""
        if car.clean_mark < self.clean_power:
            car.clean_mark = sel_
