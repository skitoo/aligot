import Flummox from 'flummox';
import NotebookActions from './actions/notebookActions';
import NotebookStore from './stores/notebookStore';


export default class App extends Flummox {
    constructor() {
        super();

        // actions ------------------------------------------------------- //
        this.createActions('notebooks', NotebookActions);

        // stores -------------------------------------------------------- //
        this.createStore('notebooks', NotebookStore, this);
    }
}
