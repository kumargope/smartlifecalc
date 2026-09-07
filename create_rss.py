import os
import re

reg_path = r'C:\Users\Mukesh\.gemini\antigravity\scratch\smartlifecalc\js\data\calculators-registry.js'
with open(reg_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

# Match each object { id: '...', slug: '...', name: '...', title: '...', category: '...', desc: '...' }
pattern = re.compile(r"\{\s*id:\s*'([^']+)',\s*slug:\s*'([^']+)',\s*name:\s*'([^']+)',\s*title:\s*'([^']+)',\s*category:\s*'([^']+)',\s*desc:\s*'([^']+)'", re.DOTALL)

matches = pattern.findall(js_content)

rss_items = []
base_url = 'https://smartlifecalc.vercel.app'
pins_dir = r'C:\Users\Mukesh\.gemini\antigravity\scratch\smartlifecalc\assets\pins'

for cid, slug, name, title, cat, desc in matches:
    link = f"{base_url}/calculators/{slug}.html"
    pin_filename = f"{slug}-pin.png"
    if os.path.exists(os.path.join(pins_dir, pin_filename)):
        img_url = f"{base_url}/assets/pins/{pin_filename}"
    else:
        img_url = f"{base_url}/assets/pinterest-banner.png"
    
    # escape XML special chars
    title_xml = title.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    desc_xml = desc.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

    item = f"""    <item>
      <title>{title_xml} — Free 3D Calculator</title>
      <link>{link}</link>
      <guid>{link}</guid>
      <description>{desc_xml} Fast 100% free US everyday 3D calculator.</description>
      <enclosure url="{img_url}" type="image/png" />
      <pubDate>Mon, 07 Sep 2026 11:00:00 GMT</pubDate>
    </item>"""
    rss_items.append(item)

rss_xml = f"""<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0" xmlns:content="http://purl.org/rss/1.0/modules/content/">
<channel>
  <title>SmartLifeCalc — 3D Everyday Calculators</title>
  <link>{base_url}</link>
  <description>Free 3D vibrant calculators for money, home, car, date, shopping and converters.</description>
  <language>en-us</language>
{chr(10).join(rss_items)}
</channel>
</rss>"""

rss_path = r'C:\Users\Mukesh\.gemini\antigravity\scratch\smartlifecalc\rss.xml'
with open(rss_path, 'w', encoding='utf-8') as f:
    f.write(rss_xml)

print('rss.xml created successfully with', len(matches), 'items!')
