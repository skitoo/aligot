import React from 'react';


export class Login extends React.Component {
    render() {
        return (
            <div className="field">
                <label>Pseudo</label>
                <div className="ui icon input">
                    <input type="text" name="login" placeholder="Pseudo" />
                    <i className="user icon"></i>
                </div>
            </div>
        );
    }
}

export class Password extends React.Component {
    render() {
        return (
            <div className="field">
                <label>Mot de passe</label>
                <div className="ui icon input">
                    <input type="password" name="password" placeholder="Mot de passe" />
                    <i className="lock icon"></i>
                </div>
            </div>
        );
    }
}
