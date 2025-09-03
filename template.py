import os
from pathlib import Path
import logging

# Define the list of files and folders to be created
list_of_files = [
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/__init__.py",
    "src/utils/logger.py",
    "src/utils/exception.py",
    "requirements.txt",
    "setup.py",
    "README.md",
]

for filepath in list_of_files:
    filepath = os.path.join(os.getcwd(), filepath)  # absolute path
    filedir, filename = os.path.split(filepath)     
    
    # Create directory if it doesn’t exist
    if filedir != "" and not os.path.exists(filedir):
        os.makedirs(filedir, exist_ok=True)
        print(f"📂 Created directory: {filedir}")

    # Create the file if it doesn’t exist or empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        print(f"📄 Created file: {filepath}")
    else:
        print(f"✅ File already exists: {filepath}")
