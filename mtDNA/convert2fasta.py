import sys

def apply_variants(dna_sequence, variants):
    mutated_sequence = list(dna_sequence)  # Convert the DNA sequence to a list for easy modification

    for variant in variants:
        position = int(''.join(filter(str.isdigit, variant))) - 1  # Convert position to 0-based index for deletions
        
        if variant.startswith('-'):    
            # Handle insertions
            position = int(variant.split('.')[0][1:])
            mutation = variant.split('.')[-1]
            if position >= 0 and position <= len(mutated_sequence):
                mutated_sequence.insert(position, mutation[-1])
                print(f"Inserted {mutation} at position {position + 1} due to variant {variant}")
            else:
                print(f"Invalid insertion position {variant}. Skipping.")
        
        elif variant.endswith('-'):
            # Handle deletions
            if position >= 0 and position < len(mutated_sequence):
                deleted_base = mutated_sequence.pop(position)
                print(f"Deleted {deleted_base} at position {position + 1} due to variant {variant}")
            else:
                print(f"Invalid deletion position {variant}. Skipping.")
        else:
            # Handle substitutions
            mutation = variant[-1]
            if position >= 0 and position < len(mutated_sequence):
                mutated_sequence[position] = mutation
                print(f"Substituted {dna_sequence[position]} with {mutation} at position {position + 1} due to variant {variant}")
            else:
                print(f"Invalid substitution position {variant}. Skipping.")

    return ''.join(mutated_sequence)

def read_dna_sequence_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        dna_sequence = ''.join(lines[:]).replace("\n", "")  # Concatenate the remaining lines as the sequence
    return dna_sequence

def custom_sort_indels(variant):
    numeric_part = float(''.join(c for c in variant if c.isdigit() or c == '.'))  # Convert to float to handle dots
    is_deletion = variant.startswith('-')
    return (numeric_part, is_deletion)

def write_to_fasta_file(output_file, sequence, description="Modified Sequence"):
    with open(output_file, 'w') as file:
        file.write(f">{description}\n")
        file.write(sequence)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py input_fasta_file output_fasta_file name variants_str")
        sys.exit(1)
    
    input_fasta_file = sys.argv[1]
    output_fasta_file = sys.argv[2]
    name = sys.argv[3]
    variants_str = sys.argv[4]

    variants = variants_str.strip().split()
    substitutions = []
    indels = []

    for variant in variants:
        if variant.count("-") > 0:
            indels.append(variant)
        # elif '.' in variant:
        #     insertions.append(variant)
        else:
            substitutions.append(variant)

    # Sort substitutions based on the number between the first and last character (highest number first)
    substitutions.sort(key=lambda x: int(''.join(filter(str.isdigit, x))), reverse=True)

    # Sort indels using the custom sorting function
    indels.sort(key=custom_sort_indels, reverse=True)  # Reverse the sorting order for indels

    sorted_variants = substitutions + indels

    dna_sequence = read_dna_sequence_from_file(input_fasta_file)

    mutated_sequence = apply_variants(dna_sequence, sorted_variants)
    mutated_sequence2 = mutated_sequence.replace("N", "")

    write_to_fasta_file(output_fasta_file, mutated_sequence2, name)

