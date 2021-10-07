from setuptools import setup, find_packages

setup(
    name='amb',
    version='0.2',
    packages=["amb"],
    install_requires=[
        'mosqito',
        'numpy',
        'matplotlib',
        'japanize-matplotlib',
        'Click',
    ],
    entry_points='''
        [console_scripts]
        amb=amb.script:cli
        amb-hello=amb.script:hello
    ''',
)