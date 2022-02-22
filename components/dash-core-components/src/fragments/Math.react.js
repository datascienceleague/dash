import React, {Component} from 'react';

export default class Math extends Component {
    constructor(props) {
        super(props);
        this.span_element = React.createRef();
        console.warn('Math.constructor');
    }

    componentDidMount() {
        console.warn('Math.render');
        window.MathJax.typeset([this.span_element.current]);
    }

    render() {
        return (
            <span ref={this.span_element}>${this.props.tex}$</span>
        )
    }
}
