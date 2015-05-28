import React from 'react';
import {RouteHandler, Link} from 'react-router';

export default class Aligot extends React.Component {
    render() {
        return <RouteHandler {...this.props} key={this.props.pathname} />;
    }
}
