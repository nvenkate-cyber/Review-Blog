import * as React from 'react';
import { Card, Button } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';

import Review from '../src/pages/review';
import Browse from '../src/pages/browse';


const App = () => {

  return (
    <div>
      <h1>Review</h1>

      <hr />
      <Review />
      <hr />
    </div>
  );
};



export default App;
