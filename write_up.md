# Task 3 & 4 Write-up
## Key Decisions
## Selective freezing for efficient learning.

1) Efficiency with Selective Freezing:

- We applied selective freezing to different parts of the model, focusing on adapting specific areas while preserving core language knowledge.
- This approach allows us to leverage the foundational language understanding built into the model, without spending additional resources on unnecessary updates. It’s particularly effective for multi-task models where certain parts of the model are shared across tasks.

2) Optimized Training Scenarios:

- Full Freezing (Except Task Heads): For scenarios where the model’s pre-trained language features align closely with task needs, freezing the entire network except the task-specific heads reduces the cost of training and minimizes the risk of overfitting.
- Freezing Only the Backbone: When the main model (backbone) already has a strong language understanding, we can allow only the task-specific heads to adapt. This keeps the backbone stable while fine-tuning the specific outputs, achieving greater efficiency and stability.
- Freezing One Task Head: In a multi-task environment, we can choose to freeze one task head while training the other. This lets us focus on improving one task without affecting the performance of a task that already works well with the existing model.

3) Strategic Transfer Learning:

- We used a powerful pre-trained transformer model that captures general language features. By selectively unfreezing certain layers, we allow the model to adapt to new tasks without changing its core language understanding.
- This method allows faster adaptation and better alignment with the specialized requirements of each task, making it cost-effective and impactful.

Key Insight: Selective freezing and transfer learning offer a balanced way to use pre-trained knowledge while efficiently adapting to each task’s unique needs.

## Layer-wise learning rates improve adaptation to tasks.
1) Customized Learning Rates per Layer:

- Lower Layers (Minimal Change): The foundational layers retain general language patterns and therefore use smaller learning rates. This ensures that we preserve the core language knowledge that benefits all tasks.
- Middle to Higher Layers (Focused Adaptation): Slightly higher learning rates allow these layers to adapt moderately, maintaining both general and task-specific patterns.
- Task-specific Heads (Full Adaptability): The highest learning rate is applied to task-specific heads to allow quick and effective tuning. This ensures each task benefits from specialized attention.

2) Benefits of Layer-wise Learning Rates:

- Efficient and Effective Training: By focusing learning rate adjustments on task-specific areas, the model can adapt efficiently without affecting core knowledge. This selective approach reduces the training time needed for effective results.
- Enhanced Multi-task Performance: Layer-wise learning rates prevent overfitting in shared layers, ensuring the model’s general language understanding remains intact. Task-specific layers gain the flexibility needed to improve each task’s performance individually.

Key Insight: Layer-wise learning rates enable us to adapt the model thoughtfully, focusing on task-specific improvements without losing foundational strengths. This is especially valuable for multi-task learning, as it maintains a stable shared understanding across tasks while optimizing each task’s performance.