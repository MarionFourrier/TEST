# Function that takes 2 parameters : temperature and rain
    # If temperature under 12 :
        # Print "Take a coat !"
    # If temperature between 12 and 19 :
        # Print "Take a pull !"
    # If temperature strictly superior to 19 :
         # Print "Just put on a T-shirt !"
    # If weather is rainy :
        # Print "Take a coat !" anyway

def get_dressed(temperature, rain = "NO"):
    """
    Function that indicates how to dress according to the weather
    :param temperature: outdoor temperature in °C
    :param pluie: 'YES' if rainy, 'NO' if not
    :return: A sentence that indicates how to dress
    """
    if temperature < 12 or rain == "YES":
        cloth = "Take a coat !"
    elif temperature > 19 and rain == "NO":
        cloth = "Just put on a T-shirt !"
    else:
        cloth = "Take a pull !"
    return cloth