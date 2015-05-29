import {Actions} from 'flummox';
import request from 'superagent';

export default class NotebookActions extends Actions {
    createNotebook(title) {
        return {
            title: title,
            created_at: Date.now()
        };
    }

    listNotebooks(token) {
        console.log(token);
        return new Promise((resolve, reject) => {
            request.get('/api/notebooks/').set(
                'Authorization', 'Token ' + token,

            ).accept('application/json').end((error, response) => {
                error ? reject(error) : resolve(response);
            });
        });
    }
}
