from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """
    This function will return list of requirements
    """
    req_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            # Read lines from file
            lines = file.readlines()
            # Process each line
            for line in lines:
                req = line.strip()
                # Ignore empty line and -e .
                if req and req!='-e .':
                    req_lst .append(req)
    except FileNotFoundError:
        print("requirements.txt not found")

    return req_lst

setup(
    name="NetworkSecurity",
    version = '0.0.1',
    author = "Shiladitya Mondal",
    author_email="shiladityam178@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)