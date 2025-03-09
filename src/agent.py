from mesa import Agent
import random

class HumanAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.engagement_level = random.uniform(0.5, 1.0)

    def step(self):
        neighbors = self.model.grid.get_neighbors(self.pos, include_center=False)
        for neighbor in neighbors:
            if isinstance(neighbor, BotAgent):
                self.engagement_level = random.uniform(1.05, 1.2)

class BotAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.influence_power = random.uniform(1.2, 1.5)
        self.engagement_level = self.influence_power  # Add this line to give BotAgent engagement_level

    def step(self):
        neighbors = self.model.grid.get_neighbors(self.pos, include_center=False)
        for neighbor in neighbors:
            if isinstance(neighbor, HumanAgent):
                neighbor.engagement_level = self.influence_power