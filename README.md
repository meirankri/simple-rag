## Simple RAG system with ollama and groq


# RAG Project Setup and Usage Guide

This README provides detailed instructions on how to set up and run the RAG (Retriever-And-Generator) project using Jupyter notebooks for embedding data and querying. Follow these steps to ensure proper setup and operation.

## Prerequisites

Ensure you have the following installed on your system:
- Python 3.8 or higher
- pip (Python package installer)
- Jupyter Notebook or JupyterLab

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/meirankri/simple-rag.git
   cd rag-project
   ```

2. **Set up a Python virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Unix or MacOS
   venv\Scripts\activate  # For Windows
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Jupyter (if not already installed):**
   ```bash
   pip install jupyterlab
   ```

5. **Start JupyterLab:**
   ```bash
   jupyter lab
   ```

## Running the Project

### Step 1: Initialize the Embeddings

Open the `embedding.ipynb` notebook in JupyterLab. This notebook contains the code to prepare and generate the embeddings necessary for querying with the RAG model.

- Follow the instructions within the notebook to run the cells.
- Make sure all data paths and configurations are set according to your dataset and environment.

### Step 2: Query the Data

Once the embeddings are initialized, proceed to the `app.ipynb` notebook. This notebook will use the embeddings to retrieve and generate responses based on your queries.

- Run the notebook cells sequentially to interact with the RAG model.
- Input your queries as instructed in the notebook to see the responses generated.

## Additional Information

- **Configuration**: Adjust settings  directly within each notebook as needed for paths, model parameters, etc.
- **Data Management**: Ensure your data is placed in the appropriate directories or adjust the path settings in the notebooks accordingly.
- **Troubleshooting**: Check the output cells in the notebooks for error messages or issues.

## Contact

For more information or assistance, please reach out to [meirankri@gmail.com](mailto:meirankri@gmail.com).

---

Thank you for using the RAG project. We hope it enhances your data querying capabilities!
```