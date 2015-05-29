import React from 'react';
import Sidebar from '../components/sidebar';

export default class NotebooksView extends React.Component {

    componentDidMount() {
        var token = this.props.flux.getStore('auth').state.token;
        this.props.flux.getActions('notebooks').listNotebooks(token);
    }

    render() {
        return (
            <div>
                <Sidebar flux={this.props.flux} />
                <div className="ui pusher">notebooks</div>
            </div>
        );
    }
}
