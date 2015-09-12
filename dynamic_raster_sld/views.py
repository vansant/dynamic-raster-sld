from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    errors = []

    # Layer ID
    if 'layer-id' in request.GET:
        try:
            layer_id = request.GET['layer-id']
        except:
            errors.append("You need to enter a layer-id parameter in the URL")
    else:
        errors.append("You need to enter a layer-id parameter in the URL")

    # Layer title
    if 'layer-title' in request.GET:
        try:
            layer_title = request.GET['layer-title']
        except:
            errors.append("You need to enter a layer-title parameter in the URL")
    else:
        errors.append("You need to enter a layer-title parameter in the URL")

    # Color Palette List
    if 'color-palette' in request.GET:
        try:
            color_palette_string = request.GET['color-palette']
            #print color_palette_string
        except:
           errors.append("You need to enter a color-palette parameter in the URL") 
    else:
        errors.append("You need to specify a color-palette parameter in the URL")

    # Color Palette List
    if 'thresholds' in request.GET:
        try:
            thresholds_string = request.GET['thresholds']
            print thresholds_string
        except:
           errors.append("You need to enter a thresholds parameter in the URL") 
    else:
        errors.append("You need to specify a thresholds parameter in the URL")

    # Return error messages if any exist
    if errors:
        return HttpResponse(errors)
    else:

         # Prepare colors and thresholds for template
        color_palette = ["#%s" % color for color in color_palette_string.split(",")]
        thresholds = ["%f" % float(threshold) for threshold in thresholds_string.split(",")]

        # Hold a list of key, value pairs for color palettes
        color_palette_list_of_dictionaries = []
        
        # Go over all colors and add them to a list
        for index in range(len(color_palette)):
            new_dictionary = {}
            try:
                new_dictionary[color_palette[index]] = thresholds[index]
                color_palette_list_of_dictionaries.append(new_dictionary)
            except:
                new_dictionary[color_palette[index]] = ''
                color_palette_list_of_dictionaries.append(new_dictionary)

        return render(request, 'dynamic_raster_sld/index.html',
        {
          "layer_id": layer_id,
          "layer_title": layer_title,
          "color_palette_list_of_dictionaries": color_palette_list_of_dictionaries
        },content_type="application/xhtml+xml")