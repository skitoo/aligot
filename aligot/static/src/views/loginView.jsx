import React from 'react';
import Button from '../components/button';
import {Login, Password} from '../components/inputs';
import {Link} from 'react-router';

export default class LoginView extends React.Component {
    render() {
        return (
            <div className="three column centered row">
                <div className="column">
                    <form className="ui form">
                        <h2 className="header">Connexion</h2>
                        <Login />
                        <Password />
                        <Button label="Connexion" color="primary" />
                        Pas de compte ? <Link to="register">S'enregistrer</Link>
                    </form>
                </div>
            </div>
        );
    }
}
