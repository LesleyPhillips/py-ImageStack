from PIL import Image

# Load both images
img1 = Image.open("map1.png").convert("RGBA")
img2 = Image.open("map2.png").convert("RGBA")

# Resize to match dimensions if needed
img2 = img2.resize(img1.size)

# Blend or overlay them
# Option 1: simple transparency blend
combined = Image.blend(img1, img2, alpha=0.5)

# Option 2: overlay with alpha compositing
# combined = Image.alpha_composite(img1, img2)

# Save or show the result
combined.save("combined_map.png")
combined.show()