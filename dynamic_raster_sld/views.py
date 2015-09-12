from django.shortcuts import render

def index(request):
    layer_name = "my_layer_name"
    layer_workspace = "my_layer_workspace"
    color_palette = ["#FF0000FF", "#FF00FFFF", "#FF00FF00", "#FFFFFF00", "#FFFFC800", "#FFFFAFAF", "#FFFF0000"]
    thresholds = [275.0, 280.0, 285.0, 290.0, 295.0, 300.0]

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

    print color_palette_list_of_dictionaries
    return render(request, 'dynamic_raster_sld/index.html',
        {
          "layer_name": layer_name,
          "layer_workspace": layer_workspace,
          "color_palette_list_of_dictionaries": color_palette_list_of_dictionaries
        },
           content_type="application/xhtml+xml")