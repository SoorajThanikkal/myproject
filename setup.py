from setuptools import setup, find_packages

setup(
    name='myproject',
    version='1.0.0',
    author='sooraj',
    author_email='tpsooraj7@gmail.com',
    description='Detection',
    packages=find_packages(),
    install_requires=[
        'scikit-learn==0.0.post12'
        
    ],
)