import React from 'react';

export default class LoginView extends React.Component {
    handleLogout(event) {
        this.props.flux.getActions('auth').logout();
    }

    render() {
        return (
            <div>
                <div className="row">
                    <div className="column">
                        IndexView
                        <button className="ui button" onClick={this.handleLogout.bind(this)}>Déconnexion</button>
                    </div>
                </div>
            </div>
        );
    }
}
