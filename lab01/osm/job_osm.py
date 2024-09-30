# Read landuse
# ============
from pyrosm import OSM
from pyrosm import get_data
import matplotlib.pyplot as plt

fp = get_data("test_pbf")
# Initialize the OSM parser object
osm = OSM(fp)
landuse = osm.get_landuse()
landuse.plot(column='landuse', legend=True, figsize=(10,6))
plt.savefig('landuse_plot.png', dpi=300, bbox_inches='tight')