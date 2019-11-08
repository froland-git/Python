def create_record(name, telephone, address):
    """Create record"""
    record = {
        "name_field": name,
        "telephone_field": telephone,
        "address_field": address
    }
    return(record)

user1 = create_record("Vasia", "+7123456789", "Moscow")

print(user1)

def give_award(medal, *persons):
    """Give Medals to persons"""
    for person in persons:
        print("Tovarish " + person.title() + " nagrajdaetsya medaliyu " + medal)

give_award("Za Berlin", "Vasia", "Petya")
give_award("Za London", "Petya", "Aleksandr", "Valintin")