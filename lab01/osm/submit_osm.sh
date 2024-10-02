#!/bin/bash -l        

#SBATCH --time=0:1:00
#SBATCH --ntasks=1
#SBATCH --mem=10g
#SBATCH --tmp=10g
#SBATCH --mail-type=ALL  
# #SBATCH --mail-user=braak014@umn.edu

# Where you need to make changes

# Change directory to home directory
# This makes sure we ALWAYS start in home directory and then navigate from there.
cd ~

# Change directory to advgeocomp2022
# Note you will need to make this directory AND move job.py into it...
# Note I also recommend moving this submission script into advgecomp2022 as well...
cd advgeocomp2022/lab01/osm

# Run the test python script called job.py
module load python3
source activate advgeocomp
python3 job_osm.py