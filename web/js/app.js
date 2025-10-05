// ===== Theme Toggle =====
const themeToggle = document.getElementById("themeToggle");
if (themeToggle) {
  themeToggle.addEventListener("click", () => {
    document.body.classList.toggle("dark-mode");
    themeToggle.textContent = document.body.classList.contains("dark-mode") ? "🌙" : "☀️";
  });
}

// ===== Profile Dropdown =====
const profileBtn = document.getElementById("profileBtn");
const profileMenu = document.getElementById("profileMenu");
if (profileBtn && profileMenu) {
  profileBtn.addEventListener("click", () => {
    profileMenu.classList.toggle("active");
  });

  window.addEventListener("click", (e) => {
    if (!profileBtn.contains(e.target) && !profileMenu.contains(e.target)) {
      profileMenu.classList.remove("active");
    }
  });
}

// ===== Plan Toggle =====
const planToggle = document.getElementById("planToggle");
if (planToggle) {
  planToggle.addEventListener("change", () => {
    const prices = document.querySelectorAll(".price");
    prices.forEach(price => {
      const month = price.getAttribute("data-month");
      const year = price.getAttribute("data-year");
      price.textContent = planToggle.checked ? `$${year} /yr` : `$${month} /mo`;
    });
  });
}
// ===== Mobile Menu Toggle =====
const mobileMenuBtn = document.getElementById("mobileMenuBtn");
const mobileMenu = document.getElementById("mobileMenu");