import random
from pandas import ExcelFile
from player import Player


class Actor(Player):
    def __init__(self, name: str, job: str, level: int) -> None:
        super().__init__(job=job)
        self.randomizer = random.Random(1)
        self.dead = False
        self.exp = 0
        self.next_exp = 10
        self.name = name
        self.x = 0
        self.y = 0
        self.job = job
        self.level = 0
        with ExcelFile("Assets/base_stats.xlsx") as xls:
            df = xls.parse(xls.sheet_names[0], index_col="job")
            self.stats = df.loc[self.job].to_dict()
            self.stats.pop("TOTAL")
            '''
            HP/MAX_HP
            MP/MAX_MP
            STR
            DEF
            INT
            RES
            AGI
            LUC
            '''
        with ExcelFile("Assets/stats_multiplier.xlsx") as xls:
            df = xls.parse(xls.sheet_names[0], index_col="job")
            self.multiplier = df.loc[self.job].to_dict()
            self.multiplier.pop("TOTAL")
        self.stats["HP"] = self.stats.get("MAX_HP")
        self.stats["MP"] = self.stats.get("MAX_MP")
        # Test stats MOV
        self.stats["MOV"] = 4
        self.level_up(level)
        self.exp = int((self.next_exp/2) +
                       self.randomizer.randint(0, (self.next_exp/2)-1))

    @classmethod
    def randomize(cls, names: str = None, job: str = None, level: int = 0):
        r = random.Random()
        if names == None:
            names = ["Dave", "Jack", "Graze", "Lucas", "Philips"]
        if job == None:
            job = ["warrior", "thief", "mage", "healer"]
        return cls(r.choice(names), r.choice(job), r.randint(level, level+2))

    def level_up(self, levels: int = 1):
        self.level += levels
        HP_before = self.stats.get("HP")
        MAX_HP_before = self.stats.get("MAX_HP")
        MP_before = self.stats.get("MP")
        MAX_MP_before = self.stats.get("MAX_MP")
        for _ in range(levels):
            lvl_up_stats = self.randomizer.choices(["MAX_HP", "MAX_MP", "STR", "DEF", "INT", "RES", "AGI", "LUC"],
                                                   self.multiplier.values(), k=6)
            for lvl in lvl_up_stats:
                self.stats[lvl] += self.randomizer.randint(2, 4)
            self.next_exp *= 2
        self.stats["HP"] = int((HP_before/MAX_HP_before)
                               * self.stats.get("MAX_HP"))
        self.stats["MP"] = int((MP_before/MAX_MP_before)
                               * self.stats.get("MAX_MP"))

    def get_exp(self, points: int):
        self.exp += points
        if self.exp > self.next_exp:
            self.level_up()

    def status(self):
        print(
            f'Name\t: {self.name}\njob\t: {self.job}\nLevel\t: {self.level}\nEXP\t: {self.exp}/{self.next_exp}\nHP\t: {self.stats["HP"]}/{self.stats["MAX_HP"]}\nMP\t: {self.stats["MP"]}/{self.stats["MAX_MP"]}\nSTR\t: {self.stats["STR"]}\nDEF\t: {self.stats["DEF"]}\nINT\t: {self.stats["INT"]}\nRES\t: {self.stats["RES"]}\nAGI\t: {self.stats["AGI"]}\nLUC\t: {self.stats["LUC"]}\n')

    def wait(self):
        pass


def attack(attacker: Actor, attacked: Actor):
    attack_point = int(1.5 * attacker.stats.get("STR") -
                       attacked.stats.get("DEF"))
    print(f"{attacked.name} loses {attack_point} HP\n")
    if (attacked.stats.get("HP")-attack_point) > 0:
        attacked.stats["HP"] -= attack_point
    else:
        print(f"")
        attacked.stats["HP"] = 0
        attacked.dead = True


if __name__ == "__main__":
    player = Actor("Sandy", "human", 2)
    player.status()
    # player.level_up()
    # player.status()
    # print("Selesai")
    # enemy = Actor("Zelda", "elf", 5)
    enemy = Actor.randomize(level=5)
    enemy.status()
    attack(player, enemy)
    enemy.status()
