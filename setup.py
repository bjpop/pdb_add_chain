#!/usr/bin/env python

from distutils.core import setup

LONG_DESCRIPTION = \
'''The program reads one or more input FASTA files. 
For each file it computes a variety of statistics, and then
prints a summary of the statistics as output.
        
The goal is to provide a solid foundation for new bioinformatics command line tools,
and is an ideal starting place for new projects.'''


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
    description=('A prototypical bioinformatics command line tool'),
    long_description=(LONG_DESCRIPTION),
    install_requires=["biopython==1.66"],
)
