from PIL import Image, ImageEnhance, ImageChops, ImageFilter

# Path to the image
image_path = r'C:\projects\M122_Aufgabe3\images\lizard.jpg'  # Replace with your actual image file name

# Load the existing image
base_image = Image.open(image_path)

# Generate the Mandelbrot effect image
# Define the size (should match the base image size or the size you desire)
size = base_image.size  # Use the size of the base image for consistency

# Define the extent of the Mandelbrot set (this controls the area of the set)
extent = (-2.0, -1.5, 1.0, 1.5)  # Typical extent for Mandelbrot set

# Define the quality (number of iterations for generating the set)
quality = 1000  # Adjust the quality as needed (higher means more detail)

# Create the Mandelbrot effect image
mandelbrot_image = Image.effect_mandelbrot(size, extent, quality)

# Optional: Apply a color palette to the Mandelbrot image
# This can be done by converting the grayscale image to RGB and applying a color map
mandelbrot_image = mandelbrot_image.convert('RGB')
mandelbrot_image = mandelbrot_image.filter(ImageFilter.CONTOUR)  # Apply contour filter to emphasize edges

# Create a color gradient
palette = Image.new('RGB', mandelbrot_image.size)
for y in range(mandelbrot_image.height):
    for x in range(mandelbrot_image.width):
        value = mandelbrot_image.getpixel((x, y))
        color = (value[0] % 256, (value[0] * 2) % 256, (value[0] * 4) % 256)  # Example color mapping
        palette.putpixel((x, y), color)

mandelbrot_image = Image.blend(mandelbrot_image, palette, alpha=0.5)

# Resize the Mandelbrot image to match the base image if needed
mandelbrot_image = mandelbrot_image.resize(base_image.size)

# Optional: Enhance the Mandelbrot image (e.g., increase contrast)
enhancer = ImageEnhance.Contrast(mandelbrot_image)
mandelbrot_image = enhancer.enhance(2)  # Increase contrast

# Combine the Mandelbrot image with the base image
# Experiment with different blending modes
combined_image = Image.blend(base_image.convert('RGBA'), mandelbrot_image.convert('RGBA'), alpha=0.5)

# Save the combined image
combined_image.save(r'C:\projects\M122_Aufgabe3\images\combined_image.png')  # Save the combined image to the same folder

# Display the combined image
combined_image.show()
