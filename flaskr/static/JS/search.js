const searchInput = document.querySelector('.search-input');
const classRange = document.getElementById('std_class').value;
console.log(classRange)

    searchInput.addEventListener('input', (e) => {
        e.preventDefault()
        console.log("user typed:", e.target.value);
        fetch('/students/search', {
            method: 'POST',
            body: JSON.stringify({
                'search': e.target.value,
                'student_class': classRange
            }),
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(function(response) {
            return response.json()
        })
        .then(function(students) {
            console.log(students)
            const tbody = document.getElementById('students-tbody');
            if (tbody) {
                tbody.innerHTML = "";
            };
            students.forEach(student => {
                const row = document.createElement('tr');
                const serialCell = document.createElement('td');
                const nameCell = document.createElement('td');
                const sIDCell = document.createElement('td');
                const studentClassCell = document.createElement('td');
                const departmentCell = document.createElement('td');
                const nameAnchor = document.createElement('a');
                nameAnchor.textContent = student.name;
                nameAnchor.href = `/student-profile/${student.id}`
                nameCell.appendChild(nameAnchor);
                serialCell.textContent = student.serial;
                sIDCell.textContent = student.sID;
                studentClassCell.textContent = student.studentClass;
                departmentCell.textContent = student.department;
                row.appendChild(serialCell);
                row.appendChild(nameCell);
                row.appendChild(sIDCell);
                row.appendChild(studentClassCell);
                row.appendChild(departmentCell);
                tbody.appendChild(row);
            })
        })
        .catch(error => {
            console.log(error);
        })
    })