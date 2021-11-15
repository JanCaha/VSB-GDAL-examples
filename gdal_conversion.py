# Výpis všech existujícíh vrstev a následná extrakce jedné vrstvy do formátu GPKG

from osgeo import gdal, ogr

ds: gdal.Dataset = gdal.OpenEx("data/czech-republic-latest-free.shp.zip")

print(ds.GetLayerCount())

for i in range(ds.GetLayerCount()):
    layer: ogr.Layer = ds.GetLayerByIndex(i)
    print(layer.GetName())

params = {"layers": ["gis_osm_landuse_a_free_1"]}

gdal.VectorTranslate("data_result/data.gpkg",
                     ds,
                     **params)


