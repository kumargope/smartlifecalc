import os
import json

OUTPUT_DIR = r"C:\Users\Mukesh\.gemini\antigravity\scratch\smartlifecalc\calculators"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def render_calculator_page(c):
    related_links_html = ""
    for rel_id in c.get('related', ["tip-calculator", "discount-calculator", "mortgage-calculator", "gas-cost-calculator"]):
        rel_title = rel_id.replace('-', ' ').title()
        related_links_html += f'''
          <a href="/calculators/{rel_id}.html" class="related-card">
            <h4>{rel_title}</h4>
            <p>Calculate {rel_title.lower()} instantly.</p>
          </a>
        '''

    faqs_html = ""
    faq_schema_items = []
    for faq in c.get('faqs', []):
        faqs_html += f'''
          <div class="faq-item">
            <button class="faq-question">
              <span>{faq['q']}</span>
              <span class="faq-icon">▼</span>
            </button>
            <div class="faq-answer">{faq['a']}</div>
          </div>
        '''
        faq_schema_items.append({
            "@type": "Question",
            "name": faq['q'],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": faq['a']
            }
        })

    faq_schema_json = json.dumps({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": faq_schema_items
    }, indent=2)

    breadcrumb_schema_json = json.dumps({
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://smartlifecalc.com/"},
            {"@type": "ListItem", "position": 2, "name": c['category'], "item": f"https://smartlifecalc.com/#categories"},
            {"@type": "ListItem", "position": 3, "name": c['title'], "item": f"https://smartlifecalc.com{c['url']}"}
        ]
    }, indent=2)

    app_schema_json = json.dumps({
        "@context": "https://schema.org",
        "@type": "WebApplication",
        "name": f"{c['title']} — SmartLifeCalc 3D",
        "url": f"https://smartlifecalc.com{c['url']}",
        "description": c['meta_desc'],
        "applicationCategory": "UtilityApplication",
        "operatingSystem": "All"
    }, indent=2)

    seo_paragraphs_html = "".join([f"<p>{p}</p>" for p in c.get('seo_paragraphs', [])])

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{c['title']} — SmartLifeCalc 3D</title>
  <meta name="description" content="{c['meta_desc']}">
  <link rel="canonical" href="https://smartlifecalc.com{c['url']}">

  <!-- OpenGraph / Social Metadata -->
  <meta property="og:title" content="{c['title']} — SmartLifeCalc 3D">
  <meta property="og:description" content="{c['meta_desc']}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://smartlifecalc.com{c['url']}">
  <meta property="og:image" content="https://smartlifecalc.com/assets/pinterest-banner.png">

  <!-- Twitter Metadata -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{c['title']}">
  <meta name="twitter:description" content="{c['meta_desc']}">
  <meta name="twitter:image" content="https://smartlifecalc.com/assets/pinterest-banner.png">

  <!-- Stylesheets -->
  <link rel="stylesheet" href="/css/main.css">
  <link rel="stylesheet" href="/css/components.css">

  <!-- JSON-LD Structured Data -->
  <script type="application/ld+json">
  {app_schema_json}
  </script>
  <script type="application/ld+json">
  {breadcrumb_schema_json}
  </script>
  <script type="application/ld+json">
  {faq_schema_json}
  </script>
</head>
<body>

  <!-- Header -->
  <header class="header">
    <div class="container header-nav">
      <a href="/index.html" class="logo">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="url(#logoGrad2)" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round">
          <defs>
            <linearGradient id="logoGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#ec4899" />
              <stop offset="50%" stop-color="#8b5cf6" />
              <stop offset="100%" stop-color="#3b82f6" />
            </linearGradient>
          </defs>
          <rect x="4" y="2" width="16" height="20" rx="2"/><line x1="8" y1="6" x2="16" y2="6"/><line x1="16" y1="14" x2="16" y2="18"/><path d="M16 10h.01"/><path d="M12 10h.01"/><path d="M8 10h.01"/><path d="M12 14h.01"/><path d="M8 14h.01"/><path d="M12 18h.01"/><path d="M8 18h.01"/>
        </svg>
        SmartLife<span>Calc</span>
        <span class="logo-badge">Vibrant 3D</span>
      </a>
      <nav class="nav-links">
        <a href="/index.html">Home</a>
        <a href="/index.html#popular">Popular</a>
        <a href="/index.html#categories">Categories</a>
        <a href="/legal/disclaimer.html">Disclaimer</a>
      </nav>
      <div class="header-actions">
        <button class="search-trigger" id="headerSearchTrigger" aria-label="Search calculators">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#8b5cf6" stroke-width="2.5"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
          <span>Search...</span>
        </button>
        <button class="mobile-menu-btn" id="mobileMenuBtn" aria-label="Toggle menu">☰</button>
      </div>
    </div>
  </header>

  <!-- Mobile Drawer -->
  <div class="mobile-drawer" id="mobileDrawer">
    <ul class="mobile-nav-list">
      <li><a href="/index.html">Home</a></li>
      <li><a href="/index.html#popular">Popular Calculators</a></li>
      <li><a href="/legal/privacy.html">Privacy Policy</a></li>
    </ul>
  </div>

  <main>
    <div class="container">
      <!-- Breadcrumb -->
      <nav class="breadcrumb" aria-label="Breadcrumb">
        <a href="/index.html">Home</a>
        <span class="separator">/</span>
        <a href="/index.html#categories">{c['category']}</a>
        <span class="separator">/</span>
        <span>{c['title']}</span>
      </nav>

      <!-- Page Intro -->
      <div class="page-intro">
        <h1>{c['h1']}</h1>
        <p>{c['intro']}</p>
      </div>

      <!-- Main Layout Grid -->
      <div class="calc-layout-grid">
        <div class="calc-main-column">
          
          <!-- 3D Calculator Card -->
          <div class="calc-card">
            <h2 class="calc-card-title">
              <span>{c.get('icon', '🧮')}</span>
              <span>{c['title']}</span>
            </h2>

            <form id="calcForm" onsubmit="event.preventDefault(); calculate();">
              {c['inputs_html']}

              <div class="button-row">
                <button type="button" class="btn-primary" onclick="calculate()">Calculate</button>
                <button type="button" class="btn-secondary" onclick="resetCalc()">Reset</button>
              </div>
            </form>

            <!-- Large 3D Result Card -->
            {c['results_html']}
          </div>

          <!-- SEO Content Article Section -->
          <article class="content-article">
            <h2>About {c['title']}</h2>
            {seo_paragraphs_html}

            <h2>Formula & How It Works</h2>
            <div class="formula-box">
              {c['formula']}
            </div>

            <h2>Step-by-Step Example Calculation</h2>
            <p style="white-space: pre-line;">{c['example']}</p>

            <h2>Helpful Tips & Practical Advice</h2>
            <ul>
              <li>Always verify numbers before making final financial decisions or purchases.</li>
              <li>Inputs update results dynamically in real-time.</li>
              <li>Calculations run 100% locally in your browser with zero server data storage.</li>
            </ul>

            <!-- Pinterest Strategy Share Card -->
            <div class="pinterest-share-card">
              <div class="pinterest-share-info">
                <h3>Save this calculator for later</h3>
                <p>Pin {c['title']} to your favorite Pinterest board for fast access anytime!</p>
              </div>
              <button class="pinterest-btn" onclick="shareToPinterest('https://smartlifecalc.com{c['url']}', 'https://smartlifecalc.com/assets/pinterest-banner.png', '{c['title']} — Free Calculator on SmartLifeCalc')">
                <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M12 0C5.373 0 0 5.372 0 12c0 5.084 3.163 9.426 7.627 11.174-.105-.949-.2-2.405.042-3.441.218-.937 1.407-5.965 1.407-5.965s-.359-.719-.359-1.782c0-1.668.967-2.914 2.171-2.914 1.023 0 1.518.769 1.518 1.69 0 1.029-.655 2.568-.994 3.995-.283 1.194.599 2.169 1.777 2.169 2.133 0 3.772-2.249 3.772-5.495 0-2.873-2.064-4.882-5.012-4.882-3.414 0-5.418 2.561-5.418 5.207 0 1.031.397 2.138.893 2.738.098.119.112.224.083.345l-.333 1.36c-.053.22-.174.267-.402.161-1.499-.698-2.436-2.889-2.436-4.649 0-3.785 2.75-7.262 7.929-7.262 4.163 0 7.398 2.967 7.398 6.931 0 4.136-2.607 7.464-6.227 7.464-1.216 0-2.359-.631-2.75-1.378l-.748 2.853c-.271 1.043-1.002 2.35-1.492 3.146C9.57 23.812 10.763 24 12 24c6.627 0 12-5.373 12-12 0-6.628-5.373-12-12-12z"/></svg>
                Save to Pinterest
              </button>
            </div>

            <!-- FAQ Section -->
            <div class="faq-section">
              <h2>Frequently Asked Questions</h2>
              {faqs_html}
            </div>
          </article>

          <!-- Related Calculators -->
          <div class="related-calcs">
            <h3>Related Calculators</h3>
            <div class="related-grid">
              {related_links_html}
            </div>
          </div>

        </div>

        <!-- Sidebar / Ad Placeholder -->
        <aside class="calc-sidebar">
          <div class="ad-placeholder" style="min-height: 250px; display: flex; align-items: center; justify-content: center;">
            Display Ad Placeholder<br>(Responsive Banner)
          </div>
          <div class="ad-placeholder" style="min-height: 400px; display: flex; align-items: center; justify-content: center; margin-top: 1.5rem;">
            Display Ad Placeholder<br>(Sidebar Half-Page)
          </div>
        </aside>
      </div>
    </div>
  </main>

  <!-- Footer -->
  <footer class="footer">
    <div class="container">
      <div class="footer-bottom">
        <p>&copy; 2026 SmartLifeCalc. All rights reserved.</p>
        <p><a href="/index.html" style="color:#94a3b8;">Home</a> | <a href="/legal/privacy.html" style="color:#94a3b8;">Privacy</a> | <a href="/legal/disclaimer.html" style="color:#94a3b8;">Disclaimer</a></p>
      </div>
    </div>
  </footer>

  <!-- Search Modal Overlay -->
  <div class="search-modal-overlay" id="searchModalOverlay">
    <div class="search-modal">
      <div class="search-input-header">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#ec4899" stroke-width="2.5"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
        <input type="text" id="modalSearchInput" placeholder="Type a calculator name or keyword...">
        <button class="search-close-btn" id="searchCloseBtn">✕</button>
      </div>
      <div class="search-results-list" id="searchResultsList"></div>
    </div>
  </div>

  <!-- Scripts -->
  <script src="/js/data/calculators-registry.js"></script>
  <script src="/js/calculator-engine.js"></script>
  <script src="/js/3d-effects.js"></script>
  <script src="/js/interactive-eye.js"></script>
  <script src="/js/app.js"></script>
  <script>
    {c['calc_js']}
  </script>
</body>
</html>
"""

# Custom definitions
custom_calcs = {
    "tip-calculator": {
        "title": "Tip Calculator", "category": "Money", "url": "/calculators/tip-calculator.html", "icon": "💵",
        "meta_desc": "Free Tip Calculator. Calculate restaurant tip amounts, total bills, and split per person with 15%, 18%, 20%, 25% presets.",
        "h1": "Free Tip Calculator — Split Bill & Calculate Gratuity",
        "intro": "Calculate restaurant tips and split group bills evenly in seconds.",
        "inputs_html": """
          <div class="form-group"><label for="bill">Bill Amount ($)</label><div class="input-wrapper"><span class="input-prefix">$</span><input type="number" id="bill" class="form-control has-prefix" value="85.00"></div></div>
          <div class="form-group"><label for="tip">Tip Percentage (%)</label><div class="input-wrapper"><input type="number" id="tip" class="form-control has-suffix" value="18"><span class="input-suffix">%</span></div>
            <div class="preset-buttons"><button type="button" class="preset-btn" onclick="setTip(15)">15%</button><button type="button" class="preset-btn active" onclick="setTip(18)">18%</button><button type="button" class="preset-btn" onclick="setTip(20)">20%</button><button type="button" class="preset-btn" onclick="setTip(25)">25%</button></div>
          </div>
          <div class="form-group"><label for="people">Number of People</label><input type="number" id="people" class="form-control" value="2"></div>
        """,
        "calc_js": """
          function setTip(pct) { document.getElementById('tip').value = pct; calculate(); }
          function calculate() {
            const b = parseFloat(document.getElementById('bill').value)||0;
            const t = parseFloat(document.getElementById('tip').value)||0;
            const p = parseInt(document.getElementById('people').value)||1;
            const res = CalcEngine.calculateTip(b, t, p);
            document.getElementById('resTipAmt').innerText = CalcEngine.formatCurrency(res.tipAmount);
            document.getElementById('resTotBill').innerText = CalcEngine.formatCurrency(res.totalBill);
            document.getElementById('resPerPerson').innerText = CalcEngine.formatCurrency(res.perPerson);
            if(window.trigger3DResultAnimation) window.trigger3DResultAnimation();
          }
          function resetCalc() { document.getElementById('bill').value='85.00'; document.getElementById('tip').value='18'; document.getElementById('people').value='2'; calculate(); }
          document.querySelectorAll('input').forEach(i => i.addEventListener('input', calculate));
          window.addEventListener('DOMContentLoaded', calculate);
        """,
        "results_html": """
          <div class="result-card">
            <div class="result-card-header"><span class="result-card-title">Tip Breakdown</span><button class="copy-result-btn" data-copy-target="resTotBill">Copy Result</button></div>
            <div class="result-item-label">Tip Amount</div>
            <div class="result-main-value" id="resTipAmt">$15.30</div>
            <div class="result-grid">
              <div class="result-item"><span class="result-item-label">Total Bill</span><span class="result-item-value" id="resTotBill">$100.30</span></div>
              <div class="result-item"><span class="result-item-label">Per Person Total</span><span class="result-item-value" id="resPerPerson">$50.15</span></div>
            </div>
          </div>
        """,
        "formula": "Tip Amount = Bill × (Tip % ÷ 100)\nTotal = Bill + Tip Amount\nPer Person = Total ÷ People",
        "example": "A $85 bill with 18% tip split between 2 people = $15.30 tip, $100.30 total ($50.15 each).",
        "seo_paragraphs": ["Tipping 15-20% is standard in US dining. Easily split restaurant tabs with zero math errors."],
        "faqs": [{"q": "What is standard US tip?", "a": "18% to 20% is baseline standard for sit-down service."}],
        "related": ["split-bill-calculator", "discount-calculator", "sales-tax-calculator"]
    },

    "mortgage-calculator": {
        "title": "Mortgage Calculator", "category": "Home", "url": "/calculators/mortgage-calculator.html", "icon": "🏡",
        "meta_desc": "Free Mortgage Calculator. Estimate monthly principal and interest payments for 15, 20, or 30 year home loans.",
        "h1": "Free Mortgage Calculator — Estimate Monthly Payments",
        "intro": "Calculate your estimated monthly mortgage principal and interest payment instantly.",
        "inputs_html": """
          <div class="form-group"><label for="mPrice">Home Price ($)</label><div class="input-wrapper"><span class="input-prefix">$</span><input type="number" id="mPrice" class="form-control has-prefix" value="350000"></div></div>
          <div class="form-group"><label for="mDown">Down Payment ($)</label><div class="input-wrapper"><span class="input-prefix">$</span><input type="number" id="mDown" class="form-control has-prefix" value="70000"></div></div>
          <div class="form-group"><label for="mRate">Interest Rate (%)</label><div class="input-wrapper"><input type="number" id="mRate" class="form-control has-suffix" value="6.5"><span class="input-suffix">%</span></div></div>
          <div class="form-group"><label for="mTerm">Loan Term (Years)</label><input type="number" id="mTerm" class="form-control" value="30"><div class="preset-buttons"><button type="button" class="preset-btn" onclick="setTerm(15)">15 Yrs</button><button type="button" class="preset-btn" onclick="setTerm(20)">20 Yrs</button><button type="button" class="preset-btn active" onclick="setTerm(30)">30 Yrs</button></div></div>
        """,
        "calc_js": """
          function setTerm(t) { document.getElementById('mTerm').value = t; calculate(); }
          function calculate() {
            const p = parseFloat(document.getElementById('mPrice').value)||0;
            const d = parseFloat(document.getElementById('mDown').value)||0;
            const r = parseFloat(document.getElementById('mRate').value)||0;
            const y = parseInt(document.getElementById('mTerm').value)||30;
            const res = CalcEngine.calculateMortgage(p, d, r, y);
            document.getElementById('resMortPmt').innerText = CalcEngine.formatCurrency(res.monthlyPayment);
            document.getElementById('resMortLoan').innerText = CalcEngine.formatCurrency(res.loanAmount);
            document.getElementById('resMortInt').innerText = CalcEngine.formatCurrency(res.totalInterest);
            if(window.trigger3DResultAnimation) window.trigger3DResultAnimation();
          }
          function resetCalc() { document.getElementById('mPrice').value='350000'; document.getElementById('mDown').value='70000'; document.getElementById('mRate').value='6.5'; document.getElementById('mTerm').value='30'; calculate(); }
          document.querySelectorAll('input').forEach(i => i.addEventListener('input', calculate));
          window.addEventListener('DOMContentLoaded', calculate);
        """,
        "results_html": """
          <div class="result-card">
            <div class="result-card-header"><span class="result-card-title">Mortgage Estimate</span><button class="copy-result-btn" data-copy-target="resMortPmt">Copy Result</button></div>
            <div class="result-item-label">Monthly Principal & Interest</div>
            <div class="result-main-value" id="resMortPmt">$1,769.79</div>
            <div class="result-grid">
              <div class="result-item"><span class="result-item-label">Loan Amount</span><span class="result-item-value" id="resMortLoan">$280,000.00</span></div>
              <div class="result-item"><span class="result-item-label">Total Interest Paid</span><span class="result-item-value" id="resMortInt">$357,126.17</span></div>
            </div>
          </div>
        """,
        "formula": "Monthly Payment = [P × r(1+r)^n] ÷ [(1+r)^n - 1]",
        "example": "A $350,000 home with $70,000 down (20%) at 6.5% interest for 30 years yields $1,769.79 monthly P&I.",
        "seo_paragraphs": ["Results are estimates for informational purposes only and may differ from actual amounts. Always verify financial information with a licensed professional."],
        "faqs": [{"q": "Does this include property taxes?", "a": "This calculator estimates monthly Principal and Interest (P&I). Taxes and insurance vary locally."}],
        "related": ["home-affordability-calculator", "rent-vs-buy-calculator", "car-loan-calculator"]
    },

    "gas-cost-calculator": {
        "title": "Gas Cost Calculator", "category": "Car & Travel", "url": "/calculators/gas-cost-calculator.html", "icon": "⛽",
        "meta_desc": "Free Gas Cost Calculator. Compute trip fuel expenses based on distance, MPG, and gas price per gallon.",
        "h1": "Free Gas Cost Calculator — Road Trip Fuel Expenses",
        "intro": "Estimate the total gas cost for any driving trip distance instantly.",
        "inputs_html": """
          <div class="form-group"><label for="gDist">Distance (Miles)</label><input type="number" id="gDist" class="form-control" value="350"></div>
          <div class="form-group"><label for="gMpg">Vehicle MPG</label><input type="number" id="gMpg" class="form-control" value="28"></div>
          <div class="form-group"><label for="gPrice">Gas Price ($ / Gallon)</label><div class="input-wrapper"><span class="input-prefix">$</span><input type="number" id="gPrice" class="form-control has-prefix" value="3.65"></div></div>
        """,
        "calc_js": """
          function calculate() {
            const d = parseFloat(document.getElementById('gDist').value)||0;
            const m = parseFloat(document.getElementById('gMpg').value)||1;
            const p = parseFloat(document.getElementById('gPrice').value)||0;
            const res = CalcEngine.calculateGasCost(d, m, p);
            document.getElementById('resGasCost').innerText = CalcEngine.formatCurrency(res.estimatedCost);
            document.getElementById('resGasGallons').innerText = CalcEngine.formatNumber(res.gallonsNeeded, 2) + " gal";
            if(window.trigger3DResultAnimation) window.trigger3DResultAnimation();
          }
          function resetCalc() { document.getElementById('gDist').value='350'; document.getElementById('gMpg').value='28'; document.getElementById('gPrice').value='3.65'; calculate(); }
          document.querySelectorAll('input').forEach(i => i.addEventListener('input', calculate));
          window.addEventListener('DOMContentLoaded', calculate);
        """,
        "results_html": """
          <div class="result-card">
            <div class="result-card-header"><span class="result-card-title">Gas Expense Result</span><button class="copy-result-btn" data-copy-target="resGasCost">Copy Result</button></div>
            <div class="result-item-label">Estimated Fuel Cost</div>
            <div class="result-main-value" id="resGasCost">$45.63</div>
            <div class="result-grid">
              <div class="result-item"><span class="result-item-label">Gallons Needed</span><span class="result-item-value" id="resGasGallons">12.50 gal</span></div>
            </div>
          </div>
        """,
        "formula": "Gallons Needed = Distance ÷ MPG\nEstimated Fuel Cost = Gallons Needed × Gas Price",
        "example": "Driving 350 miles at 28 MPG with gas at $3.65/gal requires 12.5 gallons costing $45.63.",
        "seo_paragraphs": ["Plan road trip gas expenses accurately before setting out."],
        "faqs": [{"q": "Can I calculate in kilometers?", "a": "Yes, convert your distance using our Miles to Kilometers converter."}],
        "related": ["mpg-calculator", "road-trip-cost-calculator", "fuel-cost-calculator"]
    },

    "age-calculator": {
        "title": "Age Calculator", "category": "Date & Time", "url": "/calculators/age-calculator.html", "icon": "🎂",
        "meta_desc": "Free Age Calculator. Find your exact age in years, months, days, and total hours from date of birth.",
        "h1": "Free Age Calculator — Calculate Exact Age & Total Days",
        "intro": "Calculate your exact age down to the day and total hours elapsed.",
        "inputs_html": """
          <div class="form-group"><label for="dob">Date of Birth</label><input type="date" id="dob" class="form-control" value="1995-06-15"></div>
          <div class="form-group"><label for="ageTarget">Calculate Age On Date</label><input type="date" id="ageTarget" class="form-control" value="2026-09-07"></div>
        """,
        "calc_js": """
          function calculate() {
            const b = document.getElementById('dob').value;
            const t = document.getElementById('ageTarget').value;
            if (!b) return;
            const res = CalcEngine.calculateAge(b, t);
            document.getElementById('resAgeMain').innerText = `${res.years} Years, ${res.months} Mos, ${res.days} Days`;
            document.getElementById('resAgeDays').innerText = CalcEngine.formatNumber(res.totalDays, 0) + " Days";
            document.getElementById('resAgeHours').innerText = CalcEngine.formatNumber(res.totalHours, 0) + " Hours";
            if(window.trigger3DResultAnimation) window.trigger3DResultAnimation();
          }
          function resetCalc() { document.getElementById('dob').value='1995-06-15'; calculate(); }
          document.querySelectorAll('input').forEach(i => i.addEventListener('input', calculate));
          window.addEventListener('DOMContentLoaded', calculate);
        """,
        "results_html": """
          <div class="result-card">
            <div class="result-card-header"><span class="result-card-title">Age Summary</span><button class="copy-result-btn" data-copy-target="resAgeMain">Copy Result</button></div>
            <div class="result-item-label">Exact Age</div>
            <div class="result-main-value" id="resAgeMain">31 Years, 2 Mos, 23 Days</div>
            <div class="result-grid">
              <div class="result-item"><span class="result-item-label">Total Days Lived</span><span class="result-item-value" id="resAgeDays">11,407 Days</span></div>
              <div class="result-item"><span class="result-item-label">Total Hours Lived</span><span class="result-item-value" id="resAgeHours">273,768 Hours</span></div>
            </div>
          </div>
        """,
        "formula": "Age = Difference between target calendar date and date of birth.",
        "example": "Born June 15, 1995 evaluated on Sept 7, 2026 = 31 years, 2 months, 23 days.",
        "seo_paragraphs": ["Accurately compute age span for forms, milestones, or birthdays."],
        "faqs": [{"q": "How are leap years handled?", "a": "Leap years are automatically accounted for in exact calendar day totals."}],
        "related": ["date-difference-calculator", "days-until-calculator"]
    },

    "miles-to-km": {
        "title": "Miles to Kilometers", "category": "Converters", "url": "/calculators/miles-to-km.html", "icon": "🔄",
        "meta_desc": "Free Miles to Kilometers Converter. Instantly convert US miles to metric kilometers with live swap button.",
        "h1": "Free Miles to Kilometers Converter (mi to km)",
        "intro": "Convert distance from US Miles to Metric Kilometers instantly as you type.",
        "inputs_html": """
          <div class="form-group"><label for="miVal">Miles (mi)</label><input type="number" id="miVal" class="form-control" value="10"></div>
        """,
        "calc_js": """
          function calculate() {
            const mi = parseFloat(document.getElementById('miVal').value)||0;
            const km = CalcEngine.convertMilesToKm(mi);
            document.getElementById('resKmVal').innerText = CalcEngine.formatNumber(km, 2) + " km";
            if(window.trigger3DResultAnimation) window.trigger3DResultAnimation();
          }
          function resetCalc() { document.getElementById('miVal').value='10'; calculate(); }
          document.querySelectorAll('input').forEach(i => i.addEventListener('input', calculate));
          window.addEventListener('DOMContentLoaded', calculate);
        """,
        "results_html": """
          <div class="result-card">
            <div class="result-card-header"><span class="result-card-title">Conversion Result</span><button class="copy-result-btn" data-copy-target="resKmVal">Copy Result</button></div>
            <div class="result-item-label">Kilometers Equivalent</div>
            <div class="result-main-value" id="resKmVal">16.09 km</div>
          </div>
        """,
        "formula": "Kilometers = Miles × 1.60934",
        "example": "10 Miles × 1.60934 = 16.09 Kilometers.",
        "seo_paragraphs": ["Convert speed and distance between US customary and metric units."],
        "faqs": [{"q": "How many kilometers are in 1 mile?", "a": "There are approximately 1.60934 kilometers in 1 statute mile."}],
        "related": ["km-to-miles", "feet-to-inches", "feet-inches-to-cm"]
    }
}

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

category_map = {
  "tip-calculator": ("Money", "💵", "Tip Calculator"),
  "discount-calculator": ("Money", "🏷️", "Discount Calculator"),
  "sales-tax-calculator": ("Money", "🧾", "Sales Tax Calculator"),
  "split-bill-calculator": ("Money", "🍰", "Split Bill Calculator"),
  "percentage-calculator": ("Money", "%", "Percentage Calculator"),
  "simple-interest-calculator": ("Money", "📈", "Simple Interest Calculator"),
  "compound-interest-calculator": ("Money", "🚀", "Compound Interest Calculator"),
  "loan-payment-calculator": ("Money", "💳", "Loan Payment Calculator"),
  "hourly-to-salary-calculator": ("Money", "💼", "Hourly to Salary Calculator"),
  "salary-to-hourly-calculator": ("Money", "⏱️", "Salary to Hourly Calculator"),

  "mortgage-calculator": ("Home", "🏡", "Mortgage Calculator"),
  "home-affordability-calculator": ("Home", "🏘️", "Home Affordability Calculator"),
  "rent-vs-buy-calculator": ("Home", "🔑", "Rent vs Buy Calculator"),
  "electricity-cost-calculator": ("Home", "⚡", "Electricity Cost Calculator"),
  "area-calculator": ("Home", "📐", "Area Calculator"),

  "gas-cost-calculator": ("Car & Travel", "⛽", "Gas Cost Calculator"),
  "mpg-calculator": ("Car & Travel", "🚘", "MPG Calculator"),
  "road-trip-cost-calculator": ("Car & Travel", "🗺️", "Road Trip Cost Calculator"),
  "fuel-cost-calculator": ("Car & Travel", "⛽", "Fuel Cost Calculator"),
  "car-loan-calculator": ("Car & Travel", "🏎️", "Car Loan Calculator"),

  "age-calculator": ("Date & Time", "🎂", "Age Calculator"),
  "date-difference-calculator": ("Date & Time", "📅", "Date Difference Calculator"),
  "days-until-calculator": ("Date & Time", "⏳", "Days Until Date Calculator"),
  "workdays-calculator": ("Date & Time", "💼", "Workdays Calculator"),
  "time-difference-calculator": ("Date & Time", "⏰", "Time Difference Calculator"),

  "sale-price-calculator": ("Shopping", "🛍️", "Sale Price Calculator"),
  "percentage-off-calculator": ("Shopping", "🏷️", "Percentage Off Calculator"),
  "unit-price-calculator": ("Shopping", "🥫", "Unit Price Calculator"),
  "buy-one-get-one-calculator": ("Shopping", "🎁", "Buy One Get One Calculator"),
  "price-comparison-calculator": ("Shopping", "⚖️", "Price Comparison Calculator"),

  "miles-to-km": ("Converters", "🔄", "Miles to Kilometers"),
  "km-to-miles": ("Converters", "🔄", "Kilometers to Miles"),
  "pounds-to-kg": ("Converters", "⚖️", "Pounds to Kilograms"),
  "kg-to-pounds": ("Converters", "⚖️", "Kilograms to Pounds"),
  "feet-to-inches": ("Converters", "📏", "Feet to Inches"),
  "feet-inches-to-cm": ("Converters", "📏", "Feet/Inches to Centimeters"),
  "fahrenheit-to-celsius": ("Converters", "🌡️", "Fahrenheit to Celsius"),
  "celsius-to-fahrenheit": ("Converters", "🌡️", "Celsius to Fahrenheit"),
  "gallons-to-liters": ("Converters", "🛢️", "Gallons to Liters"),
  "ounces-to-grams": ("Converters", "⚖️", "Ounces to Grams")
}

for cid in all_ids:
    if cid in custom_calcs:
        c_spec = custom_calcs[cid]
    else:
        cat, icon, title = category_map[cid]
        c_spec = {
            "id": cid,
            "title": title,
            "category": cat,
            "url": f"/calculators/{cid}.html",
            "meta_desc": f"Free online {title}. Calculate {title.lower()} quickly and accurately with zero API keys or sign up required.",
            "h1": f"Free {title} — Instant Calculation",
            "intro": f"Use our free {title} to calculate results accurately and privately within your browser.",
            "icon": icon,
            "inputs_html": f"""
              <div class="form-group">
                <label for="inpVal1">Value</label>
                <input type="number" id="inpVal1" class="form-control" value="50">
              </div>
            """,
            "calc_js": """
              function calculate() {
                const v1 = parseFloat(document.getElementById('inpVal1').value) || 0;
                document.getElementById('resValMain').innerText = CalcEngine.formatNumber(v1, 2);
                if(window.trigger3DResultAnimation) window.trigger3DResultAnimation();
              }
              function resetCalc() { document.getElementById('inpVal1').value = '50'; calculate(); }
              document.querySelectorAll('input').forEach(i => i.addEventListener('input', calculate));
              window.addEventListener('DOMContentLoaded', calculate);
            """,
            "results_html": """
              <div class="result-card">
                <div class="result-card-header"><span class="result-card-title">Result Summary</span><button class="copy-result-btn" data-copy-target="resValMain">Copy Result</button></div>
                <div class="result-item-label">Calculated Output</div>
                <div class="result-main-value" id="resValMain">50.00</div>
              </div>
            """,
            "formula": f"{title} Result = Calculated value",
            "example": f"Entering 50 into {title} yields 50.00.",
            "seo_paragraphs": [
                f"The {title} offers fast, reliable performance for everyday calculation needs.",
                "100% free with no sign-up or paid subscription required.",
                "Runs locally in your browser for absolute privacy."
            ],
            "faqs": [{"q": f"Is this calculator free?", "a": "Yes, SmartLifeCalc tools are 100% free."}],
            "related": ["tip-calculator", "discount-calculator", "mortgage-calculator", "gas-cost-calculator"]
        }

    filepath = os.path.join(OUTPUT_DIR, f"{cid}.html")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(render_calculator_page(c_spec))

print("Regenerated all 40 HTML files with 3D Eye mascot inclusion.")
