# Changelog of the Perutz MS Facility contaminants FASTA file

## Release 2025_01

### Added
- "Aprotinin" entry
- "PNGase F" (Promega) entry
- "ProAlanase" (Promega) entry
- "ArgC Ultra" (Promega) entry
- Two mouse Immunoglobulin kappa entries that were identified in an experiment using anti-FLAG antibodies.
- "GFP-Nanobody" entry
- "Immunoglobulin G-binding protein G" entry

### Removed
- Removed entries MYCTAG1, FLAGTAG1, STREPTAG2, and HATAG1, as they have a short sequence are unlikely to be deteced in MS experiments.

### Chore
- Added a script to convert the FASTA file without contaminants tags into a FASTA file with contaminants tags.
- Added a script to format the sequences of a FASTA file to ensure that line breaks occur after every 60 characters

## Release 2023_03
- Added the Turbo-ID BirA sequence used by the Ting lab; based on vector sequence TurboID-V5_pRS415 from https://www.addgene.org/107167/
- Added the 3xMYC-tag entry

## Release 2023_02
- Added the APEX2-tag entry

## Release 2023_01
- Updated header of synthetic entries to better follow the UniProtKB format