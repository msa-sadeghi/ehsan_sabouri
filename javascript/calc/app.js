let students = []


function addStudent(){
    const name = document.getElementById('studentName').value.trim()
    const math = parseFloat(document.getElementById('mathScore').value)
    const physics = parseFloat(document.getElementById('physicsScore').value)
    const chemistry = parseFloat(document.getElementById('chemistryScore').value)

    const student = {
        id:Date.now(),
        name :  name,
        scores:{
            math:math,
            physics : physics,
            chemistry : chemistry
        },
        average : (math + physics + chemistry) / 3,
        passed :((math + physics + chemistry) / 3) >= 50
    }
    students.push(student)
    document.getElementById('studentName').value = ''
    document.getElementById('mathScore').value = ''
    document.getElementById('physicsScore').value = ''
    document.getElementById('chemistryScore').value = ''
    renderTable()
}

function renderTable(){
    const tbody =  document.getElementById('studentsBody')
    if(students.length === 0){
        tbody.innerHTML = `
        <tr>
        <td>
        <p>مورد یافت نشد</p>
        </td>
        </tr>
        `
        return
    }
    tbody.innerHTML =  students.map((student, index) => `
    <tr>
        <td>${index+1}</td>
        <td>${student.name}</td>
        <td>${student.scores.math}</td>
        <td>${student.scores.physics}</td>
        <td>${student.scores.chemistry}</td>
        <td>${student.average.toFixed(2)}</td>
        <td>${student.passed ? 'قبول' : 'مردود'}</td>
        <td>
            <button>
            حذف
            </button>
        </td>
    
    `)
}