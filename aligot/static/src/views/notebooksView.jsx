import React from 'react';
import Sidebar from '../components/sidebar';

export default class NotebooksView extends React.Component {
    render() {
        return (
            <div>
                <Sidebar flux={this.props.flux} />
                <div className="ui pusher">notebooks</div>
            </div>
        );
    }
}
