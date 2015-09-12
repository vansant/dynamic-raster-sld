# dynamic-raster-sld
Portable Django App to Dynamically Create Raster SLDs (xml) to style ncWMS2 WMS Layers

## Install and use dynamic_raster_sld app
1. Put dynamic_raster_sld in your Django project root directory
2. Add dynamic_raster_sld to installed apps in settings.py
3. Configure urls.py

### Import the app views
import dynamic_raster_sld.views

### Update urlpatterns
urlpatterns = [
    url(r'^$', dynamic_raster_sld.views.index, name='index'),
]