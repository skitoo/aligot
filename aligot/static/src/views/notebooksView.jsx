import React from 'react';
import FluxComponent from 'flummox/component';
import Sidebar from '../components/sidebar';


class NotebooksList extends React.Component {
    render() {
        return (
            <div className="ui link list">
                {this.props.notebooks.map(notebook => <a className="item">{notebook.title}</a>)}
            </div>
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
