from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."  # Fixed typo in variable name

def get_requirements(file_path:str) -> List[str]:
    """This function will return the list of requirements"""
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements


setup(
name = 'mlopsproject',
version = '0.0.1', 
author= 'Dushyant', 
author_email= 'dushyant.singh.civ16@itbhu.ac.in',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')

)

#it find src by seacrhing __init__.py file