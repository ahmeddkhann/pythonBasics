def countryCode(country, area, first, last):
    return f"{country}{area}{first}{last}"

number = countryCode(country="1234-", first="097-", last="984", area="567-")
print(number)