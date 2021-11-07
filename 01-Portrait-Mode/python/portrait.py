import json
from pathlib import Path
from shutil import move, copy2

# We use Pillow for image operations.
# You can install it with: pip install Pillow
from PIL import Image, UnidentifiedImageError


DEFAULT_IMAGE_DIRECTORY = Path("~").joinpath("Pictures", "Wallpapers").expanduser()


def read_config() -> dict:
    """Read the configuration file and return its contents."""
    with open(Path("../config.json")) as f:
        return json.load(f)


def get_paths(config: dict) -> tuple[Path, Path]:
    """Read the config dict to decide whether to use the default paths or not."""
    if not config["image_directory"]:
        image_dir = DEFAULT_IMAGE_DIRECTORY
    else:
        image_dir = Path(config["image_directory"])

    if not config["output_directory"]:
        output_dir = image_dir.joinpath("Portrait")
    else:
        output_dir = Path(config["output_directory"])

    return image_dir, output_dir


def main() -> None:
    config = read_config()
    image_dir, output_dir = get_paths(config)

    # Create the output directory if it doesn't exist.
    try:
        output_dir.mkdir()
    except FileExistsError:
        pass

    # Iterate over the base directory.
    for path in image_dir.iterdir():

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

        # Copy image to new location.
        if not config["move_images"]:
            print(f"Copying {path.name} to {output_path}")
            copy2(path, output_dir)

        # Or move them instead.
        else:
            print(f"Moving {path.name} to {output_path}")
            move(path, output_path)


if __name__ == "__main__":
    main()
