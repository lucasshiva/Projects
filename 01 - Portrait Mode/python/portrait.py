from pathlib import Path
from shutil import move

# We use Pillow for image operations.
# You can install it with: pip install Pillow
from PIL import Image, UnidentifiedImageError


def main() -> None:
    images_dir = Path("~").joinpath("Pictures", "Wallpapers").expanduser()
    output_dir = images_dir.joinpath("Portrait")

    # Create the output directory if it doesn't exist.
    try:
        output_dir.mkdir()
    except FileExistsError:
        pass

    # Iterate over the base directory.
    for path in images_dir.iterdir():

        # Skip directories, we only need files.
        if path.is_dir():
            continue

        # Tries to load the file as an image.
        # Throws an exception if the file is not a valid image.
        try:
            image = Image.open(path)
        except UnidentifiedImageError:
            continue

        # Skip images that are *not* in portrait mode.
        if image.height < image.width:
            continue

        # Set the image's output path.
        output_path = output_dir.joinpath(path.name)

        # Move image to new location.
        print(f"Moving {path.name} to {output_path}")
        move(path, output_path)


if __name__ == "__main__":
    main()
