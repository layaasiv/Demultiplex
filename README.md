# Demultiplex 

## Goal
The reads were multiplexed when sequenced, meaning many different samples (from different conditions or organisms potentially) are present in the same run. We need to re-group (demultiplex) the reads again using the indexes they carry, which are unique to each group. We also need to filter out reads where index on read1 does not match index on read2, or reads with indexes with low quality scores to optimize confidence in our categorization of reads into the various index groups. 

## What do matched index-pair reads look like? 
For this project's dataset, we are working with paired end reads, where the R1, R2, R3, and R4 files contain read 1 seq, index 1 seq, index 2 seq, and read 2 seq, respectively. Matched index pair reads are expected to have the same indexes (index1 and index2) in this dataset. Therefore, mismatched indexes between paired reads indicates index hopping. Those reads that belong to the same library will all carry the same index identifier. 

## What is in this repository? 
* [Assignment the first](): Exploratory analysis of the data; looking at quality scores distribution.
    * [qscore_dist_demult.py](https://github.com/layaasiv/Demultiplex/blob/master/Assignment-the-first/qscore_dist_demult.py): Algorithm that produces histograms of average quality score per base position for each file.
    * [bioinfo.py](https://github.com/layaasiv/Demultiplex/blob/master/Assignment-the-first/bioinfo.py): Python module file that contains some useful bioinformatics functions. 
* [Assigment the second](): Pseudocode peer review & feedback of fellow students.
* [Assignment the third](): Contains final algorithms and resulting output files for the dataset used.
    * [demux.py](https://github.com/layaasiv/Demultiplex/blob/master/Assignment-the-third/dmux.py): Final demultiplexing algorithm.
    * [dmux_sbatch.sh](https://github.com/layaasiv/Demultiplex/blob/master/Assignment-the-third/dmux_sbatch.sh): Slurm script to submit algorithm script to HPC.
    * The tsv files contain counts/proportions of reads identified in each category (matched, hopped, unknown indexes).
 
## How to use the algorithm
Here's the command to run the script: 

```
./dmux.py -r1 <R1.fastq.gz> \
    -r2 <R2.fastq.gz> \
    -r3 <R3.fastq.gz> \
    -r4 <R4.fastq.gz> \
    -i <indexes.txt>
```

## Expected output
Output should be 2 fastq files per index match (one for read1 and another for read2). Since there are a total of 24 possible indexes here, we expect a total of 48 fastq files where indexes match on read1 and read2. Also, 2 fastq files to hold all unknown (indexes containing N or low quality score) reads (keeping read1 and read2 separate). Finally, 2 fastq files to hold all unmatched (index1 and index2 do not contain Ns but they do not match each other) reads (keeping read1 and read2 separate). In total, we expect 52 fastq files for this dataset. 
