import json
import urllib.request

################################################################################

file = "startup_cards.csv" # File the output is stored in
delimiter = "|" # What value to separate fields by (commas appear in card text)
api = "https://netrunnerdb.com/api/2.0/public/cards" # The source the card data

# The fields to include from each card
fields = ["title", "text", "cost", "strength", "trash_cost"]

################################################################################

def main():
    # Get the card data as a list of cards as dictionaries
    cards = json.loads(urllib.request.urlopen(api).read())["data"]

    # Data to include/exclude
    startup_pack_codes = ["sg", "su21", "df", "ur", "msbp"]
    non_startup_codes = ["30076", "30077"]

    # Filter by the above parameters, then format into a single string
    startup_cards = filter(lambda c : c["pack_code"] in startup_pack_codes and c["code"] not in non_startup_codes, cards)
    formatted = "\n".join(map(format, startup_cards))

    # Write that string to file
    f = open(file, "w")
    f.write(formatted)
    f.close()

    # Hello, World
    print("Data saved in " + file)
    print("Fields separated by " + delimiter)

################################################################################

# Formats an individual card into a single line of the output file
def format(card):
    s = ""
    for field in fields:
        if field in card: # If a field isn't present, leave it blank
            s += str(card[field]).replace("\n", " ").replace("\t", " ")
        s += delimiter
    return s[:-len(delimiter)] # Ignore the last delimiter

################################################################################

if __name__ == "__main__":
    main()
