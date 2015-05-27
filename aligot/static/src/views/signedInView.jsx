import React from 'react';
import {RouteHandler} from 'react-router';
import FluxComponent from 'flummox/component';


class LoadUserInner extends React.Component {

    componentDidMount() {
        this.props.flux.getActions('auth').loadUser();
    }

    componentDidUpdate() {
        if (this.props.token == null) {
            this.props.flux.router.replaceWith('login');
        }
    }

    render() {
        if (this.props.token != null) {
            return this.props.children;
        } else {
            return <div>Redirection...</div>
        }
    }
}


class LoadUserWrapper extends React.Component {
    render() {
        return (
            <FluxComponent flux={this.props.flux} connectToStores={['auth']}>
                <LoadUserInner>
                    {this.props.children}
                </LoadUserInner>
            </FluxComponent>
        );
    }
}


export default class SignedInView extends React.Component {
    render() {
        return (
            <LoadUserWrapper flux={this.props.flux} >
                <RouteHandler {...this.props} />
            </LoadUserWrapper>
        );
    }
}
