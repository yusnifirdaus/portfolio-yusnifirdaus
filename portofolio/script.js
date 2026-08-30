const filters = document.querySelectorAll('.filter');
const cards = document.querySelectorAll('.project-card');
filters.forEach(filter => filter.addEventListener('click', () => {
  filters.forEach(item => item.classList.remove('active'));
  filter.classList.add('active');
  const selected = filter.dataset.filter;
  cards.forEach(card => { card.style.display = selected === 'all' || card.dataset.type === selected ? '' : 'none'; });
}));
const modal = document.querySelector('.modal');
const modalImage = document.querySelector('.modal-image');
cards.forEach(card => card.addEventListener('click', () => {
  modalImage.src = card.querySelector('img').src;
  modalImage.alt = card.querySelector('img').alt;
  modal.querySelector('h3').textContent = card.dataset.title;
  modal.querySelector('p').textContent = card.dataset.meta;
  modal.classList.add('open'); modal.setAttribute('aria-hidden', 'false');
}));
function closeModal(){ modal.classList.remove('open'); modal.setAttribute('aria-hidden', 'true'); }
document.querySelector('.modal-close').addEventListener('click', closeModal);
modal.addEventListener('click', event => { if(event.target === modal) closeModal(); });
document.addEventListener('keydown', event => { if(event.key === 'Escape') closeModal(); });

// Local photography archive
document.querySelector('.project-card[data-title="Sore di Selatan"]')?.remove();
document.querySelector('.project-card[data-title="Bentuk Sehari-hari"]')?.remove();
document.querySelectorAll('.project-card .project-number').forEach((number, index) => { number.textContent = String(index + 1).padStart(2, '0'); });
const localGallery = ['20260705_173328.jpg','20260716_173540.jpg','20260730_181512.jpg','20260519_183750.jpg'];
document.querySelectorAll('.project-image img').forEach((image, index) => { image.src = localGallery[index]; });
const aboutImage = document.querySelector('.about-visual img');
if (aboutImage) aboutImage.src = '20260716_173540.jpg';

const gallery = document.querySelector('.project-grid');
if (gallery) {
  const carousel = document.createElement('div');
  carousel.className = 'gallery-carousel';
  gallery.parentNode.insertBefore(carousel, gallery);
  carousel.appendChild(gallery);
  const previous = document.createElement('button');
  const next = document.createElement('button');
  previous.className = 'gallery-arrow previous'; previous.setAttribute('aria-label', 'Foto sebelumnya'); previous.textContent = '‹';
  next.className = 'gallery-arrow next'; next.setAttribute('aria-label', 'Foto berikutnya'); next.textContent = '›';
  carousel.append(previous, next);
  const move = direction => gallery.scrollBy({left: direction * (gallery.clientWidth * .72), behavior: 'smooth'});
  previous.addEventListener('click', () => move(-1));
  next.addEventListener('click', () => move(1));
  const observer = new IntersectionObserver(entries => entries.forEach(entry => entry.target.classList.toggle('is-active', entry.isIntersecting)), {root: gallery, threshold: .72});
  gallery.querySelectorAll('.project-card').forEach(card => observer.observe(card));
}

const robloxCard = document.querySelector('.video-card[data-video-ids]');
if (robloxCard) {
  const firstRobloxId = robloxCard.dataset.videoIds.split(',')[0];
  const firstPlayer = document.createElement('iframe');
  firstPlayer.src = `https://www.tiktok.com/player/v1/${firstRobloxId}?description=1&music_info=1`;
  firstPlayer.title = 'Roblox edit TikTok';
  firstPlayer.allow = 'fullscreen';
  firstPlayer.loading = 'lazy';
  robloxCard.querySelector('.video-thumb img').replaceWith(firstPlayer);
  robloxCard.classList.add('has-embed');
}
document.querySelectorAll('.video-card[data-instagram-ids]').forEach(card => {
  const firstInstagramId = card.dataset.instagramIds.split(',')[0];
  const firstPlayer = document.createElement('iframe');
  firstPlayer.src = `https://www.instagram.com/reel/${firstInstagramId}/embed`;
  firstPlayer.title = `${card.querySelector('h3').textContent} Instagram video`;
  firstPlayer.allow = 'autoplay; encrypted-media; picture-in-picture; web-share';
  firstPlayer.loading = 'lazy';
  card.querySelector('.video-thumb img').replaceWith(firstPlayer);
  card.classList.add('has-embed');
});

document.querySelectorAll('.highlight-strip').forEach(strip => {
  const wrapper = document.createElement('div');
  wrapper.className = 'highlight-carousel';
  strip.parentNode.insertBefore(wrapper, strip);
  wrapper.appendChild(strip);

  const controls = document.createElement('div');
  controls.className = 'highlight-controls';
  controls.innerHTML = '<button type="button" aria-label="Foto sebelumnya">←</button><button type="button" aria-label="Foto berikutnya">→</button>';
  wrapper.appendChild(controls);

  const step = () => Math.max(strip.clientWidth * 0.72, 220);
  controls.firstElementChild.addEventListener('click', () => strip.scrollBy({ left: -step(), behavior: 'smooth' }));
  controls.lastElementChild.addEventListener('click', () => strip.scrollBy({ left: step(), behavior: 'smooth' }));
});

const contactCta = document.querySelector('.contact-cta');
const socialPopover = document.querySelector('.social-popover');
if (contactCta && socialPopover) {
  const closeSocialPopover = () => {
    socialPopover.classList.remove('open');
    socialPopover.setAttribute('aria-hidden', 'true');
    contactCta.setAttribute('aria-expanded', 'false');
  };
  contactCta.addEventListener('click', () => {
    socialPopover.classList.add('open');
    socialPopover.setAttribute('aria-hidden', 'false');
    contactCta.setAttribute('aria-expanded', 'true');
  });
  socialPopover.querySelector('.social-popover-close').addEventListener('click', closeSocialPopover);
  socialPopover.addEventListener('click', event => { if (event.target === socialPopover) closeSocialPopover(); });
  document.addEventListener('keydown', event => { if (event.key === 'Escape') closeSocialPopover(); });
}

const backToTop = document.querySelector('.back-to-top');
if (backToTop) {
  window.addEventListener('scroll', () => {
    backToTop.classList.toggle('visible', window.scrollY > 480);
  }, { passive: true });
  backToTop.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
}
const videoCards = document.querySelectorAll('.video-card');
videoCards.forEach(card => {
  card.setAttribute('tabindex', '0');
  card.setAttribute('role', 'button');
  const openVideoPreview = () => {
    const preview = document.createElement('div');
    preview.className = 'video-modal';
    const videoIds = card.dataset.videoIds?.split(',') || [];
    const instagramIds = card.dataset.instagramIds?.split(',') || [];
    const embeds = videoIds.map(id => `<iframe src="https://www.tiktok.com/player/v1/${id}?description=1&music_info=1" title="Roblox edit TikTok ${id}" allow="fullscreen" loading="lazy"></iframe>`).join('');
    const instagramEmbeds = instagramIds.map(id => `<iframe src="https://www.instagram.com/${id === 'CfoPJDJJ4C1' ? 'tv' : 'reel'}/${id}/embed" title="${card.querySelector('h3').textContent} Instagram video ${id}" allow="autoplay; encrypted-media; picture-in-picture; web-share" loading="lazy"></iframe>`).join('');
    const embedMarkup = videoIds.length ? embeds : instagramEmbeds;
    const embedLabel = videoIds.length ? 'Roblox edit · 07 videos' : `${card.querySelector('h3').textContent} · ${instagramIds.length} videos`;
    preview.innerHTML = (videoIds.length || instagramIds.length) ? `<div class="video-modal-inner video-tiktok-modal"><button class="video-modal-close" aria-label="Tutup preview">×</button><div class="video-modal-heading"><p>${embedLabel}</p><h3>${card.querySelector('h3').textContent}</h3></div><div class="video-embed-list">${embedMarkup}</div></div>` : `<div class="video-modal-inner"><button class="video-modal-close" aria-label="Tutup preview">×</button><img src="${card.querySelector('img').src}" alt="${card.querySelector('img').alt}"><div><p>${card.querySelector('.video-meta p').textContent}</p><h3>${card.querySelector('h3').textContent}</h3><span>Link video dapat ditambahkan dari YouTube, TikTok, atau Instagram.</span></div></div>`;
    document.body.appendChild(preview);
    const close = () => preview.remove();
    preview.querySelector('.video-modal-close').addEventListener('click', close);
    preview.addEventListener('click', event => { if (event.target === preview) close(); });
  };
  const videoLink = document.createElement('a');
  videoLink.className = 'video-open-link';
  videoLink.href = '#';
  videoLink.textContent = 'Lihat semua video ↗';
  videoLink.addEventListener('click', event => { event.preventDefault(); event.stopPropagation(); openVideoPreview(); });
  card.querySelector('.video-meta').appendChild(videoLink);
  card.addEventListener('click', openVideoPreview);
  card.addEventListener('keydown', event => { if(event.key === 'Enter' || event.key === ' ') { event.preventDefault(); openVideoPreview(); } });
});
