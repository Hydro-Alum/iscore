const submitBtn = document.getElementById('submit-btn');
const submitForm = document.getElementById('student-reg-form');

submitForm.addEventListener('submit', function(e) {
    submitBtn.disabled = true;
    console.log('loading here')

    setTimeout(() => {
        submitBtn.disabled = false;
        console.log('abled here')
    }, 5000)
})


// submitBtn.onsubmit = function() {
//     submitBtn.disabled = true;
//     submitBtn.innerHTML = 'submitting...';
//     console.log('loading here')

//     setTimeout(() => {
//         submitBtn.disabled = false;
//         submitBtn.value = 'Register Student';
//         console.log('abled here')
//     }, 5000)
// }