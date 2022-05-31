import json
import os.path
import requests
from bs4 import BeautifulSoup as b
from Character import Character


class Main:
    sila_json = []
    agility_json = []
    intelligence_json = []
    characters_strength = []
    characters_agility = []
    characters_intelligence = []
    stats_dict = {
        "name": '',
        "base strength": '',
        "strength growth": '',
        "base agility": '',
        "agility grows": '',
        "base intelligence": '',
        "intelligence growth": '',
        "picture": ''
    }

    @staticmethod
    def get_strength():
        if Main.skip_if_part_parsed('strength.json'):
            return

        print('I\'m called (get_strength)')
        url = 'https://dota2.fandom.com/wiki/Strength'
        r = requests.get(url=url)
        soup = b(r.text, 'lxml')
        sila = soup.find(
            'table',
            class_='wikitable sortable').find_all('tr')
        for i, stats in zip(range(len(sila)), sila):
            if i == 0:
                continue
            a = stats.find('img')
            picture = a.get('data-src')
            name = stats.find('td').find_next_sibling('td')
            base_strength = name.find_next_sibling('td')
            strength_growth = base_strength.find_next_sibling('td')
            base_agility = strength_growth.find_next_sibling('td')
            agility_growth = base_agility.find_next_sibling('td')
            base_intelligence = agility_growth.find_next_sibling('td')
            intelligence_growth = base_intelligence.find_next_sibling('td')
            ch = Character(name.text.strip(),
                           base_strength.text.strip(),
                           strength_growth.text.strip(),
                           base_agility.text.strip(),
                           agility_growth.text.strip(),
                           base_intelligence.text.strip(),
                           intelligence_growth.text.strip(),
                           picture
                           )

            Main.characters_strength.append(ch)

    @staticmethod
    def get_agility():
        if Main.skip_if_part_parsed('agility.json'):
            return

        print('I\'m called (get_agility)')
        url = 'https://dota2.fandom.com/wiki/Agility'
        r = requests.get(url=url)
        soup = b(r.text, 'lxml')
        agility = soup.find(
            'table',
            class_='wikitable sortable').find_all('tr')
        for i, stats in zip(range(len(agility)), agility):
            if i == 0:
                continue
            a = stats.find('img')
            picture = a.get('data-src')
            name = stats.find('td').find_next_sibling('td')
            base_strength = name.find_next_sibling('td')
            strength_growth = base_strength.find_next_sibling('td')
            base_agility = strength_growth.find_next_sibling('td')
            agility_growth = base_agility.find_next_sibling('td')
            base_intelligence = agility_growth.find_next_sibling('td')
            intelligence_growth = base_intelligence.find_next_sibling('td')
            ch = Character(name.text.strip(),
                           base_strength.text.strip(),
                           strength_growth.text.strip(),
                           base_agility.text.strip(),
                           agility_growth.text.strip(),
                           base_intelligence.text.strip(),
                           intelligence_growth.text.strip(),
                           picture
                           )

            Main.characters_agility.append(ch)

    @staticmethod
    def load_characters(dictionary: list, arr: list):
        for ch in dictionary:
            hero = Character()
            hero.name = ch['name']
            hero.base_strength = ch['base strength']
            hero.strength_growth = ch['strength growth']
            hero.base_agility = ch['base agility']
            hero.agility_growth = ch['agility growth']
            hero.base_intelligence = ch['base intelligence']
            hero.intelligence_growth = ch['intelligence growth']
            hero.picture = ch['picture']

            arr.append(hero)

    @staticmethod
    def get_intelligence():
        if Main.skip_if_part_parsed('intelligence.json'):
            return

        print('I\'m called (get_intelligence)')
        url = 'https://dota2.fandom.com/wiki/Intelligence'
        r = requests.get(url=url)
        soup = b(r.text, 'lxml')
        intelligence = soup.find(
            'table',
            class_='wikitable sortable').find_all('tr')
        for i, stats in zip(range(len(intelligence)), intelligence):
            if i == 0:
                continue
            a = stats.find('img')
            picture = a.get('data-src')
            name = stats.find('td').find_next_sibling('td')
            base_strength = name.find_next_sibling('td')
            strength_growth = base_strength.find_next_sibling('td')
            base_agility = strength_growth.find_next_sibling('td')
            agility_growth = base_agility.find_next_sibling('td')
            base_intelligence = agility_growth.find_next_sibling('td')
            intelligence_growth = base_intelligence.find_next_sibling('td')
            ch = Character(name.text.strip(),
                           base_strength.text.strip(),
                           strength_growth.text.strip(),
                           base_agility.text.strip(),
                           agility_growth.text.strip(),
                           base_intelligence.text.strip(),
                           intelligence_growth.text.strip(),
                           picture
                           )

            Main.characters_intelligence.append(ch)

    @staticmethod
    def parse_to_json():
        if Main.skip_if_parsed():
            if not Main.characters_strength:
                with open('strength.json', 'r') as file:
                    sila_json = json.load(file)
                    Main.load_characters(
                        sila_json,
                        Main.characters_strength)

            if not Main.characters_agility:
                with open('agility.json', 'r') as file:
                    agility_json = json.load(file)
                    Main.load_characters(
                        agility_json,
                        Main.characters_agility)

            if not Main.characters_intelligence:
                with open('intelligence.json', 'r') as file:
                    intelligence_json = json.load(file)
                    Main.load_characters(
                        intelligence_json,
                        Main.characters_intelligence)

            return

        for ch in Main.characters_strength:
            sila_temp = Main.stats_dict.copy()

            sila_temp['name'] = ch.name
            sila_temp['base strength'] = ch.base_strength
            sila_temp['strength growth'] = ch.strength_growth
            sila_temp['base agility'] = ch.base_agility
            sila_temp['agility growth'] = ch.agility_growth
            sila_temp['base intelligence'] = ch.base_intelligence
            sila_temp['intelligence growth'] = ch.intelligence_growth
            sila_temp['picture'] = ch.picture

            Main.sila_json.append(sila_temp)
        for ch in Main.characters_agility:
            agility_temp = Main.stats_dict.copy()

            agility_temp['name'] = ch.name
            agility_temp['base strength'] = ch.base_strength
            agility_temp['strength growth'] = ch.strength_growth
            agility_temp['base agility'] = ch.base_agility
            agility_temp['agility growth'] = ch.agility_growth
            agility_temp['base intelligence'] = ch.base_intelligence
            agility_temp['intelligence growth'] = ch.intelligence_growth
            agility_temp['picture'] = ch.picture

            Main.agility_json.append(agility_temp)
        for ch in Main.characters_intelligence:
            intelligence_temp = Main.stats_dict.copy()

            intelligence_temp['name'] = ch.name
            intelligence_temp['base strength'] = ch.base_strength
            intelligence_temp['strength growth'] = ch.strength_growth
            intelligence_temp['base agility'] = ch.base_agility
            intelligence_temp['agility growth'] = ch.agility_growth
            intelligence_temp['base intelligence'] = ch.base_intelligence
            intelligence_temp['intelligence growth'] = ch.intelligence_growth
            intelligence_temp['picture'] = ch.picture

            Main.intelligence_json.append(intelligence_temp)
        with open("strength.json", "w") as file:
            json.dump(Main.sila_json, file,
                      indent=4, ensure_ascii=False)
        with open("agility.json", "w") as file:
            json.dump(Main.agility_json, file,
                      indent=4, ensure_ascii=False)
        with open("intelligence.json", "w") as file:
            json.dump(Main.intelligence_json, file,
                      indent=4, ensure_ascii=False)

    @staticmethod
    def skip_if_parsed() -> bool:
        if Main.skip_if_part_parsed('strength.json'):
            return True
        if Main.skip_if_part_parsed('agility.json'):
            return True
        if Main.skip_if_part_parsed('intelligence.json'):
            return True

        return False

    @staticmethod
    def skip_if_part_parsed(file: str) -> bool:
        if os.path.exists(file):
            return True
        return False

    @staticmethod
    def main():
        Main.get_strength()
        Main.get_agility()
        Main.get_intelligence()
        Main.parse_to_json()


if __name__ == '__main__':
    Main.main()
