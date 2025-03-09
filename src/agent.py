from mesa import Agent
import random

class HumanAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.engagement_level = random.uniform(0.5, 1.0)
        self.sentiment_score = random.uniform(-1, 1)  # Negative to positive sentiment

    def step(self):
        neighbors = self.model.grid.get_neighbors(self.pos, include_center=False)
        for neighbor in neighbors:
            if isinstance(neighbor, BotAgent):
                influence_factor = random.uniform(0.1, 0.5) * neighbor.influence_power
                self.engagement_level *= (1 + influence_factor)
                
                # Sentiment manipulation: Bots shift sentiment towards their agenda
                sentiment_shift = random.choice([-0.2, 0.2]) * neighbor.influence_power
                self.sentiment_score = max(-1, min(1, self.sentiment_score + sentiment_shift))

class BotAgent(Agent):
    def __init__(self, unique_id, model, bias):
        super().__init__(unique_id, model)
        self.influence_power = random.uniform(1.2, 1.5)
        self.bias = bias  # Bots can be pro-game (+1) or anti-game (-1)
        self.engagement_level = self.influence_power  # Define engagement level
        self.sentiment_score = bias  # Bots have a fixed sentiment (either +1 or -1)

    def step(self):
        neighbors = self.model.grid.get_neighbors(self.pos, include_center=False)
        for neighbor in neighbors:
            if isinstance(neighbor, HumanAgent):
                neighbor.engagement_level *= self.influence_power
                
                # Shift sentiment towards bot's intended bias
                sentiment_shift = 0.3 * self.bias
                neighbor.sentiment_score = max(-1, min(1, neighbor.sentiment_score + sentiment_shift))
