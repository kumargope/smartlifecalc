import os
from PIL import Image, ImageDraw

OUTPUT_DIR = r"C:\Users\Mukesh\.gemini\antigravity\scratch\smartlifecalc\assets\pins"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Generate high-converting vertical 1000x1500 Pinterest pin graphics for top calculators
viral_pins = [
    {
        "filename": "tip-calculator-pin.png",
        "badge": "US DINING GUIDE 2026",
        "title": "Tipping in USA:\nHow Much Should\nYou Tip?",
        "subtitle": "Calculate Exact Gratuity & Split Restaurant Bills In Seconds",
        "bg_color": "#ec4899"
    },
    {
        "filename": "mortgage-calculator-pin.png",
        "badge": "HOME BUYING USA",
        "title": "Calculate Your\nMonthly Mortgage\nPayment 2026",
        "subtitle": "15, 20 & 30 Year US Home Loan Principal & Interest Estimator",
        "bg_color": "#8b5cf6"
    },
    {
        "filename": "gas-cost-calculator-pin.png",
        "badge": "ROAD TRIP HACKS",
        "title": "Gas Cost Calculator:\nHow Much Will\nYour Trip Cost?",
        "subtitle": "Calculate Fuel Expenses & Split Gas Costs Per Person Easily",
        "bg_color": "#f59e0b"
    },
    {
        "filename": "age-calculator-pin.png",
        "badge": "EVERYDAY UTILITIES",
        "title": "Exact Age & Days\nLived Calculator",
        "subtitle": "Find Your Exact Age In Years, Months, Days & Hours",
        "bg_color": "#10b981"
    },
    {
        "filename": "discount-calculator-pin.png",
        "badge": "SMART SHOPPING",
        "title": "Calculate Sale Price\n& Total Savings\nInstantly",
        "subtitle": "Never Guess Percentage Off Deals Again",
        "bg_color": "#06b6d4"
    }
]

width, height = 1000, 1500

for pin in viral_pins:
    img = Image.new("RGB", (width, height), "#0f172a")
    draw = ImageDraw.Draw(img)

    # Gradient Top Header Card
    draw.rectangle([0, 0, width, 550], fill=pin['bg_color'])

    # Inner Glass Card
    draw.rounded_rectangle([50, 220, 950, 1380], radius=35, fill="#ffffff", outline="#e2e8f0", width=4)

    # Top Badge
    draw.rounded_rectangle([100, 100, 900, 170], radius=30, fill="#ffffff")
    draw.text((120, 120), pin['badge'], fill=pin['bg_color'])

    # Title & Subtitle
    draw.text((100, 300), pin['title'], fill="#0f172a")
    draw.text((100, 600), pin['subtitle'], fill="#64748b")

    # Call to Action Box
    draw.rounded_rectangle([100, 1150, 900, 1280], radius=25, fill=pin['bg_color'])
    draw.text((180, 1190), "TRY 100% FREE CALCULATOR →", fill="#ffffff")

    # Save to Pinterest Label
    draw.text((380, 1420), "SmartLifeCalc.com", fill="#94a3b8")

    out_path = os.path.join(OUTPUT_DIR, pin['filename'])
    img.save(out_path)
    print(f"Generated Pinterest Pin Graphic: {pin['filename']}")

print("Batch Pinterest Pin Image Generation Complete!")
