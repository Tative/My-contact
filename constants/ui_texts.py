class ErrorInvalid:
    #Обязательны к заполнению
    FIRST_NAME_REQ = "firstName: Path `firstName` is required"
    LAST_NAME_REQ = "lastName: Path `lastName` is required"
    #Неверный формат
    BIRTHDATE = "birthdate: Birthdate is invalid"
    EMAIL = "email: Email is invalid"
    PHONE = "phone: Phone number is invalid"
    POSTAL_CODE = "postalCode: Postal code is invalid"
    #Максимальная длина
    FIRST_NAME_LONG = "firstName: Path `firstName`"
    LAST_NAME_LONG = "lastName: Path `lastName`"
    PHONE_LONG = "phone: Path `phone`"
    STREET1_LONG = "street1: Path `street1`"
    STREET2_LONG = "street2: Path `street2`"
    CITY_LONG  = "city: Path `city`"
    STATE_PROVINCE_LONG = "stateProvince: Path `stateProvince`"
    POSTAL_CODE_LONG = "postalCode: Path `postalCode`"
    COUNTRY_LONG = "country: Path `country`"