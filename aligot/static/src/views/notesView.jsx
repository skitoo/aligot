import React from 'react';
import Sidebar from '../components/sidebar';

export default class NotesView extends React.Component {
    render() {
        return (
            <div className="ui pushable">
                <Sidebar flux={this.props.flux} />
                <div className="pusher">notes</div>
            </div>
        );
    }
}
