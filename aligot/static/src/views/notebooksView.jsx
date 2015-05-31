import React from 'react';
import FluxComponent from 'flummox/component';
import Sidebar from '../components/sidebar';


class NotebooksList extends React.Component {
    render() {
        return (
            <div className="ui left vertical wide sidebar visible">
                <div className="item">
                    <h2 className="center">Carnet de notes</h2>
                </div>
                <div className="ui divided list">
                    {this.props.notebooks.map(notebook =>
                        <a className="item">
                            <div className="content">
                                <div className="header">{notebook.title}</div>
                                <div className="description">{notebook.note_count} notes</div>
                            </div>
                        </a>
                    )}
                </div>
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
                    <FluxComponent flux={this.props.flux} connectToStores={['notebooks']}>
                        <NotebooksList notebooks={this.props.notebooks} />
                    </FluxComponent>
                </div>
            </div>
        );
    }
}
