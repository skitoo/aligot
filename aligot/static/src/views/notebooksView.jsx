import React from 'react';
import FluxComponent from 'flummox/component';
import Sidebar from '../components/sidebar';


class NotebooksList extends React.Component {
    render() {
        return (
            <ul>{this.props.notebooks.map(notebook => <li>{notebook.title}</li>)}</ul>
        );
    }
}

export default class NotebooksView extends React.Component {

    componentDidMount() {
        var token = this.props.flux.getStore('auth').state.token;
        this.props.flux.getActions('notebooks').listNotebooks(token);
    }

    render() {
        return (
            <div className="ui pushable">
                <Sidebar flux={this.props.flux} />
                <div className="pusher">
                    <h2>Note</h2>
                    <FluxComponent flux={this.props.flux} connectToStores={['notebooks']}>
                        <NotebooksList notebooks={this.props.notebooks} />
                    </FluxComponent>
                </div>
            </div>
        );
    }
}
