# Perutz MS Facility - Protein Contaminants Repository

Welcome to the **Protein Contaminants Repository** of the Max Perutz Labs MS Facility. In mass spectrometry experiments, it's crucial to account for potential contaminants that may interfere with accurate protein identification. This repository is dedicated to managing and versioning our custom FASTA contaminants file that we use in our facility service.

## Previous Releases

If you're looking for a previous version of the contaminants file, you can find a downloadable version in the [GitHub Releases](https://github.com/maxperutzlabs-ms/perutz-ms-contaminants/releases) section.


## About the contaminants FASTA file

To ensure compatibility with a wide range of bioinformatics software, the contaminants FASTA file should only contain UniProtKB entries or entries have to adhere to the UniProtKB format, which is outlined in detail on [uniprot.org](https://www.uniprot.org/help/fasta-headers).

The UniProtKB format is specified as follows:

> \>db|UniqueIdentifier|EntryName ProteinName OS=OrganismName OX=OrganismIdentifier GN=GeneName PE=ProteinExistence SV=SequenceVersion

For custom protein entries not present in the UniProt database, such as protein tags, engineered proteins, or synthetic constructs, a specific convention is followed. The `db` field is set as "xx," `OrganismName` is designated as "Synthetic," and `OrganismIdentifier` is specified as "0000." Moreover, special care should be taken to ensure that the `UniqueIdentifier` does not overlap with any existing UniProt Accession number.

## Repository Structure

- **/archive**: This directory contains previous versions of the contaminants file that are not part of the Git version history.
- **contaminants_YYYY_NN.fasta:** The main contaminants file used in current projects of the MS facility. The file is named according to the convention `contaminants_YEAR_NUMBER.fasta`, where YEAR represents the current year, and NUMBER is a running index with two digits reset to 1 each year. The UniProt `UniqueIdentifiers` of FASTA entries are prefixed with **contam_** to indicate that they originate from a contaminants FASTA file.
    - For example, `>sp|P13646|K1C13_HUMAN` becomes `>sp|contam_P13646|K1C13_HUMAN`.
- **contaminants_notag_YYYY_NN.fasta:** Identical to the main contaminants file, with the sole distinction that the `UniqueIdentifier` of each entry is not prefixed with the **contam_** tag.

## Updating the Contaminants File

All updates to the contaminants FASTA files should be made on the **`wip`** (work-in-progress) branch. These changes are only merged into the `main` branch when a new version is ready to be released. File names are updated to reflect the new release version in the `main` branch before releasing.

To update the contaminants FASTA file with new entries, follow these steps:

1. **Add entries**: Add your new protein entries to the `contaminants_notag_YYYY_NN.fasta` file on the `wip` branch. Entries must have a valid UniProtKB header format and preferably be sourced from SwissProt or TrEMBL.

2. **Validate and format**: Run the validation and formatting script:
   ```bash
   uv run scripts/validate_and_format_fasta.py contaminants_notag_YYYY_NN.fasta
   ```
   This script validates that all headers follow the UniProtKB format, checks for duplicate identifiers and non-ASCII characters, and reformats sequences to have line breaks after 60 characters. If errors are detected, fix them and re-run the script.

3. **Generate the tagged version**: Once the notag file is validated, generate the version with contaminant tags by running:
   ```bash
   uv run scripts/add_contam_tag_to_fasta.py contaminants_notag_YYYY_NN.fasta contaminants_YYYY_NN.fasta
   ```

4. **Changelog**: Add the changes to the CHANGELOG.md file, under a new `## Pending release` section.

5. **Release**: When ready to release, merge the `wip` branch into `main`, update the file names to the new version number, and create a release with the updated files.

## Changelog

For a detailed list of changes made to the contaminants FASTA file in each release, please refer to the [CHANGELOG.md](CHANGELOG.md) file.

## Contact

If you have any questions or inquiries regarding this repository, please feel free to reach out to Markus Hartl at the [Mass Spectrometry Facility](https://www.maxperutzlabs.ac.at/research/facilities/mass-spectrometry-facility) of the Max Perutz Labs.

## License

This repository is licensed under the MIT License