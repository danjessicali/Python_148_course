__author__ = 'lidan'

CATEGORY = {"under 20":[],"under 30":[],"under 40":[],"over 40":[]}
class RaceRegistry:
    """A system for organizing a 5k running race.

    """
    def __init__(self):
        self._category = CATEGORY

    def register(self, name, speed):
        if name not in self._category[speed]:
            self._category[speed].append(name)
        else:
            self.registered(name, speed)

    def registered(self, name, speed):
        if name in self._category[speed]:
            self._category[speed].remove(name)
        self.register(name, speed)

    def get_speed(self,name):
        for key in self._category:
            if name in self._category[key]:
                return key

    def get_runner_list(self, speed):
        return self._category[speed]





