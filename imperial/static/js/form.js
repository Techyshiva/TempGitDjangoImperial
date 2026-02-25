const contactForm = document.getElementById('contactForm');
const successMessage = document.getElementById('successMessage');

if (contactForm) {
  contactForm.addEventListener('submit', function(e) {
    e.preventDefault(); // Stop the page from reloading

    // 1. Package up all the user's data
    const formData = new FormData(contactForm);

    // 2. Send it securely to Django behind the scenes
    // Make sure your HTML form has action="{% url 'contact' %}" (or whatever your URL name is)
    fetch(contactForm.action, {
        method: 'POST',
        body: formData,
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        }
    })
    .then(response => {
        // 3. If Django successfully saved it to the DB...
        if (response.ok) {
            // Hide the Form
            contactForm.style.display = 'none';

            // Show the Success Message
            successMessage.style.display = 'flex';

            // Wait 3 Seconds (3000ms), then reset
            setTimeout(() => {
              // Hide Success Message
              successMessage.style.display = 'none';
              
              // Show Form Again
              contactForm.style.display = 'block';
              
              // Clear the input fields
              contactForm.reset();
            }, 3000);
        } else {
            alert("Oops! Something went wrong on the server. Please try again.");
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert("A network error occurred. Please check your connection.");
    });
  });
}