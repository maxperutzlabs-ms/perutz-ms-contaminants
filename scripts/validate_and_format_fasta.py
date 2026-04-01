# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "profasta==0.1.1",
# ]
# ///

"""Validate and format a UniProtKB-compliant FASTA file.

This script validates that FASTA entries adhere to the UniProtKB header format and
reformats the sequence entries to ensure line breaks occur after every 60 characters.
The input file is overwritten with the validated and reformatted content.

Usage example:
    python validate_and_format_fasta.py input.fasta

Raises:
    KeyError: If the FASTA file contains entries with duplicate identifiers.
    ValueError: If the FASTA file contains headers that cannot be parsed with the
        "uniprot" header parser.
    ValueError: If the FASTA file contains non-ASCII characters in the headers.
"""

import logging
import sys

import profasta.db

LOGGER = logging.getLogger(__name__)

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    fasta_path = sys.argv[1]

    LOGGER.info(f"Reading FASTA file: '{fasta_path}'")
    db = profasta.db.ProteinDatabase.from_fasta(
        fasta_path,
        header_parser="uniprot",
        overwrite=False,
        skip_invalid=False,
    )

    issues = profasta.validation.find_header_ascii_issues(db.values())
    for issue in issues:
        LOGGER.warning(
            f"Found non-ASCII characters {issue.non_ascii_characters} in header: "
            f"{issue.header}"
        )
    if issues:
        raise ValueError(
            "FASTA file contains non-ASCII characters in headers. "
            "Please fix these issues before updating the FASTA file."
        )
    LOGGER.info(f"Finished validation, writing formatted FASTA file: '{fasta_path}'")
    db.write_fasta(fasta_path, header_writer="default", line_width=60)
