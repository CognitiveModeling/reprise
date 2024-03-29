from setuptools import setup, find_packages


pkg = __import__('reprise')

author = pkg.__author__
email = pkg.__author_email__
version = pkg.__version__
classifiers = pkg.__classifiers__
description = pkg.__description__


def load_requirements(fn):
    """Read a requirements file and create a list that can be used in setup."""
    with open(fn, 'r') as f:
        return [x.rstrip() for x in list(f) if x and not x.startswith('#')]


setup(
    name='reprise',
    version=version,
    license='MIT',
    description=description,
    long_description=open('README.rst', encoding="utf-8").read(),
    author=author,
    author_email=email,
    url='https://github.com/CognitiveModeling/reprise',
    classifiers=classifiers,
    platforms='Linux',
    packages=find_packages(),
    install_requires=load_requirements('requirements.txt'),
    extras_require={
        'tests': [
            'pylint',
            'pytest',
            'pycodestyle'],
        'docs': [
            'sphinx >= 1.4',
            'sphinx_rtd_theme',
            'numpydoc',
            'easydev==0.9.35']},
)
