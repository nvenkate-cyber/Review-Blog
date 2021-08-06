import * as React from 'react';
import './App.css';
import { Card, Button } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';

import Review from '../src/pages/review';
import Browse from '../src/pages/browse';


const App = () => {

  return (
    <div>
      <Review />
    </div>
  );
};



export default App;
