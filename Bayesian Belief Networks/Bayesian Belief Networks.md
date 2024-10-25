`Bayesian Belief Networks` (BBNs), also known as Bayesian Networks or Probabilistic Graphical Models,
are a type of statistical model that represents a set of variables and their conditional dependencies
via a directed acyclic graph (DAG). Each node in the graph represents a random variable, and the edges
between nodes represent probabilistic dependencies. The key feature of BBNs is that they allow for
the representation of uncertainty and the incorporation of prior knowledge in a structured way.

Components of a Bayesian Belief Network:
- Nodes: Each node represents a random variable, which can be discrete or continuous.
- Edges: Directed edges between nodes indicate a probabilistic dependency. An edge from node A to node B
- signifies that A influences B.
- Conditional Probability Tables (CPTs): Each node has an associated CPT that quantifies the effect of the
parent nodes on the node. If a node has no parents, its CPT represents its prior distribution.
- Example: Medical Diagnosis

Let's consider a simple example of a Bayesian Belief Network for diagnosing a medical condition based
on symptoms.

`Variables:`
- Disease (D): Represents whether a patient has a disease (True/False).
- Cough (C): Represents whether the patient has a cough (True/False).
- Fever (F): Represents whether the patient has a fever (True/False).
- Flu (FL): Represents whether the patient has the flu (True/False).
Structure:
The disease (D) can cause both cough (C) and fever (F).
The flu (FL) can also cause cough (C) and fever (F).
The relationships can be represented as follows:
D → C
D → F
FL → C
FL → F
Conditional Probability Tables (CPTs):
P(D): The prior probability of having the disease.

P(D=True) = 0.1
P(D=False) = 0.9
P(C | D): The probability of having a cough given the disease status.

P(C=True | D=True) = 0.8
P(C=True | D=False) = 0.1
P(F | D): The probability of having a fever given the disease status.

P(F=True | D=True) = 0.7
P(F=True | D=False) = 0.05
P(C | FL): The probability of having a cough given the flu status.

P(C=True | FL=True) = 0.9
P(C=True | FL=False) = 0.2
P(F | FL): The probability of having a fever given the flu status.

P(F=True | FL=True) = 0.95
P(F=True | FL=False) = 0.1
Inference:
Now, suppose a patient presents with a cough and a fever. We want to infer the probability that they have the disease (D).

Using the structure and the CPTs, we can apply Bayesian inference to calculate:

P(D=True | C=True, F=True)
Using Bayes' theorem and the chain rule of probability, we can compute this probability by summing over the joint probabilities of the symptoms given the possible states of the disease and flu.


![3f0daae9-ed03-4f51-85f3-cf13e7af4899](https://github.com/user-attachments/assets/37672bad-55a4-4552-bb05-dd4820d4f8a4)
