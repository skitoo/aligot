import React from 'react';
import Button from '../components/button';
import {Login, Password, Email, PasswordConfirmation} from '../components/inputs';
import {Link} from 'react-router';

export default class RegisterView extends React.Component {

    OnFormSubmit(event) {
        event.preventDefault();
        this.props.flux.getActions('auth')
            .register(
                event.target.username.value,
                event.target.email.value,
                event.target.password.value,
                event.target.password_confirmation.value
            )
    }

    render() {
        return (
            <main className="ui page grid">
                <div className="three column centered row">
                    <div className="column">
                        <form className="ui form" onsubmit={this.onFormSubmit.bind(this)}>
                            <h2 className="header">Inscription</h2>
                            <Login />
                            <Email />
                            <Password />
                            <PasswordConfirmation />
                            <Button label="S'inscrire" color="primary" />
                            Déjà un compte ? <Link to="login">Se connecter</Link>
                        </form>
                    </div>
                </div>
            </main>
        );
    }
}
