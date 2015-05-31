import React from 'react';
import FluxComponent from 'flummox/component';
import Sidebar from '../components/sidebar';


class NotebooksList extends React.Component {
    render() {
        return (
            <div className="ui left vertical wide sidebar menu visible">
                <div className="item"><h2>Carnet de notes</h2></div>
                <div className="item">
                    <div className="menu divided">
                        {this.props.notebooks.map(notebook =>
                            <a className="item">
                                <h4>{notebook.title}</h4>
                                <div>{notebook.note_count} note(s)</div>
                            </a>
                        )}
                    </div>
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
