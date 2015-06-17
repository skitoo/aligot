import React from 'react';


export default class Button extends React.Component {
    render() {
        return <button className={'ui button ' + this.props.color}>{this.props.label}</button>;
    }
}
