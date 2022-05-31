class Character:
    def __init__(self,
                 name='',
                 base_strength='',
                 strength_growth='',
                 base_agility='',
                 agility_growth='',
                 base_intelligence='',
                 intelligence_growth='',
                 picture=''):
        self.name = name
        self.base_strength = base_strength
        self.strength_growth = strength_growth
        self.base_agility = base_agility
        self.agility_growth = agility_growth
        self.base_intelligence = base_intelligence
        self.intelligence_growth = intelligence_growth
        self.picture = picture

    def __repr__(self):
        result = f'Герой: {self.name} \n' \
                 f'Базовая сила: {self.base_strength} \n' \
                 f'Прирост силы: {self.strength_growth} \n' \
                 f'Базовая ловкость: {self.base_agility} \n' \
                 f'Прирост ловкости: {self.agility_growth} \n' \
                 f'Базовый интеллект: {self.base_intelligence} \n' \
                 f'Прирост интеллекта: {self.intelligence_growth} \n \n \n'
        return result
