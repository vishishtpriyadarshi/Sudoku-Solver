console.log('Client side javascript is loaded.');

const createForm = document.querySelector('#create')
const solveForm = document.querySelector('#solve')

const searchURL = '/imdetails'

var a = []
for (i=0; i<81; i++) {
    var str = ".div" + (i+1).toString()
    a.push(document.querySelector(str))
}
console.log(a[0])

createForm.addEventListener('submit', (e) => {
    e.preventDefault()

    fetch(searchURL).then((response) => {
        response.json().then((data) => {
            for (i=0; i<81; i++) {
                if (data.arr[i])
                a[i].textContent = data.arr[i].toString()
            }
        })
    })
})

// solveForm.addEventListener('submit', (e) => {
//     e.preventDefault()
// })


// fetch(searchURL).then((response) => {
//     response.json().then((data) => {
//         if (data.error) {
//             // console.log(data.error);
//             message1.textContent = data.error;
//         } else {
//             // console.log(data);
//             message1.textContent = data.location;
//             message2.textContent = data.forecast;
//         }
//     });    
// });



