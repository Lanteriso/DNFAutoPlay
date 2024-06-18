import time
import random
import pydirectinput
class Skill:
    def __init__(self, name, cooldown,press_count,press_time,skill_Range):
        self.name = name
        self.cooldown = cooldown
        self.last_used_time = 0
        self.press_count = press_count
        self.press_time = press_time
        self.skill_Range = skill_Range
    def is_ready(self, current_time):
        return current_time - self.last_used_time >= self.cooldown

职业身高 = {
        '默认': 260,
        '驱魔师': 270,
        '帕拉丁': 210,
        '合金':270,
        '忍者': 240,
        '旅人': 210,
        '缪斯': 210,
        '猎人': 210,
        '男光明骑士': 240,
        '小魔女': 200,
        '召唤师': 190,
        '阿修罗': 280,
        '剑魂': 280,
        '蓝拳': 270,
        }
allskills = {
    '默认': [
            Skill("x", 1,1,0.1,(250,120)),
            ],
    '驱魔师': [
            Skill("a", 6.8, 1, 0.9,(250,120)),
            Skill("s", 12, 1, 0.9,(250,120)),
            Skill("d", 17.1, 1, 0.9,(250,120)),
            Skill("f", 34.2, 1, 0.9,(250,120)),
            Skill("g", 42.8, 1, 0.9,(250,120)),
            #Skill("h", 6, 1, 0.9,(250,120)),
            Skill("q", 11.4, 1, 0.9,(250,120)),
            Skill("w", 36.6, 1, 0.9,(250,120)),
            Skill("e", 44, 1, 0.9,(250,120)),
            Skill("r", 54, 1, 0.9,(250,120)),
            Skill("t", 180, 1, 5,(250,120)),
           ],
    '召唤师': [
        Skill("w", 60, 1, 0.9, (1500,1150)),
        Skill("e", 60, 1, 0.9, (1500,1150)),
        Skill("r", 60, 1, 0.9, (1500,1150)),
    ],
    '阿修罗': [
        Skill("a", 7, 1, 0.9, (250, 120)),
        Skill("s", 40, 1, 0.9, (250, 120)),
        Skill("d", 7, 1, 0.9, (250, 120)),
        #Skill("f", 60, 1, 0.9, (250, 120)),
        Skill("g", 10, 1, 0.9, (250, 120)),
        Skill("h", 60, 1, 0.9, (250, 120)),
        Skill("q", 16, 1, 0.9, (250, 120)),
        Skill("w", 50, 1, 0.9, (250, 120)),
        Skill("e", 6, 1, 0.9, (250, 120)),
        Skill("r", 15, 1, 0.9, (250, 120)),
        #Skill("t", 140, 1, 5, (250, 120)),

    ],
    '剑影': [
        Skill("a", 31, 1, 0.9, (250, 120)),
        Skill("s", 46, 1, 0.9, (250, 120)),
        Skill("d", 35, 1, 0.9, (250, 120)),
        #Skill("f", 60, 1, 0.9, (250, 120)),
        Skill("g", 12, 1, 0.9, (250, 120)),
        Skill("h", 39, 1, 0.9, (250, 120)),
        Skill("q", 15, 1, 0.9, (250, 120)),
        Skill("w", 4, 1, 0.9, (250, 120)),
        Skill("e", 9, 1, 0.9, (250, 120)),
        Skill("r", 32, 1, 0.9, (250, 120)),
        Skill("t", 130, 1, 5, (250, 120)),

    ],
    '狂战士': [
        Skill("a", 18, 1, 0.9, (250, 120)),
        Skill("s", 20, 1, 0.9, (250, 120)),
        Skill("d", 30, 1, 0.9, (250, 120)),
        Skill("f", 60, 1, 0.9, (250, 120)),
        Skill("g", 4, 1, 0.9, (250, 120)),
        Skill("h", 40, 1, 0.9, (250, 120)),
        Skill("q", 25, 1, 0.9, (250, 120)),
        Skill("w", 38, 1, 0.9, (250, 120)),
        Skill("e", 50, 1, 0.9, (250, 120)),
        Skill("r", 60, 1, 0.9, (250, 120)),
        #Skill("t", 180, 1, 5, (250, 120)),

    ],
    '气功师': [
        Skill("a", 36, 1, 0.9, (450, 120)),
        Skill("s", 5, 1, 0.9, (450, 120)),
        Skill("d", 42, 1, 0.9, (450, 120)),
        Skill("f", 10, 1, 0.9, (450, 120)),
        Skill("g", 19, 1, 0.9, (450, 120)),
        Skill("h", 42, 1, 0.9, (450, 120)),
        Skill("q", 15, 1, 0.9, (450, 120)),
        Skill("w", 23, 1, 0.9, (450, 120)),
        Skill("e", 30, 1, 0.9, (450, 120)),
        Skill("r", 60, 1, 0.9, (450, 120)),
        Skill("t", 180, 1, 5, (450, 120)),

    ],
    '帕拉丁': [
        Skill("s", 3, 1, 0.9, (450, 120)),
        Skill("d", 23.8, 1, 0.9, (450, 120)),
        Skill("f", 40, 1, 0.9, (450, 120)),
        Skill("g", 41, 1, 0.9, (450, 120)),
    ],
    '逐风者': [
        Skill("a", 2, 1, 0.9, (450, 120)),
        Skill("s", 6, 1, 0.9, (450, 120)),
        Skill("d", 4, 1, 0.9, (450, 120)),
        Skill("f", 12, 1, 0.9, (450, 120)),
        Skill("g", 8, 1, 0.9, (450, 120)),
        Skill("h", 35, 1, 0.9, (450, 120)),
        Skill("q", 15, 1, 0.9, (450, 120)),
        Skill("w", 37, 1, 0.9, (450, 120)),
        Skill("e", 43, 1, 0.9, (450, 120)),
        Skill("r", 60, 1, 0.9, (450, 120)),
        Skill("t", 180, 1, 5, (450, 120)),
    ],
    '合金': [
        #Skill("a", 2, 1, 0.9, (450, 120)),
        Skill("s", 11.7, 1, 0.9, (450, 120)),
        Skill("d", 13.5, 1, 0.9, (450, 120)),
        Skill("f", 11.1, 1, 0.9, (450, 120)),
        Skill("g", 18, 1, 0.9, (450, 120)),
        Skill("h", 22.5, 1, 0.9, (450, 120)),
        Skill("q", 34.2, 1, 0.9, (450, 120)),
        Skill("w", 38, 1, 0.9, (450, 120)),
        Skill("e", 22, 1, 0.9, (450, 120)),
        Skill("r", 54, 1, 0.9, (450, 120)),
        #Skill("t", 162, 1, 5, (450, 120)),
    ],
    '旅人': [
        Skill("a", 7, 1, 0.9, (450, 120)),
        Skill("s", 14, 1, 0.9, (450, 120)),
        Skill("d", 40, 1, 0.9, (450, 120)),
        Skill("f", 45, 1, 0.9, (450, 120)),
        #Skill("g", 38, 1, 0.9, (450, 120)),
        #Skill("h", 11, 1, 0.9, (450, 120)),
        Skill("q", 12, 1, 0.9, (450, 120)),
        Skill("w", 26, 1, 0.9, (450, 120)),
        Skill("e", 40, 1, 0.9, (450, 120)),
        Skill("r", 60, 1, 0.9, (450, 120)),
         Skill("t", 118, 1, 5, (450, 120)),
    ],
    '缪斯': [
        Skill("a", 11, 1, 0.9, (450, 120)),
        Skill("s", 29, 1, 0.9, (450, 120)),
        Skill("d", 29, 1, 0.9, (450, 120)),
        Skill("f", 36, 1, 0.9, (450, 120)),
        Skill("g", 22, 1, 0.9, (450, 120)),
        Skill("h", 15, 1, 0.9, (450, 120)),
        #Skill("q", 12, 1, 0.9, (450, 120)),
        #Skill("w", 26, 1, 0.9, (450, 120)),
        Skill("e", 30, 1, 0.9, (450, 120)),
        Skill("r", 44, 1, 0.9, (450, 120)),
        Skill("t", 144, 1, 5, (450, 120)),
    ],
    '猎人': [
        Skill("a", 7.6, 1, 0.9, (450, 120)),
        Skill("s", 7.6, 1, 0.9, (450, 120)),
        Skill("d", 14.2, 1, 0.9, (450, 120)),
        Skill("f", 37.8, 1, 0.9, (450, 120)),
        #Skill("g", 22, 1, 0.9, (450, 120)),
        #Skill("h", 15, 1, 0.9, (450, 120)),
        Skill("q", 20, 1, 0.9, (450, 120)),
        Skill("w", 42.5, 1, 0.9, (450, 120)),
        Skill("e", 47.2, 1, 0.9, (450, 120)),
        Skill("r", 56.7, 1, 0.9, (450, 120)),
        Skill("t", 189, 1, 5, (450, 120)),
    ],
    '妖护使': [
        Skill("a", 9.6, 1, 0.9, (450, 120)),
        Skill("s", 14.3, 1, 0.9, (450, 120)),
        Skill("d", 16.5, 1, 0.9, (450, 120)),
        Skill("f", 23.8, 1, 0.9, (450, 120)),
        Skill("g", 36.1, 1, 0.9, (450, 120)),
        #Skill("h", 15, 1, 0.9, (450, 120)),
        Skill("q", 42.8, 1, 0.9, (450, 120)),
        Skill("w", 42.8, 1, 0.9, (450, 120)),
        Skill("e", 47.5, 1, 0.9, (450, 120)),
        Skill("r", 57, 1, 0.9, (450, 120)),
        Skill("t", 171, 1, 5, (450, 120)),
    ],
    '忍者': [
        Skill("a", 10, 1, 0.9, (450, 120)),
        Skill("s", 10, 1, 0.9, (450, 120)),
        Skill("d", 15, 1, 0.9, (450, 120)),
        Skill("f", 20, 1, 0.9, (450, 120)),
        Skill("g", 25, 1, 0.9, (450, 120)),
        Skill("h", 32, 1, 0.9, (450, 120)),
        Skill("q", 35, 1, 0.9, (450, 120)),
        Skill("w", 40, 1, 0.9, (450, 120)),
        Skill("e", 40, 1, 0.9, (450, 120)),
        Skill("r", 60, 1, 0.9, (450, 120)),
        Skill("t", 180, 1, 1, (450, 120)),
    ],
    '男光明骑士': [
        Skill("a", 30, 1, 0.9, (450, 120)),
        Skill("s", 40, 1, 0.9, (450, 120)),
        Skill("d", 14.4, 1, 0.9, (450, 120)),
        Skill("f", 40, 1, 0.9, (450, 120)),
        Skill("g", 60, 1, 0.9, (450, 120)),
        #Skill("h", 20, 1, 0.9, (450, 120)),
        Skill("q", 10, 1, 0.9, (450, 120)),
        Skill("w", 20, 1, 0.9, (450, 120)),
        Skill("e", 7.5, 1, 0.9, (450, 120)),
        Skill("r", 45, 1, 0.9, (450, 120)),
        Skill("t", 180, 1, 1, (450, 120)),
    ],
    '小魔女': [
        Skill("a", 8, 1, 0.9, (450, 120)),
        Skill("s", 27, 1, 0.9, (450, 120)),
        Skill("d", 48, 1, 0.9, (450, 120)),
        Skill("f", 15, 1, 0.9, (450, 120)),
        Skill("g", 32, 1, 0.9, (450, 120)),
        Skill("h", 36, 1, 0.9, (450, 120)),
        Skill("q", 10, 1, 0.9, (450, 120)),
        #Skill("w", 40, 1, 0.9, (450, 120)),
        #Skill("e", 50, 1, 0.9, (450, 120)),
        Skill("r", 10, 1, 0.9, (450, 120)),
        #Skill("t", 144, 1, 1, (450, 120)),
    ],
    '剑魂': [
        Skill("a", 13, 1, 0.9, (450, 120)),
        #Skill("s", 27, 1, 0.9, (450, 120)),
        Skill("d", 38, 1, 0.9, (450, 120)),
        #Skill("f", 15, 1, 0.9, (450, 120)),
        Skill("g", 32, 1, 0.9, (450, 120)),
        Skill("h", 22, 1, 0.9, (450, 120)),
        Skill("q", 8, 1, 0.9, (450, 120)),
        Skill("w", 29, 1, 0.9, (450, 120)),
        Skill("e", 39, 1, 0.9, (450, 120)),
        #Skill("r", 10, 1, 0.9, (450, 120)),
        #Skill("t", 144, 1, 1, (450, 120)),
    ],
    '鬼泣': [
        Skill("a", 4, 1, 0.9, (450, 120)),
        Skill("s", 8, 1, 0.9, (450, 120)),
        Skill("d", 19, 1, 0.9, (450, 120)),
        #Skill("f", 15, 1, 0.9, (450, 120)),
        Skill("g", 45, 1, 0.9, (450, 120)),
        Skill("h", 57, 1, 0.9, (450, 120)),
        Skill("q", 15, 1, 0.9, (450, 120)),
        Skill("w", 19, 1, 0.9, (450, 120)),
        Skill("e", 37, 1, 0.9, (450, 120)),
        #Skill("r", 38, 1, 0.9, (450, 120)),
        Skill("t", 133, 1, 1, (450, 120)),
    ],
    '刃影': [
        Skill("a", 22, 1, 0.9, (450, 120)),
        Skill("s", 17, 1, 0.9, (450, 120)),
        Skill("d", 7, 1, 0.9, (450, 120)),
        #Skill("f", 15, 1, 0.9, (450, 120)),
        Skill("g", 43, 1, 0.9, (450, 120)),
        Skill("h", 52, 1, 0.9, (450, 120)),
        Skill("q", 33, 1, 0.9, (450, 120)),
        Skill("w", 14, 1, 0.9, (450, 120)),
        #Skill("e", 43, 1, 0.9, (450, 120)),
        Skill("r", 31, 1, 0.9, (450, 120)),
        Skill("t", 138, 1, 1, (450, 120)),
    ],
    '男气功': [
        Skill("a", 14, 1, 0.9, (450, 120)),
        Skill("s", 2, 1, 0.9, (450, 120)),
        Skill("d", 35, 1, 0.9, (450, 120)),
        Skill("f", 6, 1, 0.9, (450, 120)),
        Skill("g", 49, 1, 0.9, (450, 120)),
        Skill("h", 80, 1, 0.9, (450, 120)),
        Skill("q", 10, 1, 0.9, (450, 120)),
        Skill("w", 31, 1, 0.9, (450, 120)),
        Skill("e", 37, 1, 0.9, (450, 120)),
        Skill("r", 25, 1, 0.9, (450, 120)),
        Skill("t", 171, 1, 1, (450, 120)),
    ],
    '蓝拳': [
        #Skill("a", 14, 1, 0.9, (450, 120)),
        #Skill("s", 3, 1, 0.9, (450, 120)),
        #Skill("d", 34.2, 1, 0.9, (450, 120)),
        Skill("f", 3.4, 1, 0.9, (450, 120)),
        #Skill("g", 8.6, 1, 0.9, (450, 120)),
        #Skill("h", 29.9, 1, 0.9, (450, 120)),
        Skill("q", 5, 1, 0.9, (450, 120)),
        #Skill("w", 43.4, 1, 0.9, (450, 120)),
        Skill("e", 51.3, 1, 0.9, (450, 120)),
        Skill("r", 6, 1, 0.9, (450, 120)),
        Skill("t", 171, 1, 1, (450, 120)),
    ],
    '契魔者': [
        Skill("a", 7, 1, 0.9, (450, 120)),
        Skill("s", 5, 1, 0.9, (450, 120)),
        Skill("d", 8, 1, 0.9, (450, 120)),
        Skill("g", 15, 1, 0.9, (450, 120)),
        Skill("h", 40, 1, 0.9, (450, 120)),
        Skill("q", 47, 1, 0.9, (450, 120)),
        Skill("w", 40, 1, 0.9, (450, 120)),
        Skill("e", 25, 1, 0.9, (450, 120)),
        Skill("r", 60, 1, 0.9, (450, 120)),
        Skill("t", 180, 1, 1, (450, 120)),
    ],
    '暗殿骑士': [
        Skill("a", 5.1, 1, 0.9, (450, 120)),
        Skill("s", 9.2, 1, 0.9, (450, 120)),
        Skill("d", 12.6, 1, 0.9, (450, 120)),
        Skill("f", 54.2, 1, 0.9, (450, 120)),
        Skill("g", 45.1, 1, 0.9, (450, 120)),
        Skill("h", 36.1, 1, 0.9, (450, 120)),
        Skill("q", 4.3, 1, 0.9, (450, 120)),
        Skill("w", 12.6, 1, 0.9, (450, 120)),
        Skill("e", 40.6, 1, 0.9, (450, 120)),
        Skill("r", 36.1, 1, 0.9, (450, 120)),
        Skill("t", 163, 1, 1, (450, 120)),
    ],
    '流浪武士': [
        Skill("a", 19.2, 1, 0.9, (450, 120)),
        Skill("s", 9.2, 1, 0.9, (450, 120)),
        Skill("d", 23, 1, 0.9, (450, 120)),
        Skill("f", 8.6, 1, 0.9, (450, 120)),
        Skill("g", 38.5, 1, 0.9, (450, 120)),
        Skill("h", 2.4, 1, 0.9, (450, 120)),
        Skill("q", 2.4, 1, 0.9, (450, 120)),
        Skill("w", 4, 1, 0.9, (450, 120)),
        Skill("e", 5.1, 1, 0.9, (450, 120)),
        Skill("r", 23, 1, 0.9, (450, 120)),
        Skill("t", 153, 1, 1, (450, 120)),
    ],
    '驭剑士': [
        Skill("a", 10.8, 1, 0.9, (450, 120)),
        #Skill("s", 9.2, 1, 0.9, (450, 120)),
        Skill("d", 13.5, 1, 0.9, (450, 120)),
        #Skill("f", 8.6, 1, 0.9, (450, 120)),
        Skill("g", 13.5, 1, 0.9, (450, 120)),
        Skill("h", 18, 1, 0.9, (450, 120)),
        Skill("q", 22.8, 1, 0.9, (450, 120)),
        Skill("w", 42, 1, 0.9, (450, 120)),
        Skill("e", 43.5, 1, 0.9, (450, 120)),
        Skill("r", 27, 1, 0.9, (450, 120)),
        Skill("t", 163, 1, 1, (450, 120)),
    ],
    '女光明骑士': [
        Skill("a", 10, 1, 0.9, (450, 120)),
        Skill("s", 30.4, 1, 0.9, (450, 120)),
        Skill("d", 31.7, 1, 0.9, (450, 120)),
        Skill("f", 3.2, 1, 0.9, (450, 120)),
        #Skill("g", 13.5, 1, 0.9, (450, 120)),
        #Skill("h", 18, 1, 0.9, (450, 120)),
        Skill("q", 48, 1, 0.9, (450, 120)),
        Skill("w", 29.8, 1, 0.9, (450, 120)),
        Skill("e", 37.2, 1, 0.9, (450, 120)),
        Skill("r", 14.4, 1, 0.9, (450, 120)),
        Skill("t", 136, 1, 1, (450, 120)),
    ],
    '男柔道': [
        Skill("a", 9.5, 1, 0.9, (450, 120)),
        Skill("s", 11.3, 1, 0.9, (450, 120)),
        Skill("d", 23.6, 1, 0.9, (450, 120)),
        Skill("f", 36.9, 1, 0.9, (450, 120)),
        # Skill("g", 13.5, 1, 0.9, (450, 120)),
        # Skill("h", 18, 1, 0.9, (450, 120)),
        Skill("q", 14.2, 1, 0.9, (450, 120)),
        Skill("w", 14.2, 1, 0.9, (450, 120)),
        Skill("e", 37.8, 1, 0.9, (450, 120)),
        Skill("r", 42.5, 1, 0.9, (450, 120)),
        Skill("t", 56.7, 1, 1, (450, 120)),
    ],
    '黑暗武士': [
        Skill("a", 4.5, 1, 0.9, (450, 120)),
        Skill("s", 14, 1, 0.9, (450, 120)),
        Skill("d", 24, 1, 0.9, (450, 120)),
        Skill("f", 8, 1, 0.9, (450, 120)),
        Skill("g", 13, 1, 0.9, (450, 120)),
        Skill("h", 25, 1, 0.9, (450, 120)),
        Skill("q", 18, 1, 0.9, (450, 120)),
        Skill("w", 9, 1, 0.9, (450, 120)),
        Skill("e", 41, 1, 0.9, (450, 120)),
        Skill("r", 41, 1, 0.9, (450, 120)),
        Skill("t", 36.7, 1, 1, (450, 120)),
    ],
}


class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def is_alive(self):
        return self.health > 0

    def attack(self, other):

        other.health -= self.attack_power
        print(f"{self.name} skill attacks {other.name} for {self.attack_power} damage.")

    def heal(self, amount):
        self.health += amount
        print(f"{self.name} heals for {amount} health points.")

class Monster(Character):
    def __init__(self, name, health, attack_power):
        super().__init__(name, health, attack_power)

class Player(Character):
    def __init__(self, name, health, attack_power,character_class):
        super().__init__(name, health, attack_power)
        self.level = 1
        self.状态 = "默认"
        self.身高 = 职业身高.get(character_class, 260)
        self.isend = 0
        self.currentroomlist =[]
        self.currentroomlist2 = []
        self.character_class = character_class

        self.skills = allskills[self.character_class]
        self.current_time = 0
    def update(self):
        # 更新当前时间
        self.current_time = time.time()

    def use_random_available_skill(self,targetrange):
        self.update()
        random.shuffle(self.skills)
        for skill in self.skills:
            if (abs(targetrange[0]) <= skill.skill_Range[0]) and (abs(targetrange[1]) <= skill.skill_Range[1]) and skill.is_ready(self.current_time):
                skill.last_used_time = self.current_time
                print(f"施放技能: {skill.name} {targetrange}")
                #return [skill.name,skill.cooldown,skill.press_count,skill.press_time,skill.skill_Range]
                return skill
        print("No skills are available.")
        #return allskills['默认'][0]

    def resetCD(self):
        for skill in self.skills:
            skill.last_used_time = 0

    def level_up(self):
        self.level += 1
        self.health += 10
        self.attack_power += 5
        print(f"{self.name} has leveled up to level {self.level}!")

class Skill:
    def __init__(self, name, cooldown,press_count,press_time):
        self.name = name
        self.cooldown = cooldown
        self.last_used_time = 0
        self.press_count = press_count
        self.press_time = press_time

    def is_ready(self, current_time):
        return current_time - self.last_used_time >= self.cooldown

def fight(player, monster):
    while player.is_alive() and monster.is_alive():
        player.attack(monster)
        skills = player.use_random_available_skill((20,00))
        pydirectinput.press(skills.name)
        time.sleep(skills.press_time)
        if monster.is_alive():
            monster.attack(player)
        else:
            print(f"{monster.name} has been defeated!")
            # 升级逻辑
            if player.level < 5:
                player.level_up()


def main():
    player = Player("Hero", 1000, 10,'驱魔师')
    monster = Monster("Goblin", 1000, 5)
    time.sleep(3)
    print("Welcome to the RPG game! You are the hero.")
    while player.is_alive():
        fight(player, monster)
        if not monster.is_alive():
            # 游戏胜利
            print(f"Congratulations, {player.name}! You have won the game!")
            break


if __name__ == "__main__":
    main()