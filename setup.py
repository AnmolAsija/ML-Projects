## We Can considered it as the meta data information
from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:

    '''
    this function will return the list of requirements

    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
name = 'ML Project',
version='0.0.1',
author='Anmol',
author_email='anmolasija243@gmail.com',
packages=find_packages(),## it find packages automatically
install_requires = get_requirements('requirements.txt')



)

# 🧩 What is -e . in requirements.txt?
# -e stands for editable mode.
# -e . means: "Install this project in editable mode from the current directory (.)".
# This is used during development so that any changes you make in your code are immediately reflected without reinstalling the package.

# 🔸 Why is -e . sometimes included in requirements.txt?
# When you're working on a Python project — especially one with a setup.py — your dependencies are usually listed in a requirements.txt file like this:

# numpy
# pandas
# scikit-learn
# -e .
# Now let’s explain why that last line -e . is included 👇

# ✅ The Purpose of -e . in requirements.txt
# When a developer (or team) wants to set up a project from scratch using just one command like:

# pip install -r requirements.txt
# they often include -e . at the end of the file.

# ⚙️ What Does pip install -r requirements.txt Do Here?
# It tells pip to:

# Install numpy

# Install pandas

# Install scikit-learn

# And finally — install your own project (the current folder .) in editable mode (-e)

# So all the external dependencies + your local package are installed in a single command.

# 🔍 Real-Life Use Case:
# You're working on a machine learning project with this folder structure:

# arduino
# Copy
# Edit
# ML-Project/
# ├── src/
# │   └── ml_project/
# │       ├── __init__.py
# │       ├── model.py
# ├── setup.py
# ├── requirements.txt
# You include this in requirements.txt:

# numpy
# scikit-learn
# -e .
# Now, a new developer (or your future self) can simply clone the repo and run:

# pip install -r requirements.txt
# And everything will be installed, including your local project in editable mode — no need to separately run pip install -e ..

# 🧠 Summary: When to Include -e .
# Situation	Should You Include -e . in requirements.txt?
# You want to install dependencies AND your local project in one step	   ✅ Yes
# You’re writing install_requires in setup.py	                     ❌ No — skip -e . there
# You want to avoid others forgetting to install your package	        ✅ Yes — it's helpful


# pip install -r requirements.txt
# will:
# Install numpy & pandas
# Look for setup.py in the current folder and install your project in editable mode