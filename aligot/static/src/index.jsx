import React from 'react';
import Router from 'react-router';
import FluxComponent from 'flummox/component';

import Aligot from './views/aligot';
import App from './app';
import routes from './routes';


// const app = new App();
//
// React.render(<Aligot app={app} />, document.getElementById('aligot'));

let app = new App();

var router = Router.create({
    routes: routes,
    location: Router.HistoryLocation
});

router.run((Handler, state) => {
    React.render(
        <FluxComponent flux={app}>
            <Handler {...state} />
        </FluxComponent>,
        document.getElementById('aligot')
    );
});
