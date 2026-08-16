"""
Sentiment analysis pipeline for cleaned Amazon reviews.
Analyses sentiment (positive/negative/neutral) for each review"""

import pandas as pd
from transformers import pipeline 

def main():
    """Main sentiment analysis pipeline."""
    print("="*70)
    print("SENTIMENT ANALYSIS PIPELINE")
    print("=" *70)

    #Step1: Load Cleaned Data
    print("\n[1/3] Loading cleaned data.....")
    df = pd.read_csv('datasets/processed/reviews_cleaned.csv')
    print(f"loaded {len(df):,} reviews")

    #Step2: Analyze sentiment
    print("\n[2/3] Analysing Sentiment.....")
    sentiment_analyser = pipeline('sentiment-analysis')

    #Apply to each review
    sentiments = df['Text'].apply(lambda text: sentiment_analyser(text[:512])[0])
    df['sentiment'] = sentiments.apply(lambda x: x['label'])
    df['sentiment_label'] = sentiments.apply(lambda x: x['score'])

    print(f"Analysed {len(df):,} reviews")

    #step3: Save results
    print("\n[3/3] Saving results....")
    df.to_csv('datasets/processed/reviews_with_sentiment.csv', index=false)
    print(f"saved {len(df):,} reviews with semtiment")

    print("\n" + "=" * 70)
    print("SENTIMENT ANALYSIS COMPLETE")
    print("=", * 70)


if __name__ == "__main__":
    main()
