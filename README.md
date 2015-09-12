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

## Required Query String Parameters
####layer-id
  This is the name of the ID field that gets set in the admin panel of the ncWMS2 Server
####layer-title
  This is the title of the layer
####color-palette
  This is a list of colors (8 digit hex with alpha)
  The list will be 1 longer than list of thresholds
  Ex. FF0000FF,FF00FFFF,FF00FF00,FFFFFF00,FFFFC800,FFFFAFAF,FFFF0000
  Notice you do not include the # (taken out to free up character in the URL)
####thresholds
  These are the breakpoints for the color palette list
  Ex. 275.0,280.0,285.0,290.0,295.0,300.0
  Note: the thresholds list is one less than the color palette list

