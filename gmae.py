#!/usr/bin/env python
"""
does stuff
"""


class ClassProficiencies(object):
    def __init__(self):

        self.armor = None
        self.weapons = []
        self.tools = None
        self.saving_throws = []
        self.skills = []

class BaseClass(object):

    def __init__(self):
        self.hit_die = None
        self.skills = []
        self.proficiencies = ClassProficiencies
        self.features = None

    def set_proficiencies(self, armor=None, weapons=None, tools=None, saving_throws=None, skills=None):
        if armor:
            self.proficiencies.armor = armor
        if weapons:
            self.proficiencies.weapons = weapons
        if tools:
            self.proficiencies.tools = tools
        if saving_throws:
            self.proficiencies.saving_throws = saving_throws
        if skills:
            self.proficiencies.skills = skills
        return

    @staticmethod
    def choose_skills(number_of_skills, skill_list):
        chosen_skills = []
        for i in range(1, number_of_skills + 1):
            print(skill_list)
            skill = input("choose a skill:")
            chosen_skills.append(skill)
        return chosen_skills      


class RangerClass(BaseClass):

    def __init(self):
        super(BaseClass, self).__init__()
        self.hit_die = 10
        

        self.set_proficiencies(
            armor=["light armor", "medium armor", "shields"],
            weapons=["simple weapons", "martial weapons"],
            saving_throws=["strength", "dexterity"],
            skills=self.choose_skills(3, [
                "Animal Handling",
                "Athletics",
                "Insight",
                "Investigation",
                "Nature",
                "Perception",
                "Stealth",
                "Survival"
            ])
        )




