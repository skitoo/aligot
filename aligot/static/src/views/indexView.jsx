import React from 'react';
import Sidebar from '../components/sidebar';

export default class LoginView extends React.Component {
    handleLogout(event) {
        this.props.flux.getActions('auth').logout();
    }

    handleNotes(event) {

    }

    handleBlockNotes(event) {

    }

    render() {
        return (
            <div>
                <Sidebar flux={this.props.flux} />
            </div>
        );
    }
}
