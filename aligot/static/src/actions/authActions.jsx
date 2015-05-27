import {Actions} from 'flummox';
import request from 'superagent';


export default class AuthActions extends Actions {

    loadUser() {
        console.log('loadUser');
        return {
            token: sessionStorage.token,
            username: sessionStorage.username
        };
    }

    login(username, password) {
        let promise = new Promise((resolve, reject) => {
            request.post('/api/token-auth/').send({
                username: username,
                password: password
            }).accept('application/json').end((error, response) => {
                error ? reject(error) : resolve({
                    token:response.body.token,
                    username: username
                });
            });
        });
        return promise.then(val => {
            sessionStorage.token = val.token;
            sessionStorage.username = val.username;
            return val;
        });
    }

    logout() {
        sessionStorage.clear();
        return {
            token: null,
            username: null
        }
    }

    register(username, email, password) {

    }

    checkUsername(username) {

    }

    checkEmail(email) {

    }
}
