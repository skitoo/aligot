import React from 'react';
import Router from 'react-router';
import FluxComponent from 'flummox/component';

import Aligot from './views/aligot';
import Flux from './flux';
import routes from './routes';


let flux = new Flux();

var router = Router.create({
    routes: routes,
    location: Router.HistoryLocation
});

router.run((Handler, state) => {
    React.render(
        <FluxComponent flux={flux}>
            <Handler {...state} />
        </FluxComponent>,
        document.getElementById('aligot')
    );
});
