import React from 'react';
import Button from '../components/button';
import {Login, Password, Email} from '../components/inputs';
import {Link} from 'react-router';

export default class RegisterView extends React.Component {
    render() {
        return (
            <div className="three column centered row">
                <div className="column">
                    <form className="ui form">
                        <h2 className="header">Inscription</h2>
                        <Login />
                        <Email />
                        <Password />
                        <Button label="S'inscrire" color="primary" />
                        Déjà un compte ? <Link to="login">Se connecter</Link>
                    </form>
                </div>
            </div>
        );
    }
}
