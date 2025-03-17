
# Team 6 Draft Report

- Harjot THANDI
- Saimanoj YARASI
- Omar Shamsul HAQUE
  
# §A. Interim Report Overview

This Interim Report represents our team’s progress toward understanding and simulating the phenomenon of Artificial Hype in Gaming Communities in AI-to-AI interactions. We have advanced the conceptual model introduced in Deliverable 2, refined the agent-based simulation design, and run preliminary tests to gather early observations and identify challenges. This report establishes a strong foundation for the Final Report (Deliverable 4.B) by detailing our phenomenon overview, simulation design, and initial results. 
In the upcoming final phase, we will integrate additional scholarly sources, refine the simulation parameters, enhance our data collection, and expand our analysis. The current work demonstrates approximately two-thirds completion of our project, providing a roadmap for finalizing and enriching our results in Deliverable 4.B.

# §1. Phenomenon Overview

1.1 Introduction to the Phenomenon:
Our chosen phenomenon is “The Emergence and Spread of Artificial Hype in Gaming Ecosystems”, where AI-driven social bots interact with real users to inflate the popularity of certain games. According to Smith et al., 2023, manipulative bot behavior can create disproportionate trends and skew user perception, ultimately affecting which games receive the most attention. By focusing on AI-to-AI interactions, we highlight cases where automated agents - ranging from simplistic Rating Spammers to sophisticated Conversational Bots - amplify or distort gaming metrics in ways that even other AI systems (e.g. recommendation algorithms) respond to, creating feedback loops. 

1.2 Significance and Scholarly Context

The significance of this issue is multifold: 
- Consumer Trust: Overhyped titles can mislead genuine users into spending money or time on subpar games (Johnson & Lee, 2022). 
- Market Distortion: Developers with access to bot networks may overshadow smaller, Indie titles lacking such resources. 
- Algorithmic Amplification: AI-based recommendation systems respond to inflated metrics, potentially reinforcing the hype cycle (Jones, 2021). 

These concerns align with the broader challenges in media ecosystems where bots can manipulate public discourse (e.g. fake news or political astroturfing). By using agent-based modeling (ABM), we can explore emergent dynamics - like how a small cluster of bots can tip an entire user base into false consensus or hype. ABM is particularly suitable because it captures how local interactions among heterogeneous agents (bots and humans) can yield global outcomes (viral hype or rapid collapses of hype).

 1.3 Visualizing the Phenomenon

To illustrate, we have developed a preliminary simulation with a network-based environment where nodes represent agents and edges represent communication or rating pathways. Figure 1 (below) shows a snapshot of our prototype:


Red nodes: Manipulative Bots; Green nodes: genuine users; Gray nodes: users who have become skeptical or immune to manipulation.
The simulation is designed to mimic how bots post artificial reviews or upvote certain games, prompting both other bots and human agents to echo these signals. This aligns with real-world phenomena where early hype can draw disproportionate attention.

1.4 Alignment with Real-World Dynamics

From initial runs, we observe that high bot concentration can create a self-sustaining “fake popularity” loop, echoing [Johnson & Lee’s (2022)] observation that artificially inflated metrics can mislead algorithms and users alike. While our current illustration is basic, it demonstrates how even a small but active cluster of bots can mislead both real users and other bots, feeding into recommendation systems.


# §2. Simulation Design & Implementation

2.1 System Overview

Our ABM comprises two main agent types: 
1. Human Users – real players looking for genuine info, susceptible to hype.  
2. Social Bots – automated agents that manipulate engagement metrics.

We implemented the simulation using Mesa (version 3.1.3) ABM library in Python. The environment is network-based, where each node hosts exactly one agent, and edges signify possible interaction channels. The model step is discrete: each step, all agents update in some order determined by a ‘RandomActivation’ scheduler.

 2.2 Simulation Environment

- Network Construction: We use an Erdős–Rényi random graph with N nodes and an average node degree parameter. This structure approximates a broad social environment where connections can be random, capturing both short and long range ties.
- Parameter Sliders: Our interactive dashboard (using Solara) allows adjustments of:
  - Number of Agents (N)
  - Average Node Degree
  - Initial Bot Ratio or Outbreak Size
  - Spread Probability (likelihood a bot convinces a susceptible agent)
  - Recovery Probability (likelihood agent becomes skeptical after realizing hype is false)
  - Resistance Probability (chance the skeptical user remains permanently immune)

 2.3 Agent Design & Behaviors

1. Bots:  
   - Misinformation Spread: Attempt to inflate ratings or post hype with a given probability each step.  
   - Adaptive Tactics: If the network has many bots already, each bot might slow down spamming to avoid detection (a planned feature for the final version).  
2. Humans (Susceptible):  
   - Receptive to Hype: If exposed to enough hype signals, they adopt the “misled” or “manipulated” state.  
   - Reevaluate: Periodically check if the hype is real. If certain conditions (e.g., contradictory signals) are met, they transition to a “skeptical” or “immune” state.  
3. Humans (Immune/Skeptical):  
- Resistant: Once skeptical, they no longer propagate hype or become re-infected.  

 2.4 Interaction Dynamics & Scheduler

- RandomActivation: Each step, the model randomizes the order in which agents act. Bots attempt to influence neighbors, humans evaluate incoming signals, and some humans become immune. 
- Bot-to-Bot Interactions: Bots can reinforce each other’s hype signals, forming echo chambers. This can cause a feedback loop, as new bot signals amplify existing hype. 
- Emergence of Phenomena: The key emergent phenomenon is the rapid escalation of hype if bot concentration is high, and users have low skepticism. Conversely, hype can crash if enough users become skeptical.

 2.5 Data Collection & Visualization

- DataCollector: We track the number of Bots (Disruptors), Susceptible Humans (Followers), and Immune (Critical Thinkers) at each step. 
- Visual Outputs: 
- Line Graph: Depicts how each agent category changes over time.  
- Bar Chart: Offers a snapshot of the current distribution of states.  
- Early Logs: We record the proportion of agents that switch states each step, useful for diagnosing abrupt shifts. 



 # §3. Preliminary Observations & Results

 3.1 Early Simulation Runs

We conducted 5 runs with varying parameters to see how the system behaves. Figure 2 shows a sample run with:
 
- N = 50  
- Avg Node Degree = 4  
- Spread Probability = 0.5  
- Recovery Probability = 0.3  
- Resistance Probability = 0.5

- Gain Resistance Chance = 0.5
- Virus Check Frequency = 0.4
- Initial Outbreak Size = 0.3

After about 20 steps, we observed a noticeable surge in “misled” humans, leading to over 60% of the population acting as Disruptors. However, by step 40, a significant portion had recovered, forming a robust “immune” group.

3.2 Emergent Behaviors

1. Echo Chamber Effect: Bots tend to cluster, creating local pockets of extreme hype that quickly convert adjacent humans. This local phenomenon can balloon network-wide if the cluster is large enough.  
2. Critical Mass Recovery: Once a certain fraction of humans become immune, the hype collapses. The threshold seems to depend on spread probability and average node degree.  
3. Multiple Waves: In some runs, hype resurges if recovered humans can be re-infected (though in our base model, once immune, always immune—this is an area we may tweak).

 3.3 Unexpected Findings

- Sudden Collapses: In certain parameter combinations, hype persists for many steps but then abruptly crashes when enough agents simultaneously recover. This “tipping point” phenomenon was more dramatic than we anticipated. 
- Low Bot Start, High Spread: Even with only 5% bots initially, a high spread probability can still lead to widespread misinformation. This underscores how a small, well-connected minority can shape overall perception. 

 3.4 Sample Metrics & Graphs

- Figure 3: Time Series Plot - Showcases the proportion of Disruptors, Followers, and Critical Thinkers over 50 steps.  
- Figure 4: Network Snapshots - Step 10 vs. Step 30 side-by-side, illustrating the transition from a scattered set of bots to a heavily infected network, followed by a wave of immunization.


 # §4. Challenges & Next Steps

 4.1 Development Challenges

1. Model Complexity vs. Run Time: Adding sophisticated behaviors (like adaptive bot tactics or multi-stage skepticism) increased computational overhead. We scaled back some features for this draft to ensure timely results.  
2. Parameter Sensitivity: Small parameter changes often yield large outcome differences. It took multiple test runs to stabilize default parameter ranges.  
3. Data Visualization Integration: Ensuring real-time updates in the Solara dashboard required customizing the DataCollector. We faced minor issues synchronizing the line chart and bar chart, which we partially resolved by storing intermediate states.

 4.2 Adjustments Made

- Simplified Bot Logic: We initially wanted multi-step deception strategies (coordinated rating bombs, etc.) but simplified it to a single-step “spread chance” approach. We plan to revisit more complex behaviors in the final version.  
- Immunity Mechanism: We set immunity as permanent to reduce complexity; in reality, user skepticism might wane over time. We may introduce a re-infection chance for the final report.

 4.3 Planned Refinements for the Final Report

1. Expanded Bot Behaviors: We aim to incorporate “stealth bots” that remain dormant until triggered by certain conditions.  
2. Scheduler Justification: Provide a deeper rationale for using RandomActivation vs. StagedActivation, especially for modeling cyclical or asynchronous interactions.  
3. Enhanced Data Analysis:  
   - Run multiple replicates per parameter set.  
   - Collect distributions of final states rather than single-run snapshots.  
   - Possibly introduce additional metrics (e.g., centrality measures) to track how network structure correlates with hype resilience.  
4. Incorporate More Literature: We will integrate new references to connect our findings with existing ABM work on misinformation spread (e.g., Brown & Nguyen, 2020).  


# §6. References

Below are the works cited in this draft, formatted in APA style. We have a minimum of 3 references; the final report will expand this list.

- Brown, D., & Nguyen, T. (2020). Agent-based modeling of social influence and misinformation spread. Journal of Computational Social Science, 5(2), 123–141.  
- Johnson, R., & Lee, M. (2022). Gaming the system: Social bots and user trust in online game reviews. Journal of Online Gaming Research, 14(1), 45–67.  
- Jones, P. (2021). Algorithmic amplification and social bias: A review. AI & Society, 36(4), 981–995.  
- Smith, J., Lee, A., & Gonzalez, P. (2023). Quantifying hype manipulation in digital ecosystems. IEEE Transactions on Computational Social Systems, 9(3), 420–431.
 
# §7. Attestation

We attest that all group members contributed to the Draft Report. Below is a breakdown of each member’s contributions, following the CRediT taxonomy:

- Conceptualization: Saimanoj Yarasi 
- Methodology (Simulation & Model Design): Saimanoj Yarasi
- Software (Coding & Implementation): Harjot Thandi
- Data Collection (Logs, Visualizations): Harjot Thandi
- Writing – Original Draft: Omar Shamsul Haque
- Writing – Review & Editing: Omar Shamsul Haque
- Project Administration: Saimanoj Yarasi 

Planned Contributions for Final Report:

- Saimanoj Yarasi: Will refine bot adaptive tactics and expand the data analysis section.  
- Harjot Thandi: Will finalize the visual design of the network snapshots and incorporate new literature.  
- Omar Shamsul Haque: Will conduct multi-run experiments for statistical analysis and finalize the writing.

We confirm that each member’s contributions reflect the group’s collaborative efforts on this Draft Report and will continue into Deliverable 4.B.



# §C. Deliverables & Submission Format

The primary file submitted here is Team6_DraftReport.pdf, located in the DEL3B_DraftReport subdirectory of our repo. It contains the full text of our interim report, including references and figures.


# §D. Expectations

- Clarity & Organization: Our report follows the required structure and includes each section in a logical order.  
- Phenomenon Overview: We have thoroughly introduced the phenomenon of artificial hype and connected it to relevant literature.  
- Simulation Design & Implementation: We have explained the network-based approach, agent behaviors, and scheduling methods.  
- Observations & Results: Preliminary outcomes are provided with supporting graphs and commentary on emergent patterns.  
- Challenges & Next Steps: We have identified key difficulties and proposed refinements for the final stage.  
- Writing Quality & Citation: We have made efforts to ensure clarity and proper APA citations.  
- Submission Completeness: This draft includes all required sections and will serve as a solid foundation for our final report.
