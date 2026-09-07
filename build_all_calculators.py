import os
import json

OUTPUT_DIR = r"C:\Users\Mukesh\.gemini\antigravity\scratch\smartlifecalc\calculators"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Helper function to generate full HTML string for any calculator
def render_calculator_html(c):
    related_links_html = ""
    for rel_id in c.get('related', ["tip-calculator", "discount-calculator", "mortgage-calculator", "gas-cost-calculator"]):
        title = rel_id.replace('-', ' ').title()
        related_links_html += f'''
          <a href="/calculators/{rel_id}.html" class="related-card">
            <h4>{title}</h4>
            <p>Calculate {title.lower()} instantly.</p>
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
        "name": f"{c['title']} — SmartLifeCalc",
        "url": f"https://smartlifecalc.com{c['url']}",
        "description": c['meta_desc'],
        "applicationCategory": "UtilityApplication",
        "operatingSystem": "All"
    }, indent=2)

    seo_paragraphs_html = "".join([f"<p>{p}</p>" for p in c.get('seo_paragraphs', [])])

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{c['title']} — SmartLifeCalc</title>
  <meta name="description" content="{c['meta_desc']}">
  <link rel="canonical" href="https://smartlifecalc.com{c['url']}">

  <!-- OpenGraph / Social Metadata -->
  <meta property="og:title" content="{c['title']} — SmartLifeCalc">
  <meta property="og:description" content="{c['meta_desc']}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://smartlifecalc.com{c['url']}">

  <!-- Twitter Metadata -->
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="{c['title']}">
  <meta name="twitter:description" content="{c['meta_desc']}">

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
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="color:var(--primary);"><rect x="4" y="2" width="16" height="20" rx="2"/><line x1="8" y1="6" x2="16" y2="6"/><line x1="16" y1="14" x2="16" y2="18"/><path d="M16 10h.01"/><path d="M12 10h.01"/><path d="M8 10h.01"/><path d="M12 14h.01"/><path d="M8 14h.01"/><path d="M12 18h.01"/><path d="M8 18h.01"/></svg>
        SmartLife<span>Calc</span>
      </a>
      <nav class="nav-links">
        <a href="/index.html">Home</a>
        <a href="/index.html#popular">Popular</a>
        <a href="/index.html#categories">Categories</a>
        <a href="/legal/disclaimer.html">Disclaimer</a>
      </nav>
      <div class="header-actions">
        <button class="search-trigger" id="headerSearchTrigger" aria-label="Search calculators">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
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
          
          <!-- Calculator Card -->
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

            <!-- Large Result Card -->
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
              <li>Always verify figures before executing binding contracts or large purchases.</li>
              <li>Input fields accept custom values for maximum calculation flexibility.</li>
              <li>All calculations run locally inside your device browser with 100% data privacy.</li>
            </ul>

            <!-- Pinterest Strategy Share Card -->
            <div class="pinterest-share-card">
              <div class="pinterest-share-info">
                <h3>Save this calculator for later</h3>
                <p>Pin {c['title']} to your favorite Pinterest board for fast access anytime!</p>
              </div>
              <button class="pinterest-btn" onclick="shareToPinterest('https://smartlifecalc.com{c['url']}', '', '{c['title']} — Free Everyday Calculator on SmartLifeCalc')">
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
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color:var(--text-muted);"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
        <input type="text" id="modalSearchInput" placeholder="Type a calculator name or keyword...">
        <button class="search-close-btn" id="searchCloseBtn">✕</button>
      </div>
      <div class="search-results-list" id="searchResultsList"></div>
    </div>
  </div>

  <!-- Scripts -->
  <script src="/js/data/calculators-registry.js"></script>
  <script src="/js/calculator-engine.js"></script>
  <script src="/js/app.js"></script>
  <script>
    {c['calc_js']}
  </script>
</body>
</html>
"""
    return html_content

print("HTML renderer function built successfully.")
