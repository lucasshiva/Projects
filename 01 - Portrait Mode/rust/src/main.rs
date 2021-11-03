extern crate dirs;
extern crate image;

use image::image_dimensions;
use std::fs;

fn main() -> std::io::Result<()> {
    let home_dir = dirs::home_dir().unwrap();
    let image_dir = home_dir.join("Pictures").join("Wallpapers");
    let output_dir = image_dir.join("Portrait");

    // Creates the output directory.
    if !output_dir.exists() {
        fs::create_dir_all(output_dir.as_path()).ok();
    }

    // Iterate over the image directory.
    for entry in fs::read_dir(image_dir)? {
        let entry = entry?;

        // Skip directories.
        if entry.path().is_dir() {
            continue;
        }

        // Get image's dimensions.
        let (width, height) = image_dimensions(entry.path()).unwrap();
        if width > height {
            continue;
        }

        // Set the image's new path.
        let new_path = output_dir.join(entry.file_name());
        println!("Moving {:?} to {:?}", entry.file_name(), new_path);

        // Move image to output directory.
        fs::rename(entry.path(), new_path).ok();
    }

    Ok(())
}
