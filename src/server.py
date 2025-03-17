import math
import logging
import solara
//DEL3
import os
print("Using model file:", os.path.abspath(__file__))

from model import State, VirusOnNetwork, number_infected

from mesa.visualization import (
    Slider,
    SolaraViz,
    make_plot_component,
    make_space_component,
)

# Set up logging to write to debug.log in the current directory
logging.basicConfig(level=logging.DEBUG, filename='debug.log', filemode='w')

def agent_portrayal(agent):
    node_color_dict = {
        State.INFECTED: "tab:red",
        State.SUSCEPTIBLE: "tab:green",
        State.RESISTANT: "tab:gray",
    }
    return {"color": node_color_dict[agent.state], "size": 10}

def get_resistant_susceptible_ratio(model):
    ratio = model.resistant_susceptible_ratio()
    ratio_text = r"$\infty$" if ratio is math.inf else f"{ratio:.2f}"
    infected_text = str(number_infected(model))
    return solara.Markdown(
        f"Resistant/Susceptible Ratio: {ratio_text}<br>Infected Remaining: {infected_text}"
    )

model_params = {
    "seed": {
        "type": "InputText",
        "value": 42,
        "label": "Random Seed",
    },
    "num_nodes": Slider(
        label="Number of agents",
        value=10,
        min=10,
        max=100,
        step=1,
    ),
    "avg_node_degree": Slider(
        label="Avg Node Degree",
        value=3,
        min=3,
        max=8,
        step=1,
    ),
    "initial_outbreak_size": Slider(
        label="Initial Outbreak Size",
        value=1,
        min=1,
        max=10,
        step=1,
    ),
    "virus_spread_chance": Slider(
        label="Virus Spread Chance",
        value=0.4,
        min=0.0,
        max=1.0,
        step=0.1,
    ),
    "virus_check_frequency": Slider(
        label="Virus Check Frequency",
        value=0.4,
        min=0.0,
        max=1.0,
        step=0.1,
    ),
    "recovery_chance": Slider(
        label="Recovery Chance",
        value=0.3,
        min=0.0,
        max=1.0,
        step=0.1,
    ),
    "gain_resistance_chance": Slider(
        label="Gain Resistance Chance",
        value=0.5,
        min=0.0,
        max=1.0,
        step=0.1,
    ),
}

def post_process_lineplot(ax):
    ax.set_ylim(ymin=0)
    ax.set_ylabel("# people")
    ax.legend(bbox_to_anchor=(1.05, 1.0), loc="upper left")

SpacePlot = make_space_component(agent_portrayal)
StatePlot = make_plot_component(
    {"Disruptors": "tab:red", "Followers": "tab:green", "Critical Thinkers": "tab:gray"},
    post_process=post_process_lineplot,
)

# Bar Chart Component
import matplotlib.pyplot as plt

def bar_chart_component(model):
    """
    This component retrieves the latest values from the model's DataCollector and creates
    a bar chart showing the current counts for Disruptors, Followers, and Critical Thinkers.
    """
    # Get the DataCollector DataFrame
    df = model.datacollector.get_model_vars_dataframe()
    if df.empty:
        return solara.Markdown("No data collected yet.")
    
    # Use the latest row of data (i.e. the last step)
    latest = df.iloc[-1]

    labels = ["Disruptors", "Followers", "Critical Thinkers"]

    try:
        values = [latest["Infected"], latest["Susceptible"], latest["Resistant"]]
    except KeyError:
        # Fallback to alternative keys if necessary
        values = [latest.get("Disruptors", 0), latest.get("Followers", 0), latest.get("Critical Thinkers", 0)]
    
    # Create the bar chart
    fig, ax = plt.subplots()
    ax.bar(labels, values, color=["tab:red", "tab:green", "tab:gray"])
    ax.set_title("Agent States at Latest Step")
    ax.set_ylabel("Number of Agents")
    
    return solara.FigureMatplotlib(fig)

model1 = VirusOnNetwork()

df = model1.datacollector.get_model_vars_dataframe()
logging.debug("DataCollector columns: %s", df.columns)
print("DataCollector columns:", df.columns, flush=True)

page = SolaraViz(
    model1,
    components=[
        SpacePlot,
        StatePlot,
        get_resistant_susceptible_ratio,
        bar_chart_component  
    ],
    model_params=model_params,
    name="Virus Model",
)
page  # noqa
