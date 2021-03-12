# Windows 10 Spotlight Images Downloader

You saw a beautiful landscape on your PC lock screen, provided by the Windows 10 Spotlight feature, and you'd like to save it for future use.
Typically, Windows 10 Spotlight images are accessible in the folder:
```
"%localappdata%\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets"
```
However, the files in this folder have no extension, and it's not possible to see a preview. To find the image of interest one should randomly select a file and rename it with the appropriate image extension until the desired image is found.

__Win10SpotlightImagesDownloader__ is a simple script that allows you to quickly select all the Spotlight images available in the aforementioned path, change their extension and move them in a folder of your choice.

## Installation
Simply clone or download the project.

## Usage
Run the `main.py` script.

## Project Status
At the moment, the script simply selects all the files with size `>=400Kb` and stores them with extension `.jpg` in the selected folder. In the future, it is contemplated the addition of a feature to select a single image too. Also, will be added the possibility to rename the images with the names of the geographical places where they were taken.
