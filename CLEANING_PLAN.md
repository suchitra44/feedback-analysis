# Amazon Reviews - Cleaning Plan

## Dataset Info
- Total rows: 568,454
- Total columns: 10
- File size: 445.77 MB

## Data Quality Issues Found
- HTML tags: 147,324 reviews (26%)
- URLs: 11,679 reviews (2%)
- @ symbols: 894 reviews (0.15%)
- Duplicates: 0
- Nulls: Only in ProfileName (26) and Summary (27)

## Cleaning Strategy

### Columns to Keep
- `Text` - Review content (MAIN - we'll clean this)
- `Score` - Rating 1-5 (KEEP as is)

### Text Cleaning Rules
1. Remove HTML tags (`<br />`, `<b>`, etc)
2. Remove URLs (http://, https://)
3. Lowercase text
4. Normalize whitespace (multiple spaces → single space)
5. Remove special characters

### Length Filters
- Minimum: 20 characters
- Maximum: 5,000 characters

### Expected Results
- Input: 568,454 rows
- Output: ~560,000+ rows (remove very short reviews)
- Removed: ~8,000 rows (< 20 chars)

## Next Steps
1. Create cleaning functions
2. Test on sample data
3. Run on full dataset
4. Verify results