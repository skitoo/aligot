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
        var router = this.props.flux.router;
        var blocnotesClass = router.isActive('notebooks') ? 'active item' : 'item';
        var notesClass = router.isActive('notes') ? 'active item' : 'item';

        return (
            <div className="ui left vertical inverted sidebar menu visible">
                <a className={blocnotesClass} onClick={this.handleBlockNotes.bind(this)}>
                    <i className="book icon"></i> Carnets de notes
                </a>
                <a className={notesClass} onClick={this.handleNotes.bind(this)}>
                    <i className="file text outline icon"></i> Notes
                </a>
                <a className="item" onClick={this.handleLogout.bind(this)}>
                    <i className="sign out icon"></i> Déconnexion
                </a>
            </div>
        );
    }
}
