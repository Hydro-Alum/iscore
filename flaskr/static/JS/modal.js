const deleteBtn = document.getElementById('delete-btn');
const modalDiv = document.getElementById('modal');
const modalPopupDiv = document.getElementById('modal-popup');
const modalInput = document.getElementById('modal-delete-input');
const modalCancelBtn = document.getElementById('modal-close-btn');
const modalSubmitBtn = document.getElementById('modal-submit-btn');
const studentID = document.getElementById('studentID').value;

deleteBtn.addEventListener('click', (e) => {
    e.preventDefault();
    modalDiv.classList.remove('hidden');
})

modalDiv.addEventListener('click', (e) => {
    e.preventDefault();
    if (e.target !== modalPopupDiv && !modalPopupDiv.contains(e.target)) {
        modalDiv.classList.add('hidden');
    }
})

modalCancelBtn.addEventListener('click', (e) => {
    e.preventDefault();
    modalDiv.classList.add('hidden');
})

modalSubmitBtn.addEventListener('click', (e) => {
    const modalInputValue = modalInput.value.trim();
    if(modalInputValue==='DELETE') {
        console.log("here");
        fetch('/delete-student/' + studentID, {
            method: 'DELETE',
            headers: {
                'Content-Type':'application/json'
            }
        })
        .then(response => {
            if (response.ok) {
                console.log('Student deleted successfully')
                window.location.href='/student-dashboard';
            }else {
                console.error('Error deleting student')
            }
        })
        .catch(error => console.error(error))
    }
})
