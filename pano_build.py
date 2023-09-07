import yaml
yamlPath = "data/panoramas.yaml"
outputPath = "content/photos/Panoramas"
# check/clear outputPath

with open(yamlPath) as file:
    yaml_list = yaml.load(file, Loader=yaml.FullLoader)
# load yaml and slightly reshape data
for item in yaml_list['panoramas']:
    print(item['date'])
    if "date" not in item:
        raise Exception("No date for the entry" + str(item))
    if "title" not in item:
        raise Exception("No title for the entry" + str(item))
    if "resolution" not in item:
        raise Exception("No resolution for the entry" + str(item))
    # create file and add those three essentials

    # if isDaynight:
        # write dayPath and nightPath if they exist

    # else if there is a dzi path specified, override date.dzi

    # if there is a thumbnail specified, override data_thumb.jpg

    # if there is a broswer location specified, override "TOP_RIGHT"

    # write distableNav or is360 opts.
