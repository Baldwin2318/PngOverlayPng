from PIL import Image

base_path = "png1.png"
overlay_path = "png2.png"
output_path = "png3.png"

# resize factor (0.5 = 50%, 2.0 = 200%)
scale = 0.7

# open images
base = Image.open(base_path).convert("RGBA")
overlay = Image.open(overlay_path).convert("RGBA")

# resize overlay
new_width = int(overlay.width * scale)
new_height = int(overlay.height * scale)
overlay = overlay.resize((new_width, new_height), Image.LANCZOS)

# position where png2 will be placed
x = 000
y = 3000

# paste overlay
base.paste(overlay, (x, y), overlay)

# save result
base.save(output_path)