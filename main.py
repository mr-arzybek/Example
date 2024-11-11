from abc import ABC, abstractmethod

class Room(ABC):
    def __init__(self, features, price):
        self._features = features
        self.__price = price

    @abstractmethod
    def get_price(self):
        pass

    @abstractmethod
    def get_features(self):
        pass


class StandardRoom(Room):
    def __init__(self, features, price):
        super().__init__(features, price)

    def get_price(self):
        return self._Room__price

    def get_features(self):
        return self._features


class LuxuryRoom(Room):
    def __init__(self, features, price):
        super().__init__(features, price)

    def get_price(self):
        return self._Room__price

    def get_features(self):
        return self._features


class FamilyRoom(Room):
    def __init__(self, features, price):
        super().__init__(features, price)

    def get_price(self):
        return self._Room__price

    def get_features(self):
        return self._features


class WiFiService:
    def get_wifi_description(self):
        return "Быстрый Wi-Fi по всему отелю."


class BreakfastService:
    def get_breakfast_description(self):
        return "Шведский стол только со свежими продуктами."


class LuxuryRoomWithServices(LuxuryRoom, WiFiService, BreakfastService):
    def __init__(self, features, price):
        LuxuryRoom.__init__(self, features, price)
        WiFiService.__init__(self)
        BreakfastService.__init__(self)

    def get_features(self):
        features = super().get_features()
        features.append(self.get_wifi_description())
        features.append(self.get_breakfast_description())
        return features


class FamilyRoomWithWiFi(FamilyRoom, WiFiService):
    def __init__(self, features, price):
        FamilyRoom.__init__(self, features, price)
        WiFiService.__init__(self)

    def get_features(self):
        features = super().get_features()
        features.append(self.get_wifi_description())
        return features


def print_room_info(room):
    print(f"Цена: {room.get_price()}$")
    print("Удобства:")
    for feature in room.get_features():
        print(f"- {feature}")
    print(

    )


wifi_service = WiFiService()
breakfast_service = BreakfastService()

standard_room = StandardRoom(features=["Кровать", "Телевизор", "Мини-бар"], price=100)
luxury_room = LuxuryRoom(features=["Кровать King-size", "Телевизор 4K", "Спа-ванна", "Мини-бар"], price=200)
family_room = FamilyRoom(features=["Кровать King-size", "Две кровати", "Детская зона", "Телевизор"], price=125)
luxury_room_with_services = LuxuryRoomWithServices(features=["Кровать King-size", "Телевизор 4K", "Спа-ванна", "Мини-бар"], price=250)
family_room_with_services = FamilyRoomWithWiFi(features=["Кровать King-size", "Две кровати", "Детская зона", "Телевизор"], price=150)

print_room_info(standard_room)
print_room_info(luxury_room)
print_room_info(family_room)
print_room_info(luxury_room_with_services)
print_room_info(family_room_with_services)