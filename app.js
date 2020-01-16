const path = require('path');
const express = require('express');
const multer = require('multer')
const hbs = require('hbs')
const csp = require('express-csp-header')
const pshell = require('python-shell')

var storage = multer.diskStorage({
    destination: function (req, file, cb) {
        cb(null, './public/images')
    },
    filename: function (req, file, cb) {
        cb(null, 'input.jpg')
  }
})
var upload = multer({ storage: storage })

// app stores our application
const app = express();

const publicDirectoryPath = path.join(__dirname, './public');
const viewsPath = path.join(__dirname, './templates/views');

const port = process.env.PORT || 3000;

// Setup static directory to serve
app.set('view engine', 'hbs');
app.set('views', viewsPath);
app.use(express.static(publicDirectoryPath));

console.log('Running csp')
app.use(csp({
    policies: {
        defaultSrc: [`'self'`],
        imgSrc: [`'self'`, `imgur.com`]
    }
}));

app.post('/upload', upload.single('avatar'), (req,res) => {
    console.log('Received image. Now processing')
    
    res.render('solution')    
})

app.get('/imdetails', (req,res) => {
    
    const options = {
        mode: 'text',
        args: ['input.jpg']
    }

    const testPath = './public/test.py'
    const runPath = './Sudoku-Solver/solver.py'
    
    pshell.PythonShell.run(runPath, options, function(e,results) {

        var arr = []
        for (i=0; i<81; i++) {
            arr.push(+results[i])
        }

        res.send({arr})
    })
})


app.listen(port, () => {
    console.log('Server is running at port ' + port);
});