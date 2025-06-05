# AI Overview and Coding Environments

## In search of a definition of 'AI'
If you are like many others, you are probably just a little bit tired of hearing the abbreviation for Artificial Intelligence, or AI. AI seems to be used in just about every industry for every use case. Most of them time, when we reference AI, we are discussing something to do with a large language model, like ChatGPT or Gemini. But AI algorithms have been around much longer than these models, and different types of AI are best suited for different purposes. It will be interesting to see if the definition changes over the next few years to deal with some of these concepts. 

## AI taxonomies

There are plenty of these out here. But let's look at a few. 

[This one breaks it up more or less by type of algorithm in a hierarchy](https://frickingruvin.medium.com/artificial-intelligence-ai-taxonomies-caa2ddc6cc7e)

[This one is primarily by application](https://www.researchgate.net/publication/359953985_An_artificial_intelligence_life_cycle_From_conception_to_production/figures?lo=1)

[Here is one that primarily looks at the AI landscape in terms of the organizations involved](https://data.org/news/a-taxonomy-for-ai-data-for-good/)

There are many a taxonomy out there. Here's how I keep like to sort things, personally. 

- **Artificial Intelligence** - any type of algorithm used to make an intelligent decision or approximate some kind of human knowledge
    - Expert Systems or Rule-Based Approaches 
        - Algorithms
            - Series of if/Then Statements -- usually developed by a human in the loop, either with expert knowledge, or 
            - Logic-based Programming languages like Prolog (Rule base set by humans, statements set by humans, inference engine)
            - Fuzzy Logic (assigns 'fuzzy' levels to crisp values, uses a rule based approach to set outcomes)
            - State-based control (look at Theory of Computation) - 
    - **Machine Learning** (Algorithm adjusting model from provided data, usually in a dataset - 99% of the time, when someone is talking about AI, the model they are discussing falls into this category)
        - 'Traditional' (More Statistically-Concept Based) Approaches
            - Linear Regression (Uses least squares)
            - Bayesian Models (Uses Bayesian Statistics)
            - Decision Trees (Uses Information Theory) 
            - Random Forest (Uses ensemble sets of decision trees)
            - Clustering (Often uses some kind of distance metric, often unsupervised)
        - **Neural Network Approaches** (neural network setup, typically using some form of gradient descent and backpropagation underneath the hood - I would say 95% of the time, when someone is disussing an AI model, the model they are discussing is in this category)
            - Artificial Neural Network ('vanilla' 'plain-jane' neural network setup)
            - Convolutional Neural Network (matrix structured data)
                - YOLO
                - ResNet
            - Recurrent Neural Network (uses time series data, sequence inputs)
                - GNN 
                - LSTM
            - Spiking Neural Network (analog signals and accumulation)
            - Encoders and Decoders (often unsupervised - bottleneck layer called latent space)
            - Transformers (incorporates concept of 'attention' - inputs in context, often in context with themselves or other inputs. These types of models are usually considerably larger than other neural network models)
                - Large Language Models 
                    - ChatGPT 
                - Vision Transformers 
                - Other Generative Models 
        - Reinforcement Learning
            - Named Reinforcement Learning Algorithms 
                - Q-Learning
                - Policy Optimization
            - Evolutionary Computation
                - Genetic Algorithms
                - Particle Swarm Optimization
                - An entire host of approaches named after animals that are really just genetic algorithms 
            - Markov Models (similar to state machines, but learn 'rules' from data)
            - Monte Carlo Simulation (samples data from distribution by iteration) 

### Observations
- Almost all of the 'popular' techniques today come out of the machine learning cateogory. It is unsurprising that advancement in big data collection and use paved the way for AI. 
- Because of this, data science knowledge is integral. Models are usually only as good as the data that goes into them. Often, if data is good enough, model selection can be more trivial 
- Transformers are relatively new on the scene, but there is a very good chance you are interacting with one if you talk to an AI in the wild 

## Overview of some AI models 

## Concepts Specific to Machine Learning 

## One of the most important elements of machine learning - Gradient Descent 



## AI Coding Environments 

### Machine Learning Hardware Needs 

### Google Colab 

## AI Ethics

- Data
    - Representativeness
        - Are there important cases not covered in the data? 
        - Are historical decisions in the data what we want to reflect going forward? 
    - Manner of Collection
        - Privacy concerns?
        - Notification 
    - Attribution
        - Big issue with Generative Models 

- Use
    - What is the planned use of the technology?
    - Who is held accountable for an AI model's decision
    - AI job replacement?  

## University of Idaho AI Classes 

- Shameless plug for my own class - AI Data Analysis for Manufacturing, Agriculture, and Energy - AIDA-MAE (I think has been recently renamed for AI for Industrial Applications or something similar)
- Machine Vision
- Deep Learning
- Neural Networks
- Artificial Intelligence
- Computational Biology Sequence Analysis
- Python for Machine Learning
- Natural Language Processing 
- Adversarial Machine Learning 
- ... And More!