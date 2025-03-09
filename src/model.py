from mesa import Model
from mesa.time import RandomActivation
from mesa.space import NetworkGrid
import networkx as nx
from agent import BotAgent, HumanAgent
from mesa.datacollection import DataCollector
import random

class GamingBotModel(Model):
    def __init__(self, num_humans=25, num_bots=10):
        self.num_humans = num_humans
        self.num_bots = num_bots
        self.G = nx.erdos_renyi_graph(n=num_humans + num_bots, p=0.2)
        self.grid = NetworkGrid(self.G)
        self.schedule = RandomActivation(self)

        # Create human agents
        for i in range(num_humans):
            agent = HumanAgent(i, self)
            self.schedule.add(agent)
            self.grid.place_agent(agent, i)

        # Create bot agents with randomized bias
        for i in range(num_bots):
            bias = random.choice([-1, 1])  # Bots can be pro-game or anti-game
            agent = BotAgent(num_humans + i, self, bias)
            self.schedule.add(agent)
            self.grid.place_agent(agent, num_humans + i)

        self.datacollector = DataCollector(
            model_reporters={
                "Total Engagement": lambda m: sum([a.engagement_level for a in m.schedule.agents]),
                "Positive Sentiment": lambda m: sum([1 for a in m.schedule.agents if a.sentiment_score > 0]),
                "Negative Sentiment": lambda m: sum([1 for a in m.schedule.agents if a.sentiment_score < 0])
            }
        )

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()

    def save_data(self):
        import pandas as pd
        df = pd.DataFrame(self.datacollector.get_model_vars_dataframe())
        df.to_csv("engagement_log.csv", index=False)