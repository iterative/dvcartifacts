from setuptools import setup, find_packages

setup(
    name='dvcartifact',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'google-cloud-storage',
        'boto3',
        'gitPython',
        ],
    entry_points='''
        [console_scripts]
        greet=my_cli_tool.cli:greet
    ''',
)
