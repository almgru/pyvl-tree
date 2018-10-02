from distutils.core import setup


setup(
    name='PYVLTree',
    version='0.2.0',
    author='Daniel Alm Grundström',
    author_email='daniel.alm.grundstrom@protonmail.com',
    packages=[
        'pyvltree',
        'pyvltree.test'
    ],
    scripts=[],
    url='https://github.com/almgru/Algorithms',
    license='LICENSE.txt',
    description='Simple AVL tree implementation.',
    long_description=open('README.txt').read(),
    install_requires=[]
)
