import {Actions} from 'flummox';
import request from 'superagent';
import {CONNECTED, BAD_CREDENTIALS} from '../constants';

export default class AuthActions extends Actions {

    loadUser() {
        return {
            token: sessionStorage.token,
            username: sessionStorage.username
        };
    }

    login(username, password) {
        return new Promise((resolve, reject) => {
            request.post('/api/token-auth/').send({
                username: username,
                password: password
            }).end((error, response) => {
                if (error) {
                    reject({
                        username: null,
                        token: null,
                        state: BAD_CREDENTIALS
                    });
                } else {
                    sessionStorage.token = response.body.token;
                    sessionStorage.username = username;
                    resolve({
                        token: response.body.token,
                        username: username,
                        state: CONNECTED
                    });
                }
            });
        });
    }

    logout() {
        sessionStorage.clear();
        return {
            token: null,
            username: null
        };
    }

    register(username, email, password, passwordConfirmation) {

        // Client validation.


        // Send request to the server.
        let promise = new Promise((resolve, reject) => {


        });
        return promise.then();
    }

    checkUsername(username) {

    }

    checkEmail(email) {

    }
}
