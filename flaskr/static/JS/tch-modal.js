const deleteBtn = document.getElementById('tch-delete-btn');
const modalDiv = document.getElementById('tch-modal');
const modalPopupDiv = document.getElementById('tch-modal-popup');
const modalInput = document.getElementById('tch-modal-delete-input');
const modalCancelBtn = document.getElementById('tch-modal-close-btn');
const modalSubmitBtn = document.getElementById('tch-modal-submit-btn');
const teacherID = document.getElementById('teacherID').value;

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
        fetch('/delete-teacher/' + teacherID, {
            method: 'DELETE',
            headers: {
                'Content-Type':'application/json'
            }
        })
        .then(response => {
            if (response.ok) {
                console.log('Teacher deleted successfully')
                window.location.href='/teachers-dashboard';
            }else {
                console.error('Error deleting teacher')
            }
        })
        .catch(error => console.error(error))
    }
})
