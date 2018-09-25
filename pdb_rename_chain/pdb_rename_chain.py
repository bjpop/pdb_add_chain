'''
Module      : Main
Description : The main entry point for the program.
Copyright   : (c) Bernie Pope, 25 Sep 2018 
License     : BSD-3-Clause 
Maintainer  : bjpope@unimelb.edu.au 
Portability : POSIX
'''

from argparse import ArgumentParser
import sys
import logging
import pkg_resources
from Bio import SeqIO
from Bio.PDB.PDBParser import * 
from Bio.PDB.Chain import Chain
from Bio.PDB import PDBIO


EXIT_FILE_IO_ERROR = 1
EXIT_COMMAND_LINE_ERROR = 2
DEFAULT_VERBOSE = False
PROGRAM_NAME = "pdb_rename_chain"


try:
    PROGRAM_VERSION = pkg_resources.require(PROGRAM_NAME)[0].version
except pkg_resources.DistributionNotFound:
    PROGRAM_VERSION = "undefined_version"


def exit_with_error(message, exit_status):
    '''Print an error message to stderr, prefixed by the program name and 'ERROR'.
    Then exit program with supplied exit status.

    Arguments:
        message: an error message as a string.
        exit_status: a positive integer representing the exit status of the
            program.
    '''
    logging.error(message)
    print("{} ERROR: {}, exiting".format(PROGRAM_NAME, message), file=sys.stderr)
    sys.exit(exit_status)


def parse_args():
    '''Parse command line arguments.
    Returns Options object with command line argument values as attributes.
    Will exit the program on a command line error.
    '''
    description = 'Rename chain in PDB file'
    parser = ArgumentParser(description=description)
    parser.add_argument('--version',
                        action='version',
                        version='%(prog)s ' + PROGRAM_VERSION)
    parser.add_argument('--log',
                        metavar='LOG_FILE',
                        type=str,
                        help='record program progress in LOG_FILE')
    parser.add_argument('--old',
                        metavar='CHAIN_ID',
                        type=str,
                        required=True,
                        help='Replace this ID with --new')
    parser.add_argument('--new',
                        metavar='CHAIN_ID',
                        type=str,
                        required=True,
                        help='Replace --old with this ID')
    parser.add_argument('--input',
                        metavar='PDB_FILE',
                        required=True,
                        type=str,
                        help='Input PDB file')
    parser.add_argument('--output',
                        metavar='PDB_FILE',
                        required=True,
                        type=str,
                        help='Output PDB file')
    return parser.parse_args()


def process_file(options):
    logging.info("Processing PDB file from %s", options.input)
    parser = PDBParser()
    structure = parser.get_structure('structure', options.input)
    model=structure[0]
    #new_chain = Chain("A")
    new_chain = Chain(options.new)
    old_chain = [] 
    for chain in model.get_chains():
        if chain.get_id() == options.old:
            old_chain.append(chain)
            for residue in chain.get_residues():
                new_chain.add(residue)
            # We assume there is only one chain in the file
            # and ignore any remaining chains
            break
    for chain in old_chain:
        model.detach_child(chain.get_id())
    model.add(new_chain)
    io=PDBIO()
    io.set_structure(model)
    io.save(options.output)
       
       

def init_logging(log_filename):
    '''If the log_filename is defined, then
    initialise the logging facility, and write log statement
    indicating the program has started, and also write out the
    command line from sys.argv

    Arguments:
        log_filename: either None, if logging is not required, or the
            string name of the log file to write to
    Result:
        None
    '''
    if log_filename is not None:
        logging.basicConfig(filename=log_filename,
                            level=logging.DEBUG,
                            filemode='w',
                            format='%(asctime)s %(levelname)s - %(message)s',
                            datefmt='%m-%d-%Y %H:%M:%S')
        logging.info('program started')
        logging.info('command line: %s', ' '.join(sys.argv))


def main():
    "Orchestrate the execution of the program"
    options = parse_args()
    init_logging(options.log)
    process_file(options)


# If this script is run from the command line then call the main function.
if __name__ == '__main__':
    main()
