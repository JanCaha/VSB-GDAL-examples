# transforamce vstupní vrstvy do MEMORY formátu GDAL (bez určeného souborového typu)
# export tohoto MEMORY souboru do GML
# v tomto případě je kritické nesmazat proměnnou ds_memory, protože jejím smázáním končí životnost dat v paměti

from osgeo import gdal, ogr

ds: gdal.Dataset = gdal.OpenEx("data/czech-republic-latest-free.shp.zip")

params = {"layers": ["gis_osm_natural_free_1"],
          "format": "Memory"}

ds_memory: gdal.Dataset = gdal.VectorTranslate("",
                                               ds,
                                               **params)


print(ds_memory)
print(ds_memory.GetLayerCount())

gdal.VectorTranslate("data_result/data.gml",
                     ds_memory)