import {Store} from 'flummox';


export default class NotebookStore extends Store {
    constructor(flux) {
        super();

        const notebooksIds = flux.getActionIds('notebooks');

        this.register(notebooksIds.createNotebook, this.handleNotebook);
        this.register(notebooksIds.listNotebooks, this.handleListNotebooks);

        this.state = {
            notebooks: []
        };
    }

    handleListNotebooks(notebooks) {
        this.setState({
            notebooks: notebooks
        });
    }

    handleNotebook(notebook) {
        this.setState({
            notebooks: this.state.notebooks.concat([notebook])
        });
    }
}
