# -*- coding: utf-8 -*-
"""train.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/151VUE2G8dOTc3dh26bxkhY4IdOtoYM1d
"""

import torch
from transformers import AutoModel, AutoTokenizer

class MultiTaskSentenceTransformer(torch.nn.Module):
    def __init__(self, model_name="bert-base-uncased", num_classes=3, num_ner_labels=5):
        super(MultiTaskSentenceTransformer, self).__init__()
        self.transformer = AutoModel.from_pretrained(model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

        # Task-specific heads
        self.classification_head = torch.nn.Linear(self.transformer.config.hidden_size, num_classes)
        self.ner_head = torch.nn.Linear(self.transformer.config.hidden_size, num_ner_labels)

    def forward(self, sentences, task="classification"):
        inputs = self.tokenizer(sentences, return_tensors="pt", padding=True, truncation=True)
        outputs = self.transformer(**inputs)

        if task == "classification":
            pooled_output = outputs.last_hidden_state.mean(dim=1)
            return self.classification_head(pooled_output)

        elif task == "ner":
            token_embeddings = outputs.last_hidden_state
            return self.ner_head(token_embeddings)

import torch

# Initialize model and optimizer with layer-wise learning rates
model = MultiTaskSentenceTransformer()

# Define layer-wise learning rates
optimizer_params = [
    {"params": model.transformer.embeddings.parameters(), "lr": 1e-5},
    {"params": model.transformer.encoder.layer[:6].parameters(), "lr": 2e-5},
    {"params": model.transformer.encoder.layer[6:].parameters(), "lr": 3e-5},
    {"params": model.classification_head.parameters(), "lr": 5e-5},
    {"params": model.ner_head.parameters(), "lr": 5e-5}
]

optimizer = torch.optim.AdamW(optimizer_params)

# Sample training loop
num_epochs = 3
for epoch in range(num_epochs):
    model.train()

    # Sample input data
    sentences = ["I love AI.", "Transformers are powerful."]
    labels_classification = torch.tensor([0, 1])  # Classification labels

    # Define NER labels with padding tokens (-100 for padding)
    # NER labels must match the length of tokenized inputs
    labels_ner = [
        [1, 2, -100, -100],  # Labels for the first sentence
        [3, 4, 1, -100]      # Labels for the second sentence
    ]

    # Tokenize sentences and get attention mask
    tokenized_inputs = model.tokenizer(sentences, return_tensors="pt", padding=True, truncation=True)
    max_len = tokenized_inputs["input_ids"].shape[1]

    # Pad labels_ner to match the length of tokenized inputs
    padded_labels_ner = []
    for label in labels_ner:
        label += [-100] * (max_len - len(label))  # Add padding to reach max_len
        padded_labels_ner.append(label)

    # Convert labels_ner to a tensor
    labels_ner_tensor = torch.tensor(padded_labels_ner)

    # Forward pass for classification task
    outputs_classification = model(sentences, task="classification")
    loss_classification = torch.nn.CrossEntropyLoss()(outputs_classification, labels_classification)

    # Forward pass for NER task
    outputs_ner = model(sentences, task="ner")

    # Calculate NER loss with padding ignored
    loss_ner = torch.nn.CrossEntropyLoss(ignore_index=-100)(
        outputs_ner.view(-1, outputs_ner.size(-1)), labels_ner_tensor.view(-1)
    )

    # Combine losses for both tasks
    loss = loss_classification + loss_ner

    # Backward pass and optimization
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    print(f"Epoch {epoch + 1}, Loss: {loss.item()}")
