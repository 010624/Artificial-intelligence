import torch
import torch.nn as nn
import networkx as nx
import matplotlib.pyplot as plt

class BayesianNetwork(nn.Module):
    def __init__(self):
        super(BayesianNetwork, self).__init__()
        
        # Prior probabilities (learnable parameters)
        self.disease_prior = nn.Parameter(torch.tensor([0.9, 0.1]))  # P(D=0), P(D=1)
        self.flu_prior = nn.Parameter(torch.tensor([0.95, 0.05]))    # P(FL=0), P(FL=1)
        
        # Conditional probability tables (learnable parameters)
        # P(C|D,FL) - shape: [D_states, FL_states, C_states]
        self.cough_cpd = nn.Parameter(torch.tensor([
            [[0.8, 0.2],  # P(C|D=0,FL=0)
             [0.1, 0.9]], # P(C|D=0,FL=1)
            [[0.2, 0.8],  # P(C|D=1,FL=0)
             [0.05, 0.95]] # P(C|D=1,FL=1)
        ]))
        
        # P(F|D,FL)
        self.fever_cpd = nn.Parameter(torch.tensor([
            [[0.7, 0.3],  # P(F|D=0,FL=0)
             [0.2, 0.8]], # P(F|D=0,FL=1)
            [[0.3, 0.7],  # P(F|D=1,FL=0)
             [0.05, 0.95]] # P(F|D=1,FL=1)
        ]))

    def forward(self, evidence=None):
        """
        Forward pass to compute probabilities
        evidence: dictionary with observed values
        """
        # Initialize belief states
        disease_prob = torch.softmax(self.disease_prior, dim=0)
        flu_prob = torch.softmax(self.flu_prior, dim=0)
        
        # If we have evidence, update probabilities
        if evidence is not None:
            if 'D' in evidence:
                disease_prob = torch.zeros_like(disease_prob)
                disease_prob[evidence['D']] = 1.0
            if 'FL' in evidence:
                flu_prob = torch.zeros_like(flu_prob)
                flu_prob[evidence['FL']] = 1.0
        
        # Compute marginal probabilities for Cough and Fever
        # Expand dimensions for broadcasting
        d_expanded = disease_prob.unsqueeze(1).unsqueeze(2)
        fl_expanded = flu_prob.unsqueeze(0).unsqueeze(2)
        
        # Calculate joint probabilities
        cough_prob = torch.sum(torch.sum(
            self.cough_cpd * d_expanded * fl_expanded,
            dim=0), dim=0)
        fever_prob = torch.sum(torch.sum(
            self.fever_cpd * d_expanded * fl_expanded,
            dim=0), dim=0)
        
        return {
            'Disease': disease_prob,
            'Flu': flu_prob,
            'Cough': cough_prob,
            'Fever': fever_prob
        }

    def inference(self, evidence):
        """
        Perform inference with given evidence
        """
        with torch.no_grad():
            return self.forward(evidence)

# Create and visualize the network
def create_graph():
    G = nx.DiGraph()
    
    # Add nodes
    nodes = ["Disease", "Flu", "Cough", "Fever"]
    for node in nodes:
        G.add_node(node)
    
    # Add edges
    edges = [("Disease", "Cough"), ("Disease", "Fever"),
            ("Flu", "Cough"), ("Flu", "Fever")]
    G.add_edges_from(edges)
    
    return G

# Initialize the model
model = BayesianNetwork()

# Create visualization
G = create_graph()
pos = {
    "Disease": (0, 1),
    "Cough": (-1, 0),
    "Fever": (1, 0),
    "Flu": (0, -1)
}

plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_size=1500, 
        node_color="skyblue", font_size=10, 
        font_weight="bold", arrowsize=20)
plt.title("Bayesian Belief Network using PyTorch")
plt.show()

# Function to print probabilities in a readable format
def print_probabilities(probs):
    for var, prob in probs.items():
        print(f"\n{var} probabilities:")
        for i, p in enumerate(prob):
            print(f"  State {i}: {p.item():.3f}")

# Example usage
print("Prior Probabilities:")
prior_probs = model.inference(None)
print_probabilities(prior_probs)

# Example inference with evidence
print("\nInference with evidence (Disease=1):")
evidence_probs = model.inference({'D': 1})
print_probabilities(evidence_probs)

print("\nInference with evidence (Flu=1):")
evidence_probs = model.inference({'FL': 1})
print_probabilities(evidence_probs)

# Training example (if you have data)
def train_model(model, data, num_epochs=100):
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
    criterion = nn.BCELoss()
    
    for epoch in range(num_epochs):
        optimizer.zero_grad()
        
        # Forward pass
        outputs = model(data['evidence'])
        
        # Calculate loss (this is a simplified example)
        loss = criterion(outputs['Cough'], data['target_cough'])
        loss += criterion(outputs['Fever'], data['target_fever'])
        
        # Backward pass and optimize
        loss.backward()
        optimizer.step()
        
        if epoch % 10 == 0:
            print(f'Epoch [{epoch}/{num_epochs}], Loss: {loss.item():.4f}')

# Example of how to use the trained model
def make_prediction(model, evidence):
    with torch.no_grad():
        predictions = model.inference(evidence)
        print("\nPredictions given evidence:", evidence)
        print_probabilities(predictions)

# Example predictions
print("\nExample predictions:")
make_prediction(model, {'D': 1, 'FL': 0})
