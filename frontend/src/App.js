import React, {Component} from 'react'
import './App.css';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import { Link } from '@material-ui/core';
import Navbar from './components/Navbar';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Browse from './pages/browse';
import Login from './pages/login';
import Register from './pages/register';
import { Form,FormControl } from 'react-bootstrap'

const useStyles = makeStyles({
  root: {
    minWidth: 275,
  },
  bullet: {
    display: 'inline-block',
    margin: '0 2px',
    transform: 'scale(0.8)',
  },
  title: {
    fontSize: 17,
  },
  pos: {
    marginBottom: 12,
  },
});

function App() {
  const classes = useStyles();

  return (
    <>
    <head>
      <title>Review Blog</title>
    </head>
    <div className="navbar">
      <Router>
        <Navbar />
        <Switch>
          <Route path='/' />
          <Route path='/browse' component={Browse} />
          <Route path='/login' component={Login} />
          <Route path='/register' component={Register} />
        </Switch>
      </Router>
      
      <Form inline className="searchBar">
          <FormControl type="text" placeholder="Search" className="search" />
          <Button variant="outline-success">Search</Button>
      </Form>
    </div>

    <div className="App">
      <header className="App-header">
        <h1>WELCOME!</h1>
        <h2>TRENDING REVIEWS:</h2>
      <Card className="card" style={{ width: '18rem'}}>
        <CardContent style={{backgroundColor: "#FFF4F4"}}>
          <Typography className={classes.title} color="textSecondary" gutterBottom>Top Reviewed Movie</Typography>
          <Typography variant="h5" component="h2">Disney's Jungle Cruise</Typography>
          <Typography className={classes.pos} color="textSecondary">Adventure/Fantasy</Typography>
          <Typography variant="body2" component="p">4.1/5</Typography>
        </CardContent>
        <CardActions style={{backgroundColor: "#FFF4F4"}}>
          <Button size="small">Learn More</Button>
        </CardActions>
      </Card>
      <br></br>
      <Card className="card" style={{ width: '18rem' }}>
        <CardContent style={{backgroundColor: "#FFF4F4"}}>
          <Typography className={classes.title} color="textSecondary" gutterBottom>Top Reviewed Song</Typography>
          <Typography variant="h5" component="h2">Good 4 U</Typography>
          <Typography className={classes.pos} color="textSecondary">Olivia Rodrigo</Typography>
          <Typography variant="body2" component="p">Album: Sour</Typography>
        </CardContent>
        <CardActions style={{backgroundColor: "#FFF4F4"}}>
          <Button size="small">Learn More</Button>
        </CardActions>
      </Card>

      <div class="containercenter">
            <h1>LOG IN</h1>
            <form class="formcentered" action="/login" method = "POST">
                <div class="formcentered">
                    <label for="email">Email </label>
                    <input type="email" name="email" id="email" placeholder="Type email"/>
                </div>
                
                <div class="formcentered">
                    <label for="password">Password </label>
                    <input type="text" name="password" id="password" placeholder="Type password"/>
                </div>
                <input type="submit" value="login"/>
            </form>
        </div>

        <div class="containercenter">
            <h1>REGISTER</h1>
            <form class="formcentered" action="/register" method = "POST">
                <div class="formcentered">
                    <label for="name">Name </label>
                    <input type="name" name="name" id="name" placeholder="Type name"/>
                </div>

                <div class="formcentered">
                    <label for="email">Email </label>
                    <input type="email" name="email" id="email" placeholder="Type email"/>
                </div>
                
                <div class="formcentered">
                    <label for="password">Password </label>
                    <input type="text" name="password" id="password" placeholder="Type password"/>
                </div>
                <input type="submit" value="register"/>
            </form>
        </div>
        
      </header>
    </div>
    </>
  );
}

export default App;
