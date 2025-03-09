import matplotlib.pyplot as plt
import networkx as nx
from model import GamingBotModel, HumanAgent, BotAgent

def plot_network(model):
    plt.figure(figsize=(8,6))
    G = model.G
    pos = nx.spring_layout(G)

    human_nodes = [agent.unique_id for agent in model.schedule.agents if isinstance(agent, HumanAgent)]
    bot_nodes = [agent.unique_id for agent in model.schedule.agents if isinstance(agent, BotAgent)]

    nx.draw_networkx_nodes(G, pos, nodelist=human_nodes, node_color='blue', node_size=300, alpha=0.8)
    nx.draw_networkx_nodes(G, pos, nodelist=bot_nodes, node_color='red', node_size=300, alpha=0.8)
    nx.draw_networkxedges(G, pos, alpha=0.5)

    plt.title("Network Spread: Bots (Red) Influencing Users (Blue)")
    plt.show()

if __name__ == "__main__":
    model = GamingBotModel()
    for _ in range(10):
        model.step()
    plot_network(model)