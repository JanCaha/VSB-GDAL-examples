# extrakce jedné vsrstvy do souboru v paměti (ve formátu GPKG), kontrola vrstev - tisk názvu)
# nsledně buď uložení vsimem na disk (do složky) nebo transformace do jiného formátu

from osgeo import gdal, ogr

ds: gdal.Dataset = gdal.OpenEx("data/czech-republic-latest-free.shp.zip")

params = {"layers": ["gis_osm_natural_free_1"]}

vsimem_data = "/vsimem/data.gpkg"

gdal.VectorTranslate(vsimem_data,
                     ds,
                     **params)

ds1: gdal.Dataset = gdal.OpenEx(vsimem_data)

print(ds1)

for i in range(ds1.GetLayerCount()):
    layer: ogr.Layer = ds1.GetLayerByIndex(i)
    print(layer.GetName())

# gdal.Sync("/vsimem/",
#           "data_result")

gdal.VectorTranslate("data_result/data.geojson",
                     vsimem_data)
