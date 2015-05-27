import React from 'react';
import {Route, DefaultRoute} from 'react-router';
import Aligot from './views/aligot';


import LoginView from './views/loginView';
import RegisterView from './views/registerView';
import SignedInView from './views/signedInView';

import IndexView from './views/indexView';
import NotebooksView from './views/notebooksView';
import NotesView from './views/notesView';


let routes = (
    <Route handler={Aligot}>
        <DefaultRoute handler={IndexView} />

        <Route name="login" handler={LoginView} />
        <Route name="register" handler={RegisterView} />

        <Route name="signedIn" handler={SignedInView}>
            <Route name="index" path="/" handler={IndexView} />
            <Route name="notes" path="/notes" handler={NotesView} />
            <Route name="notebooks" path="/notebooks" handler={NotebooksView} />
        </Route>
    </Route>
);

export default routes;
