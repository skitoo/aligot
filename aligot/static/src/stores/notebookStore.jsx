import {Store} from 'flummox';


export default class NotebookStore extends Store {
    constructor(flux) {
        super();

        this.register(flux.getActionIds('notebooks').createNotebook, this.handleNotebook);

        this.state = {
            notebooks: []
        };
    }

    handleNotebook(notebook) {
        this.setState({
            notebooks: this.state.notebooks.concat([notebook])
        });
    }
}
