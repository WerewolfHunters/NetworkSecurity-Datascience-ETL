from setuptools import setup, find_packages
from typing import List


def get_requirements() -> List[str]:
    """
    This function will return the list of requirements
    """
    requirements_lst:List[str] = []
    try:
        with open("requirements.txt", 'r') as file:
            # Read lines from the file
            lines = file.readlines()

            # Process each lines
            for line in lines:
                requirements = line.strip()

                if requirements and requirements != "-e .":
                    requirements_lst.append(requirements)

    except FileNotFoundError:
        print("requirements.txt file was not found")
    
    return requirements_lst

setup(
    name="NetworkSecurity-DataScience",
    version="0.0.1",
    author="Awwab Mahimi",
    author_email="awwab.mahimi.0074@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)