import json
import csv
class CountryMedals:
    def __init__(self,name:str, gold:int,silver:int,bronze:int):
        self.name = name
        self.gold = gold
        self.silver = silver
        self.bronze = bronze
        self.total = self.gold + self.silver + self.bronze

    def to_json(self):
        data = {
            "name": self.name,
            "gold": self.gold,
            "silver": self.silver,
            "bronze": self.bronze,
            "total": self.total
        }
        return json.dumps(data,indent = 2)
# json information form https://docs.python.org/3/library/json.html
    def get_medals(self,medal_type:str):
        if medal_type == 'gold':
            return self.gold

        elif medal_type =='silver':
            return self.silver

        elif  medal_type == 'bronze':
            return self.bronze

        elif medal_type == 'total':
            return self.total
        else: return None

    def print_summary(self):
        return print(f"{self.name} received {self.total} medals in total;"
                     f" {self.gold} gold, {self.silver} silver, and {self.bronze} bronze")

    def compare(self, country_2):
        print_compare = f"Medals comparison between {self.name} and {country_2.name}:\n"
        if self.gold > country_2.gold: print_compare += (f"{self.name} received {self.gold} gold medal(s),"
                                                         f" {self.gold - country_2.gold} more than {country_2.name}, which received {country_2.gold}.\n")

        elif self.gold == country_2.gold: print_compare += f"Both {self.name} and {country_2.name} received {self.gold} gold medal(s)"

        else: print_compare += (f"{self.name} received {self.gold} gold medal(s),"
                             f" {country_2.gold - self.gold} less than {country_2.name}, which received {country_2.gold}.\n")

        if self.silver > country_2.silver: print_compare += (f"{self.name} received {self.silver} silver medal(s),"
                                                         f" {self.silver - country_2.silver} more than {country_2.name}, which received {country_2.silver}.\n")

        elif self.gold == country_2.gold: print_compare += f"Both {self.name} and {country_2.name} received {self.silver} silver medal(s)"

        else: print_compare += (f"{self.name} received {self.silver} silver medal(s),"
                             f" {country_2.silver - self.silver} less than {country_2.name}, which received {country_2.silver}.\n")

        if self.bronze > country_2.bronze: print_compare += (f"{self.name} received {self.bronze} bronze medal(s),"
                                                         f" {self.bronze - country_2.bronze} more than {country_2.name}, which received {country_2.bronze}.\n")

        elif self.gold == country_2.gold: print_compare += f"Both {self.name} and {country_2.name} received {self.bronze} bronze medal(s)"

        else: print_compare += (f"{self.name} received {self.bronze} bronze medal(s),"
                             f" {country_2.bronze - self.bronze} less than {country_2.name}, which received {country_2.bronze}.\n")

        if self.total > country_2.total: print_compare += (f"\nOverall {self.name} received {self.total} medal(s),"
                                                           f"{self.total - country_2.total} more than {country_2.name}, which received {country_2.total} medal(s)")

        elif self.gold == country_2.gold: print_compare += f"\nOverall Both {self.name} and {country_2.name} received {self.gold} medal(s)"

        else: print_compare += (f"\nOverall {self.name} received {self.total} medal(s),"
                                                           f"{country_2.total - self.total} less than {country_2.name}, which received {country_2.total} medal(s)")

        return print(print_compare)

############################
#Parsing the data https://docs.python.org/3/library/csv.html
############################
def parsing_the_data():
    countries = {}
    with open('medals.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row['Team/NOC']
            gold = int(row['Gold'])
            silver = int(row['Silver'])
            bronze = int(row['Bronze'])
            country = CountryMedals(name, gold, silver, bronze)
            countries[name] = country
    return countries
############################
#Creating functions to process the data
############################
def get_sorted_list_of_country_names(countries):
    return sorted(countries.keys())

def sort_countries_by_medal_type_ascending(countries, medal_type):
    if medal_type not in ['gold', 'silver', 'bronze', 'total']:
        print("medal_type error")
    country_list = list(countries.values())

    sorted_countries = sorted(country_list, key=lambda country: country.get_medals(medal_type)) #how to sort dictionary reference https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
    return sorted_countries

def sort_countries_by_medal_type_descending(countries, medal_type):
    if medal_type not in ['gold', 'silver', 'bronze', 'total']:
        print("medal_type error")
    country_list = list(countries.values())

    sorted_countries = sorted(country_list, key=lambda country: country.get_medals(medal_type), reverse = True)
    return sorted_countries

def read_positive_integer(prompt_sent:str):
    while True:
        input_integer = int(input(prompt_sent))
        if input_integer >= 0:
            return input_integer
        else: print(f"the value entered is not a positive integer, do it again")

def read_country_name(countries,prompt_sent:str):
    while True:
        input_country = input(prompt_sent)
        if input_country in countries.keys():
            return input_country
        else:
            print(f"the value entered is not a valid name\n"
                    f"Here is the list of country name\n")
            for country in countries.keys():
                print(country)

def read_medal_type(prompt_sent:str):
    valid_medal_types = ['gold', 'silver', 'bronze', 'total']
    while True:
        input_medal = input(prompt_sent)
        if input_medal in valid_medal_types:
            return input_medal
        else: print(f"the value entered is not a valid medal type")

############################
#Execution loop
############################

def user_command():

    country_data = parsing_the_data()
    valid_command = ['H','L','S','C','M','F','E','Q','l','s','c','m','f','e','q']
    while True:
        command_type = input("Insert a command (Type 'H' for help):")
        if command_type in valid_command:
            if command_type == 'H' or command_type == 'h':
                print(f"- (H)elp shows the list of comments;\n"
                      f"- (L)ist shows the list of countries present in the database;\n"
                      f"- (S)ummary prints out a summary of the medals won by a single country;\n"
                      f"- (C)ompare allows for a comparison of the medals won by two countries;\n"
                      f"- (M)ore, given a medal type, lists all the countries that received more medal than a threshold;\n"
                      f"- (F)ewer, given a medal type, lists all the countries that received fewer medals than a threshold\n"
                      f"- (E)xport, save the medals table as 'json' file;\n"
                      f"- (Q)uit.")

            elif command_type == 'L' or command_type == 'l':
                country_name_list = get_sorted_list_of_country_names(country_data)
                print(f"The dataset contains {len(country_name_list)} countries: {country_name_list}")

            elif command_type == 'S' or command_type == 's':
                sentence = 'Insert a country name (\'q\' for quit): '
                if sentence == 'q' or sentence == 'Q':
                    break
                country_name = read_country_name(country_data, sentence)

                country = country_data[country_name]
                country.print_summary()

            elif command_type == 'C' or command_type == 'c':
                sentence = 'Insert a country name (\'q\' for quit): '

                if sentence == 'q' or sentence == 'Q':
                    break

                country1 = read_country_name(country_data, sentence)
                sentence = f'Insert a name of the country you want to compare against \'{country1}\' '

                if sentence == country1:
                    print(f'You input same country')
                    break

                country2 = read_country_name(country_data,f'Insert a name of the country you want to compare against \'{country1}\' ')
                country = country_data[country1]
                country.compare(country_data[country2])

            elif command_type == 'M' or command_type =='m':
                print(f'Given a medal type, list all the countries that receive more medals than a threshold;')
                sentence = 'Insert a medal type (choose among \'gold\', \'silver\', \'bronze\', or \'total\': '
                medal_type = read_medal_type(sentence)
                sentence = 'Enter the threshold (a positive integer)'
                threshold = read_positive_integer(sentence)

                sorted_country = sort_countries_by_medal_type_descending(country_data,medal_type)
                selected_list = []
                for country in sorted_country:
                    if country.get_medals(medal_type) >= threshold:
                        selected_list.append(country)
                    else: pass

                for country in selected_list:
                    print(f"{country.name} received {country.get_medals(medal_type)}")

            elif command_type == 'F' or command_type == 'f':
                print(f'Given a medal type, list all the countries that receive more medals than a threshold;')
                sentence = 'Insert a medal type (choose among \'gold\', \'silver\', \'bronze\', or \'total\': '
                medal_type = read_medal_type(sentence)
                sentence = 'Enter the threshold (a positive integer)'
                threshold = read_positive_integer(sentence)

                sorted_country = sort_countries_by_medal_type_ascending(country_data,medal_type)

                selected_list = []
                for country in sorted_country:
                    if 0< country.get_medals(medal_type) <= threshold:
                        selected_list.append(country)
                    else:
                        pass


                for country in selected_list:
                    print(f"{country.name} received {country.get_medals(medal_type)}")

            elif command_type == 'E' or command_type == 'e': #How to save with json in Python ref: https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/
                file_name = input('Enter the file name (.json)Exported')

                json_data = list(country_data.values())

    #TypeError: Object of type 'FileItem' is not JSON serializable <-- Error occur
    #TypeError: Object of type CountryMedals is not JSON serializable <-- Error occur

                with open(file_name, mode='w', encoding='utf-8') as outfile:
                    for num in range(len(json_data)):
                        json.dump(json_data[num].to_json(), outfile, indent = 2)

            elif command_type == 'Q' or command_type == 'q': break

        else: print(f"the value entered is not a valid command type")

def main():
    user_command()
    return 0
if __name__ == '__main__':
    main()
