from setuptools import setup

with open("README.md","r") as f:
    description_more = f.read()
    
setup(
    name='family_project',
    version='0.1',  
    description='Geektrust Family tree problem',
    author='Lahari Sengupta',
    author_email='jhinik8@gmail.com',
    packages=['family_project'],

    classifiers=[ 
        'Operating System :: OS Independent',        
        'Programming Language :: Python :: 3',
    ],
)