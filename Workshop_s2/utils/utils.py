import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objs as go
# Set random seed for reproducibility
np.random.seed(42)


def generate_data(num_samples: int = 100):
    # Generate synthetic data
    # Random values in the range [0, 10)
    x1 = np.random.rand(num_samples, 1) * 10
    # Random values in the range [0, 10)
    x2 = np.random.rand(num_samples, 1) * 10
    noise = np.random.randn(num_samples, 1) * 2  # Gaussian noise

    # Apply the non-linear equation
    y = 2 * x1**2 + 3 * x2 + np.sin(x1) - np.cos(x2) + noise

    return x1, x2, y


def plot_data(x1, x2, y):
    # Create a 3D scatter plot
    fig = go.Figure(data=[go.Scatter3d(
        x=x1.flatten(),
        y=x2.flatten(),
        z=y.flatten(),
        mode='markers',
        marker=dict(
            size=5,
            opacity=0.8,
        )
    )])

    # Update plot layout
    fig.update_layout(title='Non-linear Synthetic Dataset with 2 Inputs and 1 Output',
                      scene=dict(
                          xaxis_title='Feature 1',
                          yaxis_title='Feature 2',
                          zaxis_title='Target'
                      ),
                      autosize=False,
                      width=800,
                      height=600,
                      margin=dict(l=65, r=50, b=65, t=90))

    return fig

# Function to plot images
def plot_images(images, labels, nrows, ncols):
    class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 
               'dog', 'frog', 'horse', 'ship', 'truck']

    """Plot nrows x ncols images from images and labels."""
    fig, axes = plt.subplots(nrows, ncols)
    fig.subplots_adjust(hspace=0.5, wspace=0.5)
    for i, ax in enumerate(axes.flat):
        # Plot image
        ax.imshow(images[i])
        # Remove ticks
        ax.set_xticks([])
        ax.set_yticks([])
        # Set label
        label = class_names[labels[i][0]]
        ax.set_xlabel(label)
    plt.show()