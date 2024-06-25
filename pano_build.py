import yaml
import shutil
import os
from sigfig import round

def num_fmt(n: float, sf: int = 3) -> str:

    
    # return f"{n:.0f}"
    # this is broken, maybe fix later
    """
    https://stackoverflow.com/questions/66895001/how-do-i-suppress-scientific-notation-while-controlling-significant-figures-in-p
    Returns number as a formatted string with specified number of significant figures
    :param n: number to format
    :param sf: number of sig figs in output
    """
    r = f'{n:#.{sf}}'  # use existing formatter to get to right number of sig figs
    if 'e' in r:
        # for big numbers, strip scientific notation and pad with zeros
        exp = int(r[-2:])
        r = r[0]+r[2:-4] + '0' * (exp-sf+1)
    return r

def getResString(resIn):
    resIn = float(resIn)
    if resIn < 1e6:
        raise Exception("Resolution under 1 MP? Really?")
    elif resIn < 1e9:
        return f"{num_fmt(resIn/1e6, sf=2)} Megapixels"
    elif resIn < 1e12:
        return f"{num_fmt(resIn/1e9, sf=2)} Gigapixels"
    else:
        raise Exception("Terapixel resolution not supported, yet...")

yamlPath = "data/panoramas.yaml"
outputPath = "content/panoramas/"

with open(yamlPath) as file:
    yaml_list = yaml.load(file, Loader=yaml.FullLoader)
# load yaml and slightly reshape data
panoPath = yaml_list["panoPath"]
for item in yaml_list['panoramas']:
    if "date" not in item:
        raise Exception("No date for the entry" + str(item))
    thisDate = item['date']
    if "title" not in item:
        raise Exception("No title for the entry" + str(item))
    if "resolution" not in item:
        raise Exception("No resolution for the entry" + str(item))
    #
    thisResString = getResString(item['resolution'])
    thisPath = os.path.join(outputPath, str(thisDate))
    thisFile = os.path.join(thisPath, 'index.html')
    # if there is a thumbnail specified, override date_thumb.jpg
    if "thumbnail" in item:
        thisThumbnailFile = item["thumbnail"]
    else:
        thisThumbnailFile = f"{thisDate}_thumb.jpg"
    # append thumbnail file to path
    thisThumbnail = os.path.join(panoPath, thisThumbnailFile)
    # write disableNav
    if "disableNav" in item:
        if bool(item["disableNav"]):
            thisEnableNav = "False"
    else:
        thisEnableNav = "True"
    # if there is a broswer location specified, override "TOP_RIGHT"
    if "browserLoc" in item:
        thisBrowserLoc = item['browserLoc']
    else:
        thisBrowserLoc = "TOP_RIGHT"
    # is360 option
    if "is360" in item:
        if bool(item["is360"]):
            thisIs360 = "True"
    else:
        thisIs360 = "False"

    if not os.path.exists(thisPath):
        os.makedirs(thisPath)
    with open(thisFile, "w") as htmlFile:
        # opened file, write our results
        lineList = ["---",
                             f"title: {thisDate}",
                             "layout: seadragonpano",
                             f"description: {item['title']}",
                             "resolution: " + thisResString,
                             f"weight: {item['resolution']}",
                             "thumbnail: " + thisThumbnail,
                             "enableNav: " + thisEnableNav,
                             "browserLoc: " + thisBrowserLoc,
                             "is360: " + thisIs360]
        # silly python writelines without newlines
        htmlFile.writelines(line + '\n' for line in lineList)
        # only thing that's most convenient to switch in the Hugo template is this:
        if "dayPath" in item:
            if "nightPath" in item:
                # write dayPath and nightPath if they exist
                dayPath = os.path.join(panoPath, str(thisDate), item['dayPath'])
                nightPath = os.path.join(panoPath,str(thisDate),  item['nightPath'])
                htmlFile.writelines(["isDayNight: true\n",
                             f"dayPath: {dayPath}\n",
                             f"nightPath: {nightPath}\n"])
            else:
                raise Exception(f"dayPath specified but nightPath isn't for {thisDate}")
        # else if there is a dzi path specified, override date.dzi
        else:
            if "dziPath" in item:
                thisDziPath = item["dziPath"]
            else:
                thisDziPath = f"{thisDate}.dzi"
            thisDzi = os.path.join(panoPath, str(thisDate), thisDziPath)
            htmlFile.writelines([f"dziPath: {thisDzi}\n"])
        htmlFile.writelines("---")