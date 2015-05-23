import {Store} from 'flummox';


export default class NotebookStore extends Store {
    constructor(app) {
        super();

        this.register(app.getActionIds('notebooks').createNotebook, this.handleNotebook);

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
