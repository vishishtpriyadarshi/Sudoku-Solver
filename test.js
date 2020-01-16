const pshell = require('python-shell')

const options = {
    mode: 'text',
    args: ['input.jpg']
}

const testURL = './public/test.py'
const runURL = './Sudoku-Solver/solver.py'

pshell.PythonShell.run(testURL, options, (e,results) => {
    // const arr = results[0][0].
    // console.log(arr)
    console.log(results)
})

// var shell = new pshell.PythonShell('./public/test.py');

