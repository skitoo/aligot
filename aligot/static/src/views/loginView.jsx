import React from 'react';
import FluxComponent from 'flummox/component';

import Button from '../components/button';
import {Login, Password} from '../components/inputs';
import {Link} from 'react-router';


class LoginViewInner extends React.Component {

    onFormSubmit(event) {
        event.preventDefault();
        this.props.flux.getActions('auth').login(event.target.login.value, event.target.password.value);
    }

    componentDidUpdate() {
        if (this.props.token != null) {
            this.props.flux.router.replaceWith('index');
        }
    }

    render() {
        return (
            <main className="ui page grid">
                <div className="three column centered row">
                    <div className="column">
                        <form className="ui form" onSubmit={this.onFormSubmit.bind(this)}>
                            <h2 className="header">Connexion</h2>
                            <Login />
                            <Password />
                            <Button label="Connexion" color="primary" />
                            Pas de compte ? <Link to="register">S'enregistrer</Link>
                        </form>
                    </div>
                </div>
            </main>
        );
    }
}


export default class LoginView extends React.Component {
    render() {
        return (
            <FluxComponent flux={this.props.flux} connectToStores={['auth']}>
                <LoginViewInner />
            </FluxComponent>
        );
    }
}
