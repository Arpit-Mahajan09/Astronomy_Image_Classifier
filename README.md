# Astronomy_Image_Classifier

An end-to-end deep learning pipeline built with PyTorch to classify astronomical objects into 5 morphological categories. The project uses ResNet18 and Gradio.

---

## Dataset Sources Used

The final dataset contains a collection of **782 images** evenly distributed across 5 classes:

1. **Spiral Galaxies (0):** Extracted from the [Galaxy Zoo - The Galaxy Challenge](https://www.kaggle.com/competitions/galaxy-zoo-the-galaxy-challenge) dataset. Filtered via `pandas` to isolate highly confident samples where human votes met a certain threshold.
2. **Elliptical Galaxies (1):** Isolated from the *Galaxy Zoo* dataset using voting probability consensus. 
3. **Nebulae (2):** Scrapped fromt the **NASA/Hubble Image API** using targeted keyword  searches(`nebula`).
4. **Planetary Objects (3):** Used [Planets and Moons Dataset](https://www.kaggle.com/datasets/emirhanai/planets-and-moons-dataset-ai-in-space), by Julian Emirhan Bulut on kaggle. 
5. **Star Clusters (4):** Scrapped from a NASA hubble astronomical archives.


## Setup & Installation Instructions

Best way to use would be forking the kaggle notebook made by me
[Kaggel Notebook Link](https://www.kaggle.com/code/arpitmahajan09/astronomy-image-classifier)


**Local Setup Guide**

1. Environment Requirements
- Python 3.10+ environment equipped with a CUDA-compatible GPU framework. Install the dependencies using pip:

```Bash
pip install -r requirement.txt
```

2. File Organization

Before initiating training, execute the following code to unzip the galaxy-zoo dataset into your local workspace:

```Python
import zipfile
import os

os.makedirs("/kaggle/working/galaxy_zoo/images", exist_ok=True)

with zipfile.ZipFile("/kaggle/input/competitions/galaxy-zoo-the-galaxy-challenge/training_solutions_rev1.zip", 'r') as z:
    z.extractall("/kaggle/working/galaxy_zoo/")

with zipfile.ZipFile("/kaggle/input/competitions/galaxy-zoo-the-galaxy-challenge/images_training_rev1.zip", 'r') as z:
    z.extractall("/kaggle/working/galaxy_zoo/images")
```

## Inference Time

Average Execution Speed: ~8.5 ms per image (Tested on NVIDIA T4 GPU accelerator environment).

Efficiency Analysis: The sub-10ms latency is achieved due to the use of ResNet18 and direct compilation of the classification tensor. This makes the architecture suited for real-world deployments and real-time interactive frames.

