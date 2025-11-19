#!/usr/bin/env python3
"""
report_generator.py
Generates a simple text report from processed CSV.
Usage: python report_generator.py input_processed_csv output_report.txt
"""
import sys
import pandas as pd

def generate(infile, outfile):
    df = pd.read_csv(infile, parse_dates=['date'])
    total_rev = df['total_amount'].sum()
    total_orders = df['order_id'].nunique()
    top_prod = df.groupby('product_name')['total_amount'].sum().sort_values(ascending=False).head(5)
    with open(outfile, 'w', encoding='utf-8') as f:
        f.write("Daily Sales Report\\n")
        f.write("==================\\n")
        f.write(f"Total Revenue: Rp {total_rev:,.0f}\\n")
        f.write(f"Total Orders: {total_orders}\\n\\n")
        f.write("Top Products:\\n")
        for p, amt in top_prod.items():
            f.write(f"- {p}: Rp {amt:,.0f}\\n")
    print(f"Report saved to {outfile}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python report_generator.py processed.csv report.txt")
    else:
        generate(sys.argv[1], sys.argv[2])
