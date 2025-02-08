# Artificial Hype: The Role of Bots in Gaming Ecosystem Manipulation

- Harjot THANDI
- Saimanoj YARASI
- Omar Shamsul HAQUE

https://github.com/Harjot1711/EECS-4461-Group6


# - Section 1 Phenomena of interest: Description

The gaming industry has developed into an elaborate digital environment where player perception is influenced by both natural interactions and AI-powered bots that affect online discussion, engagement metrics, and 
reviews. Through metric manipulation, fake interaction, and trend amplification, these bots manipulate game popularity on sites like Steam, Reddit (subreddits), Twitch, and Discord. Bots generate a false impression
of player consensus by inflating ratings, spamming positive or negative comments, and creating fake viewership, which deceives developers and consumers alike. This manipulation is the result of several important
dynamics. By oversaturating platforms with skewed ratings, artificial review inflation and deflation affect how people evaluate games. Certain storylines are promoted via social media and forum amplification, 
which produces fabricated controversy or hype. Manipulation of viewing and fake engagement inflate numbers, which affect YouTube recommendations and Twitch rankings. To address these dangers, platform detection 
systems and anti-bot countermeasures are always evolving, while AI-powered bots adapt in response, posing an ongoing challenge.


# - Section 2 Phenomena of interest: Related Works

Karataş & Şahin (2017) review different ways to detect social bots on online platforms. They explain three main methods: machine learning, network analysis, and content analysis. The paper highlights that bots are becoming more advanced and harder to detect. The authors suggest that combining multiple detection techniques, such as analyzing user behaviour and content patterns, is the best approach. They also discuss new research trends, like deep learning, to improve detection methods.

1. Karataş, A., & Şahin, S. (2017). A review on social bot detection techniques and research directions. ResearchGate. Retrieved from [https://www.researchgate.net/publication/322853694_A_Review_on_Social_Bot_Detection_Techniques_and_Research_Directions](https://www.researchgate.net/publication/322853694_A_Review_on_Social_Bot_Detection_Techniques_and_Research_Directions)

Wang et al. (2019) study how to detect fake reviews in app stores. Fake reviews can trick users and affect app rankings. The authors analyze how fake reviews are written, when they are posted, and who writes them. They use machine learning to create models that identify fake reviews. Their research shows that looking at user behaviour and writing style helps detect fake reviews. They suggest that using deep learning and sentiment analysis can improve accuracy.

2. Wang, Y., Zhang, J., Chau, M., & Chang, K. (2019). Towards understanding and detecting fake reviews in app stores. Empirical Software Engineering, 24(3), 1674–1705. [https://link.springer.com/article/10.1007/s10664-019-09706-9](https://link.springer.com/article/10.1007/s10664-019-09706-9)


# - Section 3: Describe the Core Components of the Simulation

- __3.1 Entities:__ Human users and social bots are the main players in this simulation, and each has a unique influence on how people view online games. In order to locate trustworthy information and take part in gaming communities, human users participate in discussions, post reviews, upvote or downvote content, and respond to social trends. Social bots, on the other hand, fabricate ratings, create fake engagement, and exaggerate preferred storylines in order to manipulate metrics. They fabricate a false impression of popularity or controversy by manipulating trends, influencing recommendations, and spamming reviews. While the Virus on a Network Model shows how false information spreads in a self-sustaining way, the Boid Flocking Model offers an alternate perspective as bots coordinate their behaviours to mimic organic involvement.
- __3.2 Affordances:__ Both human users and bots take advantage of the affordances offered by gaming platforms to affect the popularity of games. Bots can propagate hashtags, generate artificial trends, and exaggerate particular narratives through tagging and sharing systems. They can manipulate public perception by inflating or deflating game scores through upvoting, downvoting, and rating systems. Bots control the legitimacy of material and generate emotional reactions, like outrage or hype, to influence user opinion by flooding Reddit, Steam, and Twitch with automated reviews. The Schelling Segregation Model reflects this behaviour, with bots using mass upvoting and downvoting to reinforce particular biases and form echo chambers. Furthermore, bots use targeted disinformation and controversy to stir up conflict, escalating polarization, as illustrated by the Epstein Civil Violence Model. 
- __3.3 Algorithms:__ Content visibility is largely determined by platform algorithms, which bots aggressively take advantage of to sway interaction. By manipulating watch duration, engagement rates, and click-through data, recommendation engines on YouTube, Twitch, and Steam are deceitfully boosted for specific titles. Similar mass engagement strategies are used to manipulate Reddit and Discord's content prioritization systems, which artificially enhance or hinder particular narratives. Adaptive bots always evolve to evade detection, which presents a persistent difficulty even though some platforms employ sentiment analysis and moderation techniques to identify bot-like activity. This dynamic is best captured by the Virus on a Network Model, in which bot-driven disinformation propagates via engagement loops, using platform algorithms to expand their audience and skew public opinion. 

# - Section 4: Simulation Anticipated Outcomes

![IMG_1766](https://github.com/user-attachments/assets/745ab836-c4a7-4ef9-92ab-ae2af1cb6d81)

$\color{red}{\text{Red Nodes}}$: Bots generating fake engagement and disinformation.

$\color{blue}{\text{Blue Nodes}}$: Human users interacting naturally but susceptible to bot influence.

Edges (Connections): Pathways where misinformation spreads through reviews, upvotes, and recommendations.


