# Estimating the Economic Value of Landslide Regulation by Forests

## Description

This project estimates the economic value of landslide regulation by forests by integrating multiple geospatial datasets. The final outcome is the estimated number of avoided deaths at the ADM 3 regional level. While the datasets have global coverage, the project's scope is currently limited to Nepal as a proof of concept. Advanced geospatial computing techniques, including raster and vector data processing, were applied to achieve these results.

## How to Run

1. Open `project.html` in a web browser to view the full project description, code, and outputs.

2. Alternatively, view the source code and outputs using:
    - `project.ipynb` (Jupyter Notebook format)
    - `project.pdf` (PDF format)

3. All files were generated from `project.qmd`, which is included for reproducibility.

4. Ensure all dependencies listed below are installed and the required data files are organized as described in the "Data Files" section.

## Script Files

- `project.html`: The primary file containing the project overview, Python code, and results in a single document.

- `project.ipynb`: Jupyter Notebook format of the project for interactive exploration.

- `project.pdf`: Printable version of the project.

- `project.qmd`: The source Quarto file used to generate the above formats.


### Dependencies

The necessary packages, system information, python version, and other information are displayed in the ***Preliminary*** section. 

- Python 3.8+
- Jupyter Notebook
- Quarto (for .qmd only)
- Required Python libraries: os, platform, sys, numpy, pandas, geopandas, rasterstats, matplotlib, pygeoprocessing, gdal, ogr, natcap.invest.sdr.sdr, and statsmodels 

## Data Files

- EMDAT Historical Landslide Death Data (1960-2018)
    - Linked to NASA Geocoded Disasters (GDIS)
- NASA Gridded Population Data (GPW) (2000, 2005, 2010, 2015, 2020)
- Sediment Export Data
    - Digital elevation model (DEM)
    - Rainfall erosivity raster
    - Soil Erodibility Raster
    - Land use/land cover raster (ESA-CCI 2000-2020)
    - Watersheds shapefile
    - Biophysical table to assign C and P factor
    - Values to different LULC classes


Most of the data was stored in a `landslides` folder:
```
landslides
│   full_noforest_panel.gpkg
│   full_panel.gpkg    
│
└───borders
└───emdat
└───invest_inputs
└───invest_sdr
└───nasa-gpw
└───pend-gdis-1960-2018-disasterlocations-gpkg
```

Some of the raw data was already stored on disk, and not copied to the `landslides` to save storage space: `gadm_410-levels.gpkg`, `alt_m.tif`, `Global Erosivity/GlobalR_NoPol-002.tif`, `Global Soil Erodibility/Data_25km/RUSLE_KFactor_v1.1_25km.tif`, and all of the ESA-CCI land use/land cover data. Intermediate files are fully contained within the `landslides` folder. (Note: to keep the submission file within a reasonable size, not all files were included in the landslides folder.)

## Known Issues and Limitations

- The analysis is limited to Nepal; results may not generalize to other regions.

- Certain raw data files are not included in the submission due to size constraints.

- Users must manually configure the file paths if replicating the analysis on a different system.

## Authors

Matt Braaksma
<braak014@umn.edu>
