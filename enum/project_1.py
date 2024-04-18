from enum import Enum
class Country(Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672
    iran=8500

print(Country.Afghanistan.value)
print(Country.iran.value)
print(Country.iran.name)