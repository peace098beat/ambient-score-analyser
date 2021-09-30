from setuptools import setup, find_packages

setup(
    name='amb',
    version='0.1',
    # package_dir = {'': 'src'},
    packages=find_packages("src"),
    # py_modules=['featurizer', "monolizer", "pipeline", "script"],
    install_requires=[
        'Click',
        'mosqito',
        'numpy',
        'matplotlib',
        'japanize-matplotlib',
    ],
    entry_points='''
        [console_scripts]
        amb=amb.script:cli
    ''',
)