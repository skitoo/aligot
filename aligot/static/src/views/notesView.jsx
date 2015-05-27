import React from 'react';
import Sidebar from '../components/sidebar';

export default class NotesView extends React.Component {
    render() {
        return (
            <div>
                <Sidebar flux={this.props.flux} />
                <div className="ui pusher">notes</div>
            </div>
        );
    }
}
