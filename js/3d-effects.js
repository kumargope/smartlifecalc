/* SmartLifeCalc - Colorful 3D Visual Engine */

document.addEventListener('DOMContentLoaded', () => {
  initColorful3DCanvas();
  init3DCardsTilt();
  init3DButtonFeedback();
});

// Vibrant 3D Canvas Scene with Multi-Color Particles
function initColorful3DCanvas() {
  const canvas = document.createElement('canvas');
  canvas.id = 'bg3dCanvas';
  canvas.style.position = 'fixed';
  canvas.style.top = '0';
  canvas.style.left = '0';
  canvas.style.width = '100vw';
  canvas.style.height = '100vh';
  canvas.style.pointerEvents = 'none';
  canvas.style.zIndex = '-1';
  canvas.style.opacity = '0.75';
  document.body.prepend(canvas);

  const ctx = canvas.getContext('2d');
  let width, height;

  function resize() {
    width = canvas.width = window.innerWidth;
    height = canvas.height = window.innerHeight;
  }
  window.addEventListener('resize', resize);
  resize();

  const colorPalette = [
    { stroke: '#ec4899', fill: 'rgba(236, 72, 153, 0.25)' }, // Vibrant Pink
    { stroke: '#8b5cf6', fill: 'rgba(139, 92, 246, 0.25)' }, // Purple
    { stroke: '#3b82f6', fill: 'rgba(59, 130, 246, 0.25)' }, // Blue
    { stroke: '#10b981', fill: 'rgba(16, 185, 129, 0.25)' }, // Emerald
    { stroke: '#f59e0b', fill: 'rgba(245, 158, 11, 0.25)' }, // Amber
    { stroke: '#06b6d4', fill: 'rgba(6, 182, 212, 0.25)' }   // Cyan
  ];

  const nodes = [];
  const count = 45;

  for (let i = 0; i < count; i++) {
    const col = colorPalette[i % colorPalette.length];
    nodes.push({
      x: (Math.random() - 0.5) * width * 1.6,
      y: (Math.random() - 0.5) * height * 1.6,
      z: Math.random() * 800 + 100,
      vx: (Math.random() - 0.5) * 0.6,
      vy: (Math.random() - 0.5) * 0.6,
      vz: (Math.random() - 0.5) * 0.6,
      rotX: Math.random() * Math.PI * 2,
      rotY: Math.random() * Math.PI * 2,
      vRotX: (Math.random() - 0.5) * 0.025,
      vRotY: (Math.random() - 0.5) * 0.025,
      size: Math.random() * 28 + 16,
      strokeColor: col.stroke,
      fillColor: col.fill,
      type: i % 4
    });
  }

  let mouseX = 0, mouseY = 0;
  let targetMouseX = 0, targetMouseY = 0;

  document.addEventListener('mousemove', (e) => {
    targetMouseX = (e.clientX - width / 2) * 0.2;
    targetMouseY = (e.clientY - height / 2) * 0.2;
  });

  function render() {
    ctx.clearRect(0, 0, width, height);

    mouseX += (targetMouseX - mouseX) * 0.05;
    mouseY += (targetMouseY - mouseY) * 0.05;

    const fov = 400;
    const cx = width / 2 + mouseX;
    const cy = height / 2 + mouseY;

    nodes.forEach(node => {
      node.x += node.vx;
      node.y += node.vy;
      node.z += node.vz;
      node.rotX += node.vRotX;
      node.rotY += node.vRotY;

      if (node.x < -width) node.x = width;
      if (node.x > width) node.x = -width;
      if (node.y < -height) node.y = height;
      if (node.y > height) node.y = -height;
      if (node.z < 100) node.z = 900;
      if (node.z > 900) node.z = 100;

      const scale = fov / (fov + node.z);
      const projX = cx + node.x * scale;
      const projY = cy + node.y * scale;
      const projSize = node.size * scale;

      ctx.save();
      ctx.translate(projX, projY);
      ctx.rotate(node.rotX);

      ctx.strokeStyle = node.strokeColor;
      ctx.fillStyle = node.fillColor;
      ctx.lineWidth = 2 * scale;
      ctx.shadowBlur = 12 * scale;
      ctx.shadowColor = node.strokeColor;

      if (node.type === 0) {
        // 3D Cube
        const s = projSize;
        ctx.beginPath();
        ctx.strokeRect(-s/2, -s/2, s, s);
        ctx.fillRect(-s/2, -s/2, s, s);
        ctx.strokeRect(-s/4, -s/4, s, s);
        ctx.moveTo(-s/2, -s/2); ctx.lineTo(-s/4, -s/4);
        ctx.moveTo(s/2, -s/2); ctx.lineTo(3*s/4, -s/4);
        ctx.moveTo(-s/2, s/2); ctx.lineTo(-s/4, 3*s/4);
        ctx.moveTo(s/2, s/2); ctx.lineTo(3*s/4, 3*s/4);
        ctx.stroke();
      } else if (node.type === 1) {
        // 3D Pyramid
        const s = projSize * 1.2;
        ctx.beginPath();
        ctx.moveTo(0, -s);
        ctx.lineTo(-s, s);
        ctx.lineTo(s, s);
        ctx.closePath();
        ctx.stroke();
        ctx.fill();
      } else if (node.type === 2) {
        // Concentric Glowing Rings
        ctx.beginPath();
        ctx.arc(0, 0, projSize, 0, Math.PI * 2);
        ctx.stroke();
        ctx.beginPath();
        ctx.ellipse(0, 0, projSize, projSize * 0.4, node.rotY, 0, Math.PI * 2);
        ctx.stroke();
      } else {
        // Math Symbols
        const s = projSize;
        ctx.font = `bold ${s}px sans-serif`;
        ctx.fillStyle = node.strokeColor;
        ctx.fillText("%", -s/2, s/2);
      }

      ctx.restore();
    });

    requestAnimationFrame(render);
  }

  render();
}

// 3D Cards Hover Tilt
function init3DCardsTilt() {
  const cards = document.querySelectorAll('.calc-card, .related-card, .pinterest-share-card, .hero-3d-card');

  cards.forEach(card => {
    card.style.transition = 'transform 0.15s cubic-bezier(0.2, 0, 0.2, 1), box-shadow 0.25s ease';
    card.style.transformStyle = 'preserve-3d';

    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      
      const centerX = rect.width / 2;
      const centerY = rect.height / 2;

      const rotateX = ((y - centerY) / centerY) * -10;
      const rotateY = ((x - centerX) / centerX) * 10;

      card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateZ(15px) scale3d(1.02, 1.02, 1.02)`;
    });

    card.addEventListener('mouseleave', () => {
      card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) translateZ(0px) scale3d(1, 1, 1)';
    });
  });
}

// Button Feedback
function init3DButtonFeedback() {
  const buttons = document.querySelectorAll('.btn-primary, .btn-secondary, .preset-btn, .pinterest-btn');

  buttons.forEach(btn => {
    btn.style.transition = 'all 0.15s cubic-bezier(0.175, 0.885, 0.32, 1.275)';

    btn.addEventListener('mousedown', () => {
      btn.style.transform = 'translateY(3px) scale(0.96)';
    });

    btn.addEventListener('mouseup', () => {
      btn.style.transform = 'translateY(-2px) scale(1.03)';
    });

    btn.addEventListener('mouseleave', () => {
      btn.style.transform = '';
    });
  });
}

window.trigger3DResultAnimation = function() {
  const resultCard = document.querySelector('.result-card');
  if (resultCard) {
    resultCard.classList.remove('flip-3d-active');
    void resultCard.offsetWidth;
    resultCard.classList.add('flip-3d-active');
  }
};
