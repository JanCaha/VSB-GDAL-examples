# Ukázka práce s daty pomocí GDAL v paměti

Skripty předpokládájí, že existuje složka **data** se souborem **czech-republic-latest-free.shp.zip** staženým z [https://download.geofabrik.de/europe/czech-republic.html](https://download.geofabrik.de/europe/czech-republic.html).

Všechny skripty pracují se **zip** souborem jako s `gdal.Datasouce` a jednotlivé **shp** soubory berou jako dílčí vrstvy. Obdobného výsledku lze dosáhnout i pokud nezadáme jako cestu k souboru, ale ke složce, která obsahuje **shp** soubory.

Skripty názorně ukazují, jak lze pracovat s daty v **/vsimem/** prostoru (soubory existující pouze v paměti) a jak lze pracovat s GDAL **Memory** driverem (data pouze v paměti bez spefického souborového typu). 