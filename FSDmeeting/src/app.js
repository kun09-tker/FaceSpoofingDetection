const multer = require('multer')
const fs = require('fs')
const path = require('path')
const express = require('express')
const app = express()
const httpolyglot = require('httpolyglot')
const https = require('https')
const cors = require("cors");
var appRoot = require('app-root-path');
app.use(cors());
////// CONFIGURATION ///////////
// insert your own ssl certificate and keys
const options = {
    key: fs.readFileSync(path.join(__dirname,'..','ssl','key.pem'), 'utf-8'),
    cert: fs.readFileSync(path.join(__dirname,'..','ssl','cert.pem'), 'utf-8')
}

const port = process.env.PORT || 8000 

const storage = multer.diskStorage({
  destination: (req, file, cb) => {
      cb(null, './uploads/')
  },
  filename: (req, file, cb) => {
      // will insert even if file existed
      // const uniqueSuffix = Date.now() + '-' + Math.round(Math.random() * 1E9)
      // cb(null, uniqueSuffix + '-' + file.originalname)

      // will not insert if file existed
      console.log(file);
      cb(null, file.originalname)
  }
});

const fileFilter = (req, file, cb) => {
  const extension = path.extname(file.originalname).toLowerCase();
  const allows = ['.jpg', '.png', '.jpeg', '.gif'];
  if (allows.includes(extension)) {
      cb(null, true);
  } else {
      cb(new Error('Only images allowed'), false);
  }
};

 
var upload = multer({
  storage: storage,
  limits: {
      fileSize: 1024 * 1024 * 4
  },
  fileFilter: fileFilter
});

list_info = [];

app.post('/dataFrame', upload.single('image'), (req, res, next) => {
  const file = req.body.image
  const filename = req.body.name
  list_info.push({
    image : file,
    name : filename
  })
  res.json({
    image : file,
    name : filename
  })

  // fs.writeFile('./frameData/'+filename+'.txt', file, function (err) {
  //   if (err) throw err;
  // });
  if (!file) {
    const error = new Error('Please upload a file')
    error.httpStatusCode = 400
    return next(error)
  }
  
})

app.get("/dataFrame",(req,res)=>{
    res.json(list_info)
})  

require('./routes')(app)

const httpsServer = httpolyglot.createServer(options, app)
const io = require('socket.io')(httpsServer)
require('./socketController')(io)

httpsServer.listen(port, () => {
    console.log(`listening on port ${port}`)
})




