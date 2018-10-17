from setuptools import setup


setup(
    name='pyvltree',
    version='0.3.2',
    author='Daniel Alm Grundström',
    author_email='daniel.alm.grundstrom@protonmail.com',
    packages=[
        'pyvltree'
    ],
    test_suite='pyvltree.test',
    scripts=[],
    url='https://github.com/almgru/pyvl-tree',
    license='LICENSE.txt',
    description='Simple AVL tree implementation.',
    long_description=open('README.rst', 'rt').read(),
    install_requires=[]
)
