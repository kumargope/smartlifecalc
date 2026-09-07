/* SmartLifeCalc - Main Application Controller */

document.addEventListener('DOMContentLoaded', () => {
  initSearchModal();
  initMobileMenu();
  initFaqAccordions();
  initCopyResultButtons();
  initAnalyticsPlaceholder();
});

// 1. Search Modal Controller
function initSearchModal() {
  const triggerBtns = document.querySelectorAll('.search-trigger, [data-action="open-search"]');
  const overlay = document.getElementById('searchModalOverlay');
  const closeBtn = document.getElementById('searchCloseBtn');
  const searchInput = document.getElementById('modalSearchInput');
  const resultsContainer = document.getElementById('searchResultsList');

  if (!overlay || !searchInput || !resultsContainer) return;

  function openSearch() {
    overlay.classList.add('active');
    searchInput.value = '';
    searchInput.focus();
    renderSearchResults('');
    trackEvent('calculator_search_opened', {});
  }

  function closeSearch() {
    overlay.classList.remove('active');
  }

  triggerBtns.forEach(btn => btn.addEventListener('click', openSearch));
  if (closeBtn) closeBtn.addEventListener('click', closeSearch);

  overlay.addEventListener('click', (e) => {
    if (e.target === overlay) closeSearch();
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && overlay.classList.contains('active')) {
      closeSearch();
    }
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
      e.preventDefault();
      openSearch();
    }
  });

  searchInput.addEventListener('input', (e) => {
    renderSearchResults(e.target.value);
  });

  function renderSearchResults(query) {
    const q = query.trim().toLowerCase();
    resultsContainer.innerHTML = '';

    if (!window.CALCULATORS_REGISTRY) return;

    const matches = window.CALCULATORS_REGISTRY.filter(calc => {
      if (!q) return true; // show all / popular if query empty
      return calc.title.toLowerCase().includes(q) ||
             calc.category.toLowerCase().includes(q) ||
             calc.description.toLowerCase().includes(q) ||
             calc.keywords.some(k => k.toLowerCase().includes(q));
    });

    if (matches.length === 0) {
      resultsContainer.innerHTML = `<div style="padding: 1.5rem; text-align: center; color: var(--text-muted);">No calculators found for "${query}".</div>`;
      return;
    }

    matches.slice(0, 10).forEach(calc => {
      const item = document.createElement('a');
      item.href = calc.url;
      item.className = 'search-result-item';
      item.innerHTML = `
        <div>
          <div class="item-title">${calc.title}</div>
          <div style="font-size: 0.825rem; color: var(--text-muted);">${calc.description}</div>
        </div>
        <span class="item-category">${calc.category}</span>
      `;
      item.addEventListener('click', () => {
        trackEvent('calculator_search_click', { calcId: calc.id, query: q });
      });
      resultsContainer.appendChild(item);
    });
  }
}

// 2. Mobile Nav Drawer
function initMobileMenu() {
  const menuBtn = document.getElementById('mobileMenuBtn');
  const drawer = document.getElementById('mobileDrawer');

  if (!menuBtn || !drawer) return;

  menuBtn.addEventListener('click', () => {
    drawer.classList.toggle('open');
    const isOpen = drawer.classList.contains('open');
    menuBtn.setAttribute('aria-expanded', isOpen);
  });
}

// 3. FAQ Accordion Handler
function initFaqAccordions() {
  const faqQuestions = document.querySelectorAll('.faq-question');
  faqQuestions.forEach(question => {
    question.addEventListener('click', () => {
      const item = question.closest('.faq-item');
      if (item) {
        item.classList.toggle('active');
      }
    });
  });
}

// 4. Copy Result Clipboard Helper
function initCopyResultButtons() {
  document.querySelectorAll('[data-copy-target]').forEach(btn => {
    btn.addEventListener('click', () => {
      const targetId = btn.getAttribute('data-copy-target');
      const targetEl = document.getElementById(targetId);
      if (targetEl) {
        const textToCopy = targetEl.innerText || targetEl.textContent;
        navigator.clipboard.writeText(textToCopy.trim()).then(() => {
          const originalText = btn.innerText;
          btn.innerText = 'Copied!';
          btn.style.background = '#10b981';
          setTimeout(() => {
            btn.innerText = originalText;
            btn.style.background = '';
          }, 2000);
        });
      }
    });
  });
}

// 5. Analytics & Event Tracking Placeholder
function initAnalyticsPlaceholder() {
  window.trackEvent = function(eventName, payload = {}) {
    console.log(`[SmartLifeCalc Analytics] Event: ${eventName}`, payload);
    if (window.gtag) {
      window.gtag('event', eventName, payload);
    }
  };
}

// 6. Pinterest Share Action Helper (with valid media parameter fallback)
function shareToPinterest(url, image, description) {
  // Default image URL if none provided
  const mediaUrl = image || 'https://smartlifecalc.vercel.app/assets/pinterest-banner.png';
  const pinUrl = `https://pinterest.com/pin/create/button/?url=${encodeURIComponent(url)}&media=${encodeURIComponent(mediaUrl)}&description=${encodeURIComponent(description)}`;
  
  window.open(pinUrl, 'pinterestShareWindow', 'width=750,height=600,toolbar=no,menubar=no,scrollbars=yes');
  if (window.trackEvent) {
    window.trackEvent('pinterest_click', { url, mediaUrl });
  }
}
