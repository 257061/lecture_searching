import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)  # spojuje dvě cesty dohromady, ke konkrétnímu adresáři

    allowed_fields = {"unordered_numbers", "ordered_numbers", "dna_sequence"}    # množina narozdíl od slovníku nemá klíče, pouze hodnoty
    # Funkce ověří, že zadaný klíč pochází z množiny povolených řešení (viz soubor
    # "sequential.json"). Pokud ne, funkce vrátí hodnotu None
    if field not in allowed_fields:
        return None

    # Funkce pomocí modulu json načte *.json soubor ve formě slovníku. Funkce vrátí
    # hodnoty uložené pod klíčem definovaným druhým vstupním parametrem (field).
    with open(file_path, "r") as file:
        data = json.load(file)   # pokud načítám ze stringu používám loads()
    print(data)  # s odsazením, protože se ten print provádí až je ten soubor zase zavřený
    return data[field]  # ze slovníku vybereme správnou hodnotu podle klíče "field"


# Funkci read_data() zavolejte z hlavní funkce se vstupním argumentem
# "sequential.json" a "unordered_numbers".
def main():
    numbers = read_data("sequential.json", "unordered_numbers")
    print(numbers)





if __name__ == '__main__':
    main()