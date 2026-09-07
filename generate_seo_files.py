import os

BASE_URL = "https://smartlifecalc.com"

# 40 Calculators + Homepage + Legal
urls = [
    "/index.html",
    "/legal/privacy.html",
    "/legal/terms.html",
    "/legal/disclaimer.html",
    "/legal/contact.html"
]

all_ids = [
  "tip-calculator", "discount-calculator", "sales-tax-calculator", "split-bill-calculator", "percentage-calculator",
  "simple-interest-calculator", "compound-interest-calculator", "loan-payment-calculator", "hourly-to-salary-calculator", "salary-to-hourly-calculator",
  "mortgage-calculator", "home-affordability-calculator", "rent-vs-buy-calculator", "electricity-cost-calculator", "area-calculator",
  "gas-cost-calculator", "mpg-calculator", "road-trip-cost-calculator", "fuel-cost-calculator", "car-loan-calculator",
  "age-calculator", "date-difference-calculator", "days-until-calculator", "workdays-calculator", "time-difference-calculator",
  "sale-price-calculator", "percentage-off-calculator", "unit-price-calculator", "buy-one-get-one-calculator", "price-comparison-calculator",
  "miles-to-km", "km-to-miles", "pounds-to-kg", "kg-to-pounds", "feet-to-inches",
  "feet-inches-to-cm", "fahrenheit-to-celsius", "celsius-to-fahrenheit", "gallons-to-liters", "ounces-to-grams"
]

for cid in all_ids:
    urls.append(f"/calculators/{cid}.html")

# Create sitemap.xml
sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
sitemap_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

for u in urls:
    priority = "1.0" if u == "/index.html" else "0.8"
    sitemap_content += f"""  <url>
    <loc>{BASE_URL}{u}</loc>
    <lastmod>2026-09-07</lastmod>
    <changefreq>weekly</changefreq>
    <priority>{priority}</priority>
  </url>\n"""

sitemap_content += '</urlset>'

with open(r"C:\Users\Mukesh\.gemini\antigravity\scratch\smartlifecalc\sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap_content)

# Create robots.txt allowing Pinterestbot and Googlebot
robots_content = """# SmartLifeCalc Robots.txt
User-agent: *
Allow: /

User-agent: Pinterestbot
Allow: /

User-agent: Googlebot
Allow: /

Sitemap: https://smartlifecalc.com/sitemap.xml
"""

with open(r"C:\Users\Mukesh\.gemini\antigravity\scratch\smartlifecalc\robots.txt", "w", encoding="utf-8") as f:
    f.write(robots_content)

print("Generated sitemap.xml and robots.txt successfully!")
