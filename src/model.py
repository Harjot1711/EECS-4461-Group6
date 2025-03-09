from mesa import Model
from mesa.time import RandomActivation
from mesa.space import NetworkGrid
import networkx as nx
from agent import BotAgent, HumanAgent
from mesa.datacollection import DataCollector

class GamingBotModel(Model):
    def __init__(self, num_humans=25, num_bots=10):
        self.num_humans = num_humans
        self.num_bots = num_bots
        self.G = nx.erdos_renyi_graph(n=num_humans + num_bots, p=0.2)
        self.grid = NetworkGrid(self.G)
        self.schedule = RandomActivation(self)

        for i in range(num_humans):
            agent = HumanAgent(i, self)
            self.schedule.add(agent)
            self.grid.place_agent(agent, i)

        for i in range(num_bots):
            agent = BotAgent(num_humans + i, self)
            self.schedule.add(agent)
            self.grid.place_agent(agent, num_humans + i)

        self.datacollector = DataCollector(
            model_reporters={"Engagement": lambda m: sum([a.engagement_level for a in m.schedule.agents])}
        )

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()

    def save_data(self):
        import pandas as pd
        df = pd.DataFrame(self.datacollector.get_model_vars_dataframe())
        df.to_csv("engagement_log.csv", index=False)