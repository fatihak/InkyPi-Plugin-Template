from plugins.base_plugin.base_plugin import BasePlugin
from PIL import Image, ImageDraw, ImageFont
import logging

logger = logging.getLogger(__name__)


class Template(BasePlugin):
    """
    Example InkyPi plugin template.

    This plugin demonstrates how to generate a Pillow image and return it
    to InkyPi for display. Plugin authors can use this as a starting point
    for building custom plugins.
    """

    def generate_image(self, settings, device_config):
        """
        Generate and return a PIL image for display.

        Args:
            settings (dict):
                Values from the plugin's settings page form.
                Example:
                    title = settings.get("title", "Hello World")

            device_config:
                Device configuration. Can be used to load secrets
                or device-level configuration:
                    api_key = device_config.load_env_key("MY_API_KEY")
                    dimensions = device_config.get_resolution()

        Returns:
            PIL.Image.Image:
                The rendered image to be displayed on the device.
        """
        # Example: load a value from plugin settings
        text = settings.get("title", "Hello World")

        # Target display size, handling display orientation from device config
        dimensions = device_config.get_resolution()
        if device_config.get_config("orientation") == "vertical":
            dimensions = dimensions[::-1]

        # Create a blank image
        image = Image.new("RGB", (width, height), "white")
        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default()

        # Measure text size
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        # Center text
        x = (width - text_width) // 2
        y = (height - text_height) // 2

        # Draw text
        draw.text((x, y), text, fill="black", font=font)

        logger.debug("Template plugin rendered image (%dx%d)", width, height)

        return image
