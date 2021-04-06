import json
from pathlib import Path

home = str(Path.home())

path = input("[>] Paste your .sxcu file path: ")
try:
    f = open(path, "r")
    f2 = open(path, "r")

    data = json.load(f)

    json_format = '{"DefaultFileUploader": "' + data["Name"] + '","DefaultImageUploader": "' + data["Name"] + '", "XineramaHead": 0, "NotificationTime": 30, "NotifyUploading": true, "NotifyCommand": "", "ClipboardTime": 5, "SaveFolder": ".local/share/sharenix", "Services": [ '+ f2.read() +' ]}'
    f = open(f"{home}/.sharenix.json", "w")
    f.write(json_format)
    f.close()
    print("")
    print("[>] .sharenix.json was successfully updated!")
    print("[!] If you get any error (ex. jsonpath not found) try to check manually the file")

except:
    print("")
    print("[X] Error, try to check your path")

