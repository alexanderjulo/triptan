from setuptools import setup, find_packages

setup(
    name='flexigrate',
    version='0.1.0',
    description='Datastore independent migration tool',
    author='Alexander Jung-Loddenkemper',
    author_email='alexander@julo.ch',
    packages=find_packages(),
    install_requires=[
        'Click==6.0',
        'click-log==0.1.4',
        'PyYAML==3.11',
        'jinja2==2.7.3'
    ],
    entry_points={
        'console_scripts': ['flexigrate=flexigrate.cli:main']
    }
)