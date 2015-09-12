from django.shortcuts import render

def index(request):
    layer_name = "my_layer_name"
    layer_workspace = "my_layer_workspace"
    return render(request, 'dynamic_raster_sld/index.html', {"layer_name": layer_name, "layer_workspace": layer_workspace},
        content_type="application/xhtml+xml")