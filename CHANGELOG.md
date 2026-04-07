# Changelog of the Perutz MS Facility contaminants FASTA file


## Release 2026_01
Released: 2026-04-01

### Added
- "LysC" (Promega, V1671) entry Q02SZ7

### Chore
- Validation: Updated the formatting script to include a strict check for non-ASCII characters within headers to prevent encoding issues.
- CI: Integrated a GitHub Actions workflow to automatically validate UniProt header formats and enforce standard FASTA line-wrapping and spacing.
- Documentation: Added a "Contributing" section to the README.md with specific guidelines on how to modify and propose changes to FASTA files.

---

## Release 2025_01
Released: 2025-05-14

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

---

## Release 2023_03
Released: 2023

- Added the Turbo-ID BirA sequence used by the Ting lab; based on vector sequence TurboID-V5_pRS415 from https://www.addgene.org/107167/
- Added the 3xMYC-tag entry

---

## Release 2023_02
Released: 2023

- Added the APEX2-tag entry

---

## Release 2023_01
Released: 2023

- Updated header of synthetic entries to better follow the UniProtKB format