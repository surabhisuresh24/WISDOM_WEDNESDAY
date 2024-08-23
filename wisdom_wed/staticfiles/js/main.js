document.addEventListener('DOMContentLoaded', function() {
    const ctaButtons = document.querySelectorAll('.cta-button');
    ctaButtons.forEach(button => {
        button.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.1)';
        });
        button.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1)';
        });
    });

    // Quiz functionality
    const quizOptions = document.querySelectorAll('.quiz-options li');
    quizOptions.forEach(option => {
        option.addEventListener('click', function() {
            const correctOption = parseInt(this.parentElement.dataset.correct);
            const selectedValue = parseInt(this.dataset.answer);
            if (selectedValue === correctOption) {
                this.classList.add('correct');
            } else {
                this.classList.add('incorrect');
            }
        });
    });
});
