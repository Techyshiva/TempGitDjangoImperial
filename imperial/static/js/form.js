// =========================================================
// CONTACT FORM HANDLING
// =========================================================

const contactForm = document.getElementById('contactForm');
const successMessage = document.getElementById('successMessage');

if (contactForm) {
  contactForm.addEventListener('submit', function(e) {
    e.preventDefault(); // Stop the page from reloading

    // 1. Hide the Form
    contactForm.style.display = 'none';

    // 2. Show the Success Message
    successMessage.style.display = 'flex';

    // 3. Wait 3 Seconds (3000ms), then reset
    setTimeout(() => {
      // Hide Success Message
      successMessage.style.display = 'none';
      
      // Show Form Again
      contactForm.style.display = 'block';
      
      // Optional: Clear the input fields
      contactForm.reset();
    }, 3000);
  });
}