import {Actions} from 'flummox';


export default class NotebookActions extends Actions {
    createNotebook(title) {
        return {
            title: title,
            created_at: Date.now()
        };
    }
}
