import pandas as pd
import sys


def find_region_pairs(df, min_dist=5000, max_dist=200000):
    pairs = []
    for chrom in df['chrom'].unique():
        chrom_df = df[df['chrom'] == chrom].sort_values(by='start')
        for i, (start1, end1) in chrom_df[['start', 'end']].iterrows():
            for j, (start2, end2) in chrom_df[['start', 'end']].iterrows():
                if i != j:
                    distance = start2 - end1
                    if min_dist <= distance <= max_dist:
                        pairs.append([chrom, start1, end1, chrom, start2, end2])
    return pairs


def load_bed_file(filepath):
    df = pd.read_csv(filepath, sep='\t', header=None, names=['chrom', 'start', 'end'])
    return df


def process_file(filepath):
    df = load_bed_file(filepath)
    

    region_pairs = find_region_pairs(df)
    

    output_filepath = filepath.replace('.bed', '_pairs.bedpe')
    

    if region_pairs:
        pairs_df = pd.DataFrame(region_pairs, columns=['chrom1', 'start1', 'end1', 'chrom2', 'start2', 'end2'])
        pairs_df.to_csv(output_filepath, sep='\t', index=False, header=False)
        print(f"Pairs saved to file: {output_filepath}")
    else:
        print(f"There are no matching matches for file {filepath}.")


def main():

    filepaths = sys.argv[1:]
    if not filepaths:
        print("Please provide one or more .bed files to process..")
        return
    for filepath in filepaths:
        process_file(filepath)

if __name__ == "__main__":
    main()