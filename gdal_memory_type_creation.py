# tvorba GDAL datasource v paměti a následné zkopírování vrstvy do tohoto datasource
# opět je důležité neodstranit proměnnou ds_memory, protože tím by došlo ke ztrátě dat

from osgeo import gdal, ogr

driver_mem: gdal.Driver = gdal.GetDriverByName("Memory")

ds_memory: gdal.Dataset = driver_mem.Create("nazev", 0, 0, 0)

print(ds_memory)
print(ds_memory.GetLayerCount())

ds: gdal.Dataset = gdal.OpenEx("data/czech-republic-latest-free.shp.zip")

layer: ogr.Layer = ds.GetLayerByName("gis_osm_natural_free_1")

ds_memory.CopyLayer(layer, layer.GetName())

print(ds_memory.GetLayerCount())

gdal.Translate("data_result/data.shp",
               ds_memory)
