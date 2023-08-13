from setuptools import setup, find_packages

setup(
    name='sharkpyro',
    version='1.4.4',
    description='Pyrogram fork for SharkUserBot',
    author="Dan",
    author_email="dan@pyrogram.org",
    packages=find_packages(),
    install_requires=[
        'tgcrypto',
    ],
)
