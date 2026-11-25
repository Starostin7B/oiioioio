from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self, name: str, speed: int, capacity: int) -> None:
        if not isinstance(name, str):
            raise TypeError("name must be str")
        if not isinstance(speed, int) or isinstance(speed, bool):
            raise TypeError("speed must be int")
        if not isinstance(capacity, int) or isinstance(capacity, bool):
            raise TypeError("capacity must be int")

        self.name = name
        self.speed = speed
        self.capacity = capacity

    @abstractmethod
    def move(self, distance: float) -> float:
        ...

    @abstractmethod
    def fuel_consumption(self, distance: float) -> float:
        ...

    @abstractmethod
    def info(self) -> str:
        ...

    def calculate_cost(self, distance: float, price_per_unit: float) -> float:
        return self.fuel_consumption(distance) * price_per_unit


class Car(Transport):
    def move(self, distance: float) -> float:
        return distance / self.speed

    def fuel_consumption(self, distance: float) -> float:
        return distance * 0.07

    def info(self) -> str:
        return f"Авто: {self.name}, швидкість: {self.speed} км/год, місткість: {self.capacity}"


class Bus(Transport):
    def __init__(self, name: str, speed: int, capacity: int, passengers: int = 0) -> None:
        super().__init__(name, speed, capacity)
        if not isinstance(passengers, int) or isinstance(passengers, bool):
            raise TypeError("passengers must be int")
        self.passengers = passengers

    def move(self, distance: float) -> float:
        return distance / self.speed

    def fuel_consumption(self, distance: float) -> float:
        return distance * 0.15

    def info(self) -> str:
        status = "Перевантажено!" if self.passengers > self.capacity else "В нормі"
        return (
            f"Автобус: {self.name}, швидкість: {self.speed} км/год, "
            f"пасажири: {self.passengers}/{self.capacity} ({status})"
        )


class Bicycle(Transport):
    MAX_SPEED = 20

    def __init__(self, name: str, speed: int, capacity: int = 1) -> None:
        super().__init__(name, speed, capacity)
        self.speed = min(self.speed, self.MAX_SPEED)

    def move(self, distance: float) -> float:
        return distance / self.speed

    def fuel_consumption(self, distance: float) -> float:
        return 0.0

    def info(self) -> str:
        return f"Велосипед: {self.name}, швидкість: {self.speed} км/год, місткість: {self.capacity}"


class ElectricCar(Car):
    def battery_usage(self, distance: float) -> float:
        return distance * 0.2

    def fuel_consumption(self, distance: float) -> float:
        return 0.0

    def info(self) -> str:
        return (
            f"Електромобіль: {self.name}, швидкість: {self.speed} км/год, "
            f"місткість: {self.capacity}"
        )
