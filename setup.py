#!/usr/bin/env python

from distutils.core import setup

LONG_DESCRIPTION = \
'''Add a chain ID to a PDB file'''

setup(
    name='pdb_add_chain',
    version='0.1.0.0',
    author='Bernie Pope',
    author_email='bjpope@unimelb.edu.au',
    packages=['pdb_add_chain'],
    package_dir={'pdb_add_chain': 'pdb_add_chain'},
    entry_points={
        'console_scripts': ['pdb_add_chain = pdb_add_chain.pdb_add_chain:main']
    },
    url='https://github.com/bjpop/pdb_add_chain',
    license='LICENSE',
    description=('Add a chain ID to a PDB file'),
    long_description=(LONG_DESCRIPTION),
    install_requires=["biopython", "numpy"],
)
