# Multi-Task Sentence Transformer with Layer-wise Learning Rates

## Project Overview
This project implements a **multi-task transformer model** designed for natural language processing (NLP) tasks. The model performs **sentence classification** and **Named Entity Recognition (NER)** simultaneously, sharing a common language backbone and using task-specific heads for each function. The approach includes:
- **Selective Freezing**: Controls which layers are trained for each task, preserving general language understanding while allowing task-specific fine-tuning.
- **Layer-wise Learning Rates**: Applies different learning rates to different layers to maximize efficiency and adaptivity in training.

## Key Features
- **Multi-Task Learning**: Handles multiple NLP tasks within one model, improving resource efficiency and model adaptability.
- **Efficient Training**: By leveraging selective freezing and layer-wise learning rates, the model retains valuable pre-trained language features while adapting to new tasks quickly.
- **Future Scalability**: The setup allows for easy addition of new tasks with minimal retraining.

## File Structure
```plaintext
multi_task_transformer/
├── README.md                # Project overview and instructions
├── requirements.txt         # List of dependencies
├── write_up.md              # Key decisions and insights for Tasks 3 and 4
└── src/
    ├── model.py             # Multi-task model implementation
    ├── train.py             # Training script with layer-wise learning rates


## Setup Instructions

##1 Install Dependencies
- pip install -r requirements.txt

##2 Run the Training Script.
- python src/train.py

This script will:

Initialize the model.
Apply selective freezing and layer-wise learning rates.
Train the model for both sentence classification and NER tasks.

## Key Decisions and Insights

Our approach uses selective freezing and layer-wise learning rates to maximize model efficiency and adaptability:

- Selective Freezing: Allows us to train only specific parts of the model, preserving general language knowledge in core layers and focusing updates on task-specific heads.
- Layer-wise Learning Rates: Helps balance foundational language retention with task-specific specialization by applying different learning rates to each layer. This enables faster convergence and better generalization across tasks.


---

### Explanation of Each Section

1. **Project Overview**: Briefly explains the purpose and high-level goals of the project.
2. **Key Features**: Highlights the project’s strengths, especially the multi-task learning and efficient training.
3. **File Structure**: Helps users understand the contents and organization of the repository.
4. **Setup Instructions**: Provides the steps to install dependencies and run the training script.
5. **Key Decisions and Insights**: Summarizes important design choices, making the project’s approach clear to stakeholders and contributors.
6. **Dependencies**: Lists the main libraries used, referencing `requirements.txt`.
7. **Contributing and License**: Encourages contributions and clarifies the licensing terms.

This `README.md` is comprehensive and will help anyone new to the project understand its purpose, structure, and how to get started. Let me know if you’d like further customization!

