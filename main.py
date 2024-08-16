from PIL import Image

def compress_image(input_path, output_path, quality=85):
    # Open the image
    img = Image.open(input_path)

    # Save the image with JPEG compression
    img.save(output_path, quality=quality)

# Example usage
input_image_path = "input_image.jpg"
output_image_path = "compressed_image.jpg"
compress_image(input_image_path, output_image_path, quality=75)
