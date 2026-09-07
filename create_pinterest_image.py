from PIL import Image, ImageDraw, ImageFont
import os

OUTPUT_PATH = r"C:\Users\Mukesh\.gemini\antigravity\scratch\smartlifecalc\assets\pinterest-banner.png"
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

# 1000 x 1500 Pinterest Vertical Aspect Ratio (2:3)
width, height = 1000, 1500
image = Image.new("RGB", (width, height), "#f8fafc")
draw = ImageDraw.Draw(image)

# Background Top Banner Card
draw.rectangle([0, 0, width, 500], fill="#2563eb")

# Decorative Card Inner Container
draw.rounded_rectangle([60, 250, 940, 1380], radius=30, fill="#ffffff", outline="#e2e8f0", width=4)

# Text Header
draw.text((100, 120), "SmartLifeCalc", fill="#ffffff")

# Banner Main Text
draw.text((120, 320), "FREE EVERYDAY CALCULATORS", fill="#2563eb")
draw.text((120, 420), "Simple Calculators\nFor Everyday Life", fill="#0f172a")

# Features List Box
features = [
    "💵 Tip & Split Bill Calculator",
    "🏷️ Discount & Sales Tax Calculator",
    "🏡 Mortgage & Home Loan Calculator",
    "⛽ Gas & Road Trip Cost Calculator",
    "🎂 Age & Date Difference Calculator",
    "🔄 Instant Unit Converters"
]

y_pos = 620
for feature in features:
    draw.rounded_rectangle([120, y_pos, 880, y_pos + 90], radius=16, fill="#f1f5f9")
    draw.text((150, y_pos + 25), feature, fill="#1e293b")
    y_pos += 110

# Bottom Badge
draw.rounded_rectangle([250, 1400, 750, 1470], radius=35, fill="#e60023")
draw.text((380, 1420), "Save to Pinterest", fill="#ffffff")

image.save(OUTPUT_PATH)
print("Successfully generated assets/pinterest-banner.png!")
