import React from 'react';
import FluxComponent from 'flummox/component';

import Button from '../components/button';
import {Login, Password} from '../components/inputs';
import Message from '../components/message';
import {Link} from 'react-router';
import {CONNECTED, BAD_CREDENTIALS} from '../constants';


class LoginViewInner extends React.Component {

    onFormSubmit(event) {
        event.preventDefault();
        this.props.flux.getActions('auth').login(event.target.login.value, event.target.password.value);
    }

    componentDidUpdate() {
        if (this.props.state === CONNECTED) {
            this.props.flux.router.replaceWith('index');
        }
    }

    render() {
        let message;
        if (this.props.state === BAD_CREDENTIALS) {
            message = <Message header="Erreur de connexion" content="Le mot de passe que vous avez saisi est incorrect." type="error" />;
        }
        return (
            <main className="ui page grid">
                <div className="three column centered row">
                    <div className="column">
                        <form className="ui form" onSubmit={this.onFormSubmit.bind(this)}>
                            <h2 className="header">Connexion</h2>
                            {message}
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
