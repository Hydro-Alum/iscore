const alert = document.getElementById('alert-btn');
const closeBtn = document.getElementById('close-btn');

if (alert) {
    closeBtn.addEventListener('click', function(){
        alert.classList.add('hidden');
    })
    
    setTimeout(function() {
        alert.classList.add('hidden')
    }, 5000)
}

