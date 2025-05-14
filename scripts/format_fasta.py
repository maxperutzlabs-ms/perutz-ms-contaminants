# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "profasta==0.0.5",
# ]
# ///

"""Format sequences of a FASTA file.

This script reformats the sequence entries of a FASTA file to ensure line breaks occur 
after every 60 characters. The input file is overwritten with the reformatted content.

Usage example:
    python format_fasta.py input.fasta
"""

import sys

import profasta.db

if __name__ == "__main__":
    fasta_path = sys.argv[1]

    print(f"Reading FASTA file: '{fasta_path}'")
    db = profasta.db.ProteinDatabase()
    db.add_fasta(fasta_path, header_parser="default")
    print(f"Writing formatted FASTA file: '{fasta_path}'")
    db.write_fasta(fasta_path, header_writer="default")
