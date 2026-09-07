/* SmartLifeCalc - Interactive 3D Cursor & Touch Tracking Eye Mascot */

document.addEventListener('DOMContentLoaded', () => {
  initSmartEyeMascot();
});

function initSmartEyeMascot() {
  // Inject Hero Eye Widget container if hero exists
  const heroContainer = document.querySelector('section style')?.parentElement || document.querySelector('main .container');
  
  // Create Hero 3D Eye Component if on homepage or calculator page
  const eyeWrapper = document.createElement('div');
  eyeWrapper.className = 'smart-eye-container';
  eyeWrapper.innerHTML = `
    <div class="smart-eye-3d" id="smartEye3D">
      <div class="eye-outer-ring"></div>
      <div class="eye-sclera">
        <div class="eye-iris" id="eyeIris">
          <div class="eye-pupil" id="eyePupil">
            <div class="eye-glint"></div>
          </div>
        </div>
      </div>
      <div class="eye-eyelid top-eyelid"></div>
      <div class="eye-eyelid bottom-eyelid"></div>
    </div>
    <div class="smart-eye-label">
      <span class="pulse-dot"></span> Smart Eye AI Tracker
    </div>
  `;

  // Attach to Hero section on Homepage or Page Intro on Calculator pages
  const pageIntro = document.querySelector('.page-intro') || document.querySelector('section > .container');
  if (pageIntro) {
    pageIntro.style.position = 'relative';
    pageIntro.insertBefore(eyeWrapper, pageIntro.firstChild);
  }

  const eyeElement = document.getElementById('smartEye3D');
  const irisElement = document.getElementById('eyeIris');
  const pupilElement = document.getElementById('eyePupil');

  if (!eyeElement || !irisElement) return;

  // Tracking Mechanics
  let eyeCenterX = 0;
  let eyeCenterY = 0;
  let targetX = 0;
  let targetY = 0;
  let currentX = 0;
  let currentY = 0;

  function updateEyeCenter() {
    const rect = eyeElement.getBoundingClientRect();
    eyeCenterX = rect.left + rect.width / 2;
    eyeCenterY = rect.top + rect.height / 2;
  }

  window.addEventListener('resize', updateEyeCenter);
  window.addEventListener('scroll', updateEyeCenter);
  updateEyeCenter();

  // Desktop Mouse Move Tracking
  document.addEventListener('mousemove', (e) => {
    targetX = e.clientX;
    targetY = e.clientY;
  });

  // Mobile Touch & Tap Tracking
  document.addEventListener('touchstart', handleTouch, { passive: true });
  document.addEventListener('touchmove', handleTouch, { passive: true });

  function handleTouch(e) {
    if (e.touches && e.touches.length > 0) {
      targetX = e.touches[0].clientX;
      targetY = e.touches[0].clientY;
    }
  }

  // Animation Loop with Smooth Trigonometric Easing
  function animateEye() {
    // Distance from eye center to target (cursor or touch)
    const dx = targetX - eyeCenterX;
    const dy = targetY - eyeCenterY;
    const distance = Math.hypot(dx, dy);

    // Maximum distance the pupil can move within socket
    const maxDistance = 28; // pixels
    const angle = Math.atan2(dy, dx);

    // Calculate clamped displacement
    const moveDist = Math.min(distance * 0.1, maxDistance);
    const destIrisX = Math.cos(angle) * moveDist;
    const destIrisY = Math.sin(angle) * moveDist;

    // Smooth Lerp easing
    currentX += (destIrisX - currentX) * 0.12;
    currentY += (destIrisY - currentY) * 0.12;

    // Apply 3D transform to Iris and Pupil
    irisElement.style.transform = `translate3d(${currentX}px, ${currentY}px, 10px) rotateX(${currentY * -0.5}deg) rotateY(${currentX * 0.5}deg)`;

    // Subtle 3D tilt of the entire Eye socket towards target
    const socketRotateX = (currentY / maxDistance) * -12;
    const socketRotateY = (currentX / maxDistance) * 12;
    eyeElement.style.transform = `perspective(800px) rotateX(${socketRotateX}deg) rotateY(${socketRotateY}deg)`;

    requestAnimationFrame(animateEye);
  }

  animateEye();

  // Periodic Blink Animation
  setInterval(() => {
    if (Math.random() > 0.3) {
      eyeElement.classList.add('blinking');
      setTimeout(() => {
        eyeElement.classList.remove('blinking');
      }, 180);
    }
  }, 4000);

  // Dilate pupil when hovering over inputs
  document.querySelectorAll('input, button, a').forEach(el => {
    el.addEventListener('mouseenter', () => {
      if (pupilElement) pupilElement.classList.add('dilated');
    });
    el.addEventListener('mouseleave', () => {
      if (pupilElement) pupilElement.classList.remove('dilated');
    });
  });
}
