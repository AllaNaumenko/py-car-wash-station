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
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def _needed_diff(self, car: Car) -> int:
        """Возвращает, насколько нужно очистить машину (0, если уже чистая)."""
        return max(self.clean_power - car.clean_mark, 0)

    def calculate_washing_price(self, car: Car) -> float:
        """Вычисляет стоимость мойки для одной машины."""
        diff = self._needed_diff(car)
        if diff == 0:
            return 0.0
        price = car.comfort_class * diff * self.average_rating / self.distance_from_city_center
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        """Моет одну машину, если это нужно."""
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power  # ✅ исправлено: теперь корректное присваивание

    def serve_cars(self, cars: list[Car]) -> float:
        """Моет все подходящие машины и возвращает доход станции."""
        total_income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                price = self.calculate_washing_price(car)
                total_income += price
                self.wash_single_car(car)
        return round(total_income, 1)  # ✅ добавлено округление, как требует задание

    def rate_service(self, new_rating: float) -> None:
        """Добавляет новый рейтинг и пересчитывает средний."""
        total_rating = self.average_rating * self.count_of_ratings + new_rating
        self.count_of_ratings += 1
        self.average_rating = round(total_rating / self.count_of_ratings, 1)
