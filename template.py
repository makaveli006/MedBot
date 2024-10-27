import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trials.ipynb"
]

# list_of_files = [
#     "src/__init__.py",
#     "src/helper.py",
#     "src/prompt.py",
#     ".env",
#     "requirements.txt",
#     "setup.py",
#     "app.py",
#     "research/trials.ipynb"
# ]

for filepath in list_of_files:
    # print(filepath)
    filepath = Path(filepath)
    # Forward slash is converted to Backward slash.
    # print(type(filepath))
    print(filepath)
    filedir, filename = os.path.split(filepath)
    # print(filedir)
    # print(filename)

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        # os.makedirs(filedir,exist_ok=False)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) ==0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exists")