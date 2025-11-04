import argparse
import pandas as pd

def get_parser():
    parser = argparse.ArgumentParser(
        prog="incident_counter.py",
        description="Count incidents of complaint types (determined by keyword matches) from NYC 311 complaints file."
    )
    parser.add_argument("-i", "--input", type=str, required=True, help="Path to the input CSV file containing 311 complaints.")
    parser.add_argument("-o", "--output", type=str, required=False, help="Path to the output CSV file to save incident counts.")
    parser.add_argument("-k", "--keywords", nargs="+", required=True, help="List of keywords to search for in complaint descriptions.")
    return parser

def main():
    use_cols = ["Unique Key", "Complaint Type", "Community Board"]
    args = get_parser().parse_args()
    input_file = pd.read_csv(args.input, usecols=use_cols, dtype=str)
    keywords = [k.lower() for k in args.keywords]
    complaint_lower = input_file["Complaint Type"].str.lower()
    mask = complaint_lower.apply(lambda x: any(k in x for k in keywords))
    input_file = input_file.loc[mask].copy()

    summary = input_file.groupby("Community Board").size().reset_index(name="Incident Count")

    if args.output:
        summary.to_csv(args.output, index=False)
    else:
        print(summary)

if __name__ == "__main__":
    main()