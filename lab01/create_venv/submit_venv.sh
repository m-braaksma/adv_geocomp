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

# Create new venv
module load python3
mamba create --name advgeocomp1 python=3 pyrosm --channel conda-forge
