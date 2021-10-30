# Projects
This repository is a compilation of small/medium projects made in different programming languages. 

## Why?
This repository is purely for educational purposes.

The goal is to recreate the same project in different languages in order to become more familiar with said languages. 

## Important Notes
- Unless specified otherwise, important variables will be hardcoded for simplicity. Some projects will have default values. 
- Each project should be recreated with the same functionality as described in the project's description. Due to the different behaviors some languages might have, this rule can be stretched a little if the changes are commented in the code, i.e. filtering images by extension instead of trying to open the file as an image.
- There will be a list of steps to achieve the desired functionality in each project's description.
- Some projects may not be cross-platform, meaning they will only work on Linux or Windows. The projects are *not* made with Mac OS support in mind.
- Projects *can* depend on external libraries/frameworks to achieve the desired functionality. The goal is to understand more about the languages, not to code everything from scratch. However, the dependencies *must* be stated as a comment in the language's project.

## Project List
---
### Portrait Mode
Move all images in portrait mode from a directory to another. 

This project aims for speed and simplicity. We *only* need the image's dimension. If its width and height can be read without opening/loading the entire image, then do so.

The program should work in a way that it does not need to filter the files by their extensions in order to load the images, but if that is not possible, then filter by **.jpg** and **.png**.

Files with the same name in the output directory will be overwritten.

**Defaults**  
The default base directory is: 
`/home/<user>/Pictures/Wallpapers` on **Linux**.

The output directory is named **Portrait** and it should be located inside the base directory. This directory will be created if it doesn't exist.

**Main Steps**  
1. Get/define the image's directory.
2. Set the output directory and create it if needed. It should be called **Portrait** and *must* reside inside the base directory.
3. Iterate over the contents of the base directory.
4. Load the files as images
5. Check the image's dimensions. The height *must* be greater than the width for an image to be in portrait mode.
6. Move the images to the output directory.
