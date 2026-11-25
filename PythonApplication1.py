from models import Bicycle, Bus, Car, ElectricCar, Transport


def show_transports(transports: list[Transport], distance: float = 100.0) -> None:
    for item in transports:
        time_hours = item.move(distance)
        fuel = item.fuel_consumption(distance)
        print(
            f"{item.info()} | На {distance:.0f} км: час = {time_hours:.2f} год, "
            f"пальне = {fuel:.2f}"
        )


def main() -> None:
    transports: list[Transport] = [
        Car("Toyota Corolla", 90, 5),
        Bus("Mercedes Sprinter", 70, 20, passengers=25),
        Bicycle("Trek Marlin", 35, 1),
        ElectricCar("Tesla Model 3", 110, 5),
    ]
    show_transports(transports, 100.0)


if __name__ == "__main__":
    main()
