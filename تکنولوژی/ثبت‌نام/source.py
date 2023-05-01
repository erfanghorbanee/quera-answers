def check_registration_rules(**userpass):

    for i in list(userpass):
        if (
            i == "quera"
            or i == "codecup"
            or len(i) < 4
            or len(userpass[i]) < 6
            or userpass[i].isnumeric() == True
        ):
            userpass.pop(i)

    return list(userpass)


# check_registration_rules(saeed='1234567', ab='afj$L12')
