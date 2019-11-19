from setuptools import setup

setup(
    name='ec2snapshoter',
    version='0.1',
    author="Jaime Ramirez",
    author_email="ramirja@gmail.com",
    description="Ec2Snapshoter is a toold to manager AWS EC2 snapshots",
    license="GPLv3+",
    packages=['shotty'],
    url="https://github.com/ramirja/ec2snapshoter",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',

)