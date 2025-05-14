# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "profasta==0.0.5",
# ]
# ///

"""Add a contaminant tag to the protein identifiers in a FASTA file.

This script reads a FASTA file that does not contain a contaminant tag in the
protein identifiers and adds the contaminant tag "contam_" to each identifier. The
output is saved in a new FASTA file with the same name as the input file, but with
"_notag_" replaced by "_".

Usage example:
    `python add_contam_tag_to_fasta.py input_notag.fasta``
"""

import sys

import profasta.db

if __name__ == "__main__":
    fasta_path_input = sys.argv[1]
    if "_notag_" not in fasta_path_input:
        raise ValueError(
            (
                "Input file name must contain '_notag_' to indicate it does not have "
                "the contaminant tag."
            )
        )
    fasta_path_output = fasta_path_input.replace("_notag_", "_")
    contam_tag = "contam_"

    print(f"Reading FASTA file: '{fasta_path_input}'")
    db = profasta.db.ProteinDatabase()
    db.add_fasta(fasta_path_input, header_parser="uniprot_like")
    for protein in db.values():
        new_id = contam_tag + protein.header_fields["identifier"]
        protein.header_fields["identifier"] = new_id

    print(f"Writing FASTA file with contaminants tag: '{fasta_path_output}'")
    db.write_fasta(fasta_path_output, header_writer="uniprot_like")
