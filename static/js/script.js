// Cybersecurity Escape Room JavaScript
document.addEventListener('DOMContentLoaded', function() {
    // Timer functionality
    const timerElement = document.getElementById('timer');
    if (timerElement) {
        let timeLeft = 1200; // 20 minutes in seconds
        
        const countdown = setInterval(() => {
            timeLeft--;
            const minutes = Math.floor(timeLeft / 60);
            const seconds = timeLeft % 60;
            
            timerElement.textContent = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
            
            if (timeLeft <= 0) {
                clearInterval(countdown);
                alert('Time is up! The hacker has escaped with the data.');
                window.location.href = '/';
            }
        }, 1000);
    }
    
    // Hint system
    const hintButtons = document.querySelectorAll('.hint-button');
    hintButtons.forEach(button => {
        button.addEventListener('click', function() {
            const hintId = this.getAttribute('data-hint');
            const hintElement = document.getElementById(hintId);
            if (hintElement) {
                hintElement.style.display = 'block';
                this.disabled = true;
            }
        });
    });
    
    // Form validation
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const input = this.querySelector('input[type="text"]');
            if (input && input.value.trim() === '') {
                e.preventDefault();
                alert('Please provide an answer before submitting.');
            }
        });
    });
});
