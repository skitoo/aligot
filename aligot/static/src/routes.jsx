import React from 'react';
import {Route, DefaultRoute} from 'react-router';
import Aligot from './views/aligot';
import LoginView from './views/loginView';
import RegisterView from './views/registerView';


let routes = (
    <Route handler={Aligot}>
        <DefaultRoute handler={LoginView} />
        <Route name="login" handler={LoginView} />
        <Route name="register" handler={RegisterView} />
    </Route>
);

export default routes;
