"""
Pipeline to clean Amazon reviews dataset.

Usage: python3 scripts/clean_pipeline.py
"""

import pandas as pd
from data.cleaner import clean_text, filter_by_length

def main():
    """Main pipeline function."""
    print("=" * 70)
    print("AMAZON REVIEWS CLEANING PIPELINE")
    print("=" * 70)
    
    # Step 1: Load data
    print("\n[1/4] Loading data...")
    df = pd.read_csv('datasets/raw/Reviews.csv')
    print(f"✓ Loaded {len(df):,} reviews")
    
    # Step 2: Clean text
    print("\n[2/4] Cleaning text...")
    df['text_cleaned'] = df['Text'].apply(clean_text)
    print(f"✓ Text cleaned")
    
    # Step 3: Filter by length
    print("\n[3/4] Filtering by length...")
    df_filtered = df[df['text_cleaned'].apply(filter_by_length)]
    removed = len(df) - len(df_filtered)
    print(f"✓ Removed {removed:,} reviews (too short/long)")
    
    # Step 4: Save cleaned data
    print("\n[4/4] Saving cleaned data...")
    df_output = df_filtered[['text_cleaned', 'Score']].copy()
    df_output.columns = ['Text', 'Score']
    df_output.to_csv('datasets/processed/reviews_cleaned.csv', index=False)
    print(f"✓ Saved {len(df_output):,} reviews")
    
    print("\n" + "=" * 70)
    print("PIPELINE COMPLETE")
    print("=" * 70)


if __name__ == '__main__':
    main()