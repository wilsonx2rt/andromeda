import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';

import React, { Component } from 'react';
import { Provider } from 'react-redux';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

import store from './store';
import Layout from './components/container/Layout'

import Home from './routes/Home';
// import LoginHome from './routes/LoginHome';


class App extends Component {
  render() {
    return (
      <Provider store={ store }>
       <MuiThemeProvider>
          <Router>
            <Switch>
              <Layout>
                  <Route exact path="/" component={ Home } />
                  {/*<Route exact path="/login" component={ LoginHome } />*/}
              </Layout>
            </Switch>
          </Router>
        </MuiThemeProvider>
      </Provider>
    );
  }
}

export default App;
