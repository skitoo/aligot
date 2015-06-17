import React from 'react';


export default class Message extends React.Component {
    render() {
        let header;
        if (this.props.header) {
            header = <div className="header">{this.props.header}</div>;
        }
        return (
            <div className={'ui message visible ' + this.props.type}>
                {header}
                <p>{this.props.content}</p>
            </div>
        );
    }
}
