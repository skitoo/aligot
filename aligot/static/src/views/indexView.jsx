import React from 'react';
import Sidebar from '../components/sidebar';

export default class LoginView extends React.Component {
    render() {
        return (
            <div>
                <Sidebar flux={this.props.flux} />
            </div>
        );
    }
}
