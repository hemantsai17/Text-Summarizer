from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'
def install_requirements(path:str)->List[str]:
    #This function will return list of requirements from requirements.txt
    req =[]
    with open(path) as file_obj:
        req= file_obj.readlines()
        new_req = [r.replace('\n','') for r in req]
        if HYPHEN_E_DOT in new_req:
            new_req.remove(HYPHEN_E_DOT)
        
    return new_req

setup(
    name="text_summarizer",
    version="0.1",
    packages=find_packages(),  # Automatically discovers all packages in `src`
    package_dir={"": "src"},  # Specify that packages are under the `src` directory
    install_requires=install_requirements('requirements.txt'),  # Add any dependencies your project needs
)
