import React from 'react';
import {RouteHandler, Link} from 'react-router';

export default class Aligot extends React.Component {
    render() {
        return (
            <div>
                <header></header>
                <main className="ui page grid">
                    <RouteHandler {...this.props} key={this.props.pathname} />
                </main>
                <footer></footer>
            </div>
        );
    }
}
