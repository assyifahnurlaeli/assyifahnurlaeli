#!/usr/bin/env python3
"""
etl.py
Simple ETL example:
Usage: python etl.py input_csv output_csv
"""
import sys
import pandas as pd

def run(infile, outfile):
    df = pd.read_csv(infile, parse_dates=['date'])
    df = df.dropna(subset=['order_id','product_id','quantity','price'])
    df['quantity'] = df['quantity'].astype(int)
    df['price'] = df['price'].astype(float)
    df['total_amount'] = df['quantity'] * df['price']
    # Example enrichment: product category mapping (static)
    # Save processed
    df.to_csv(outfile, index=False)
    print(f"Saved processed data to {outfile}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python etl.py input.csv output.csv")
    else:
        run(sys.argv[1], sys.argv[2])
