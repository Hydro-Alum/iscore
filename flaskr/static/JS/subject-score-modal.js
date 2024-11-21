const deleteBtns = document.querySelectorAll('.delete-score');
const modalDiv = document.getElementById('modal');
const modalPopupDiv = document.getElementById('modal-popup');
const modalInput = document.getElementById('modal-delete-input');
const modalCancelBtn = document.getElementById('modal-close-btn');
const modalSubmitBtn = document.getElementById('modal-submit-btn');
// const teacherID = document.getElementById('score_id').value;


deleteBtns.forEach(button => {
    button.addEventListener('click', () => {
        console.log("result delete clicked!")
        const itemId = button.getAttribute('data-item-id');
        button.addEventListener('click', (e) => {
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
                modalDiv.classList.add('hidden');
                fetch(`/delete-subject-score/${itemId}`, {
                    method: 'DELETE',
                    headers: {
                        'Content-Type':'application/json'
                    }
                })
                .then(response => {
                    if (response.ok) {
                        return response.json();
                    } else {
                        throw new Error('Failed to delete item');
                    }
                })
                .then(data => {
                    // Handle the response (e.g., remove the item from the DOM or show a success message)
                    console.log(data.message);
                    const row = button.closest('tr');
                        if (row) {
                            row.remove(); // Remove the entire row from the table
                        }
                })
                .catch(error => {
                    console.error('Error:', error);
                    alert('An error occurred while deleting the item.');
                });
            };
        });
    });
});


