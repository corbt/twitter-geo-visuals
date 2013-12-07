The data processing pipeline I went through is as follows:

1. Run pull_sample.py as long as necessary to get the data you need (I got about 100k tweets in 24 hours)
2. Run get_subset.py to extract a random subset of the tweets collecting using a specific filtering criteria if desired
3. 