from setuptools import setup


setup(
    name='PYVLTree',
    version='0.3.1',
    author='Daniel Alm Grundström',
    author_email='daniel.alm.grundstrom@protonmail.com',
    packages=[
        'pyvltree'
    ],
    test_suite='pyvltree.test',
    scripts=[],
    url='https://github.com/almgru/Algorithms',
    license='LICENSE.txt',
    description='Simple AVL tree implementation.',
    long_description=open('README.txt').read(),
    install_requires=[]
)
