import React, { Component } from 'react';
import { Provider } from 'react-redux';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import store from './store';
import Layout from './components/container/Layout'

import Home from './routes/Home';


class App extends Component {
  render() {
    return (
      <Provider store={ store }>
          <Router>
            <Switch>
              <Layout>
              <Route exact path="/" component={ Home } />
              </Layout>
            </Switch>
          </Router>
      </Provider>
    );
  }
}

export default App;
