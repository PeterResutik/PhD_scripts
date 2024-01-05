# From variants to FASTA file

The goal of this project is to convert variants in a mitochondrial DNA (mtDNA) into a FASTA file. 

### Executing program

```
python script.py input_fasta_file output_fasta_file name variants_str
```
* where input_fasta is the NC_012920.1.fasta file with the revised Cambridge Reference Sequence (rCRS) of the mtDNA,
* the output file is the desired name of the output file,
* the name is the name included in the first line of the outpu FASTA file
* variants_str is a string of variants that conform to forensic nomenclature (ref): e.g. "A73G A523- -315.1C" indicating a subsitution, a deletion, and an insertion.
* note: the N base on position 3107 is deleted from the final FASTA file.

## Authors

Contributors names and contact info

Peter Resutik: peter.resutik@irm.uzh.ch

## License

This project is licensed under the MIT License.

<!--
## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)
-->
