const multer = require('multer')
const fs = require('fs')
const path = require('path')
const express = require('express')
const app = express()
const httpolyglot = require('httpolyglot')
const https = require('https')
const cors = require("cors");
const axios = require('axios');
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


app.post('/dataFrame', upload.single('image'), async (req, res, next) => {
  const file = req.body.listFrame;
  // res.json({
  //   frameArray: file,
  // })
  const response = await axios.post('http://localhost:3000/Frame', {
    frameArray : file,
  })
  res.send(response.data)
})

require('./routes')(app)

const httpsServer = httpolyglot.createServer(options, app)
const io = require('socket.io')(httpsServer)
require('./socketController')(io)

httpsServer.listen(port, () => {
    console.log(`listening on port ${port}`)
})




