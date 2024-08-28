import ijson
import json
import gzip
import argparse

def filter_matching_files(output_file, keywords, f):
    reporting_structure_objs = ijson.items(f, 'reporting_structure.item')
    
    seen_urls = set() # Keep track of URLs we see to avoid duplicate results
    
    filtered_files = (
            mrf for rso in reporting_structure_objs
            for mrf in rso.get('in_network_files', []) + ([rso['allowed_amount_file']] if 'allowed_amount_file' in rso else []) # iterate through all files in the reporting struct
            if all(keyword in mrf['description'] for keyword in keywords) and mrf['location'] not in seen_urls and not seen_urls.add(mrf['location']) # filter for keywords and duplicates
        )

    for entry in filtered_files:
        output_file.write(json.dumps(entry) + '\n')

def main():
    parser = argparse.ArgumentParser(description="Process and filter a JSON or JSON.GZ file.")
    parser.add_argument('input_file', type=str, help="Path to the input JSON or JSON.GZ file.")
    parser.add_argument('output_file', type=str, help="Path to the output JSON file.")
    parser.add_argument('keywords', nargs='+', type=str, help="List of keywords to match in the description field.")

    args = parser.parse_args()

    with open(args.output_file, 'w') as output_file:
        if args.input_file.endswith('.gz'):
            with gzip.open(args.input_file, 'rt') as f:
                filter_matching_files(output_file, args.keywords, f)
        else:
            with open(args.input_file, 'r') as f:
                filter_matching_files(output_file, args.keywords, f)

if __name__ == "__main__":
    main()
