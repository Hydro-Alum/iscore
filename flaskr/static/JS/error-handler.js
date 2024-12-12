const parentDivs = document.querySelectorAll('.student-reg-input');

parentDivs.forEach((parentDiv) => {
    const error = parentDiv.querySelectorAll('.reg-error');
    if (error) {
        parentDiv.classList.add('red-border');
    }

})