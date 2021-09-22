# trgn510_assignment3
# Script 1: extract_phonenum.py
## Usage
This script will take numbers that are in text file format, pull them out and display them one-line per phone number. More specifically, numbers will be formatted as [+][country code] ([AreaCode]) [local phone number]. [+][country code] optional output if number is international.

This program is installable via git clone https://github.com/MPachicano/trgn510_assignment3.git, and use script extract_phonenum.py with any text file you want. For testing purposes, there is a preexisting 'testing.txt' file with text and phone numbers.

On the command-line: python3 extract_phonenum.py mytextfile.txt

## Description
Extracts phone numbers from a text file and prints out formatted phone numbers.
## Known Issues
At this point in time, this script does not include parentheses around (area code). I know this is an issue with my regular expression, and will come back to this.

# Script 2: ensg2hugo.py
## Usage
This script builds a dictionary (ens2gene) of gene Ensemble ID's and Hugo ID's from file *Homo_sapiens.GRCh37.75.gtf*, and replacing all Ensemble ID's with Hugo IDs. Then, it loops into a second CSV file, which will replace all of the CSV's gene Ensemble ID's, with the Hugo ID's that were pulled from the file *Homo_sapiens.GRCh37.75.gtf*.  It will then put the output data into a new CSV file called "output.csv".

This script is installable via git clone https://github.com/MPachicano/trgn510_assignment3.git.

Because *Homo_sapiens.GRCh37.75.gtf* is a large file (roughly 1.8 million lines long), you can 'curl' the path on the command line: **curl -O trgn510_assignment3/Homo_sapiens.GRCh37.75.gtf**

There are two unit tests that I used for this program. Use git clone.
1) https://github.com/davcraig75/unit
2) https://github.com/davcraig75/rna

On the command-line: python3 ensg2hugo.py
## Description
Creates a dictionary to loop up a gene's Ensembl name and output the Hugo ID.
## Known Issues
There are going to be many 'Known Issues' for this script, because I was unable to put some pieces together. Nonetheless, I will document them here so that I can come back and rework the script to properly match the Ensembl ID's in both files.

1) In the dictionary I have created for the *Homo_sapiens.GRCh37.75.gtf* file, the Ensemble ID formatting does not 'match' with the Ensemble ID's of the second file, unit/expres.anal.csv. This is because the Ensembl ID in unit/expres.anal.csv have a decimal followed by a number (ie 'ENSG00000248546.3'). Because of this, the script is not finding any matches. I know this has to do with my dictionary and possibly have to include a re.split for my second CSV file, but I will do some more research and come back to this.

Despite this issue, I do have the ability to pull out matches, and replace the Ensembl with the Hugo ID in the unit test  rna/expression_results.csv. This file has Ensemble ID's that match with the formatting of the *Homo_sapiens.GRCh37.75.gtf* file and is able to replace them with the Hugo ID. Even though this is not what the assignment required, it is still a unit test that confirms my dictionary exists, works, and replaces with Hugo ID.

2) The output with the Hugo ID replacement has repeats, in other words, each line of the *Homo_sapiens.GRCh37.75.gtf* file is not unique with the Ensembl ID. The reason is because the script is reading line by line of the gtf file. I will need to revisit this.

3) I was unable to figure out how to add an option “-f [0-9]” where -f2 would pick the 2nd column. If there is no “-f” then the first column is used. I researched and tried to import the "argparse" module in order to select specific columns but was not able to succesfully run the script. I will need to revisit this https://docs.python.org/3/library/argparse.html and figure out what I was doing wrong.

4) Although the script does output us a csv file, because I was unable to figure out why the row it is outputting is incorrect. I thinkn this has to do with not having a way to select columns that was mentioned in Known Issues #3.

5) Lastly, I was unable to enable this script to use .tsv. This program works with csv files as of right now. I will need to come back to this after researchig.

# Script 3: histogram.py
## Usage
This program is installable via git clone https://github.com/MPachicano/trgn510_assignment3.git.

This program takes a csv file and attempts to create a histogram from the data file, and outputs a png file. 

Installations:
python -m pip install --user pandas
python -m pip install --user numpy
python -m pip install --matplotlib

The unit test I used for this program is 
https://github.com/davcraig75/rna (use git clone to retrieve the file)

## Description
Creates a histogram as a png file using a specified column in a tab delimited file.
## Known Issues 
There are also going to be many 'Known Issues' for this program, as I was not able to succesfully program it to take any data file (no tsv). 

1) This program can only read csv files. This is because I was unsure how to get the script to import a .tsv file, but I did learn that it can work with the 'import csv' module. I just need more time to research this.

2) Another known issue is that I did not figure out how add the option '-f [#]' in order for the program to know which columns to plot. I wanted to use argparse for this (similar to previous script) but after many days, I could not get it to work properly. I will need to come back to this once I find out how to apply argeparse. 

3) Although it does plot something... it does not necessarily plot what looks to be a histogram. Because of 'Known Issue #2', my program is trying to plot everything in the csv file. So, the output plot itself looks strange. The program does output a .png file, but it does not plot anything in it for some reason. I have to figure this out.  
