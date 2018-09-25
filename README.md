[![travis](https://travis-ci.org/bjpop/pdb_add_chain.svg?branch=master)](https://travis-ci.org/bjpop/pdb_add_chain)

# Overview 

In the examples below, `$` indicates the command line prompt.

# Licence

This program is released as open source software under the terms of [BSD-3-Clause License](https://raw.githubusercontent.com/bjpop/pdb_add_chain/master/LICENSE).

# Installing

Clone this repository: 
```
$ git clone https://github.com/bjpop/pdb_add_chain
```

Move into the repository directory:
```
$ cd pdb_add_chain
```

Pdb_add_chain can be installed using `pip` in a variety of ways (`$` indicates the command line prompt):

1. Inside a virtual environment:
```
$ python3 -m venv pdb_add_chain_dev
$ source pdb_add_chain_dev/bin/activate
$ pip install -U /path/to/pdb_add_chain
```
2. Into the global package database for all users:
```
$ pip install -U /path/to/pdb_add_chain
```
3. Into the user package database (for the current user only):
```
$ pip install -U --user /path/to/pdb_add_chain
```


# General behaviour


Example usage:
```
pdb_add_chain --in example.pdb --out output.pdb
```

## Help message

Pdb_add_chain can display usage information on the command line via the `-h` or `--help` argument:

```
$ pdb_add_chain -h
usage: pdb_add_chain [-h] [--version] [--log LOG_FILE] [--input PDB_FILE]
                     [--output PDB_FILE]

Read one or more FASTA files, compute simple stats for each file

optional arguments:
  -h, --help         show this help message and exit
  --version          show program's version number and exit
  --log LOG_FILE     record program progress in LOG_FILE
  --input PDB_FILE   Input PDB file
  --output PDB_FILE  Output PDB file
```


## Logging

If the ``--log FILE`` command line argument is specified, pdb_add_chain will output a log file containing information about program progress. The log file includes the command line used to execute the program, and a note indicating which files have been processes so far. Events in the log file are annotated with their date and time of occurrence. 


# Exit status values

Pdb_add_chain returns the following exit status values:

* 0: The program completed successfully.
* 1: File I/O error. This can occur if at least one of the input FASTA files cannot be opened for reading. This can occur because the file does not exist at the specified path, or pdb_add_chain does not have permission to read from the file. 
* 2: A command line error occurred. This can happen if the user specifies an incorrect command line argument. In this circumstance pdb_add_chain will also print a usage message to the standard error device (stderr).


