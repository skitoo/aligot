import React from 'react';

export default class Sidebar extends React.Component {
    handleLogout(event) {
        this.props.flux.getActions('auth').logout();
    }

    handleNotes(event) {
        this.props.flux.router.replaceWith('notes');
    }

    handleBlockNotes(event) {
        this.props.flux.router.replaceWith('notebooks');

    }

    render() {
        return (
            <div className="ui left vertical inverted sidebar menu visible">
                <a className="item" onClick={this.handleBlockNotes.bind(this)}>
                    <i className="book icon"></i> Carnets de notes
                </a>
                <a className="item" onClick={this.handleNotes.bind(this)}>
                    <i className="file text outline icon"></i> Notes
                </a>
                <a className="item" onClick={this.handleLogout.bind(this)}>
                    <i className="sign out icon"></i> Déconnexion
                </a>
            </div>
        );
    }
}
