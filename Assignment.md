## 2 identical XLS files are shared which contains data sampled at 1 record/second

## Task

1. Combine the data scattered around in multiple sheets into one. For this task take data starting from sheet no 4. Combine all the sheets where "Detail_" is present in the name row-wise into 1 dataframe. Combine all the sheets where "DetailVol_" is present in the name into 1 dataframe. Combine all the sheets where "DetailTemp_" is present in the name into one dataframe.
2. Apply downsampling method to reduce the sampling rate of the whole dataframe to 1 sample/minute.
3. Try to implement Coding Style Guide [PEP-8], and use pylint or flake8 to check the code for PEP-8  violations.
4. Run profile for all the functions; use `cProfile` for profiling of individual functions.
5. Run unit test on each function,i.e., write test cases for each function. Use `unittest` for the same
6. Try to write the code in a modular way and implement functions for the operations which are performed more than once.
7. At the end commit every stage to git and mainatin a clean git tree structure. 
## Goal
**Share the code base over a public `GitHub` repository with a clean git tree for better understandning of the code base, include one `Readme` and share the `GitHub` link at *`saradindu@nunam.com`***