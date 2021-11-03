# Projects
This repository is a compilation of small/medium projects made in different programming languages. 

## Why?
This repository is purely for educational purposes.

The goal is to recreate the same project in different languages in order to become more familiar with said languages. 

## Important Notes
- Projects may use (and share) a configuration file to allow more customization.
- There will be a list of steps to achieve the desired functionality in each project's description.
- Some projects may not be cross-platform, meaning they will only work on Linux or Windows. The projects are *not* made with Mac OS support in mind.
- Projects *can* depend on external libraries/frameworks to achieve the desired functionality. The goal is to understand more about the languages, not to code everything from scratch.

## Project List
---
### Portrait Mode
Move or copy all images in portrait mode from a directory to another. 

This project aims for speed and simplicity. We *only* need the image's dimension. If its width and height can be read without opening/loading the entire image, then do so.

The program should work in a way that it does not need to filter the files by their extensions in order to load the images, but if that is not possible, then filter by **.jpg** and **.png**.

Files with the same name in the output directory will be overwritten.

**Defaults**  
The default base directory is: 
- **Linux**: `/home/<user>/Pictures/Wallpapers`
- **Windows**: `C:\Users\<user>\Pictures\Wallpapers`

The default output directory is named **Portrait** and it will be located inside the base directory. In other words, the default output directory is `"{base_directory}/Portrait"`. 

The directory will be created, if needed. Otherwise, the program will simply use the existing directory.

**Configuration**  
The configuration file is called `config.json` and has the following settings:
- `image_directory` (string): The directory containing all the images.
- `output_directory` (string): The directory where files will be moved/copied to.
- `move_images` (boolean): Whether to move (true) or copy (false) images.

**Note**: Avoid using tilde or environment variables, i.e. `~` or `$HOME` instead of `/home/<user>`. The former may be not interpreted correctly. 
