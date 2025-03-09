from mesa import Agent
import random

class HumanAgent(Agent):
    def init(self, unique_id, model):
        super().init(unique_id, model)
        self.engagement_level = random.uniform(0.5, 1.0)

    def step(self):
        neighbors = self.model.grid.get_neighbors(self.pos, include_center=False)
        for neighbor in neighbors:
            if isinstance(neighbor, BotAgent):
                self.engagement_level = random.uniform(1.05, 1.2)

class BotAgent(Agent):
    def init(self, unique_id, model):
        super().init(unique_id, model)
        self.influence_power = random.uniform(1.2, 1.5)

    def step(self):
        neighbors = self.model.grid.get_neighbors(self.pos, include_center=False)
        for neighbor in neighbors:
            if isinstance(neighbor, HumanAgent):
                neighbor.engagement_level= self.influence_power