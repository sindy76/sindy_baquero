
from setuptools import setup,find_packages

setup (
    name= "sindy_baquero",
    version= "0.0.1",
    author= "Sindy Baquero",
    author_email= "sindy.baquero@est.iudigital.edu.co",
    description= "",
    py_modules= ["Entregable actividad 1 y 2"],
    install_requires= [
        "kagglehub[pandas-datasets]>=0.3.8",
        "kaggle",
        "matplotlib>=3.5.0",
        "seaborn>=0.11.2",
        "pandas",
        "numpy",
        "matplotlib",
        "openpyxl",
        "requests"
 ]
 )