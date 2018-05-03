import React, { Component } from 'react';
import { Provider } from 'react-redux';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import store from './store';
import Layout from './components/container/Layout'
import Home from './routes/Home';
import LoginHome from './components/container/LoginHome';
import UserRegistration from './routes/UserRegistration';
import UserProfile from './routes/UserProfile';
import RegisterValidation from './routes/RegisterValidation';
import RegisterEmail from './routes/Email'
import Review from './routes/Review';
import NewRestaurantForm from './components/container/NewRestaurantForm';
import { fetchLocalUser } from './store/actions/currentUser';
import Restaurants from './components/container/Restaurants'

store.dispatch(fetchLocalUser());

class App extends Component {
  render() {
    return (
      <Provider store={ store }>
          <Router>
            <Switch>
              <Layout>
              <Route exact path="/" component={ Home } />
                  <Route exact path="/login" component={ LoginHome } />
                  <Route exact path="/user" component={ UserProfile } />
                  <Route exact path="/register" component={ UserRegistration } />
                  <Route exact path="/register/validation" component={ RegisterValidation } />
                  <Route exact path="/register/email" component={ RegisterEmail } />
                  <Route exact path="/restaurants" component={ Restaurants } />
                  <Route exact path="/restaurants/new" component={ NewRestaurantForm } />
                  <Route exact path="/review" component={ Review } />
                  <Route exact path="/review/:restaurantId" component={ Review } />
              </Layout>
            </Switch>
          </Router>
      </Provider>
    );
  }
}

export default App;