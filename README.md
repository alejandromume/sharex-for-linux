# ShareX for Linux

### <ins>Updates
* Added `install_sxcu.py` to simply add your `.sxcu` file path and it will add to your `~/.sharenix.json`
* For add it to your path, move the `installer/install_sxcu` to `/usr/bin`

![Prev](https://raw.githubusercontent.com/alejandromume/sharex-for-linux/main/installer/20203.png)


### <ins>Requirements

* [Download Sharenix source](https://github.com/Francesco149/sharenix/releases) and follow the steps

```bash
tar xvf sharenix-*.tar.xz

sudo cp sharenix-*/sharenix /usr/bin
sudo chmod +x /usr/bin/sharenix
sudo cp sharenix-*/src/sharenix-section /usr/bin
sudo chmod +x /usr/bin/sharenix-section
sudo cp sharenix-*/src/sharenix-window /usr/bin
sudo chmod +x /usr/bin/sharenix-window 

cp sharenix-*/sharenix.json ~/.sharenix.json
sharenix -h
```

### <ins>Issues
 
 * If you see that it throws a request error, just check if the image is uploaded and if is it, just ignore the message

### <ins>Steps

* Open your `.sxcu` file and copy all the JSON 
* Open `~/.sharenix.json`
* Find `"DefaultImageUploader"` at the top and change it for the `"Name"` field 
  * It will do it with [clippy.gg image uploder](https://clippy.gg) 

    <ins>Example

    ```
    // sxcu file
    "Name": "clippy.gg file uploader",

    |   |
    V   V

    // ~/.sharenix.json
    "DefaultImageUploader": "clippy.gg file uploader",
    ```

* Find something like this

    ```json
    {
            "Name": "imgur.com (account)",
            "RequestType": "POST",
            "Headers": {
                "Authorization": "Bearer something"
            },
            "RequestURL": "https://api.imgur.com/3/image",
            "FileFormName": "image",
            "Arguments": {
                "type": "file"
            },
            "ResponseType": "Text",
            "URL": "$json:data.link$",
            "DeletionURL": "https://imgur.com/delete/$json:data.deletehash$"
        },
    ```

    and replace it by the whole `.sxcu` file

    ```json
    {
  "Name": "clippy.gg file uploader",
  "DestinationType": "ImageUploader, FileUploader",
  "RequestType": "POST",
  "RequestURL": "API URL",
  "FileFormName": "file",
  "Body": "MultipartFormData",
  "Headers": {
    "key": "XXXXXXX"
  },
  "URL": "$json:imageUrl$",
  "DeletionURL": "$json:deletionUrl$",
  "ErrorMessage": "$json:error$"
    }
    ```

* Save the file 


    ### <ins>How to Use

* You will be able to use the following commands

    ```
    sharenix -h for a list of available options
    sharenix-section to select a region and upload it
    sharenix-window to screenshot a window and upload it
    ```

    ### <ins>Extra

* Add some hotkeys for each function
  * I'm using i3wm so I will add `ALT+SHIFT+X` for take a section screenshot
  
  ```
  bindsym $mod+Shift+x exec sharenix-section -q
  ```

