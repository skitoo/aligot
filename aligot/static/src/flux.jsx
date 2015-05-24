import Flummox from 'flummox';
import NotebookActions from './actions/notebookActions';
import NotebookStore from './stores/notebookStore';
import AuthActions from './actions/authActions';


export default class Flux extends Flummox {
    constructor() {
        super();

        // actions ------------------------------------------------------- //
        this.createActions('notebooks', NotebookActions);
        this.createActions('auth', AuthActions);

        // stores -------------------------------------------------------- //
        this.createStore('notebooks', NotebookStore, this);
    }
}
