const pshell = require('python-shell')
const path = require('path')

const options = {
    mode: 'text',
    args: ['input.jpg']
}

const testURL = path.join(__dirname, './public/test.py') 
const runURL = path.join(__dirname, './solver.py')

pshell.PythonShell.run(runURL, options, (e,results) => {
    // const arr = results[0][0].
    // console.log(arr)
    console.log(results)
})
// console.log(__dirname)

// var shell = new pshell.PythonShell('./public/test.py');

