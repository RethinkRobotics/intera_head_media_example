const express = require('express');
var cors = require('cors');
const app = express();

const port = 3007;
app.use(cors());
app.use(express.static('./', {fallthrough: false}));

app.get('/', (req, res) => res.send('Hello World!'));

app.listen(port, () => console.log(`Example app listening on port ${port}!`));