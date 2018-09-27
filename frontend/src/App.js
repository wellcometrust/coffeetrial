import React, { Component } from 'react';
import Header from './components/header';
import Home from './views/index';
import TakeAPick from './views/take-your-pick';
import MatchMaker from './views/match-maker';
import PleaseConfirm from './views/please-confirm';
import Confirmation from './views/confirmation';
import './App.css';
import { BrowserRouter as Router, Route } from "react-router-dom";
class App extends Component {
  render() {
      console.log(TakeAPick);
    return (
      <div className="App">
        <Header />
          <Router>
              <div>
                  <Route exact path="/" component={Home} />
                  <Route path="/take-your-pick" component={TakeAPick} />
                  <Route path="/match-maker" component={MatchMaker} />
                  <Route path="/please-confirm" component={PleaseConfirm} />
                  <Route path="/confirmation" component={Confirmation} />

              </div>
          </Router>

      </div>
    );
  }
}

export default App;
